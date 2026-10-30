# How to Use This Skill

Hey Claude, I just added the "retention-cohort-analyst" skill. Here is my orders export. Build the retention cohort table by first-order month, show me where customers fall away, and tell me when to send refill reminders.

## What you need

- **Your orders,** one of these:
  - an orders export from your store (Shopify, WooCommerce, Magento or any other) as a CSV file
  - a subscriptions export from your billing system, or your app's retention export
  - or, through the InsightfulPipe MCP, a connected Shopify, WooCommerce or Magento store, a BigQuery table, a Google Sheet or a Klaviyo account, and the skill pulls the orders itself
- **Columns it needs:** order id, customer id or email, order date, status, net revenue and refunds. Add the order's source (UTM or referrer) to compare channels, and the products on each order to time refill reminders. Shopify's standard Orders export has no UTM column, so for the channel comparison connect the store or use a report that carries each order's UTM source.
- **Your shipping time,** so reminders land before the customer runs out. Without it, the skill allows 7 days.

## Example requests

**Cohort table from an export**
Hey Claude, I just added the "retention-cohort-analyst" skill. Here is our Shopify orders export since launch. Build the cohort retention analysis by first-order month and tell me how many customers come back by day 90.

**Which channels bring repeat buyers**
Hey Claude, I just added the "retention-cohort-analyst" skill. Compare customers by the channel of their first order. I think our Meta Ads customers never come back; check whether that's real or noise.

**Refill reminder timing**
Hey Claude, I just added the "retention-cohort-analyst" skill. We sell coffee beans and filters. Work out how long people take to reorder each product and give me the delays for my Klaviyo replenishment flows. We ship in 3 days.

**Subscriptions**
Hey Claude, I just added the "retention-cohort-analyst" skill. Here is our subscriptions export. Show retention by start month and tell me in which month most people cancel.

**From the warehouse**
Hey Claude, I just added the "retention-cohort-analyst" skill. Our orders are in BigQuery in the shop.orders table. Run the customer cohort analysis there and put the cohort table in a new tab of my Google Sheet.

## What you get

1. **A data check:** rows read, orders kept, and what was dropped (tests, cancellations, full refunds, guest orders, zero-value orders).
2. **The cohort table:** customers per first-order month, the share active in each month after, repeat by day 90 and 180 with margins, value per customer by month 3, 6 and 12, and revenue kept. Cohorts under 30 customers are marked too small to read.
3. **Where cohorts fall away:** days to the second order, the day by which most second orders have happened, and how few customers come back after it.
4. **Product reorder clocks:** the typical days between purchases of each product, or a plain "too irregular" or "too few repeats" when the data can't time it.
5. **First channel and first product:** which ones bring repeat buyers or one-time buyers, tested so a gap is only called real when it is.
6. **Triggers with exact delays:** a refill reminder per timed product and a second-order nudge, each with the numbers behind its delay and the steps to build it in Klaviyo.

## What it can change for you

With your yes on the exact change, it can write the cohort table into a new tab of a Google Sheet you name. It never builds or changes Klaviyo flows, and never edits orders or customers.

## Tips

- Give it your whole order history, even if you only care about recent months. Otherwise returning customers look new.
- Rerun it each quarter. Newer cohorts need time before their day-90 and day-180 numbers fill in.
- If your monthly cohorts are small, trust the quarter pools over any single month.
