# How to Use This Skill

Hey Claude, I just added the "pricing-research-survey" skill. Analyse our price survey in Google Sheets, tell me whether last month's price rise hurt sales, and recommend the price to test next.

## What you need

- **Survey answers,** as a Google Sheet, an uploaded CSV or pasted rows: the four Van Westendorp price answers and, if you ran one, a price ladder rated 1 to 5. No survey yet? The skill writes one for you, with the sheet layout it reads.
- **For price elasticity:** the old and new price and the change date (or your test arms), plus units sold and sessions by day. With the InsightfulPipe MCP connected, it pulls orders from Shopify or WooCommerce and sessions from GA4 itself (the store connectors were untested when this skill was built, because no store was connected; the GA4 read by day ran live).
- **Optional:** your unit cost (turns on the profit-maximising price), your segments, and 2 to 5 rival products with price and pack size.
- **No connection at all?** Paste the survey and a table of sales by day. Every calculation runs the same way.

## Example requests

**Write the survey**
Hey Claude, I just added the "pricing-research-survey" skill. Write a willingness to pay survey for our new 12-week training plan, with Van Westendorp questions and a price ladder, and give me the Google Sheet columns to collect it in.

**Analyse Van Westendorp results**
Hey Claude, I just added the "pricing-research-survey" skill. Here is the CSV from our Van Westendorp price sensitivity survey. Clean it, draw the curves and give me the acceptable price range by customer type.

**Calculate price elasticity**
Hey Claude, I just added the "pricing-research-survey" skill. We raised our candle from $24 to $28 on March 3. How do I calculate price elasticity from our Shopify orders, and was the rise worth it?

**Read a live price test**
Hey Claude, I just added the "pricing-research-survey" skill. We split traffic between $49 and $59 for three weeks. Here are visitors and buyers per arm. What is the elasticity, and can we trust it?

## What you get

1. **A cleaning table:** every response removed and why (failed attention check, blank, a typo like 260 for 26, answers in the wrong order, a ladder where interest rises with price).
2. **Van Westendorp results:** the acceptable price range, optimal and indifference price points with 90% intervals, and the full curve table.
3. **A demand curve:** buyers per 100, revenue and profit at each ladder price, and the elasticity between rungs.
4. **Segments side by side,** and the ones with too few answers to price.
5. **Price elasticity from real orders,** with a 95% interval, discounted orders removed and season controlled for, or a plain reason why it can't be measured yet.
6. **Rival prices** in the same unit, placed against your range.
7. **One price to test,** the checks behind it, and what to expect from the test.

## What it can change for you

With your yes on the exact change, it can add a "Price analysis" tab to your survey spreadsheet and write the curve and demand tables into it. It never touches the tab that holds your responses, and it never changes prices, products or discounts in your store.

## Tips

- Show the same product description to every respondent, and ask all prices in one unit and currency.
- Aim for 100 or more valid answers per segment you want priced (about 120 responses each), and expect about 15% to be removed.
- Leave the change day out and keep promotion codes off during a price test. The skill removes discounted orders either way, but a clean window gives a tighter interval.
