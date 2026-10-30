# How to Use This Skill

Hey Claude, I just added the "returns-refunds-analyst" skill. Our refunds feel high. Find which products and campaigns drive our returns, why customers send things back, and what to fix first.

## What you need

- **Your orders and refunds.** Paste or upload an orders export and a refunds export from Shopify, WooCommerce or Magento. If the InsightfulPipe MCP is connected to Claude with your store added, the skill pulls them itself.
- **Your return window,** if it isn't in your refund policy. Without it, the skill uses 30 days.
- **Optional, for sharper answers:** a returns-app export with reason codes, a reviews export, ad spend by campaign with your target ROAS, your unit cost and what each return costs you to handle.

## Example requests

**Shopify refunds report**
Hey Claude, I just added the "returns-refunds-analyst" skill. Build a refunds report for my Shopify store: return rate by product, size and colour, and the reasons behind it.

**Net ROAS after returns**
Hey Claude, I just added the "returns-refunds-analyst" skill. Here's my ad spend by campaign. Show me each campaign's revenue and ROAS after refunds. My target ROAS is 3.0.

**Why things come back**
Hey Claude, I just added the "returns-refunds-analyst" skill. I've attached our returns-app export and our product reviews. Tell me why customers return our top sellers and what to change on the listings.

**Discounts and returns**
Hey Claude, I just added the "returns-refunds-analyst" skill. Did our 30% off sale bring in buyers who sent everything back? Compare orders with each discount code against full-price orders.

**WooCommerce or Magento**
Hey Claude, I just added the "returns-refunds-analyst" skill. Run a return rate analysis on my WooCommerce store and use the product reviews to explain the worst products.

## What you get

1. **A header** with orders, units sold, units returned, refunded revenue, the unit return rate and the refund rate, for orders old enough for their return window to close.
2. **Top fixes,** ranked by the money at stake each month, each with the evidence behind it.
3. **Products and variants** with their return rate against your store's own rate, flagged high, watch or normal.
4. **Sources, campaigns and discount codes** with gross, refunded and net revenue, and gross and net ROAS when you give spend.
5. **Why it comes back:** the reason mix and the themes in low-rated reviews.
6. **A keep-out list** of products and variants to pull from ads and discount codes until their fix is live.
7. **Data checks,** including whether GA4 receives your refunds at all.

## What it changes

Nothing. It's read only. It never issues or cancels a refund, and never edits a product, policy, discount or campaign. Every fix is yours to make.

## Tips

- Recent orders always look better because their returns haven't arrived yet. The skill leaves them out on purpose.
- Run it monthly, and again one return window after a fix goes live to see the rate fall.
- A returns export with reason codes beats refund notes. Most returns apps can export one.
