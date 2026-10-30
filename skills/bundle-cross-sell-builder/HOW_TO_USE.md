# How to Use This Skill

Hey Claude, I just added the "bundle-cross-sell-builder" skill. Here is our orders export for the last 180 days and our products export with costs. Which products should we bundle, at what price, and what should we cross-sell after each purchase?

## What you need

- **Your orders for the last 180 days, with line items.** An export from Shopify, WooCommerce or Magento works, and so does any sheet with the order id, date, status and each product and quantity. Add the customer id if you want the follow-up emails. If your store is connected through the InsightfulPipe MCP, the skill pulls the orders itself.
- **Your price and unit cost per product,** from a products export with a cost column, or your overall gross margin. Without costs, bundle margins are estimates.
- **Each product's type or category,** so the skill can tell two sizes of the same thing (substitutes) from unrelated products.
- **Optional:** the lowest margin you'll accept on a bundle, your delivery time in days, and how many bundles you want to launch.

## Example requests

**What should we bundle?**
Hey Claude, I just added the "bundle-cross-sell-builder" skill. Use our orders export to find which products are frequently bought together, and tell me which pairs are strong enough to sell as a bundle.

**How should we price this bundle?**
Hey Claude, I just added the "bundle-cross-sell-builder" skill. We want to bundle our grow light with the plug timer. Check the pair in our orders and give me a bundle price that keeps at least a 50% margin.

**What should we offer after checkout?**
Hey Claude, I just added the "bundle-cross-sell-builder" skill. Find the best post-purchase offer for each of our top products, and the follow-up emails worth sending, with the day to send each one.

**Connected store**
Hey Claude, I just added the "bundle-cross-sell-builder" skill. Pull the last 180 days of orders and unit costs from Shopify, build our bundles and cross-sells, and draft the bundle listings for me to check.

**From Klaviyo or BigQuery**
Hey Claude, I just added the "bundle-cross-sell-builder" skill. Our orders are in Klaviyo as Placed Order events. Run a market basket analysis on them; I'll paste our cost sheet.

## What you get

1. **The pair table:** every pair with orders together, support, confidence both ways and lift, sorted into bundle candidates, pairs-well-with, a watch list and substitutes. A pair needs 15 shared orders and has to beat chance even at the low end of its range before it is trusted.
2. **Bundles priced on a ladder:** each discount step with its margin, whether it keeps your margin floor, and how many more bundle orders it needs to pay for the discount given to shoppers who already buy both. Then a launch, test or no-discount call.
3. **Placements:** "pairs well with" picks for each product page, post-purchase offers that only reach orders without the add-on, and follow-up purchases with the day to send each email.
4. **The copy:** a name, pitch and product page line for each bundle, and the subject, preview and body for each follow-up email.
5. **What the orders can't show,** and the changes it can make for you.

## What it can change for you

With your yes on the exact change, and a Read & Write connection, it can:
- create a draft bundle listing on Shopify for you to check and publish
- set cross-sells and upsells on a WooCommerce product
- create an email template in Klaviyo

It never sends an email, changes a flow or changes the price of an existing product. Shopify recommendations and every Magento change come as steps for your store admin.

## Tips

- Pairs need volume. With fewer than 300 orders that have two or more products, results are marked low confidence; under 100, you get the counts only. A longer window helps.
- A pair already bought together half the time rarely needs a big discount: most of the discount goes to shoppers who would buy both anyway. The ladder shows you how much.
- Launch one bundle at a time and compare bundle orders against the break-even count over the same number of days.
