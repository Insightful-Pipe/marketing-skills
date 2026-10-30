# How to Use This Skill

Hey Claude, I just added the "store-site-search-analyst" skill. Here are our site search terms for the last 30 days and our products export. Which searches fail, what should we fix first, and which products should we pin?

## What you need

- **Your site search terms for the last 30 days,** with how many times each was searched. Any of these works: the Shopify searches report, a GA4 export of search terms, the Magento Search Terms report, or your search app's export. If GA4 or your Shopify store is connected through the InsightfulPipe MCP, the skill pulls the terms itself.
- **Your products export** from Shopify, WooCommerce or Magento: title, type or category, tags, SKU, status and stock. With the store connected, the skill reads the live catalogue instead.
- **Who bought after searching,** if you can get it: a GA4 funnel exploration with step 1 `view_search_results` broken down by search term and step 2 `purchase`. It is what lets the skill rank fixes by money. Without it, fixes are ranked by search volume.
- **Your store totals** for the same dates: visitors, buyers, orders and revenue.

If GA4 is not recording site search yet, the skill tells you and gives you the setup steps.

## Example requests

**Find failed searches**
Hey Claude, I just added the "store-site-search-analyst" skill. Pull our GA4 search terms and our Shopify products, and show me every search for something we sell that still finds nothing.

**Shopify search shows no results**
Hey Claude, I just added the "store-site-search-analyst" skill. Here is our Shopify "searches with no results" list. Tell me which of these are misspellings, which need a synonym or a tag, and which are products we don't stock.

**Searches that don't sell**
Hey Claude, I just added the "store-site-search-analyst" skill. Which of our top searches have shoppers who rarely buy, and which products should we pin to the top for each one?

**Analyse, then fix**
Hey Claude, I just added the "store-site-search-analyst" skill. Run the analysis on our WooCommerce store, then add the missing tags you find. Show me every change first.

## What you get

1. **A tracking check:** whether GA4 records site search, and the setup steps if it doesn't.
2. **Searchers against other shoppers:** how often each group buys.
3. **Every top search, classed:** an exact product, a collection, found, found but sold out, only in descriptions, not on sale yet, a misspelling, a synonym or not carried, with the evidence from your catalogue.
4. **Fixes ranked by the buyers each search loses** against your store's average buy rate, with the money at stake marked as an estimate.
5. **Ready lists:** synonyms, redirects for exact-product and collection searches, products to pin for each top search, tag and title changes, and the searches for products you don't sell.

## What it can change for you

With your yes on the exact change, and with the store connected with a Read & Write connection, it can add tags and change product titles on Shopify and WooCommerce, and change product names on Magento.

It never creates redirects, synonyms or pins: no connector can, so it writes them out with the steps for your platform. It never changes prices, stock or what is published.

## Tips

- Run it monthly, and after a catalogue change or a new collection.
- Searches for products you don't stock are a product question, not a search fix. The skill lists them for a range review.
- Run it again a month after the fixes to see whether failed searches and their buy rates moved.
