# How to Use This Skill

Hey Claude, I just added the "paid-organic-overlap" skill. Am I paying Google Ads for searches I already rank #1 for? Tell me which keywords to bid down.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the data itself; you don't need to export anything.
- **Search Console for the same site, if you have it.** It gives Google's own organic positions. Without it, the skill uses DataForSEO rankings for your domain.
- **DataForSEO connected** for the live results-page check (one rankings call and up to 5 page checks a run).
- **Your target CPA,** if you have one. Without it, the skill uses your account's own CPA for the window.

## Example requests

**The #1 question**
Hey Claude, I just added the "paid-organic-overlap" skill. Which keywords do I rank #1 for organically and still pay for in Google Ads? Should I bid them down?

**The full overlap**
Hey Claude, I just added the "paid-organic-overlap" skill. Show me how my paid and organic search overlap for the last 30 days, and where each one is doing the other's job.

**Brand spend**
Hey Claude, I just added the "paid-organic-overlap" skill. We rank first for our own name. Is our brand campaign wasting money?

**SEO versus ads**
Hey Claude, I just added the "paid-organic-overlap" skill. Which converting search terms have no page in the organic results, so ads carry them alone? And which organic terms should we test with ads?

## What you get

1. **The overlap at a glance:** your visible search terms split by organic rank (1, 2 to 4, lower, or not in the organic data), with spend and conversions for each group.
2. **The terms that rank at the top,** checked on the live results page in the area your campaigns target: your organic rank, your map-pack slot, AI Overviews and any ads seen.
3. **A verdict for each:** bid-down test, defend, or keep. Each one is priced by what a conversion the ad really adds would cost, using Google's published research on how many ad clicks are new at each organic rank.
4. **A test plan** for each bid-down candidate: the exact change for your bidding strategy, the savings estimate, the conversions at risk and when to undo it.
5. **SEO gaps the ads are covering,** and **organic terms with no visible ad traffic** worth a paid test.
6. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- add a term as an exact-match negative keyword, to pause it in a Smart Bidding campaign for a test
- lower a keyword's bid in a Manual CPC campaign
- lower the CPC ceiling of a Target impression share campaign, such as a brand campaign

It never pauses campaigns, switches bidding strategies or moves budget.

## Tips

- Connect Search Console for the site your ads point to. The skill only compares your ads with that same site.
- Link Search Console inside Google Ads too, in its linked-accounts settings. It gives you a combined paid-plus-organic clicks baseline before a test.
- Treat a bid-down as a 4-week test, not a decision. Run the skill again after it to see what changed.
