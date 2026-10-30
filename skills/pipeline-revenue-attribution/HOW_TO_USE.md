# How to Use This Skill

Hey Claude, I just added the "pipeline-revenue-attribution" skill. Here is our CRM export. Show me pipeline and revenue by source and campaign for the last 12 months, and what each stage cost.

## What you need

- **A CRM export of leads and deals.** Paste it, upload a CSV, or keep it in a Google Sheet or a BigQuery table. It needs each lead's created date and the source it came in with (UTMs, a click id such as gclid, or your CRM's original source field), the qualified date, and each deal's opportunity date, close date, outcome and amount. A touch history makes the last-touch and influenced views complete.
- **Your ad spend.** With the InsightfulPipe MCP connected, the skill pulls spend by campaign and month from Google Ads, Meta, LinkedIn Ads and Microsoft Ads itself. Otherwise paste it.
- **Other costs** you want counted, such as a trade show or a partner fee, as a monthly figure.
- **GA4 (optional),** to check whether your tags reach the CRM.

There is no CRM connector: the CRM side always comes from your export.

## Example requests

**The full report**
Hey Claude, I just added the "pipeline-revenue-attribution" skill. Our CRM export is in the Google Sheet. Show me pipeline and revenue by source and campaign for the last 12 months, with what each stage cost. The March trade show cost $18,000.

**Paid campaigns only**
Hey Claude, I just added the "pipeline-revenue-attribution" skill. Which of our Google Ads and LinkedIn campaigns bring leads that turn into opportunities, and which bring leads that never qualify? Here is the deals export.

**First touch or last touch**
Hey Claude, I just added the "pipeline-revenue-attribution" skill. Sales says brand search closes everything and LinkedIn does nothing. Compare first-touch and last-touch credit for each source from this export.

**Feed bidding**
Hey Claude, I just added the "pipeline-revenue-attribution" skill. Work out which CRM stages and values we should send back to Google Ads and Microsoft Ads, from our own numbers.

## What you get

1. **A source table:** leads, qualified leads, opportunities, pipeline, won deals and revenue for every source, paid and unpaid, with cost per qualified lead, per opportunity and per won deal, pipeline and revenue per dollar, and days to close.
2. **The same table by campaign** for each ad platform.
3. **First touch against last touch,** with each source labelled as one that opens deals, closes them, or both.
4. **Sourced against influenced pipeline.**
5. **Maturity by month:** recent months whose deals haven't had time to close, measured from your own close times, are marked and not judged on revenue.
6. **Sources whose leads stall at the first stage,** with the spend that went into them.
7. **Sales velocity by source.**
8. **An offline conversion set:** the qualified, opportunity and won stages with click ids and values from your own numbers, ready for the `offline-conversion-setup` skill or a manual import.
9. **Data quality:** unknown sources, campaign tags that match nothing, campaigns with spend and no leads, and GA4 key events that never reached the CRM.

## What it can change for you

With your yes, it can write the report tables into a new tab of your spreadsheet. It never edits your CRM export, your ad accounts or your conversion settings.

## Tips

- Export at least 12 months of leads. B2B deals take months, and the newest months are always still maturing.
- Capture UTMs and click ids in hidden form fields on every landing page. The data-quality section shows where they go missing.
- Run it again a month after a fix to see Unknown shrink and the maturing months land.
