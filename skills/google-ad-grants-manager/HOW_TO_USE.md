# How to Use This Skill

Hey Claude, I just added the "google-ad-grants-manager" skill. Check our Google Ad Grants account against every grant rule, tell me what to fix first, and show me how to use more of the grant.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ad Grants account added.** The skill pulls the data itself. No connection? Paste or upload the keyword report (with Quality Score), the campaign report by month, and your sitelink, location and conversion action lists.
- **Google's compliance email,** if you got one. Paste it and the skill starts with the rule it names.
- **Your brand words and any approved medical terms,** so it doesn't flag them as single-word keywords.
- **When the grant account was created,** if you know. Accounts created on or after 22 April 2019 must use conversion-based Smart Bidding.

## Example requests

**Got a warning email**
Hey Claude, I just added the "google-ad-grants-manager" skill. Google says our Ad Grants account missed the 5% CTR rule last month. Here's the email. What do I pause so we don't get deactivated?

**Monthly compliance check**
Hey Claude, I just added the "google-ad-grants-manager" skill. Run the monthly Ad Grants compliance check on our account and list anything that breaks a rule.

**Account won't spend**
Hey Claude, I just added the "google-ad-grants-manager" skill. We only spend about a third of our 10,000 USD grant. Show me where the rest could go without hurting our CTR.

**From exports, no connection**
Hey Claude, I just added the "google-ad-grants-manager" skill. I've attached our keyword report with Quality Score and our campaign report for the last three months. Check them against the grant rules.

**Check, then fix**
Hey Claude, I just added the "google-ad-grants-manager" skill. Check our grant account, then pause the keywords that break the rules. Show me the list and the CTR after the change first.

## What you get

1. **Account CTR by month,** and what happens, by when, if nothing changes.
2. **A compliance scorecard:** the 5% CTR rule, Quality Score 1 or 2, single-word and generic keywords, 2 ad groups per campaign, 2 sitelinks, geo-targeting, Smart Bidding, conversion tracking and the program survey, each naming the exact keywords, campaigns or conversion actions behind it.
3. **A CTR fix plan:** the keywords to pause, in order, with the account CTR after each one. A keyword that brings conversions is never paused just to lift CTR; only a rule break can put it on the list.
4. **Above the 2 USD cap:** how many of your conversions came from keywords that average more than the 2 USD manual bid limit under Maximize conversions.
5. **A spend plan:** your headroom under the grant, budget-limited campaigns with an upper bound on extra spend, campaigns to move to Maximize conversions, and new keywords taken from your own search terms.

## What it can change for you

With your yes on the exact change, through a Read & Write connection, it can:
- pause keywords (never remove them)
- add replacement keywords you approve
- add negative keywords from your own search terms
- add sitelinks
- set campaign locations

It never changes bids, budgets, bid strategies or conversion actions. It tells you the exact setting to change in Google Ads.

## Tips

- Run it in the last week of every month, while there's still time to lift that month's CTR.
- Run it again before you request reinstatement: Google checks that the last week's CTR is at least 5%.
- Google updates the Ad Grants rules from time to time. If your compliance email says something different, the skill follows the email.
