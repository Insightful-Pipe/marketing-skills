# How to Use This Skill

Hey Claude, I just added the "marketing-data-warehouse" skill. Check our marketing data warehouse against Google Ads and Meta for the last 30 days and tell me what's broken.

## What you need

- **A warehouse, or its schema.** With BigQuery connected through the InsightfulPipe MCP, the skill reads the schema and runs read-only SELECT queries itself (the PostgreSQL and MySQL connectors follow the same steps and are untested until connected). With Snowflake, Redshift, SQL Server or nothing connected, paste the schema (the skill gives you the one query to run) and a few sample rows.
- **Your ad accounts connected through the InsightfulPipe MCP,** for the live reconciliation: Google Ads and Meta Ads were tested live; Microsoft Ads, LinkedIn Ads and TikTok Ads use the same steps and are untested until connected. Without them, paste each platform's daily spend export.
- **Your reporting currency and time zone,** and how many days your scheduled load rewrites. Without them, the skill uses the biggest account's currency and time zone and asks to see the scheduled query.

## Example requests

**Check the loaded tables**
Hey Claude, I just added the "marketing-data-warehouse" skill. Our dashboard never matches Google Ads. Check the ad spend tables in BigQuery against each platform for the last 30 days and rank what's wrong by the money it misstates.

**Design the warehouse**
Hey Claude, I just added the "marketing-data-warehouse" skill. We run Google Ads, Meta and LinkedIn in USD and GBP. Design one daily table for all of them with joins to GA4 and our orders, and write the SQL I need to save in BigQuery.

**From a pasted schema**
Hey Claude, I just added the "marketing-data-warehouse" skill. We're on Snowflake. Here's our information_schema output. Write the staging views and the daily MERGE for our Google Ads and Meta tables.

**Ask a question in plain English**
Hey Claude, I just added the "marketing-data-warehouse" skill. What did a new paid customer cost us by channel last month? Write the SQL, run it and explain the answer.

## What you get

1. **A verdict:** ready for dashboards, usable with notes, or fix first, with the spend each fault misstates.
2. **A check table:** freshness, missing days, duplicate rows, currency, and a day-by-day reconciliation of spend and conversions with each platform, graded per ad account.
3. **Ranked fixes,** each with the evidence and the SQL to save.
4. **The SQL set** when you ask for a design: the daily table, one staging view per source, the union view with currency conversion, the scheduled MERGE and the GA4 view.
5. **Answers in SQL:** the result table, what it means and what it leaves out, and the query to keep.

## What it changes

Nothing. It sends only single SELECT statements and dry runs. Every CREATE, MERGE or DELETE is written for you to review, save and schedule yourself.

## Tips

- Run the check after any loader change, backfill or new ad account, and before a dashboard goes to anyone new.
- Set the reload lookback to your longest conversion window, or conversions in the warehouse will trail the platforms.
- Keep platform conversions, GA4 key events and CRM orders in separate columns; they answer different questions.
