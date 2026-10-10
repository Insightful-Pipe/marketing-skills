# How to Use This Skill

Hey Claude, I just added the "facebook-ads-launch-checklist" skill. Check my paused Meta campaign before I switch it on, and tell me what will break.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta ad account added.** The skill reads the campaign, ad sets, ads, creatives, pixel, budgets and landing page itself; you don't need to export or screenshot anything.
- **Which campaign,** if the account has more than one waiting. Without it, the skill lists the paused campaigns that haven't ended and asks.
- **When it should run and what it's for:** the start and end dates, the result you want (sales, leads, site visits, engagement), what you're advertising and where you sell.

Not connected yet? Describe the setup or share screenshots, and the skill runs the same checklist, marking what it couldn't read as items for you to confirm.

## Example requests

**Before a new launch**
Hey Claude, I just added the "facebook-ads-launch-checklist" skill. I built a leads campaign in Ads Manager and it's paused. Check it before I turn it on tomorrow.

**Relaunching an old campaign**
Hey Claude, I just added the "facebook-ads-launch-checklist" skill. I want to run last month's campaign again for a week from Monday. What do I need to change?

**A new ad account or a new client**
Hey Claude, I just added the "facebook-ads-launch-checklist" skill. I just took over this client's Meta ad account. Check the account and their first campaign before we spend anything.

**Launched, but nothing is coming in**
Hey Claude, I just added the "facebook-ads-launch-checklist" skill. My campaign went live yesterday and shows no conversions. Run the checklist and show me what's wrong.

## What you get

1. **A verdict:** READY, READY WITH FIXES or NOT READY, with the blockers first.
2. **A three-tier checklist:** critical (account, page identity, dates, ads that can serve, tracking for the goal, Meta's budget floor, landing page, special ad category), important (goal and conversion event fit, learning volume, audience size and targeting, exclusions, creative specs, copy, landing page speed and match) and optimisation (ads to test, UTMs, names, placements, attribution, bid strategy, campaign or ad set budget). Every row shows the value it was judged on.
3. **A sign-off list** of what only you can check, such as a test conversion, Conversions API deduplication, the pixel firing on every page and the landing page on a phone, and where to look.
4. **A plan for the first week** after launch.

## What it can change for you

With your yes on the exact change, it can:
- move an ad set's start or end date
- raise a daily budget to Meta's minimum or to your plan
- rename campaigns, ad sets and ads
- add UTMs, by making a copy of the creative with tracking tags and pointing the ad at it
- change an ad set's age or location targeting, when you ask for that change in words

It never switches anything on: you do that in Ads Manager once the checklist is clear.

## Tips

- Run it after the campaign is fully built and paused, not halfway through setup.
- Run it again after the fixes. The verdict should move.
- If you advertise credit, jobs, housing or politics, say so: the special ad category check depends on it.
