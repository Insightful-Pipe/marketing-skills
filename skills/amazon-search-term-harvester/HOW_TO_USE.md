# How to Use This Skill

Hey Claude, I just added the "amazon-search-term-harvester" skill. Here are my Sponsored Products search term reports and my bulk file. My target ACOS is 30%. Harvest the winners into exact, add the negatives and give me the bulk file to upload.

## What you need

- **Your search term report for the last 30 days,** from Sponsored Products and, if you run them, Sponsored Brands (Amazon Ads console, Measurement and reporting, Sponsored ads reports, report type "Search term").
- **The same report for the last 7 days** (the last 14 days for Sponsored Brands and for vendors), or one report with daily rows instead. The skill uses it to tell a term that failed from one whose orders haven't arrived yet.
- **A bulk file download** from Bulk operations for the same campaigns. It holds the IDs the upload needs and the keywords, negatives and product targets you already have. Without it you get copy-paste lists instead of a ready file.
- **Your target ACOS,** if you have one. Without it, the skill uses your own ACOS on non-brand terms in the window.
- **Your brand words and the competitor brands** you bid on or never want to bid on.
- **Optional:** the InsightfulPipe MCP with Google Sheets connected, if your reports live in a spreadsheet.

## Example requests

**Weekly harvest**
Hey Claude, I just added the "amazon-search-term-harvester" skill. Here are this week's Sponsored Products search term reports and my bulk file. Target ACOS 25%. Run the harvest and give me the rows to upload.

**Negatives only**
Hey Claude, I just added the "amazon-search-term-harvester" skill. My auto campaigns are burning money. Find the search terms I should add as negative keywords, and tell me which ones are still too new to judge.

**Stop cannibalization**
Hey Claude, I just added the "amazon-search-term-harvester" skill. I already have exact keywords for my best terms, but my auto and broad campaigns still pay for the same searches. Find them and add the cross-campaign negatives.

**Competitor ASINs**
Hey Claude, I just added the "amazon-search-term-harvester" skill. Which competitor ASINs in my auto campaigns sell well enough to target directly, and which ones should I negate?

**From Google Sheets**
Hey Claude, I just added the "amazon-search-term-harvester" skill. My search term report is on the "SP terms Oct" tab of my connected spreadsheet. Analyze it and put the bulk rows on a new tab.

## What you get

1. **Your conversion rate and negation point,** with the math: the number of clicks after which a term with no orders gets negated, set from your own account.
2. **Terms to move into exact match,** each with a bid worked out from its own sales per click and your target ACOS.
3. **Cross-campaign negatives,** so auto, broad and phrase campaigns stop bidding against your exact keywords.
4. **Negatives for wasted spend,** with the spend they would have saved.
5. **Competitor ASINs** to target directly and ASINs to negate.
6. **A watch list:** terms whose orders may still arrive (with a date to look again), terms one order short of a harvest, your own keywords that aren't selling, and competitor terms it asks you about first.
7. **Bulk-operations rows** in your own file's layout, ready for you to review and upload.

## What it can change for you

Nothing in Amazon. You review the bulk file and upload it yourself.

If Google Sheets is connected, and you say yes to the exact change, it can put the bulk rows on a new tab of your spreadsheet. It never writes over an existing tab.

## Tips

- Run it every week, on the same day, so the watch list dates line up.
- Use a fresh bulk file download each time: the IDs and your existing negatives change as you work.
- It never negates your brand words, and it asks before negating a competitor's name.
- If you sell on several marketplaces, run it once per marketplace: currencies and conversion rates differ.
