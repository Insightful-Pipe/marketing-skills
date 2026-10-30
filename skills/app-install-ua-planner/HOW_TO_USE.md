# How to Use This Skill

Hey Claude, I just added the "app-install-ua-planner" skill. Plan our paid user acquisition for the next 4 weeks: what we can afford to pay per install, where the next dollar should go, and which network to open next.

## What you need

- **Your cohort revenue curve** for iOS and Android: cumulative net revenue per install at day 7, day 30 and your payback day, from your measurement partner (AppsFlyer, Adjust, Singular, Branch) or your subscription tool. Paste it or upload the export.
- **The share of installs** that start a trial, subscribe or purchase within 7 days.
- **Your payback day and margin**, and a budget cap for the next 4 weeks. Without them the skill uses day 180 for a subscription app (day 90 otherwise), break-even, and last month's spend plus 20%.
- **Results by network**, if nothing is connected: spend, installs and day 7 revenue for each network on each platform over the last 28 days of install cohorts, in two 14-day halves.
- **Optional, the InsightfulPipe MCP** with Google Ads, Meta Ads, TikTok Ads or Snapchat Ads connected. The skill then pulls each network's app campaign spend, installs and optimization goal itself, and reads your App Store and Google Play listings. Apple Ads has no connector; paste its campaign report.

## Example prompts

**Full plan:**
> Plan our app install campaigns for the next 4 weeks. Payback by day 180 with a 15% margin, $110,000 cap. Here is our AppsFlyer cohort export.

**Max CPI only:**
> Here is our day 0 to day 180 revenue per install for iOS and Android. What is the most we can pay per install, and what day 7 ROAS should each campaign hit?

**Where the next dollar goes:**
> Our Meta iOS CPI keeps climbing as we spend more. Score every network we run and tell us where to move budget.

**Lower CPI:**
> How do we lower CPI for our app installs? Check which networks have creative fatigue and which events our campaigns should optimize for.

**Open a new network:**
> We run Apple Ads, Meta and TikTok on iOS. Should we add Google App campaigns or AppLovin next, and how big should the test be?

## What you get

- What one install is worth on each platform: max CPI, the day 7 ROAS target, a day 30 checkpoint, and the max cost per trial start or purchase.
- A scorecard for every network on every platform: CPI per half, day 7 ROAS, projected payback ROAS, what the next installs cost, a creative fatigue flag, and a verdict (scale, hold, trim, cut and fix, pause, too few installs to judge, unknown).
- A week-by-week budget for the next 4 weeks under your cap, with a Monday check before each scale step.
- The network to open next, with its event, target cost and test budget.
- The event each campaign should optimize for, the creative each network needs, store listing checks and the measurement gaps to close.

The skill changes nothing in your ad accounts. You make the budget changes, or hand the plan to a campaign-building skill.
