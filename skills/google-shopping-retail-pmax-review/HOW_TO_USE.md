# How to Use This Skill

Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. Review my Shopping and Performance Max campaigns product by product and propose a better structure. My target ROAS is 400%.

## What you need

- **Either the InsightfulPipe MCP connected to Claude with your Google Ads account added, or two exports:** the Shopping product report for the last 30 days and your product feed. With Google Ads connected, the skill pulls products, product groups, listing filters, item status and search terms itself.
- **Your target ROAS or target cost per sale,** if you have one. Without it, the skill sorts products against your retail campaigns' own 30-day ROAS and says so.
- **What your custom labels mean,** if you use them (for example label 0 is margin band). Otherwise it reads the values and asks you to confirm.
- **Optional:** Merchant Center or your store (Shopify, WooCommerce or Magento) connected too, for item status and stock.

## Example requests

**Full review**
Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. Audit my Google Shopping campaign structure for the last 30 days and rank the fixes by the money at stake.

**Standard Shopping or PMax?**
Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. I run Standard Shopping and Performance Max side by side. Which products serve in both, and how should I split them?

**Products that never show**
Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. Half my catalogue gets almost no impressions. Tell me which products are disapproved, which my campaigns leave out and which are just outbid.

**Custom labels**
Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. Check how my custom labels are used and write a performance label I can load as a supplemental feed.

**From exports, nothing connected**
Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. Here are my Shopping product report and feed export. Which products should I cut, and which haven't had a fair chance yet?

**Review, then fix**
Hey Claude, I just added the "google-shopping-retail-pmax-review" skill. Review my Shopping account, then add the negatives you find and draft the new campaign. Show me every change before you make it.

## What you get

1. **Area results** (pass, warn, fail or unknown) for product spend, products that barely serve, product groups and asset groups, priority and overlap, custom labels and search terms.
2. **Top fixes,** ranked by last-30-day spend at stake, each with the numbers behind it and who does it.
3. **A product ledger:** every product in one tier against your target. A product is only called a loser after spending 2 to 3 times its target cost per sale with no sale; smaller spenders are marked too early, with the spend still needed for a verdict.
4. **Products that barely serve,** split into not eligible, not targeted and outbid, with item IDs and issue codes.
5. **Overlap between Standard Shopping and PMax,** with the ROAS of each side on the same items.
6. **Negative candidates** from your own Shopping and PMax search terms, with how much of the spend Google shows.
7. **A proposed layout:** which products go where, the moves, starting budget and bid for a low-cost campaign, and a custom label table for a supplemental feed.

## What it can change for you

With your yes on the exact change, it can:
- add negative keywords from your own search terms
- create the low-cost Standard Shopping campaign and its ad group, always paused
- create a new PMax asset group (paused) and point it at chosen item IDs
- pause an asset group or a campaign the new layout replaces

It never changes bids or targets and never writes your feed. Splitting Standard Shopping product groups and editing a listing filter tree that is already subdivided are done in Google Ads; the skill tells you exactly what to set.

## Tips

- Run it monthly. The performance label moves products between campaigns as their results change.
- Give moved products a few weeks before judging the new layout.
- If `merchant-center-feed-fixer` is installed, run it first: this skill uses its profit and stock view.
