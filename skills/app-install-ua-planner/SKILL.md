---
name: app-install-ua-planner
description: Plans paid user acquisition for a live mobile app across Apple Ads, Google App campaigns, Meta, TikTok, Snapchat and AppLovin, setting max CPI, day 7 ROAS targets and a 4 week budget. Use when asked for an app UA strategy, how to lower CPI, or where the next app ad dollar should go.
---

# App Install (User Acquisition) Campaign Planner

A paid UA plan for an app that is already live and already buying installs, or about to. It answers five questions in order: what one install is worth to this app, which network and platform lines are buying installs worth more than they cost, where the next dollar should go over the next 4 weeks, which network to open next, and what each line needs (event, creative, measurement) to keep working.

Every number is the app's own. The ceiling on cost per install comes from the app's cohort revenue curve, not from a category benchmark, and every verdict shows the numbers behind it.

## Before you start

The skill works with no connection at all. Ask for these, and use the default when the user doesn't know:

| Input | Default |
|---|---|
| **Revenue curve per platform:** cumulative net revenue per install (after store fees and refunds) at day 0, 1, 3, 7, 14, 30, 60, 90 and 180, from install cohorts old enough to have reached the last day | none; ask. A measurement partner (AppsFlyer, Adjust, Singular, Branch) cohort export or a subscription tool export both work |
| **7-day event rates:** the share of installs that start a trial, subscribe or purchase within 7 days, per platform | from the same export |
| **Event timing:** the median hours from install to each event | ask; needed only for iOS event choice |
| **Payback day:** the day by which an install cohort must have earned back its cost | day 180 for a subscription app, day 90 for in-app purchases or ads |
| **Margin** on top of payback | 0% (break-even) |
| **Budget cap** for the next 4 weeks | the last 4 weeks' spend plus 20% |
| **Results by network and platform:** spend, installs and day 7 net revenue for the last 28 days of install cohorts, split into two 14-day halves | from the connectors and the export (see below) |
| **What each campaign optimizes for:** installs, an in-app event, or value | from the connectors, or ask |
| **Measurement setup:** which networks are integrated with the measurement partner, which events each network receives, the iOS postback conversion window | ask |
| **Store listings:** App Store id and Google Play package name | ask |

The results window is 28 days of install cohorts that **ends 7 days before today**, so every cohort has reached its day 7. State the dates, the currency and the payback day at the top of the report.

Never invent a revenue figure. If the curve stops before the payback day, use its last measured day, label the max CPI "measured only to day N, so a floor", and say so in the unknowns.

### If the InsightfulPipe MCP is connected

Spend comes from each network. Installs and day 7 revenue come from the measurement partner export when there is one, because each network counts its own installs and the totals overlap. Without an export, use the network-reported installs and conversion value, and label the line "network-reported; may double count across networks".

1. Call `query_contexts` with `request="accounts"` for `google-ads`, `facebook-ads`, `tiktok-ads`, `snapchat-ads`, `apple-store` and `google-play`. If your workspace also lists an `applovin-ads` connection, include it. Note `workspace_id`, `brand_id` and each account id. Use only the accounts that run this app's campaigns.
2. Call `query_contexts` with `request="actions_details"` for `gaql` (google-ads), `get_insights_adaccount` (facebook-ads), `integrated_report_basic` (tiktok-ads), `get_campaigns` and `get_campaign_stats` (snapchat-ads), `lookup_by_id` (apple-store) and `app_details` (google-play), plus `get_report` for applovin-ads if it is connected. Follow the body shapes it returns.

## How to pull the results

Pull each half (days 1 to 14 and 15 to 28 of the window) separately, or pull by day and add up.

**Google App campaigns** (`google-ads`, action `gaql`). App campaigns are `MULTI_CHANNEL`. The app store field tells you the platform.

```sql
SELECT campaign.id, campaign.name, campaign.advertising_channel_sub_type,
       campaign.app_campaign_setting.app_id, campaign.app_campaign_setting.app_store,
       campaign.app_campaign_setting.bidding_strategy_goal_type,
       segments.date, metrics.cost_micros, metrics.biddable_app_install_conversions,
       metrics.biddable_app_post_install_conversions, metrics.conversions_value
FROM campaign
WHERE campaign.advertising_channel_type = 'MULTI_CHANNEL'
  AND segments.date BETWEEN 'YYYY-MM-DD' AND 'YYYY-MM-DD'
```
Divide `cost_micros` by 1,000,000. `bidding_strategy_goal_type` says whether the campaign bids for installs, in-app actions or value.

**Meta** (`facebook-ads`, action `get_insights_adaccount`). Use `level` `campaign`, a `time_range` per half, and the fields `campaign_name`, `objective`, `optimization_goal`, `spend`, `actions` and `action_values`. App installs are the `mobile_app_install` entry in `actions`. An app promotion campaign promotes one store's app, so the campaign tells you the platform; ask if the names don't.

**TikTok** (`tiktok-ads`, action `integrated_report_basic`). `report_type` `BASIC`, `data_level` `AUCTION_CAMPAIGN`, `dimensions` `["campaign_id"]`, and the metrics `campaign_name`, `objective_type`, `spend`, `app_install`, `cost_per_app_install` and `total_purchase_value`. Metrics come back as strings; convert them before adding.

**Snapchat** (`snapchat-ads`). `get_campaigns` lists the campaigns and their `objective`. Then `get_campaign_stats` per app campaign with `granularity` `TOTAL` and the fields `spend`, `total_installs`, `conversion_start_trial`, `conversion_subscribe` and `conversion_purchases_value`. `start_time` and `end_time` must fall on the hour, and the account's time zone applies. Spend is in micros.

**AppLovin**, only if your workspace lists an AppLovin connection (`applovin-ads`, action `get_report`). Columns `day`, `campaign`, `platform`, `cost`, `conversions`, `iap_rev_7d` and `iap_roas_7d`. The report needs an APP account; a web account returns nothing.

**Apple Ads** has no connector. Ask for a campaign report export (spend and installs by campaign) and use the measurement partner for day 7 revenue.

**Store listings.** `lookup_by_id` (apple-store, numeric Apple id) and `app_details` (google-play, package name) give the rating, rating count, screenshots and whether Play has a promo video.

If a call fails or returns nothing, mark that line **unknown**, say which call and why, and keep going. Never fill a gap with a guess.

## Step 1: What one install is worth

Per platform, from the revenue curve:

- **Payback value** = cumulative net revenue per install at the payback day.
- **Max CPI** = payback value × (1 − margin). This is the most an average install can cost.
- **Curve multiplier** = payback value ÷ day 7 value. It turns a day 7 result into a projected payback result.
- **Target day 7 ROAS** = day 7 value ÷ max CPI. A cohort at this ROAS on day 7 is on track.
- **Day 30 checkpoint ROAS** = day 30 value ÷ max CPI. Use it to confirm a line a month later.
- **Max cost per event** = max CPI ÷ the event's 7-day rate, for each event the app tracks. This is the target to give a campaign that optimizes for that event.

iOS and Android get separate numbers. Never blend them: their curves usually differ by a factor of two or more.

## Step 2: The hurdle

The payback ROAS a line needs is 1 ÷ (1 − margin). From it:

| Line | Value |
|---|---|
| Scale at or above | 1.1 × the payback ROAS needed |
| Hold at or above | 0.9 × the payback ROAS needed |
| Pause below | 0.7 × the payback ROAS needed |

These bands are this skill's starting point. Say so, and widen them when the curve rests on few cohorts.

## Step 3: Score each network and platform line

A line is one network on one platform (Meta iOS, Meta Android and so on). For each line, over the full 28 days:

- **CPI** = spend ÷ installs, and the CPI of each half.
- **Day 7 ROAS** = day 7 net revenue ÷ spend.
- **Projected payback ROAS** = day 7 ROAS × the platform's curve multiplier. This assumes the line's cohorts follow its platform's curve from day 7 on; the day 30 checkpoint tests that.
- **Marginal CPI**, what the next installs cost:
  - If the late half spent at least 10% more than the early half: (late spend − early spend) ÷ (late installs − early installs). If installs did not rise, the line is **saturated** and its next-dollar ROAS is 0.
  - Otherwise: the late-half CPI.
- **Next-dollar ROAS** = day 7 net revenue per install × curve multiplier ÷ marginal CPI. It is what the next dollar on this line is projected to return by the payback day.
- **Creative fatigue signal:** spend moved by 10% or less between the halves, but CPI rose more than 15%. Same money, dearer installs: the ads have usually worn out.

## Step 4: Verdicts

Apply in this order:

1. **Unknown:** no day 7 revenue for the line (the network isn't in the measurement partner, or the export misses it).
2. **Too few installs to judge:** fewer than 100 installs in the 28 days.
3. **Pause:** projected payback ROAS under the pause line.
4. **Cut and fix:** projected payback ROAS under the hold line.
5. **Scale:** next-dollar ROAS at or above the scale line.
6. **Hold:** next-dollar ROAS at or above the hold line.
7. **Trim:** everything else. The average pays back, but the last dollars added did not.

## Step 5: The 4-week plan

Start from each line's current weekly spend (late-half spend ÷ 2):

| Verdict | Weeks 1 to 4 |
|---|---|
| Scale | +20% a week, compounding |
| Hold, too few installs | flat |
| Trim | back to the early half's weekly spend |
| Cut and fix | 70% of current, while the fix runs |
| Pause | 0 |
| Unknown | flat for 2 weeks while measurement is fixed, then 0 if it still can't be measured |

Add up the plan. If it goes over the budget cap, remove scale steps from the line with the lowest next-dollar ROAS first. Whatever is left under the cap pays for a new network test (Step 6) and the rest is held back, not spread around: it goes only to a line that clears the scale line at a weekly check.

**Weekly check.** Each Monday, rerun the scorecard on the cohorts that have reached day 7. A scale step happens only if the line still clears the scale line.

## Step 6: Which network to open next

Take the platform with the higher max CPI, then walk this order and pick the first network not already running there. The order is this skill's starting point; change it when the app's audience says otherwise (a game, for example, moves AppLovin up).

- **iOS:** Apple Ads, Meta, Google App campaigns, TikTok, AppLovin, Snapchat
- **Android:** Google App campaigns, Meta, TikTok, AppLovin, Snapchat

The test runs for 2 weeks and optimizes for the deepest event that will get enough volume (Step 7), at the max cost per event. Its budget is 2 × the network's weekly events needed × that max cost. Run it only if it fits in what is left under the cap. Judge it on the same scorecard once it has 100 installs with a day 7.

## Step 7: The event each line optimizes for

Each network needs enough weekly conversions of an event to learn on it. Use these weekly minimums per campaign:

| Network | Events a week |
|---|---|
| Google App campaigns | 70 (Google asks for at least 10 users a day completing the action, and a daily budget of at least 10 times the target cost per action) |
| Meta, TikTok, Snapchat, AppLovin | 50 |

For each line still spending in week 1: weekly installs at the planned spend (planned spend ÷ late-half CPI) × each event's 7-day rate ÷ number of campaigns. Pick the deepest event (subscribe or purchase, then trial start or sign-up) that clears the minimum. Two conditions:

- **iOS:** the event must usually happen inside the privacy postback conversion window. An event whose median time from install is longer than the window barely reaches the network, so step down to the next event.
- **The event must already be sent to the network.** If not, stay on installs and list "send the event" under measurement.

Apple Ads bids on keywords and taps, not on in-app events, so judge it by cost per event in the measurement partner. Switch a line to a new event in a **new campaign**, not by editing the running one, which resets its learning.

## Step 8: Creative each line needs

| Network | What it runs on |
|---|---|
| Apple Ads | no uploads; custom product pages per keyword group, so the first screenshots match the search |
| Google App campaigns | up to 5 headlines and 5 descriptions, images and videos in landscape, square and portrait; without your own video Google builds one from the store listing |
| Meta | vertical 9:16 and 4:5 video, plus square images |
| TikTok | 9:16 video made for TikTok, with sound and a person on screen |
| Snapchat | full-screen 9:16 video with the app on screen early |
| AppLovin | playable and short video ads |

A line with the fatigue signal gets 3 new concepts this week, whatever its verdict, and is judged again only once they have run. A scaling line gets 3 new concepts a month. These counts are this skill's starting point.

Check the listings too: a Google Play listing with no promo video means Google App campaigns will build video from screenshots unless you supply your own, and a rating under 4.0 or a listing with few screenshots holds conversion back on every network. Store page work itself belongs to an App Store conversion skill (see Go deeper).

## Step 9: Measurement each line needs

Per network: is it integrated with the measurement partner, does it receive the events it should optimize for, and for iOS, do the postback conversion values cover the events that matter inside the window. Apple Ads needs the AdServices attribution token passed to the measurement partner. A network that isn't integrated can't be scored; that is why its verdict is unknown and its spend stops after 2 weeks.

## The report

1. **Header:** app, platforms, currency, install cohort dates, payback day and margin, and the source of each number (export, connector, from the user).
2. **Top findings:** 4 to 6 lines, each with its number.
3. **What an install is worth:** the Step 1 table per platform.
4. **The hurdle:** the Step 2 lines.
5. **Network scorecard:** one row per line with spend, installs, CPI per half, day 7 ROAS, projected payback ROAS, marginal CPI and its basis, next-dollar ROAS, fatigue signal, verdict and why.
6. **The 4-week plan:** weekly spend per line, totals, the new network test, what is held back and why, and the weekly check.
7. **Open next:** network, platform, event, target cost per event, test budget, and anything to set up first.
8. **Optimization events:** current and recommended event per line, with the weekly volume.
9. **Creative:** what each line needs now.
10. **Store page checks** and **measurement:** status per network and what to fix.
11. **Unknowns:** every gap and assumption.

## Fixes this skill can run

None. This skill reads and plans. It never changes a budget, bid, event or campaign. Budget changes are yours to make in each network; campaign builds go to a campaign-building skill if installed (see Go deeper). Say this in the report.

## Rules

- Every number is measured, from the user, or computed from those. No category benchmarks for CPI, retention or ROAS.
- iOS and Android are scored separately, always.
- Spend from the network; installs and revenue from the measurement partner when there is one.
- A verdict needs 100 installs with a day 7. Fewer, and the line holds.
- Never scale a line on its average alone: the next-dollar ROAS decides.
- Don't project the curve past the last day it was measured.
- An empty result is reported as empty, with the reason, never filled in.

## Go deeper

- **app-marketing-plan**, if installed: the whole app plan, from pre-launch and store positioning to the first paid budget. It hands the running of install campaigns to this skill.
- **google-app-campaigns-manager**, if installed: builds and reviews the Google App campaigns this plan opens or changes.
- **app-store-conversion-analyst**, if installed: the store page work behind a low install rate.
- **cross-platform-budget-allocator**, if installed: the same next-dollar question for web campaigns.
- **ltv-cac-ratio-optimizer**, if installed: LTV to CAC across the whole business, beyond app installs.
- **ad-creative-fatigue-detector**, if installed: ad-by-ad fatigue once this plan flags a line.
