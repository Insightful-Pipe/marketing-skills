# How to Use This Skill

Hey Claude, I just added the "meta-catalog-product-set-planner" skill. Plan my Facebook catalog ads: which products should get spend, which product sets to build for prospecting and retargeting, and the ad text.

## What you need

- **Your catalog.** The InsightfulPipe MCP connected with your Meta ad account and catalog access, or a catalog CSV from Commerce Manager or your feed app.
- **Sales and stock per product** for the last 30 days. Connect Shopify, WooCommerce or Magento through InsightfulPipe, or paste a sales-by-SKU export and your current stock.
- **Unit cost per product.** Shopify holds it when you fill it in; otherwise paste a cost sheet with SKU and unit cost.
- **Your other costs** (payment fees, shipping, returns) as a share of the price, and a target ROAS if you have one. Without a target, the skill uses what your catalog ads actually returned.

## Example requests

**Set up catalog ads from scratch**
Hey Claude, I just added the "meta-catalog-product-set-planner" skill. I'm launching Advantage+ catalog ads for my Shopify store. Here are my catalog CSV, last month's sales by SKU and my cost sheet. Build the product sets and the ad text.

**Stop spending on the wrong products**
Hey Claude, I just added the "meta-catalog-product-set-planner" skill. My catalog ads run on one "All products" set. Find the products that are out of stock, about to run out or below my margin, and tell me how much they spent last month.

**Prospecting and retargeting split**
Hey Claude, I just added the "meta-catalog-product-set-planner" skill. Split my catalog into product sets for broad prospecting and for people who viewed or added to cart. My target ROAS is 3.5 and fees and shipping are 12% of the price.

**Plan, then create the sets**
Hey Claude, I just added the "meta-catalog-product-set-planner" skill. Plan my product sets, check each filter against the catalog, and create them in Meta once I say yes.

## What you get

1. **The margin bar** each product has to clear, and where it came from.
2. **The spend at stake:** catalog ad spend that went to out-of-stock, low-stock, low-margin or rejected products.
3. **A product set plan:** profit leaders, new arrivals, stock movers and price bands, each with its audience, product count, margin earned and spend.
4. **The excluded products,** each with its reason and the number behind it.
5. **Catalog ad text and overlays** for each set, using Meta's product tags, plus the filter and payload for every set, marked "not run".

## What it can change for you

With your yes on the exact change, and a Read & Write connection with catalog access, it can:
- create a planned product set, after checking the filter returns the planned products
- repoint an existing product set to a new filter

It never builds ads or ad sets, and never changes budgets, audiences, overlays or your feed. Those it plans, and you set them in Ads Manager, Commerce Manager or your feed app.

## Tips

- Rerun it monthly, or after a big stock change: the sets are lists of products, so they don't update themselves.
- If your feed app can write custom labels, ask for the custom label version of each set; those keep up with stock on their own.
- Add the missing costs to your cost sheet. Products without a cost only go to retargeting.
