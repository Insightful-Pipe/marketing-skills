# How to Use This Skill

Hey Claude, I just added the "ga4-weekly-report" skill. Give me last week's GA4 report and tell me what really changed.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the data itself; you don't need to export anything.
- **Google Search Console on the same site,** if you have it. It lets the skill check whether GA4 is recording all your visits.
- **The key events you care about most,** if you want the report to focus on a few. Without them, it covers all of them.

## Example requests

**Weekly report**
Hey Claude, I just added the "ga4-weekly-report" skill. Run my GA4 weekly report for last week and compare it with the week before and the same week last year.

**Week-over-week explainer**
Hey Claude, I just added the "ga4-weekly-report" skill. Our sessions dropped this week. Tell me whether it's a real change and which channels and pages caused it.

**Anomaly check**
Hey Claude, I just added the "ga4-weekly-report" skill. Check my GA4 traffic for unusual days since last Monday and tell me what caused each one.

**Key events and engagement**
Hey Claude, I just added the "ga4-weekly-report" skill. Break down my key events and engagement rate for last week, and show me which pages hold attention longest.

**Monthly executive summary**
Hey Claude, I just added the "ga4-weekly-report" skill. Give me a monthly executive summary of GA4 for last month, against the month before and last year.

## What you get

1. **A three-line headline:** what moved for real, what is noise, and the one thing to act on.
2. **A KPI table** for sessions, users, engagement, key events and views, with week-over-week and year-over-year change, and a real-or-noise verdict on each.
3. **What drove each real change,** by channel and by page.
4. **Unusual days,** each with its normal level, its channel split and a likely cause.
5. **A key events breakdown,** including key events that never fire and test events left behind.
6. **Top pages and engagement time.**
7. **A today-so-far snapshot** and the days since the week ended.
8. **Data quality notes:** missing tracking, stray hostnames and broken page paths.

## What it can change for you

With your yes on the exact change, it can:
- mark an event that already fires as a key event
- change how a key event counts (once per event or once per session)

It never deletes key events, adds filters or changes your tags.

## Tips

- Run it every Monday morning, so the week is complete.
- Connect Search Console too. A tracking gap makes every other number misleading, and this is how the skill finds one.
- Small sites: expect many "noise" verdicts. That's the skill stopping you from reacting to chance.
