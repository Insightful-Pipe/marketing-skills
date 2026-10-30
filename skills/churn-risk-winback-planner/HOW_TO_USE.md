# How to Use This Skill

Hey Claude, I just added the "churn-risk-winback-planner" skill. Work out which of our customers have lapsed and plan a win-back.

## What you need

- **Your orders, renewals or usage,** in any of these forms:
  - Shopify, WooCommerce or Magento connected through the InsightfulPipe MCP, and the skill reads the orders itself
  - a BigQuery table of orders, billing or product usage, connected through the InsightfulPipe MCP
  - an orders CSV, a subscription or billing export, or a product-usage export you paste or upload
  - or, with no data at all, a description of how often people buy each thing you sell
- **Your gross margin per product line,** if your data has no unit cost. Shopify unit cost (and Magento cost, when filled in) is read for you.
- **Klaviyo or Mailchimp** connected, if you have a win-back flow already. The skill checks it before proposing anything new.

## Example requests

**Who has lapsed**
Hey Claude, I just added the "churn-risk-winback-planner" skill. Run a customer churn analysis on our Shopify orders: who has stopped buying, and who is about to?

**Fix the flow we have**
Hey Claude, I just added the "churn-risk-winback-planner" skill. Our Klaviyo win-back flow fires 90 days after the last order. Is that right for what we sell, and what is it earning?

**From an export**
Hey Claude, I just added the "churn-risk-winback-planner" skill. Here's our orders CSV from the last two years. Our margin is about 55% on coffee and 35% on equipment. Plan a win-back.

**Subscriptions or software**
Hey Claude, I just added the "churn-risk-winback-planner" skill. This is our product-usage export, one row per account per active day. Which accounts have gone quiet, and how do we bring them back?

**Build the list**
Hey Claude, I just added the "churn-risk-winback-planner" skill. Plan the win-back, then put the lapsed repeat buyers on a Klaviyo list. Show me the list first.

## What you get

1. **A lapse point for each product line,** measured from how often your own customers rebuy it, with a stop point after which almost nobody comes back.
2. **Where every customer stands:** active, close to lapsing, lapsed, or let go, with fast and slow buyers judged on their own pace.
3. **What they used to spend:** lifetime revenue and gross margin, and the yearly value of repeat buyers at their old pace.
4. **A check of your existing win-back flow:** whether its timing fits each line, how many people it reaches too early, and what its discount gives away.
5. **A plan per group:** the reason to come back, whether an offer is justified and the most each customer's margin can pay for, the channel, the touch days, and when to stop.
6. **Hand-offs:** the emails go to email-sequence-builder, and paid reach for large groups goes to retargeting-sequence-designer, if you have them installed.

## What it can change for you

With your yes on the exact list, it can:
- create a static Klaviyo list of one group and add those customers to it
- create a static Mailchimp segment of one group

It never sends email, edits or starts a flow, creates discount codes, or suppresses anyone.

## Tips

- Give it two years of orders, or more if you sell something people buy once a year or less often. If your history is too short for a line, the report says so.
- If a product line has only a handful of repeat buyers, the skill will ask how often people buy it. A rough answer is fine; it is labelled as yours.
- Run it again a month after the plan starts, and compare each group's order rate with the month before.
