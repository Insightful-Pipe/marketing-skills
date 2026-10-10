# How to Use This Skill

Hey Claude, I just added the "month-end-report-generator" skill. Write last month's Google Ads report for my client and tell me what to do next month.

## What it does

It connects to your Google Ads account through the InsightfulPipe MCP and pulls the month itself: account and campaign results, the month before, the same month last year, impression share, what your conversions are made of, devices, day and hour, and the account's change history. Then it writes the report: an executive summary, a graded scorecard, goal results, campaign tiers, insights, the changes made and whether they worked, and next month's plan. When the month closes a quarter, it can also outline the quarterly review deck with speaker notes.

You don't paste anything. It runs 11 read-only calls for a month report and 12 with the quarterly review, and it changes nothing in the account.

## Example requests

**Monthly client report**
Hey Claude, I just added the "month-end-report-generator" skill. Write the September report for the managing partner. He isn't a marketer.

**Graded against your goals**
Hey Claude, I just added the "month-end-report-generator" skill. Our goals are 200 leads a month at a $30 CPA on a $6,000 budget. How did last month do?

**Quarterly business review**
Hey Claude, I just added the "month-end-report-generator" skill. Outline the Q3 review deck with speaker notes, against Q2 and against Q3 last year.

**A month that missed**
Hey Claude, I just added the "month-end-report-generator" skill. We missed target last month. Write an honest report that explains why and shows the recovery plan.

**Short formats**
Hey Claude, I just added the "month-end-report-generator" skill. Give me last month as a one-page summary for our CEO, and as an email to the client.

## What to tell it

- **The month:** by default it uses the last complete month.
- **Who reads it:** executive, marketing lead, marketing manager or a client who isn't a marketer. The tone and the amount of detail follow from that.
- **Goals:** conversions, CPA or ROAS, and the monthly budget. Without goals, it grades against your own 3-month average and labels it that way. Budget use is graded only when you give a monthly budget.
- **What the data can't show:** promotions, site changes, office closures, and changes made more than 30 days ago. Google keeps only 30 days of change history.

## What you get

1. A header and a 3–4 sentence executive summary
2. A scorecard against last month, last year and the goal, with green, amber and red status
3. Goal results, with one line on why each was hit or missed
4. Every campaign tiered (star, solid, needs attention, low volume), with impression share lost to budget and to rank
5. 3–5 insights, each an observation, what it means and what to do, backed by numbers
6. The changes made this month, from the change history, and whether they worked yet
7. Next month's priorities, tests, a budget recommendation and the dates to plan around
8. An appendix with devices, day and hour, the lead mix and a search term summary
9. Optional: an 8-slide quarterly review outline with speaker notes

## Tips

- Run it in the first days of the new month. The change history then still covers most of the month you're reporting on.
- Tell it about changes made outside Google Ads, such as a new landing page or a call-handling change, so the insights can connect them to results.
- If the account counts calls and website call taps separately, it will flag a possible double count. The `conversion-tracking-auditor` skill, if installed, can check it.

## Not connected yet?

Paste a campaign report for the month and the month before (campaign, cost, clicks, impressions, conversions). You'll get the summary, scorecard, goals, campaigns, insights and plan. Impression share, change history, lead mix, devices, and day and hour need the connection.
