# How to Use This Skill

Hey Claude, I just added the "conversion-reconciliation" skill. Reconcile last month's ad platform conversions against GA4 and tell me which gaps are real.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your ad accounts and your GA4 property added.** It reads Google Ads, Meta, LinkedIn, TikTok and Microsoft Ads, whichever you use, and pulls the data itself. No connection? Paste or upload the platform reports, a GA4 export and your order export instead; the report says which numbers came from files.
- **Your store, if you want the money checked against real sales.** The skill reads Shopify, WooCommerce or Magento orders. Those paths haven't run on a live store yet, so the first run on yours is their first live test. The order-level check needs the store, connected or exported.
- **The result to reconcile** (purchases, leads or sign-ups) and its GA4 key event name, if it isn't obvious. The skill proposes a mapping and shows it to you first.

## Example requests

**Platforms vs GA4**
Hey Claude, I just added the "conversion-reconciliation" skill. Google Ads says 120 leads last month and GA4 says 70. Find out where the other 50 went.

**Meta over-reporting**
Hey Claude, I just added the "conversion-reconciliation" skill. Meta claims far more purchases than GA4 shows. How much of that is view-through, and is anything actually broken?

**Platform revenue vs Shopify**
Hey Claude, I just added the "conversion-reconciliation" skill. Compare the revenue Google Ads and Meta report with what GA4 and Shopify recorded for September.

**New vs returning**
Hey Claude, I just added the "conversion-reconciliation" skill. How much of our paid traffic and spend goes to people who already visited, and how much reaches new visitors?

**Order by order: GA4 revenue doesn't match Shopify**
Hey Claude, I just added the "conversion-reconciliation" skill. GA4 revenue is about 25% below Shopify for September. Match our orders to GA4 purchases and tell me which ones are missing and why.

**Duplicate purchase events**
Hey Claude, I just added the "conversion-reconciliation" skill. I think GA4 is counting some purchases twice. Find the duplicates, what they have in common and how much revenue they add.

**From exports, no connection**
Hey Claude, I just added the "conversion-reconciliation" skill. Here is our Shopify order export and a GA4 exploration with transaction ids for October. Check which orders GA4 never recorded.

**A past period**
Hey Claude, I just added the "conversion-reconciliation" skill. Reconcile March and April.

## What you get

1. **A source list:** every ad account, GA4 property and store of the business, marked active, idle, broken, unknown or untested until connected.
2. **A reconciliation table:** for each platform, three checks: clicks against GA4 sessions, conversions against GA4 key events, and conversion value against GA4 revenue and store sales. Each is graded match, explained, investigate or not graded.
3. **The gaps, explained with numbers:** how much is view-through, phone calls, lead-gen forms or the click-date shift, and how much is left over.
4. **An investigate list,** ranked by spend, with the one check that would confirm each problem.
5. **A new vs returning split** of each platform's paid sessions, and an estimate of the spend that reached returning visitors.
6. **Which number to use** for bidding, for comparing platforms and for finance.
7. **With the order-level check:** a capture rate for each device, payment method, day and ad platform against your store's own normal rate, the purchases GA4 missed, counted twice or got from test and cancelled orders, wrong or missing values, refunds GA4 never got, how your purchase tracking is installed, and the fixes ranked by the revenue at stake.

## What it changes

Nothing. It only reads your accounts, your store and your tag container.

## Tips

- Reconcile a month that ended at least a week ago. Platforms keep adding late conversions, and GA4 needs a couple of days to finish.
- If one brand holds several businesses, say which one. The skill never compares one business's ads with another's GA4.
- Fix the investigate items, then run it again on the next full month.
