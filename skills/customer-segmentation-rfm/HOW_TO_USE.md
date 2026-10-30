# How to Use This Skill

Hey Claude, I just added the "customer-segmentation-rfm" skill. Run an RFM analysis on my orders, build customer segments, and tell me what to send each one and how often.

## What you need

- **Your order history.** Either upload or paste an orders export (order id, customer email or id, date, value, status), or connect your store through the InsightfulPipe MCP: Shopify, WooCommerce, Magento, a BigQuery orders table or a Google Sheet. The skill pulls the orders itself when a store is connected.
- **Email activity, if you want steps 5 and 6.** Connect Klaviyo or Mailchimp, or upload a subscriber export with emails received, opened and clicked in the last 90 days.
- **The deepest discount you're willing to give.** Without it, no segment gets a percent-off offer.
- **How far back to look,** if 24 months (ending yesterday) is wrong for how often your customers buy.

## Example requests

**Full RFM analysis from Shopify and Klaviyo**
Hey Claude, I just added the "customer-segmentation-rfm" skill. Build RFM segments from our Shopify orders, check how each segment responds to our Klaviyo emails, and give me a plan per segment. We never go above 15% off.

**From a CSV, no connection**
Hey Claude, I just added the "customer-segmentation-rfm" skill. Here's our orders export for the last two years. Score every customer, show me the cut-offs you used, and tell me each segment's share of revenue.

**Who has gone quiet**
Hey Claude, I just added the "customer-segmentation-rfm" skill. Which of our big spenders haven't ordered in a long time, how much did they spend, and are they still clicking our emails?

**Email list segmentation**
Hey Claude, I just added the "customer-segmentation-rfm" skill. Split our email list into buyers by RFM segment and subscribers who never bought, and set a sending frequency for each group.

**Segments into Klaviyo**
Hey Claude, I just added the "customer-segmentation-rfm" skill. Run the segmentation, then put each segment on its own Klaviyo list. Show me the lists and counts before you create anything.

## What you get

1. **A data quality line:** orders read, kept and dropped, and why.
2. **The cut-offs:** where recency, frequency and spend scores start and stop for your store.
3. **A segment table:** customers, revenue and share of revenue for best customers, big spenders gone quiet, loyal, new, growing, slipping, one-time buyers and dormant.
4. **Tiers for subscribers who never bought,** judged on clicks, not opens.
5. **How each segment answers email,** and the sending frequency that follows from it.
6. **A plan per segment:** the message, the offer rule within your discount cap, and the frequency.
7. **Klaviyo segment conditions** to build live segments by hand, each checked against the RFM table so you see who it catches. Under 500 buyers Klaviyo can't split on spend, so best customers and loyal become one segment, and big spenders gone quiet and dormant another.
8. **Files:** a per-customer score file and an ad-audience customer list.

## What it can change for you

With your yes on the exact change, it can:
- create a static Klaviyo list per segment and add the customers to it
- create a static Mailchimp segment per segment

It never sends emails, suppresses anyone or changes discounts. The ad-audience file is yours to upload.

## Tips

- Rerun it monthly: static lists don't update themselves, and customers move between segments.
- Leave wholesale and staff accounts out; they distort the spend cut-offs.
- If most of your customers have ordered once, that's normal. The frequency score splits repeat buyers on their own spread for that reason.
