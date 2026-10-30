---
name: funnel-dropoff-diagnostician
description: Finds where a conversion funnel loses people, on live data pulled through the InsightfulPipe MCP. Builds the funnel itself from GA4 events, pages and sessions, adds the ad and search steps above the site (impression share, impressions and clicks from Google Ads, Meta, LinkedIn and Search Console), compares every step with the prior period and across devices, channels, countries or regions, campaigns and landing pages, and ranks the leaks by the conversions they cost. Use when someone asks where they are losing people, why conversions dropped, for a signup, checkout, lead-form or full-funnel (impression to revenue) report, to compare mobile and desktop, to judge a redesign before and after, or to design a marketing funnel. Offers a GA4 key event and a drop-off audience that it creates only after the user confirms.
---

# Funnel Drop-off Diagnostician

A drop is only a problem when it is worse than it should be and big enough to matter. Half of all visitors leaving after the first page can be normal; a fifth of checkout starters vanishing can be the most expensive leak in the business. This skill measures every step, decides which drops are real, and ranks them by the conversions they cost.

It reads the data itself. Every number in the report comes from a call below, and the report says which call it came from.

## Before you start

You need the InsightfulPipe MCP connected. GA4 gives the steps on the site. Google Ads, Meta, LinkedIn Ads and Search Console are optional and give the steps above it.

1. Call `query_contexts` with `request="accounts"` for `google-analytics`, and for each of `google-ads`, `facebook-ads`, `linkedin-ads` and `google-search-console` the user wants in the funnel. Note `workspace_id`, `brand_id` and each account id. **Use the accounts of one business only.** If a workspace holds several businesses, ask which one; never put one company's ads on top of another company's site.
2. Call `query_contexts` with `request="actions_details"` for every action below on its platform, and follow the body shapes it returns.
3. Ask the user, and use the defaults when they don't know:
   - **The funnel type and its steps.** Default: pick the type from the events that fire (call 2) using the step library below.
   - **What one conversion is worth** (an order's margin, a lead's value, a signup's value). Default: none. Impact is then counted in conversions, plus ad spend where there is some.
   - **A change date** (a redesign, a new form, a price change). With one, compare equal windows before and after it instead of the prior period.
   - **A target rate** for the final step, if they have one.

**Window.** Use the last 30 days ending 2 days before today (GA4 is still processing the most recent days). Call the first day `START` and the last day `END`. The comparison window is the 30 days before `START` (`PRIOR_START` to `PRIOR_END`). Print both windows at the top of the report.

## The step library

Funnels are built from GA4 events and page paths. These are the defaults, using GA4's recommended event names; swap in the user's own.

| Funnel | Steps |
|---|---|
| Lead generation | session → engaged session → key page (contact, quote, demo) → `form_start` → `form_submit` or `generate_lead` → `qualify_lead` → `close_convert_lead` |
| SaaS signup | session → engaged session → pricing page → signup start (the signup page, or the outbound click to the app) → `sign_up` → the activation event → `purchase` |
| Ecommerce | session → `view_item` → `add_to_cart` → `begin_checkout` → `add_payment_info` → `purchase` |
| Content and newsletter | session → engaged session → `scroll` → `sign_up` or `generate_lead` |

Above the site, the paid and search steps are: eligible impressions → impressions → clicks → sessions that landed. Below it, revenue: `purchase` value in GA4, conversion value in the ad platform, or a closed-deal event. When a step has no event, write **not tracked** in its row and keep going, and name the event or import that would add it (report item 9).

## How to run the calls

GA4 calls go through `query_data` with `platform="google-analytics"`; other calls name their platform. Add `workspace_id` and `brand_id` from step 1 to each body. Rules the API enforces, all seen on live runs:

- **Request keys are camelCase where GA4 defines them.** Filters go in `dimensionFilter`. After any filtered call, check that the rows match the filter.
- **This is an open funnel.** GA4's Data API counts sessions in which each event happened; it does not know their order, and a session can enter at any step. GA4's ordered (closed) funnel exists only in the Explore screen. So a step rate here is "sessions with step N ÷ sessions with step N−1". When a later step is bigger than the step before it, say so: the earlier step is under-tracked, or people skip it.
- **Count sessions.** Each session has one device, one channel, one country and region, one landing page and one new-or-returning value, so session rows can be added up across those dimensions. Users can't: one person can sit in several rows.
- **An empty result is zero**, not an error. GA4 returns no rows when every metric is 0.
- **Google Ads:** money fields end in `_micros` (divide by 1,000,000); impression share comes back as a fraction (0.27 is 27%); any segment you filter on must also be in `SELECT`. A tap on the call button in an ad counts as a click, so calls from ads sit inside the clicks step.
- **Rate limits.** When a call is refused with "Retry in N seconds", tell the user how long that is, then wait or stop. Don't retry in a loop.

If a call fails, keep going. Mark what it feeds **unknown**, say which call failed and why, and never fill the gap with a guess.

## Part 1: can the funnel be trusted?

**1. Key events configured.**
```json
{"action": "list_key_events", "property_id": "properties/<id>"}
```

**2. Event inventory.** Which steps fire at all.
```json
{"action": "events", "property_id": "properties/<id>",
 "dimensions": ["eventName"], "metrics": ["eventCount", "totalUsers", "sessions"],
 "start_date": "START", "end_date": "END"}
```

**3. What the property sees.** Hosts other than the site (a staging host, `localhost`) are test traffic.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["hostName"], "metrics": ["sessions"], "start_date": "START", "end_date": "END"}
```

**4. Is tracking steady?** Sessions by week over the window and the comparison window together.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["isoYearIsoWeek"], "metrics": ["sessions", "engagedSessions", "keyEvents"],
 "start_date": "PRIOR_START", "end_date": "END"}
```

| Check | Fail when |
|---|---|
| The final step is measured | the goal event never fires in the window (a key event that never fires counts as not measured) |
| Value is measured | warn when the final step carries no revenue or conversion value: impact can then only be counted in conversions, and the steps after it (qualified, closed, paid) are not tracked |
| Tracking is steady | a full week has more than 3 times, or less than a third of, the median of the other weeks. Read rates only inside the steady weeks, and don't compare across the break. |
| Test traffic is kept out | a test host shows up in call 3, or an admin or test page in calls 7 or 9 |
| Steps run in order | a later step has more sessions than the step before it (warn) |
| Ad clicks reach the site | GA4 paid sessions for a platform are under 70% of that platform's clicks (warn; see Part 3) |
| Ad conversions are real leads | an ad platform counts a button tap (a click-to-call or call-or-text button on the site) as a conversion next to confirmed calls or forms (warn: the "lead" step is inflated by up to that action's share). Name and type in call 16 tell you; when unsure, say what to confirm. |

Without GA4, the steady and test-traffic checks are skipped (ad platforms record impressions and clicks themselves) and the click-to-session check is unknown; say so.

A failed or warned check is the first fix in the report, ahead of any drop-off fix, because every rate after it is unreliable. When the final step isn't measured, the funnel is **not graded**.

## Part 2: the site funnel in GA4

**5. Sessions and engagement by segment.** The base of the funnel and of every segment. For a business that serves one country, put `region` in place of `country`.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["deviceCategory", "sessionDefaultChannelGroup", "newVsReturning", "country"],
 "metrics": ["sessions", "engagedSessions", "keyEvents", "totalRevenue"],
 "start_date": "START", "end_date": "END", "limit": 100000}
```

**6. Sessions with each step, by segment.** Put the funnel's step events in `values`. Summed over all rows, this is the funnel; summed by device, channel, new-or-returning or country (or region, as in call 5), it is that segment's funnel.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["deviceCategory", "sessionDefaultChannelGroup", "newVsReturning", "country", "eventName"],
 "metrics": ["sessions"], "start_date": "START", "end_date": "END", "limit": 100000,
 "dimensionFilter": {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["session_start", "view_item", "add_to_cart", "begin_checkout", "purchase", "form_start", "form_submit", "generate_lead", "sign_up"]}}}}
```

**7. Page steps.** Sessions that reached the key pages (pricing, contact, signup, demo). Swap in the site's own paths, and drop pages that only mention the word, such as a blog post about pricing.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["pagePath"], "metrics": ["sessions", "totalUsers"],
 "start_date": "START", "end_date": "END",
 "dimensionFilter": {"orGroup": {"expressions": [
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "pricing"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "contact"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "signup"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "demo"}}}]}}}
```
One page's sessions are a step. Several pages can't be added up (one session can see two of them), so a step made of several pages is "at least" its biggest page.

**8. Landing pages.** Where the sessions that leak came in. Put the first step and the goal event in `values`. Rank landing pages by sessions and compare each one's goal rate with the site's.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["landingPage", "eventName"], "metrics": ["sessions"],
 "start_date": "START", "end_date": "END", "limit": 100000,
 "dimensionFilter": {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["session_start", "form_submit", "generate_lead", "purchase", "sign_up"]}}}}
```

**9. The lead form report.** Starts and submissions per page. A page with form starts and no submissions either loses everyone or doesn't record the submission; check the thank-you step before calling it a leak.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["pagePath", "eventName"], "metrics": ["eventCount", "sessions", "totalUsers"],
 "start_date": "START", "end_date": "END",
 "dimensionFilter": {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["form_start", "form_submit", "generate_lead"]}}}}
```

**10. Form and funnel parameters.** If a parameter such as `form_id`, `form_name`, `plan_name` or `signup_method` is registered, add it to call 9 as `customEvent:<parameter>` to split the report by form or plan.
```json
{"action": "list_custom_dimensions", "property_id": "properties/<id>"}
```

**11. Value by channel.** Revenue and key events per channel, for the bottom of a full-funnel report.
```json
{"action": "traffic_sources", "property_id": "properties/<id>",
 "dimensions": ["sessionDefaultChannelGroup"],
 "metrics": ["sessions", "engagedSessions", "keyEvents", "totalRevenue"],
 "start_date": "START", "end_date": "END"}
```

**12. The comparison window.** Run calls 5 and 6 again with `PRIOR_START` and `PRIOR_END` (or the before-and-after windows around the change date).

## Part 3: the steps above the site

Use each platform the business advertises on. For a platform it doesn't use, leave the row out.

**Google Ads.** These go through `query_data` with `platform="google-ads"` and `action="gaql"`, with the customer id as `account_id`.

13. Impression share by campaign: the impressions the campaigns were eligible for and lost to budget or to rank.
```sql
SELECT campaign.name, campaign.advertising_channel_type, metrics.impressions,
       metrics.search_impression_share, metrics.search_budget_lost_impression_share,
       metrics.search_rank_lost_impression_share
FROM campaign
WHERE segments.date BETWEEN 'START' AND 'END' AND metrics.impressions > 0
```
Eligible impressions = impressions ÷ impression share. Missed to budget = eligible × budget-lost share; missed to rank = eligible × rank-lost share. Search campaigns only; other campaign types return no share.

14. The ad funnel by campaign and device.
```sql
SELECT campaign.name, segments.device, metrics.impressions, metrics.clicks,
       metrics.cost_micros, metrics.conversions, metrics.conversions_value
FROM campaign
WHERE segments.date BETWEEN 'START' AND 'END' AND metrics.impressions > 0
```

15. What the conversions are. Split the conversions by action, so the lead step shows how leads arrive (calls from the ad, call or text taps on the site, forms).
```sql
SELECT campaign.name, segments.device, segments.conversion_action_name,
       segments.conversion_action_category, metrics.conversions, metrics.all_conversions
FROM campaign
WHERE segments.date BETWEEN 'START' AND 'END'
```

16. How each conversion action counts.
```sql
SELECT conversion_action.name, conversion_action.category, conversion_action.type,
       conversion_action.primary_for_goal, conversion_action.include_in_conversions_metric,
       conversion_action.counting_type, conversion_action.status
FROM conversion_action WHERE conversion_action.status = 'ENABLED'
```
Only actions with `include_in_conversions_metric = true` are in `metrics.conversions`. A page-load action that isn't counted (for example the contact page) shows up only in `all_conversions`; use it as a site step, not as a lead.

17. Landing pages from the ads.
```sql
SELECT landing_page_view.unexpanded_final_url, metrics.clicks, metrics.cost_micros, metrics.conversions
FROM landing_page_view
WHERE segments.date BETWEEN 'START' AND 'END' AND metrics.clicks > 0
```
Read the page path and ignore the tracking template (`{ignore}?campaignid=...`), but keep a templated and a plain version of the same page apart, since they come from different ads. Calls from ads have no landing page, so this report's conversions are fewer than the account's; say so.

18. Where the searchers are: the ad funnel by the searcher's state or province.
```sql
SELECT campaign.name, segments.geo_target_region, metrics.impressions, metrics.clicks,
       metrics.cost_micros, metrics.conversions
FROM user_location_view
WHERE segments.date BETWEEN 'START' AND 'END' AND metrics.impressions > 0
```
Each click has one searcher location, so the rows add up to the account's clicks and leads. Compare each region's click-to-lead rate with the rest; regions with under 30 clicks are added together into "other regions" for the test, never graded one by one. Read a campaign that targets other places on purpose (an out-of-state campaign) with that in mind.

19. Region names. Call 18 returns regions as ids (`geoTargetConstants/<id>`); name the ones in the report.
```sql
SELECT geo_target_constant.resource_name, geo_target_constant.name,
       geo_target_constant.country_code, geo_target_constant.target_type
FROM geo_target_constant
WHERE geo_target_constant.resource_name IN ('geoTargetConstants/<REGION_ID_1>', 'geoTargetConstants/<REGION_ID_2>')
```

Run calls 13, 14 and 15 again for the comparison window.

**Meta Ads.**
```json
{"platform": "facebook-ads", "action": "get_insights_adaccount", "ad_account_id": "<META_AD_ACCOUNT_ID>",
 "level": "account", "time_range": {"since": "START", "until": "END"},
 "fields": ["spend", "impressions", "inline_link_clicks", "actions"]}
```
Use `inline_link_clicks` as the click step. In `actions`, count only the action types that match the funnel's goal (such as `lead` or `purchase`); never add every action type together.

**LinkedIn Ads.**
```json
{"platform": "linkedin-ads", "action": "get_account_analytics", "ad_account_id": "<LINKEDIN_AD_ACCOUNT_ID>",
 "start_date": "START", "end_date": "END", "time_granularity": "ALL",
 "fields": ["impressions", "clicks", "costInUsd", "externalWebsiteConversions", "oneClickLeads"]}
```
Lead-form leads (`oneClickLeads`) never reach the site; show them as their own route.

**Search Console** (the organic steps).
```json
{"platform": "google-search-console", "action": "search_analytics", "site_url": "<GSC_SITE>",
 "dimensions": ["date"], "start_date": "START", "end_date": "END", "row_limit": 500}
```
Add up clicks and impressions from the date rows. Search Console lags 2 to 3 days, so count the dates that came back.

**Do the clicks arrive?** Compare each platform's clicks with GA4's sessions for the same channel in call 5 (Google Ads with Paid Search, Search Console with Organic Search, Meta and LinkedIn with Paid Social). Under 70% is a leak between the ad and the page: a slow page, a broken tag, consent banners, or redirects that strip the tracking. Above 100% usually means other sources share the channel.

**When GA4 isn't connected for this business,** run the funnel on the ad platform alone: eligible impressions → impressions → clicks → leads, with the site steps taken from the platform's own page-load and form actions (call 15 `all_conversions`) where they run in order. A page-load action with fewer conversions than the form after it is not a step before the form (the form also sits on other pages); leave it out and say so. Mark the GA4 rows **not connected** and say what they would add.

**Evidence for a landing-page leak (optional).** Slow mobile pages are a common cause of an arrival leak; check the leaking page's speed with Core Web Vitals Fixer (if installed) before blaming the copy. Microsoft Clarity, when connected, can add behaviour signals (dead clicks, rage clicks, quick backs) for the same page through its `query_dashboard` action; that path is untested until a Clarity project is connected.

## Part 4: diagnose

**Step rates.** For every transition: sessions (or impressions, clicks) entering, leaving, the step rate, and the share of the first step still left. Show the funnel as a map:

```
STEP                 ENTERING   STEP RATE   LOST
Impressions            12,000
Clicks                    840      7.0%     11,160
Leads                     210     25.0%        630
Qualified leads     not tracked
```

**Is the drop real?** A gap between two rates is real only when it is larger than twice its standard error: for rates p1 and p2 on n1 and n2 entering, the gap must exceed 2 × √(p(1−p)(1/n1 + 1/n2)), where p is the pooled rate. Below that, call it noise. Never grade a transition with fewer than 30 entering, and never compare a segment with fewer than 30.

**What to compare with.** Each rate has one reference, and that reference alone sets its severity. The other comparisons are shown next to it as context and never change the grade, even when they disagree.

| Rate | Graded against | Shown as context |
|---|---|---|
| Each transition of the whole funnel (account level) | the same step in the comparison window, when tracking was steady in both | the usual range |
| A campaign's impression share and click rate | the campaign's own comparison window. Both depend on the campaign's keywords, budget and competition (a brand campaign's click rate is naturally several times a generic one's), so they are never graded across campaigns | the other campaigns |
| Click-to-lead and the site steps of a segment (campaign, device, channel, new or returning, country or region, landing page) | everyone else on the same step in the same window. Compare like with like: leave brand campaigns out of the group a non-brand campaign is measured against, and grade a brand campaign against its own comparison window | the segment's own comparison window |

**Rough starting points.** The "low below" line is a floor that always applies, with or without history: a rate under it is at least High, whatever its reference says. The ad lines are for non-brand traffic, so they apply to non-brand campaigns and to account totals, never to a brand campaign. The usual range becomes the reference only when there is no history and no peer group to compare with (a new account, or the first month of tracking). Both are rules of thumb, not benchmarks for your industry; replace them with the business's own numbers as soon as it has 3 months of history.

| Transition | Low below | Usual range |
|---|---|---|
| Session → engaged session | 40% | 50–70% |
| Session → form start (lead gen) | 3% | 5–20% |
| Form start → submit | 30% | 40–65% |
| Session → signup start (SaaS) | 3% | 5–15% |
| Signup start → signup complete | 50% | 60–85% |
| Product view → add to cart | 4% | 5–15% |
| Add to cart → checkout start | 30% | 40–65% |
| Checkout start → purchase | 35% | 45–70% |
| Search ad impression → click (non-brand) | 2% | 3–10% |
| Search ad click → lead | 4% | 5–25% |
| Search impression share (non-brand) | 30% | 40–80% |

**Severity.** For each transition, and each segment of it:

| Severity | When |
|---|---|
| Critical | the rate is under half its reference, and the gap is real |
| High | the rate is 50–75% of its reference and the gap is real, or it is under the "low below" line (the floor, whatever the reference) |
| Moderate | 75–90% of its reference with a real gap, or any real gap of at least 5 points |
| Normal | anything else (including gaps that are noise) |

**Impact.** For each leak: the conversions a month it costs = entering × (reference rate − current rate) × the rate from the next step to the final step, scaled to 30 days. Multiply by the value per conversion when the user gave one. Where ads pay for the step, also show the spend that went through the leaking segment and its cost per conversion against the account's. For missed impressions, split them into those lost to budget (the fix is budget) and those lost to rank (the fix is bids or ad quality). Each = eligible impressions × that lost share × the campaign's own click rate × its click-to-conversion rate, stated as a ceiling, because the extra impressions are usually lower quality. Count the budget-lost part only on a campaign whose cost per conversion is at or below the account's; buying more of an expensive campaign is not a fix. The leak's impact is the larger part that counts; name that part as the counted part, and when the budget part was left out although it was the bigger loss, say so.

**High or low impact.** A leak is high impact when it costs at least 5% of the window's conversions, or when its excess spend (spend − its conversions × the account's cost per conversion) is at least 10% of the window's spend. Everything else is low impact.

**Causes.** A hypothesis per leak, with the evidence that would confirm it and the call or skill that checks it:

| Stage | Symptom | Likely causes | Evidence |
|---|---|---|---|
| Above the site | impressions fall, share lost to budget | budget caps the best campaign | call 13; a budget move |
| Above the site | low click rate on one campaign | broad match or ad text that doesn't fit the search | search terms, ad copy |
| Arrival | clicks don't become sessions | slow page, tag missing, redirects | the click-to-session check, page speed |
| Arrival | sessions don't engage | the page doesn't match the ad, slow on mobile, wrong audience | landing-page rates (call 8 or 17), device split, page speed |
| Consideration | key page seen, no form start or add to cart | value unclear, price shock, no proof | page steps (call 7), pricing page |
| Action | form starts, few submits | too many fields, errors, a required phone number, no reassurance | lead form report (call 9) |
| Checkout | checkout starts, few purchases | surprise costs, forced account, few payment options | checkout steps by device |
| After conversion | leads that never qualify, signups that never activate | wrong promise in the ad or page, slow follow-up | qualify and activation events |

A hypothesis is never presented as the cause. Say what would prove it: a session recording, a form-field report, a test.

**Fixes to try, by stage.** Pick from these only after the evidence points at the stage:

| Stage | Fixes to try |
|---|---|
| Above the site | move budget to the campaigns with the cheapest conversions; tighten match types and add negatives from real search terms; ad text that repeats the searcher's words |
| Arrival | a landing page per intent instead of the home page; a faster mobile page; a headline that answers the ad |
| Consideration | lead with the outcome and proof (results, reviews, guarantees); show a price or a starting price with what's included; a comparison page |
| Action | fewer form fields; an optional phone number; errors shown next to the field; a progress bar on multi-step forms; say what happens after submitting |
| Checkout | all costs shown before checkout; guest checkout; wallets and more payment options; a reminder for abandoned carts |
| After conversion | same-day follow-up for leads; a quick first win in onboarding; a clear trigger to upgrade |

**Funnel health score.** Start at 100. Take off 20 for each critical transition, 10 for each high and 4 for each moderate. Each transition counts once, at the worse of its account-level severity and its worst segment's. Grade: 85–100 A (well tuned), 70–84 B (healthy, clear wins), 55–69 C (leaks are costing conversions), 40–54 D (several stages broken), under 40 F (fix now). **Not graded** when the final step isn't measured or, on the GA4 path, tracking isn't steady across the window; say which.

## Report format

1. **Summary:** funnel type, windows, source per step, entering and converting volume, the overall rate, the score and grade (or "not graded" and why), and in one line each: the biggest leak, its likely cause, the first fix.
2. **The funnel map** with every step, including the "not tracked" ones.
3. **Transition table:** one row per transition of the whole funnel, labelled account level: entering, rate, comparison-window rate, reference, real or noise and the account-level severity, plus the worst segment severity on that transition. The score counts the worse of the two.
4. **Segments:** device, channel, new or returning, country or region, campaign and landing page, only where the gap is real or the segment is large; say "no real gap" where there is none.
5. **Priority matrix:** every leak found gets a fix, and each fix is placed by impact (high or low, as defined above) and effort (low, medium, high): do first (high impact, low or medium effort), plan next (high impact, high effort), quick wins (low impact, low effort), later (the rest). Trust fixes always go in "do first".
6. **Top 5 fixes:** trust fixes first, then by conversions a month. Each with the step, the current and target rate, the impact, the cause hypothesis and its evidence, the fix, effort, and the skill to go deeper.
7. **Tests:** for the top 3 leaks, a test written as "if we change X, step Y's rate rises from A to B, because C". For a page or form leak, give the sessions (or clicks) each version needs to detect that lift (95% confidence, 80% power: 7.85 × (p1(1−p1) + p2(1−p2)) ÷ (p2 − p1)²) and how many months that takes at today's volume; when it is more than 2 months, say so and suggest a before-and-after comparison with the same gap test instead. For a budget leak, a stepped budget test with a stop rule (stop when the cost per conversion passes the account's).
8. **Monitoring:** for each step, the current rate, a warning line (the comparison window's rate minus its 2-standard-error band) and a critical line (half the reference), checked weekly. Add the mobile-versus-desktop gap on the conversion step, with the gap that would count as real at today's volume as its warning line.
9. **What couldn't be checked,** and why. For each step marked not tracked, name the event or import that would add it (for example `generate_lead`, `qualify_lead`, or an offline import of signed deals into the ad platform).

## Design a funnel

When the user has no funnel yet, or asks for funnel ideas, map one before diagnosing:

| Stage | The question it answers | What moves people on | How it's measured |
|---|---|---|---|
| Awareness | Do the right people find us? | search, social, partner and ad reach | impressions, Search Console impressions |
| Interest | Do they want to know more? | a page that matches the search or the ad | engaged sessions, scroll |
| Consideration | Do they believe it fits them? | proof, comparisons, pricing, a demo or sample | key page views, return visits |
| Conversion | Do they act? | one clear action with little effort | the key event |
| Retention and referral | Do they stay and bring others? | onboarding, follow-up email, referral offers | repeat purchase, activation, referrals |

Use the data the skill pulled: which channels already bring engaged sessions (call 11), which pages already lead to action (call 8), and which stages have no event yet. For each stage give two or three ideas that fit the business, the event that measures it, and the target to beat next month. Ideas to draw on: a lead magnet or quiz for interest, a comparison or calculator page for consideration, a shorter form or a calendar booking for conversion, a remarketing audience built from the drop-off step, a welcome or onboarding sequence for retention.

## Fixes this skill can run

Only after the user confirms each one, with the exact payload shown first. Both need a Read & Write connection, and an owner, admin or operator can switch them off. It never changes the site, the ads, tags or forms; those it writes up as recommendations.

**Mark the goal as a key event,** when the final step fires but isn't a key event (call 1):
```json
{"action": "create_key_event", "property_id": "properties/<id>",
 "event_name": "generate_lead", "counting_method": "ONCE_PER_SESSION"}
```

**Build a drop-off audience** for remarketing, for example people who started the form in a session and didn't submit it in that session. First list the existing audiences, so the skill never creates one that already does the same job:
```json
{"action": "list_audiences", "property_id": "properties/<id>"}
```
Then, after the user confirms (`membership_duration_days` can't be changed later):
```json
{"action": "create_audience", "property_id": "properties/<id>",
 "display_name": "Form started, not submitted (30 days)",
 "description": "Started the lead form and did not submit it in the same session",
 "membership_duration_days": 30,
 "filter_clauses": [
   {"clauseType": "INCLUDE", "simpleFilter": {"scope": "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION",
     "filterExpression": {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [
       {"eventFilter": {"eventName": "form_start"}}]}}]}}}},
   {"clauseType": "EXCLUDE", "simpleFilter": {"scope": "AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION",
     "filterExpression": {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [
       {"eventFilter": {"eventName": "form_submit"}}]}}]}}}}]}
```
The same shape builds "added to cart, no purchase" or "saw pricing, no signup" (swap the events).

Offer them only when they apply: no key event for a goal that never fires, and no audience for a step with under 100 sessions a month.

## Without a connection

If the user hasn't connected GA4 or an ad platform, ask for each step's name and count (sessions or users), ideally by device and source, for the window and the one before it. Run Parts 1 and 4 on those numbers, mark every figure "from your data, not checked", and say which calls above would replace them once connected.

## Rules

- One business per funnel. Never mix accounts of different companies.
- Trust fixes come before drop-off fixes. A funnel whose final step isn't measured is not graded.
- Every rate shows its entering count. Nothing with fewer than 30 entering is graded (show it as "not graded"), no segment comparison on fewer than 30 per side, and no gap called real without the test.
- Open funnel, stated: steps are sessions with each event, not ordered paths.
- Never add users across rows, and never add up several pages as one step.
- Count conversions only from the actions the platform counts, and say how leads arrive (call, form, tap).
- Impact is in conversions a month, and in money only with a value the user gave or the platform's own value. Ad spend is shown as spend and excess spend, never as lost revenue.
- A cause is a hypothesis with its evidence, never a fact.
- Write actions only after confirmation, one at a time.

## Go deeper

- Page-level fixes for a leaking landing page: Landing Page Auditor; the form itself: Form CRO; signup steps: Signup Flow CRO; after signup: Onboarding CRO.
- The ad-to-page match behind an arrival leak: Ad Landing Page Match Scorer.
- Checkout and product steps for a store: GA4 Ecommerce Funnel (if installed).
- Budget moves for impressions lost to budget: Budget Allocation Optimizer.
- Tests for the top leaks: A/B Test Designer.
