# How to Use This Skill

Hey Claude, I just added the "applovin-ads-analyzer" skill. Review my AppLovin campaigns for the last 30 days and tell me which ones hit goal and what to fix first.

## What you need

- **Your AppLovin data,** one of two ways:
  - the InsightfulPipe MCP connected to Claude with your AppLovin Ads account added, so the skill pulls the reports itself; or
  - an AppLovin dashboard CSV of the last 30 days, broken down by day, campaign, country and creative set, with cost, impressions, clicks, results and 7-day revenue or ROAS.
- **Your target** per campaign: a cost per install, cost per purchase, cost per lead or a ROAS. Without one, it uses the goal set on each campaign, or your own average, and says so.
- **Your daily budgets,** if the connection has only AppLovin's Reporting Key or you're working from a CSV. Pacing needs them.
- **Meta and TikTok,** connected or as totals for the same dates, if you want the comparison.

## Example requests

**Store (web) account review**
Hey Claude, I just added the "applovin-ads-analyzer" skill. We sell outdoor gear and run AppLovin web campaigns. Review the last 30 days against each campaign's own goal and tell me which countries and creatives drag.

**App account review**
Hey Claude, I just added the "applovin-ads-analyzer" skill. Review our AppLovin app campaigns. Our target is $4 per install on Android and a 7-day ROAS of 0.3 on the iOS purchase campaign.

**From a CSV export**
Hey Claude, I just added the "applovin-ads-analyzer" skill. Here's our AppLovin dashboard export for the last 30 days by day, campaign, country and creative set. Our daily budgets are $600 and $900. Target is $45 a purchase.

**AppLovin beside Meta and TikTok**
Hey Claude, I just added the "applovin-ads-analyzer" skill. Is AppLovin cheaper per purchase than Meta and TikTok for us? Put all three on one scale for the same days.

**New campaign check**
Hey Claude, I just added the "applovin-ads-analyzer" skill. We launched a holiday campaign on AppLovin two weeks ago. Has it reached its goal yet, and did our early changes slow it down?

**Review, then fix creative**
Hey Claude, I just added the "applovin-ads-analyzer" skill. Find our worn creative sets, then add these two new videos to the worst one. Show me the exact change first.

## What you get

1. **A campaign table** with a verdict for each campaign (scale, hold, fix, cut or too early), spend, results, cost per result, ROAS, ratio to target, money at stake and pacing.
2. **Top actions** ranked by money at stake, each with the numbers behind it and who does it.
3. **Countries** that drag a campaign below target, with the campaign's ratio with and without each one.
4. **Time to goal** for campaigns that started in the window.
5. **Worn creative sets and assets,** and sets with too few videos.
6. **Pacing and recent changes** that reset what AppLovin's model learned.
7. **AppLovin beside Meta and TikTok** on one cost-per-result scale, plus a GA4 or Shopify check for stores.
8. **A scorecard** and a list of what couldn't be checked, and why.

## What it can change for you

With your yes on the exact change, and AppLovin's Campaign Management key on the connection, it can:
- copy a winning creative set into another campaign
- add fresh assets you supply to a worn creative set
- pause a worn creative set

It tells you first when a change will start serving straight away. It never changes budgets, goals, bids or countries.

## Tips

- Ask for the last 30 days. The last 8 are shown as still maturing, because 7-day purchases keep arriving.
- If the report says "too early", it also tells you how much more spend and how many more days it needs.
- Run it again a week after a change to see the verdicts move.
