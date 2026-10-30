# How to Use This Skill

Hey Claude, I just added the "keyword-performance-analyzer" skill. Go through my Google Ads keywords for the last 30 days: which ones make money, which ones waste it, and what should I pause?

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls keywords, Quality Score, search terms, conversion settings, locations and serving status itself; you don't export anything.
- **Your target CPA or target ROAS per campaign,** if you have one. Campaigns with a ROAS target (yours, or a Target ROAS setting in the account) are judged on ROAS; the rest on CPA. Without a target, the skill uses each campaign's own target CPA setting, then its 30-day CPA, then the account's non-brand CPA, and says which one it used.
- **A date range,** if you want one other than the last 30 complete days.
- **What a conversion is worth,** if your account doesn't record conversion values. Without it, profit per keyword is marked as not graded instead of guessed.

No connection? Export the Keywords report (with Quality Score and its components) and the Search terms report (with the Keyword column) for the date range and attach them. The location and serving-status checks are then marked unknown.

## Example requests

**Full keyword review**
Hey Claude, I just added the "keyword-performance-analyzer" skill. Review every keyword in my Google Ads account and tell me which to keep, fix or pause.

**Profit per keyword**
Hey Claude, I just added the "keyword-performance-analyzer" skill. A lead is worth about $300 to us. Which keywords make a profit and which lose money?

**Duplicates and cannibalisation**
Hey Claude, I just added the "keyword-performance-analyzer" skill. Are my ad groups bidding against each other? Find duplicate keywords and search terms that show up in more than one ad group.

**ROAS target**
Hey Claude, I just added the "keyword-performance-analyzer" skill. My search campaigns run on a 400% target ROAS. Which keywords fall below it over the last 90 days?

**Broad match**
Hey Claude, I just added the "keyword-performance-analyzer" skill. Which of my campaigns are ready to test broad match?

**Low search volume**
Hey Claude, I just added the "keyword-performance-analyzer" skill. Which of my keywords have low search volume, and which can I remove without losing anything?

**Pause above target**
Hey Claude, I just added the "keyword-performance-analyzer" skill. My target CPA is $60. Pause the keywords that cost more than twice that. Show me the list first.

## What you get

1. **A keyword health colour** (green, yellow or red) with the math shown, the account currency and dates, and the target used for each campaign (CPA or ROAS) with its source.
2. **A scorecard for seven areas:** keyword tiers and waste, profit with conversion value, Quality Score, match types and cannibalisation, duplicate keywords, ad group theme drift, and low search volume.
3. **Up to 6 top actions,** ranked by the spend they touch, each with the query and numbers behind it.
4. **Tables:** stars, bleeders, Quality Score victims, the pause list, a review list, match type health with a Migrate to Exact list (steady phrase converters that deserve an exact version), cannibalised search terms, duplicates, off-theme terms by ad group, low-volume keywords by campaign, and broad match readiness per campaign.
5. **Bid advice where bids matter:** keyword bid changes for Manual CPC campaigns; for automated bidding, advice on the campaign target instead.
6. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- pause keywords on the pause list
- change keyword CPC bids in Manual CPC campaigns
- add exact or phrase negative keywords taken from your own search terms

It never pauses brand keywords and never changes budgets, targets or bidding strategies.

## Tips

- Set a real target CPA per campaign. Without one, keywords that convert at a high CPA go to a review list instead of the pause list.
- Google hides low-volume search terms, so the search-term checks cover only the visible share of spend. The report states that share.
- Run it monthly, and again a few weeks after pausing or restructuring, to let conversions catch up.
