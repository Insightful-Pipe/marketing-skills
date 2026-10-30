# How to Use This Skill

Hey Claude, I just added the "campaign-launch-preflight" skill. Check whether my campaign is ready to launch and tell me what would stop it.

## What you need

- **The InsightfulPipe MCP connected to Claude,** with the ad account the campaign runs in (Google Ads, Meta or LinkedIn Ads). The skill reads it itself; you don't export anything.
- **GA4 and Search Console for the landing page's site,** so it can check that the site measures the result. Without them, those checks come back unknown.
- **Notion,** only if your campaign brief lives there.
- **The plan:** the campaign, the daily budget, the start date, the landing page URL with its tracking parameters, and the result you judge it on. The skill asks for anything it can't find.

## Example requests

**Before launch**
Hey Claude, I just added the "campaign-launch-preflight" skill. We switch on the LinkedIn campaign "Spring webinar" on Monday at $80 a day, sending people to our webinar page. Is it ready?

**Before raising a budget**
Hey Claude, I just added the "campaign-launch-preflight" skill. I want to raise the budget on my Google Ads campaign "Generic - Search" from $100 to $150 a day. Is it safe?

**From a Notion brief**
Hey Claude, I just added the "campaign-launch-preflight" skill. Read the "Q4 retargeting" brief in Notion, check the Meta campaign against it, and post the verdict on the brief.

**Launch readiness across tracking, pages and budget**
Hey Claude, I just added the "campaign-launch-preflight" skill. Run a launch readiness check on tracking, landing page and budget for my new Google Ads campaign before I enable it.

## What you get

1. **A verdict:** GO, GO WITH FIXES or NO-GO.
2. **Blockers first,** each with its number, its fix, and who can make it.
3. **A checklist** across eight areas:
   - the account can spend
   - the campaign will serve
   - the ads are approved and on
   - the platform sees the result
   - the site's analytics sees the result
   - the landing page works
   - the budget can buy enough results
   - in scale mode, whether more budget is safe
4. **A budget estimate** built from your account's own past costs, or the budget steps when scaling.
5. **A list of what couldn't be checked,** and why.

## What it can change for you

Only after your yes on the exact change, it can do the following. It never switches anything on or raises a budget on a NO-GO.
- switch on a LinkedIn campaign group, creative or campaign, or set its daily budget
- enable a Google Ads campaign or set its daily budget
- set a Meta campaign or ad set budget (Meta's API doesn't switch campaigns on, so you activate them in Ads Manager)
- post the verdict as a comment on your Notion brief

It never pauses or removes anything, and it never changes targeting, bids or what your ads say.

## Tips

- Give the landing page URL exactly as the ad will use it, with its UTMs. The skill checks that the page keeps them.
- Run it again after you fix the blockers. The verdict should move.
- Before a big budget change, plan a few steps of up to 20% each. The skill shows them.
