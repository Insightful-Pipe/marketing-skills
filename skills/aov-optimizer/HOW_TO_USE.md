# How to Use This Skill

Hey Claude, I just added the "aov-optimizer" skill. Here is my orders export for the last 90 days. How do I increase average order value, and what would each change earn me?

## What you need

- **Your orders for the last 90 days.** An export from Shopify, WooCommerce or Magento works, and so does any sheet with one row per order or per line item. If your store is connected through the InsightfulPipe MCP, the skill pulls the orders itself.
- **Your unit costs,** from a products export with a cost column, or your overall gross margin. Without them you get the margin each change needs to break even instead of the margin it earns.
- **Your shipping settings and carrier cost:** the fee you charge, where free shipping starts in each zone, and what a typical label costs you.
- **Your coupon settings,** if your orders use codes.

## Example requests

**Where should free shipping start?**
Hey Claude, I just added the "aov-optimizer" skill. We give free shipping over $50. Use our orders export to tell me where the line should be, and what moving it would do to margin.

**Is a spend-and-get offer worth it?**
Hey Claude, I just added the "aov-optimizer" skill. We're thinking of "spend $100, get $10 off". Check it against our orders and tell me if it pays.

**Why is our AOV stuck?**
Hey Claude, I just added the "aov-optimizer" skill. Our average order value hasn't moved in months. Show me what makes it up and which products and channels hold it down.

**Connected store**
Hey Claude, I just added the "aov-optimizer" skill. Pull the last 90 days of orders, our shipping zones and our coupons from WooCommerce and give me the AOV plan. Carrier cost is about $7.40 an order.

## What you get

1. **The AOV snapshot:** items per order times price per item, the median and percentiles, and how many orders are a single item.
2. **The spread of order values** in buckets, the most common basket, and whether your free-shipping line already pulls baskets up.
3. **What pulls AOV up or down:** products, channels and discount codes.
4. **Every lever priced in margin dollars:** the free-shipping line, a gift with purchase or a spend-and-save tier, add-ons, upsells and minimums on codes, each with a low, base and high case and the top-up rate it needs to break even.
5. **A short plan** in order, a way to test it, and what couldn't be checked.

## What it can change for you

On WooCommerce, with your yes on the exact change, it can:
- add a minimum spend to an existing coupon
- create a spend-and-save coupon for a tier that passed

It never changes prices, products or shipping methods. Changes on Shopify and Magento are given as steps for your store admin.

## Tips

- Ninety days with at least 300 orders gives steady thresholds. From 100 to 299 orders the levers are marked low confidence, and under 100 you get the snapshot and the spread only.
- If you know your own top-up rate from past offers, give it: the estimates use it instead of the defaults.
- Make one change at a time and run it for 4 weeks, watching margin per session as well as AOV.
