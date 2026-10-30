# How to Use This Skill

Hey Claude, I just added the "competitor-price-tracker" skill. Compare my product prices with my competitors, tell me which products are overpriced or underpriced, and set a repricing rule for each collection.

## What you need

- **Your products:** a pasted list or an export with SKU, title, price and, ideally, the barcode (GTIN). Or connect Shopify, WooCommerce or Magento through the InsightfulPipe MCP and the skill reads the catalogue itself.
- **Your unit costs and fees.** Without costs it still compares prices, but it sets no floors and proposes no price cuts.
- **Your competitors:** their product page links, a price list, or an Amazon export you paste. With Merchant Center connected, it can also find the sellers Google shows next to you.
- **Optional:** a Google Sheet to keep a price log, so each run shows what changed since the last one.

## Example requests

**Weekly price check**
Hey Claude, I just added the "competitor-price-tracker" skill. Here are my 30 best sellers with costs, and links to the same products on three rival shops. Which ones are priced well above or well below the market?

**Repricing rules**
Hey Claude, I just added the "competitor-price-tracker" skill. Set a rule per collection: match the market on kettles and grinders, beat it on brewers, and never go under a 25% margin. Show me the new prices before changing anything.

**Who am I up against?**
Hey Claude, I just added the "competitor-price-tracker" skill. Use Merchant Center to find the shops Google shows next to mine, then compare our prices on the products we both sell.

**What changed this week**
Hey Claude, I just added the "competitor-price-tracker" skill. Rerun last week's price check from my Google Sheet log and tell me which rivals started a sale or ran out of stock.

## What you get

1. **A price table:** your landed price (with shipping) next to the market reference for every product, the gap, and a band from well below to well above.
2. **A floor and a ceiling for each product,** the floor worked out from your cost, fees and minimum margin.
3. **One rule per product group** (match, beat, premium or hold) written as a sentence you can hand to a repricing tool, and the proposed price for each product.
4. **Shipping and promotions:** your free-shipping threshold against each rival's, live sales, and what changed since the last run.
5. **The money at stake,** labelled as an estimate, and a list of anything it couldn't match or read.

## What it can change for you

With your yes on the exact change, it can:
- update prices in Shopify, WooCommerce or Magento
- add this run's prices to a Google Sheets price log

It never prices below your floor, never creates discounts, and never edits Merchant Center product data directly.

## Tips

- Give it barcodes (GTINs). Exact matches make the comparison trustworthy, and Merchant Center only benchmarks products with a GTIN.
- Run it on the same day each week and keep the Sheets log, so promotions and price moves show up with dates.
- If a rival's page can't be read, paste that price; the skill never guesses one.
