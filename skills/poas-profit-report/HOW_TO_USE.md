# How to Use This Skill

Hey Claude, I just added the "poas-profit-report" skill. Work out POAS for every campaign over the last 30 days and tell me which campaigns and products lose money once product cost, shipping, fees, discounts and refunds are counted.

## What you need

- **Your orders for the window, one row per order line:** SKU, quantity, price, discount, refunds, shipping charged, tax and, if your export has it, the landing page URL with its UTM tags. A Shopify, WooCommerce or Magento orders export is enough.
- **A cost sheet:** landed unit cost and fulfilment cost per unit for each SKU, plus its product group.
- **Your payment fee** (percent plus any fixed fee per order) and packaging cost per order.
- **Ad results for the same days:** spend, conversions and conversion value per campaign, and the product-level reports where your platforms give them (Google Shopping and Performance Max, Meta catalog ads).
- **What purchase value your pixel sends:** the order total with tax and shipping, the subtotal after discounts, or the price before discounts. If you don't know, the skill works it out.
- **Or skip the exports:** connect your store and ad accounts through the InsightfulPipe MCP and the skill pulls them itself. Your costs still come from a sheet or from you.

## Example requests

**POAS for every campaign**
Hey Claude, I just added the "poas-profit-report" skill. Here are my Shopify orders, my cost sheet and my Google, Meta and TikTok campaign reports for the last 30 days. Give me POAS next to ROAS for each campaign.

**POAS vs ROAS by product**
Hey Claude, I just added the "poas-profit-report" skill. My Shopping and Performance Max campaigns look fine on ROAS. Price each product at its own margin and show me which ones lose money after ads.

**Set a target ROAS from my margins**
Hey Claude, I just added the "poas-profit-report" skill. Work out the break-even ROAS and a target ROAS for each product group. I want 15% of net revenue left as profit after ads.

**Check my live targets**
Hey Claude, I just added the "poas-profit-report" skill. My Google Ads account is connected. Compare the target ROAS on each campaign with what my margins need.

## What you get

1. **The store's profit after ads,** with the value basis your platforms use and the store-wide break-even ROAS.
2. **Every campaign with ROAS and POAS side by side,** its margin and where that margin came from, profit after ads and a verdict.
3. **The campaigns and products whose revenue hides a loss,** listed first.
4. **Break-even and target ROAS per product group,** on the same value basis your platforms report, so you can type them straight in.
5. **How many orders matched a campaign, matched only a platform, or matched nothing,** and how much more the platforms claim than those orders were worth.
6. **Suggested targets** next to the live ones, each marked not applied.

## What it changes

Nothing. It only reads your store and ad accounts. Every target is a suggestion for you, or another skill, to apply after you confirm.

## Tips

- Keep the cost sheet current. A margin is only as good as the unit cost and fulfilment cost behind it.
- Tag your ads with `utm_campaign` (campaign name or id). More orders then match a campaign, and the product mix behind each campaign is read from your own orders.
- Run it monthly, and again after a price change, a new discount code or a carrier rate change.
