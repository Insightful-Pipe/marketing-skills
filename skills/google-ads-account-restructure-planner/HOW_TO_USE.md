# How to Use This Skill

Hey Claude, I just added the "google-ads-account-restructure-planner" skill. Plan a restructure of my Google Ads account and write out exactly how to move, step by step.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill reads campaigns, ad groups, keywords, negatives, shared lists, sitelinks and conversion goals itself.
- **No connection?** Paste a campaign report by week and an ad group report with final URLs for the last 13 weeks. You get the same plan; the carry-over items you didn't export become manual checks.
- **Your brand terms,** if they aren't obvious from the account name.
- **Your own volume floors or CPA tolerance,** if you have them. Otherwise the skill uses its defaults and says so.

## Example requests

**Too many small campaigns**
Hey Claude, I just added the "google-ads-account-restructure-planner" skill. We have 11 Search campaigns and most get a handful of leads a month. Plan a consolidation and show me what each new campaign would have had over the last 90 days.

**Taking over an account**
Hey Claude, I just added the "google-ads-account-restructure-planner" skill. I inherited this Google Ads account. Is the campaign structure holding Smart Bidding back, and if so, how do I move without losing what works?

**Brand mixed into non-brand**
Hey Claude, I just added the "google-ads-account-restructure-planner" skill. Our brand keywords sit in a few service campaigns. Plan how to pull them out and what that does to each campaign's target.

**From an export**
Hey Claude, I just added the "google-ads-account-restructure-planner" skill. Here are my campaign and ad group reports for the last 13 weeks. Tell me what should merge, what should split, and in what order.

## What you get

1. **Before and after:** campaign count, and how many campaigns sit under the conversion volume their bid strategy needs.
2. **The proposed structure,** one block per campaign: what it absorbs, which ad groups are rebuilt or folded, and the pooled 90-day spend and conversions next to each part's own numbers.
3. **Budgets and targets:** spend-neutral budgets, and targets that start at the pooled cost per conversion, never tighter.
4. **A carry-over checklist:** negatives to carry, negatives that would block the keywords you move in, shared lists, sitelinks, schedules and duplicate keywords.
5. **A migration timeline:** a build week, one cutover per week, what to check in the first 48 hours and in weeks 1 to 4, and a rollback line taken from each move's own worst fortnight.
6. **Every payload,** marked not run.

## What it can change for you

With your yes on each exact step, it can rebuild ad groups and copy their best ad (both created paused), add keywords, carry negatives and sitelinks, and on the cutover day switch the new ad groups on, pause the old campaigns and set the new budget and bid strategy. It never removes anything, so every move can be undone. Removing a negative and attaching a shared list are done in Google Ads.

## Tips

- Run it when Smart Bidding campaigns keep sitting in "Learning" or missing their targets on thin data.
- One move a week, the cheapest first. Read weeks 3 and 4 against the rollback line before you judge a move.
- Run `bid-strategy-auditor` after the moves, if installed, to decide when a campaign has earned its target back.
