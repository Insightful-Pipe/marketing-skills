# How to Use This Skill

Hey Claude, I just added the "loyalty-vip-program-designer" skill. Design a loyalty program with a VIP tier from our order data, and tell me what it needs to pay for itself.

## What you need

- **Your orders from the last two years,** in any of these forms:
  - Shopify, WooCommerce or Magento connected through the InsightfulPipe MCP, and the skill reads the orders itself
  - an orders CSV you paste or upload, from any store or point of sale
  - a customer export with lifetime orders and spend, if that is all you have (the tiers are then labelled lifetime, not 12-month)
- **Your gross margin.** Without it the skill still sets tiers and writes the emails, but marks the reward rate, cost and break-even unknown.
- **For a program you already run:** the loyalty app's member export (tier now and a year ago, points earned, redeemed, expired and outstanding), today's rules and the app's monthly fee. There is no points-app connector, so the export is how the skill sees redemption and tier movement.
- **Klaviyo** connected, if you send email there. The skill checks for loyalty flows and VIP segments you already have before writing new emails.
- **Any VIP perk and what it costs you,** for example free express shipping at a cost per order.

## Example requests

**Start a program**
Hey Claude, I just added the "loyalty-vip-program-designer" skill. How do we create a loyalty program for our Shopify store? Our margin is about 55%. Set the tiers from what our customers actually spend.

**Review the one we have**
Hey Claude, I just added the "loyalty-vip-program-designer" skill. Here's our points app export. Is our rewards program paying for itself, and is the Gold tier set in the right place?

**Add a VIP tier**
Hey Claude, I just added the "loyalty-vip-program-designer" skill. We want a VIP customer program for our top spenders with free express shipping, which costs us $6 an order. Where should the line be, and what will it cost?

**Paid membership**
Hey Claude, I just added the "loyalty-vip-program-designer" skill. Would a $49 a year paid membership with free shipping work for our best customers, or would it lose money?

**From a CSV**
Hey Claude, I just added the "loyalty-vip-program-designer" skill. This is our orders export from the last two years. Give me customer loyalty program ideas that fit our numbers, and write the launch email.

## What you get

- A baseline: repeat rate, AOV, how much of revenue the top 5% and 25% bring, and the spend percentiles
- For a running program: redemption rate, reward cost, the points liability, tier movement, and how members compare with non-members (labelled an upper bound)
- Tier lines placed on your own spend distribution and rounded to numbers customers remember, with a 12-month soft landing for anyone who would lose a tier
- An earn and redeem rate sized to a share of your gross margin, plus the expected cost, the worst-case ceiling, and the repeat-rate lift the program needs to break even
- Six emails (launch, welcome, two tier-reached, near-tier, points balance), each with its audience count
- Tier lists by customer id, ready to tag

## What it changes

Nothing until you say yes to the exact change. It can tag customers with their tier in Shopify and save the emails as Klaviyo templates. It never sends email, turns on a flow or changes your loyalty app: you make those changes from its checklist.
