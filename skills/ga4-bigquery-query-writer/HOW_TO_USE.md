# How to Use This Skill

Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Write and run the BigQuery SQL on my GA4 export that answers my question, show me the scan before it runs, and check the result against GA4.

## What you need

- **Your GA4 data in BigQuery,** through the GA4 BigQuery export. If you also load Google Ads data with the BigQuery Data Transfer Service, the skill can join cost to GA4 sessions.
- **Best: the InsightfulPipe MCP connected to Claude, with BigQuery added** (and GA4, so it can read your time zone, currency and key events and check its answers against GA4's own totals). The skill finds the export dataset, reads the schema and table sizes, and runs the query after you say yes.
- **No connection?** Paste your table schema, a few sample rows or a result you already have. You get the SQL to run yourself, explained line by line, with what to check when it comes back.

## Example requests

**Ask a question in plain words**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Which landing pages start the sessions that end in a purchase? Use the last 28 days.

**Page paths**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Where do people go after the pricing page, and how many leave the site from it?

**An unsampled funnel**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Build a funnel from view_item to add_to_cart to begin_checkout to purchase, where each step has to happen in order in the same session.

**Attribution across sessions**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Show October revenue by channel under first touch, last non-direct, linear and position-based, with a 30-day lookback.

**Cohort lifetime value**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Show revenue per user by month since first visit, for the cohorts since April.

**Cost per purchase by campaign**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Join my Google Ads cost to GA4 purchases by campaign for October, and tell me what each purchase costs.

**Why BigQuery and GA4 don't match**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. My sessions in BigQuery are lower than in GA4. Find out why.

**Explain or fix my query**
Hey Claude, I just added the "ga4-bigquery-query-writer" skill. Here's my sessions query. Explain it, fix anything wrong, and tell me how much it scans.

## What you get

1. **Your question in one line,** with the dates, your property's time zone and currency.
2. **Where the data came from:** the tables used and which traffic source field each column uses.
3. **The scan estimate** from a dry run, as GiB and as a share of BigQuery's first 1 TiB of on-demand queries each month. Nothing runs until you say yes.
4. **The answer** as a small table with 2 to 4 findings.
5. **A check against GA4** for the same dates, with each gap explained by how GA4 counts, or flagged as real.
6. **The SQL,** ready to save as a view or a scheduled query.

## What it can change for you

Nothing. It only reads, and only sends single SELECT statements and dry runs. Anything that creates a table, view or scheduled query is handed to you as SQL to run yourself.

## Tips

- Ask for the smallest date range that answers the question; the scan grows with every day.
- If BigQuery and GA4 disagree, run the check first, before you trust any breakdown.
- Save the queries you reuse as views, so the next question starts from your own session table.
