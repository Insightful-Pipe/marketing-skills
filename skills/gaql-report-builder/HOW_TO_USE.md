# How to Use This Skill

Hey Claude, I just added the "gaql-report-builder" skill. Write me a GAQL query for cost per lead by hour of day for our non-brand search campaigns over the last 90 days, run it, and show me the table.

## What you need

- **Nothing, to get a query.** Describe the report you want, or paste a query that fails, and you get a checked query in API, Google Ads script and BigQuery form.
- **The InsightfulPipe MCP connected to Claude with your Google Ads account,** to have the query run live. The skill then fixes anything Google refuses before you see a result, and returns the table.
- **Optional: BigQuery connected through InsightfulPipe,** if your Google Ads data already lands there through the BigQuery Data Transfer. The skill can then run the SQL version on your transfer tables.

## Example requests

**Build a report from a question**
Hey Claude, I just added the "gaql-report-builder" skill. I need conversions and cost by campaign and week for the last quarter. Write the GAQL, run it and explain each field.

**Fix a query that won't run**
Hey Claude, I just added the "gaql-report-builder" skill. This query fails with an error about the date. Fix it and run it: SELECT campaign.name, segments.hour, metrics.cost_micros FROM campaign WHERE segments.date DURING LAST_90_DAYS

**Get it as a script**
Hey Claude, I just added the "gaql-report-builder" skill. Give me a Google Ads script that logs yesterday's spend and conversions for every enabled search campaign.

**Move a report to BigQuery**
Hey Claude, I just added the "gaql-report-builder" skill. We use the BigQuery Data Transfer for Google Ads. Turn this GAQL report into a custom transfer report and the SQL that reads it.

## What you get

1. **The query,** ready to copy, with the date window and time zone stated.
2. **A note for every field:** what it is, its unit, and the traps (money in micros, shares from 0 to 1).
3. **The table,** when Google Ads is connected, with a totals row and ratios worked out from the totals.
4. **A totals check:** the split rows add up to the same total as the unsplit query.
5. **A list of repairs,** when you pasted a query: what was wrong, how it was caught and what changed.
6. **The same report three ways:** an API call, a Google Ads script and a BigQuery Data Transfer query.

## What it can change for you

Nothing. Every query is read only, and the skill runs no write action.

## Tips

- Say what counts as a lead or a sale. By default the skill uses the account's Conversions column.
- Paste the exact error text along with a broken query; it names the field Google refused.
- Hours and dates follow your account's time zone. Say so if your market runs on another clock.
