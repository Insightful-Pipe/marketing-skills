# How to Use This Skill

Hey Claude, I just added the "call-tracking-analyst" skill. Build a call tracking report for the last 30 days: which ads and keywords bring real phone leads, when we miss calls and what that costs us, and whether Google Ads counts our calls right.

## What you need

- **A call log.** Either the CallRail MCP server connected through InsightfulPipe, or a call log CSV from any call tracking tool (CallRail, CallTrackingMetrics, WhatConverts, Invoca or your phone system), uploaded or pasted.
- **Your qualifying call length:** how long a call usually lasts when it's a real enquiry. Without it, the skill uses 90 seconds and says so.
- **Your opening hours, average job value and how many qualified calls become paying jobs,** if you want missed calls priced in dollars. Without the last two, you get leads lost, not dollars.
- **Optional:** Google Ads, GA4 and Google Business Profile connected through InsightfulPipe, to check how calls are counted there.

## Example requests

**Monthly call report**
Hey Claude, I just added the "call-tracking-analyst" skill. Give me last month's call tracking report from CallRail. A real enquiry lasts at least 2 minutes.

**From a pasted export**
Hey Claude, I just added the "call-tracking-analyst" skill. Here's our call log export from CallTrackingMetrics. Which sources bring first-time callers who actually talk to us?

**Missed calls**
Hey Claude, I just added the "call-tracking-analyst" skill. When do we miss the most calls, and what is it costing us? Our average job is $650 and we book about half of real enquiries.

**Google Ads call conversions**
Hey Claude, I just added the "call-tracking-analyst" skill. Check whether Google Ads counts our calls once and with the right call length, and compare it with CallRail.

**Report, then act**
Hey Claude, I just added the "call-tracking-analyst" skill. Run the report, then tag the qualified calls in CallRail and draft a text to yesterday's missed callers. Show me everything before you send.

## What you get

1. **Phone leads at a glance:** inbound calls, answered rate, first-time callers, qualified calls, and the leads and revenue lost to missed calls as labelled estimates.
2. **Every call graded by stated rules:** marked by a person, missed, repeat caller, short or qualified.
3. **Leads by source, campaign and keyword,** with cost per qualified call when spend is known.
4. **A missed-call map** by day and two-hour block, with callbacks counted as recovered and staffing gaps named.
5. **Call length and tags:** whether your qualifying length fits the calls your team marked as good.
6. **Counting checks:** your length against the Google Ads call length (60 seconds unless changed), double counting across call actions, GA4 phone taps and Business Profile call clicks.
7. **Up to 5 next steps,** ranked by the calls at stake.

Caller numbers are masked to their last two digits everywhere.

## What it can change for you

With your yes on the exact change, it can:
- tag qualified calls or mark them as good leads in CallRail
- text first-time callers you missed in the last 48 hours and never reached, from your CallRail number
- set a double-counted Google Ads conversion action to secondary

For the Google Ads call length and counting settings, it tells you the exact setting to change in Google Ads.

It never deletes calls, tags or conversion actions, and never places calls.

## Tips

- Tag or mark calls in your call tracking tool as you go. Marked calls make the grading and the length check much sharper.
- Run it monthly, and again two weeks after any staffing or counting change to see the missed rate and the Google Ads numbers move.
- If you run several locations in one CallRail account, say which company to report on.
