# How to Use This Skill

Hey Claude, I just added the "checkout-cro-auditor" skill. Audit my store's checkout and tell me which fixes would win back the most revenue.

## What you need

- **Screenshots of your cart and every checkout screen** up to the pay button, on a phone and on a desktop, with something in the cart. Add one of an error if you can (press pay with the card fields empty).
- **Your store's URL and platform.** If you're on Shopify and haven't connected it, say which plan you're on; it decides which fixes you can make.
- **The InsightfulPipe MCP connected to Claude,** if you want the skill to pull the numbers itself:
  - **GA4** for each checkout step by device and browser
  - **Shopify, WooCommerce or Magento** for your orders, abandoned checkouts, delivery rates and policies (these run as soon as a store is connected; they haven't had a live test run yet)
  - **PageSpeed Insights** for how fast your cart loads on a phone
  - **Microsoft Clarity**, optional, for rage clicks on a step that's already flagged (untested until a Clarity project is connected)

No connection? Paste a funnel table (sessions at cart, checkout start, delivery, payment and purchase, by device if you have it), your order count and delivery rates, and share the screenshots. The skill audits what you give it and marks the rest not checked.

## Example requests

**Full checkout audit**
Hey Claude, I just added the "checkout-cro-auditor" skill. Audit our Shopify checkout for the last 30 days. Screenshots of the cart and checkout on my phone are attached.

**Is it real or is it tracking?**
Hey Claude, I just added the "checkout-cro-auditor" skill. GA4 says half our checkouts never finish. Check our orders and abandoned checkouts first and tell me whether that's real drop-off or a tracking gap.

**One device looks broken**
Hey Claude, I just added the "checkout-cro-auditor" skill. Mobile sales feel low. Show me each checkout step by device and browser and tell me where phones lose people.

**Delivery costs**
Hey Claude, I just added the "checkout-cro-auditor" skill. We charge $6.95 shipping under $75. Is that pushing people out of checkout, and how many carts were close to free shipping?

**No connection, screenshots only**
Hey Claude, I just added the "checkout-cro-auditor" skill. Here are screenshots of our cart and checkout and a funnel export from our analytics. What are the checkout page best practices we're missing, and what should we fix first?

**Plan the tests**
Hey Claude, I just added the "checkout-cro-auditor" skill. Audit the checkout, then tell me how long a test of each top fix would take with our traffic. We're on WooCommerce.

## What you get

1. **A tracking check:** how many of your orders GA4 records, and whether GA4 and your store agree on where shoppers stop.
2. **Each checkout step** with sessions, rate, shoppers lost and revenue lost, by device, plus any device or browser that falls well behind the rest.
3. **Your numbers beside published research:** your cart abandonment next to the 70.22% average across 50 studies, and the reasons shoppers give for leaving.
4. **A delivery cost check:** who pays shipping among leavers and buyers, and the carts that were close to your free-delivery threshold.
5. **A review of every cart and checkout screen,** each finding quoted from your screenshots and tied to the step it sits on.
6. **The top 5 fixes,** ranked by revenue at stake, each saying where the change is made and whether your plan allows it.
7. **Tests for the top 3,** with the sessions and days your traffic needs, or a before-and-after plan where a test can't run.

## What it can change for you

Nothing. It reads and recommends; you or your developer make the changes.

## Tips

- Take the screenshots as a shopper would: a real phone, a real product, every screen up to the pay button.
- Run it again 4 weeks after a fix and compare the step that changed.
- If the tracking check fails, fix tracking first. The rest of the report is only as good as the numbers under it.
