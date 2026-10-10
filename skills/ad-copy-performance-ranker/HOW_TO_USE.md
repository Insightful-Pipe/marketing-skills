# How to Use This Skill

Hey Claude, I just added the "ad-copy-performance-ranker" skill. Rank my responsive search ads and tell me which headlines and descriptions are working and which to replace.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the ads, the numbers for every headline and description, and Google's ratings itself; you don't need to export anything.
- **Your brand terms,** if your brand campaign doesn't have "brand" in its name. Brand ads are ranked on their own so they don't skew the baseline.
- **No connection yet?** Export the Ads table and the Assets table for your responsive search ads (last 30 days) from Google Ads and paste them in. The ranking and line checks still run; the combinations and the actions don't.

## Example requests

**Full ad copy review**
Hey Claude, I just added the "ad-copy-performance-ranker" skill. Pull my RSAs for the last 30 days, rank them, and show me the winning headlines and the patterns behind them.

**Find the weak ads**
Hey Claude, I just added the "ad-copy-performance-ranker" skill. Which of my ads are underperforming and need new copy? Only call a loser where the numbers are clear.

**Headline ideas from what works**
Hey Claude, I just added the "ad-copy-performance-ranker" skill. Based on my best headlines, suggest new ones to test, and only use claims my ads already make.

**Ad strength reality check**
Hey Claude, I just added the "ad-copy-performance-ranker" skill. Are my "Excellent" and "Good" ads actually performing better, or is ad strength misleading me?

## What you get

1. **A health light** (red, yellow or green) with the reasons, and the share of your spend that runs on responsive search ads.
2. **Every serving ad ranked** by conversions per 1,000 impressions against your own non-brand baseline, in five tiers from Star to Underperformer. Ads with too little data are listed but not ranked, and brand ads are ranked on their own.
3. **Head-to-heads inside each ad group,** with a significance test on CTR, conversion rate and conversions per impression, so a loser is called only when the numbers are clear.
4. **Ad strength against real results,** by band and head-to-head.
5. **Every headline and description scored:** how often Google serves it, whether it earns more clicks than its ad's average, Google's rating, and a verdict: keep, watch, replace, rewrite or too early.
6. **The copy angles that win** (proof, offers, questions, calls to action and more), any gaps, and the weak headlines: feature-only lines that just name the service, and generic ones that could run for any business.
7. **Every description audited:** whether it uses 80 or more of its 90 characters, has a call to action, and gives a reason to choose you (proof, an offer or the searcher's problem), plus the ad groups whose descriptions have no proof, no offer or no call to action.
8. **Copy hygiene:** lines about the wrong service, single-line pins, policy problems, and the combinations Google serves most.
9. **New headlines and descriptions** with character counts, built from what already works, plus pinning advice and up to five quick wins.

## What it can change for you

With your yes on the exact change, it can:
- create a challenger ad (always created paused) from the lines that work plus the suggested ones
- turn that challenger on after you've reviewed it
- pause an ad that clearly lost its head-to-head
- rewrite an ad's lines in place

It never sets pins, bids, budgets or keywords, and it never deletes an ad. Rewriting an ad in place may reset its pins, so check them in Google Ads afterwards.

## Tips

- Run it monthly. Line data needs volume: an ad under 500 impressions gets "too early" on its lines.
- When it creates a challenger, leave both ads running for about 30 days, then run it again to read the head-to-head.
- To write a full new ad for one ad group from its keywords and landing page, use `rsa-ad-copy-writer` if you have it.
