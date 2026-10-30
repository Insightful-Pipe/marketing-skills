# How to Use This Skill

Hey Claude, I just added the "discount-promo-analyst" skill. Here is our orders export for the last 12 months and our discount codes. Which codes and sales actually make us money, and what should our next offer be?

## What you need

- **Your orders for the last 12 months** (6 at least). An export from Shopify, WooCommerce or Magento works, and so does any sheet with one row per order, as long as it has the customer, the subtotal, the discount and the code or sale used. If your store is connected through the InsightfulPipe MCP, the skill pulls the orders and your discount rules itself.
- **Your gross margin,** store-wide or per product. Without it you get the lift each discount needs to break even instead of the margin it made.
- **Your code list:** what each code gives and who it was meant for (new subscribers, an influencer's followers, past customers).
- **The dates of any sitewide sales** that ran without a code.
- **Where orders came from,** if your export has it (referring site, landing page with UTM tags, or WooCommerce order attribution). It is how the skill spots codes on coupon sites. GA4, if connected, adds the same view.

## Example requests

**Are our discounts profitable?**
Hey Claude, I just added the "discount-promo-analyst" skill. Our margin is about 60%. Use our orders export to tell me how much margin our codes and sales gave away, and which ones paid for themselves.

**Did a code leak?**
Hey Claude, I just added the "discount-promo-analyst" skill. Our influencer code suddenly got a lot of uses. Check whether it ended up on coupon sites and who is using it.

**Was the sale worth it?**
Hey Claude, I just added the "discount-promo-analyst" skill. We ran 25% off over Labor Day. Compare it with the weeks before and after and tell me if it made money.

**Design the next offer**
Hey Claude, I just added the "discount-promo-analyst" skill. Pull our Shopify orders and discount codes, then design our next promotion: how deep, for whom, how long, and how to test it.

## What you get

1. **A short summary** and a ranked plan, each action with the money at stake.
2. **Every code measured:** orders, discount given, margin after discount, new versus returning buyers, how much went to customers who usually pay full price, its sources and UTM campaigns, and a verdict.
3. **Whether code buyers come back,** compared with full-price buyers.
4. **Every sale against its baseline:** the order lift, the lift it needed to break even, the dip after, and the margin it made or lost.
5. **Leaked codes,** with the coupon sites they appeared on.
6. **Whether you lean on discounts more than before,** on days without a sale.
7. **The next offer:** the amount, minimum spend, audience, length, guardrails and a holdout to prove it works.

## What it can change for you

With your yes on the exact change, and a Read & Write connection, it can:
- expire a leaked WooCommerce coupon or create the new offer as a WooCommerce coupon
- create a Klaviyo coupon and upload unique codes to it
- post a public sale or code as a Merchant Center promotion

Shopify discounts can't be created or changed through the connector, so for Shopify it writes out the exact admin steps.

## Tips

- Give it your real margin. A 20% sale on a 40% margin needs far more extra orders than on a 70% margin.
- Run it after every major sale, while the 14 days after are still fresh.
- Tell it which codes are meant for one channel (an influencer, an affiliate); that is how it spots codes used outside their channel.
