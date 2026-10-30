# How to Use This Skill

Hey Claude, I just added the "marketing-dashboard-builder" skill. Build a marketing dashboard in my Google Sheet from my live ad data, and show me every change before you write anything.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your data sources added:** Google Ads, Meta, LinkedIn Ads, GA4, Search Console or Bing Webmaster, whichever you use. The skill pulls the numbers itself.
- **A destination connected with Read & Write access:** a Google Sheet, a Notion workspace, a Slack workspace, or an Airtable base (the Airtable path is untested until a base is connected).
- **Optional:** a budget tab or your monthly budgets, a campaign plan tab, and a target cost per result.
- **No connection yet?** Paste or upload your platform exports, budget plan and invoices, or a screenshot of a Looker Studio report. The skill drafts the same spec, tables and payloads from those figures and marks each line as coming from your paste.

## Example requests

**Full dashboard**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Design a marketing dashboard for our weekly Monday meeting, then build it in my Google Sheet from live data.

**Weekly KPI snapshot**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Add last week's KPIs as a new row in the Weekly tab of my sheet.

**Daily spend log**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Append every day of ad spend since the last row in my Daily tab.

**Budget vs actual**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Compare this month's spend with the budgets in my Budget tab and tell me which campaigns are over or under pace.

**Plan vs live**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Check the campaigns in my Plan tab against what is actually live in Google Ads.

**Weekly report to Notion or Slack**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Write last week's marketing report as a Notion page and post a short summary to our marketing channel in Slack.

**Looker Studio dashboard**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Build a Looker Studio marketing dashboard with Google Ads, Meta, LinkedIn and TikTok spend next to GA4 sign-ups.

**Review a Looker Studio report**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Here is a screenshot of our Looker Studio report and its data sources. Check it for wrong formulas and misleading charts.

**Month close and spend reconciliation**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Close September for finance: budget vs actual on every line with reasons, accruals, ad spend reconciled against these invoices, and a re-forecast for the rest of the year.

**Dashboard spec only**
Hey Claude, I just added the "marketing-dashboard-builder" skill. Write a dashboard design spec for our agency's client dashboards: reader, questions, KPIs with formulas, and layout.

## What you get

1. **A dashboard spec:** who reads it, the questions it answers, up to 8 KPIs with formulas and sources, the layout, and what isn't included.
2. **A source list:** every source marked active, idle, not connected, broken or unknown.
3. **A layout preview:** each tab with its headers, first rows and formulas exactly as they will be written.
4. **This week's numbers:** the KPI table, what moved (no % changes on numbers too small to mean anything), budget pacing and plan-versus-live findings.
5. **Every write payload,** numbered and marked not run, for you to approve.
6. **For Looker Studio:** the staged daily table, the calculated fields (every rate a ratio of sums), the blend plan, a link that opens a report already connected to the table, numbered build steps, and for a review, each finding with its fix.
7. **For a month close:** a close table (budget, actual, variance and reason per line), accruals, a reconciliation of each ad account against its invoice or charges, and a re-forecast two ways.

## What it can change for you

With your yes on the exact payloads, it can:
- add tabs, rows, formulas, formatting, colour rules and a chart in Google Sheets
- create a report page in Notion (Looker Studio itself has no API for building pages, so that layout comes as steps you follow)
- post a summary message in Slack
- create or update records in Airtable (untested until a base is connected)

It never overwrites your data: the Daily and Weekly logs only grow, only the Campaigns and Budget tabs it created are refreshed, and it never deletes anything, changes a campaign or writes to BigQuery. These writes need a Read & Write connection, and an owner, admin or operator can switch them off.

## Tips

- If the dashboard includes GA4 or Search Console, run the weekly snapshot on Wednesday or later, once both have caught up on Sunday's data. A Monday run still works, but GA4's last days are marked provisional and Search Console usually doesn't have Sunday yet.
- If the InsightfulPipe MCP answers with a rate limit, the skill doesn't sit and wait for hours. It shows what it already pulled, marks the rest unknown with the time the limit clears, and carries on from there when you ask again.
- A staged Looker Studio tab is a snapshot: it gains days when you ask the skill to append them, so add a "data through" date to the report (the build steps include one).
- For a month close, wait until the platforms' invoices are in, usually the first days of the next month, and paste them net of tax.
- Keep one business per spreadsheet. If your brand holds several clients, say which one the dashboard is for.
- Share the Notion parent page with the InsightfulPipe MCP's Notion integration and invite the app to the Slack channel before asking for a report there.
