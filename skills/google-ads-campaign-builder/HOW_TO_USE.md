# How to Use This Skill

Hey Claude, I just added the "google-ads-campaign-builder" skill. Build a new Search campaign for my service in my area at $25 a day. Draft it and show me the payloads; don't create anything yet.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill reads the account itself; you don't need to export anything.
- **A short brief:** the service or product, the place, and a daily budget. The landing page and the goal are optional: without them, the skill uses the most specific page your account has used for that service and the conversions your account already counts.
- **A Read & Write connection** if you want it to create the campaign after you approve the plan. With read access it still drafts everything.
- **For a keyword plan and budget forecast, no connection is needed.** Paste a Keyword Planner export (or seed terms with Google Ads or DataForSEO connected), your place, a budget or a lead goal, and your conversion rate. Add your close rate and the profit from a new customer to get a break-even CPA.
- **For a Smart campaign migration,** connect the account, or paste the Smart campaign's search terms with its budget, location and conversions by type.

## Example requests

**From a brief**
Hey Claude, I just added the "google-ads-campaign-builder" skill. Create a Search campaign for emergency plumbing in Denver, $40 a day, sending people to our emergency service page.

**Relaunch a service**
Hey Claude, I just added the "google-ads-campaign-builder" skill. We used to advertise expungement. Build a fresh campaign for it, and reuse whatever worked last time.

**Launch checklist only**
Hey Claude, I just added the "google-ads-campaign-builder" skill. Run the launch checklist on my Google Ads account. Is it ready for a new campaign?

**Build it**
Hey Claude, I just added the "google-ads-campaign-builder" skill. The plan looks good. Create it paused, and tell me what I still need to do in Google Ads before I turn it on.

**Keyword plan and budget forecast**
Hey Claude, I just added the "google-ads-campaign-builder" skill. How much should I spend on Google Ads to get 40 leads a month for garage door repair in Tucson? Here's my Keyword Planner export. About 12% of visitors contact us, we close 40% of leads, and a new customer is worth $180 in gross profit.

**Smart campaign to Search campaign**
Hey Claude, I just added the "google-ads-campaign-builder" skill. I run a Smart campaign for my grooming business. Look at the search terms it paid for and tell me if I should switch to a Search campaign, and how to do it without losing calls.

## What you get

1. **A launch checklist of 10 checks:** conversion tracking, location, shared negative lists, overlap with live campaigns, inherited assets and the landing page. Each one is pass, warn, fail or unknown, and you get a ready, ready with warnings or blocked verdict.
2. **What your account already knows:** any earlier campaign for the same service, with its spend, CPA, converting keywords and search terms.
3. **The campaign plan:**
   - settings
   - ad groups, with keywords and match types
   - negatives, each with a reason
   - a budget check, with clicks a day and conversions a month as estimates
   - one responsive search ad per ad group, with every line's character count and source
   - sitelinks and callouts
4. **The exact payloads,** in run order, each marked "not run" until you approve.
5. **Launch steps,** including anything that has to be done by hand in Google Ads.

In the keyword plan and budget forecast mode you get keyword groups with match types, a best, mid and cautious forecast of clicks, cost, leads and CPA, the spend your goal needs, a break-even CPA, the keywords your budget can't reach, and the busiest and quietest months. In the Smart campaign mode you get what the Smart campaign actually paid for, a keep, test or move verdict, the replacement Search campaign, and a staged budget switch-over.

## What it can change for you

With your yes on the plan, it creates:
- the campaign
- its location or radius targeting
- ad groups and keywords
- negatives
- responsive search ads
- sitelinks, callouts and a structured snippet

The campaign, its ad groups and its ads are created paused. Turning them on is a second, separate yes. It never changes a live campaign's budget, bids or status. The only change it may suggest to a live campaign is a negative keyword, and only when the new campaign would compete with it. The exception is a Smart campaign migration: there it lowers the Smart campaign's budget in stages and pauses it at the end, each step only after your yes.

## Tips

- Name the place the way people search for it: a state, a city or a postal code. The skill matches it to the location your live campaigns already use.
- If you used to run the service under a campaign name that doesn't mention it, say which campaign. The skill finds earlier campaigns by name, and their converting keywords and search terms are the best seed list you have.
- Run `search-term-gold-miner` a week after launch, if you have it, to see what the new campaign actually matched.
