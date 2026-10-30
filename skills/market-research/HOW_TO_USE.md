# How to Use This Skill

Hey Claude, I just added the "market-research" skill. Research the market for my product category: how big is demand, is it growing, who owns it, and which channels and countries should we go after?

## What you need

- **The InsightfulPipe MCP connected to Claude, with DataForSEO added.** The skill pulls every number itself from public data; you don't need to export anything or connect your own ad accounts.
- **The market in a sentence,** and three to five phrases people search for it. Without the phrases, the skill picks them from the market map and shows you.
- **Search Console (optional),** if you also want to see where your own site stands.
- **For store mode,** your product list: Shopify or WooCommerce connected, or a product export, or a short description. Merchant Center (best sellers) and GA4 (site search) add more when connected, and their exports work too. Add your margin floor per product type if you want margins graded.

## Example requests

**Market size and trend**
Hey Claude, I just added the "market-research" skill. How big is the US market for AI meeting note-takers, and is it still growing?

**Target market**
Hey Claude, I just added the "market-research" skill. Who searches for plant-based protein powder? Give me age, gender and what they're looking for.

**Hidden trends and trending products**
Hey Claude, I just added the "market-research" skill. Find the rising and early-stage products inside the smart home security market before they get crowded.

**Industry analysis**
Hey Claude, I just added the "market-research" skill. Who owns the search results for project management software, and how concentrated is the industry?

**Channels and social networks**
Hey Claude, I just added the "market-research" skill. Which channels and social networks should we use to reach buyers of e-bikes? Show me the evidence.

**International**
Hey Claude, I just added the "market-research" skill. We sell in the US. Which country should we expand to next for our CRM for real estate agents?

**Store mode: what to add to my store**
Hey Claude, I just added the "market-research" skill. I run an online store selling home cold plunge tubs. What trending products should I add or push next, and when should I list the seasonal ones?

## What you get

1. **Five answers first:** size, direction, who owns the market, where to show up and which countries.
2. **Four grades** for the segment you care about: demand, momentum, commercial value and openness, each with its number and rule.
3. **A market map:** every keyword cleaned of unrelated meanings and duplicates, sorted into segments with searches, share, cost per click and intent.
4. **Direction:** year-over-year change since the first searches, seasonality where there's enough history, and a weekly Trends check on the latest turn.
5. **Rising keywords, early signals and trending products,** ranked by searches added.
6. **The audience:** age and gender of searchers, and whether they are learning or looking for a product.
7. **The players:** which kinds of sites and which businesses own the results, and how concentrated they are.
8. **Channels and social networks:** use, test or skip for each channel, and a points ranking of social networks with the reason for every point.
9. **Countries:** an interest ranking of your shortlist, confirmed with real search volumes and cost per click for the top two.
10. **Where you stand,** if Search Console is connected: which keywords you already show for, and the gaps.

In **store mode** you get instead: your range by product type and price band, a ranked list of products to add (each with its source, searches, trend, season peak and list-by month, fit with your range, margin and verdict), the best sellers to push or restock, and the site searches for things you don't stock.

## What it can change for you

With your yes on the exact payload, it can add a tab to a Google Sheet you name and write the tables into it. It never edits your site, launches ads, adds or edits products, or changes any account.

## Tips

- A full run uses about 11 DataForSEO calls (7 without the country comparison), and store mode uses 3. It asks before going past 12.
- If your core word has other meanings (like "crm", or "cold plunge", which is also a body wash scent), the skill shows you the unrelated keywords first and asks which to exclude.
- Rerun it monthly in a fast-moving market, and compare the grades with the last run.
