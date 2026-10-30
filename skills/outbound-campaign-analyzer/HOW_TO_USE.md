# How to Use This Skill

Hey Claude, I just added the "outbound-campaign-analyzer" skill. Here's the export from our sending tool for last month's cold email campaign. Why are replies low, what do we change first, and what should we test next?

## What you need

- **Your campaign results,** in any of these forms:
  - a CSV or spreadsheet export from your sending tool or CRM sequence report (one row per step, variant, list and mailbox, or one row per contact)
  - the numbers pasted in chat: sent, bounced and replied for each step
  - a Google Sheet holding the export, if the Google Sheets MCP server is connected through InsightfulPipe
- **What counts as a positive reply,** for example your tool's "interested" label.
- **Where meetings are recorded,** if not in the export. Without them, the skill can still find delivery, list and message problems, but not offer problems.

Opens are not needed. The skill doesn't use them.

## Example requests

**Why nobody replies**
Hey Claude, I just added the "outbound-campaign-analyzer" skill. Our cold emails are getting almost no replies. Here's the CSV. Is it our copy, our list or our inboxes?

**Is our reply rate good?**
Hey Claude, I just added the "outbound-campaign-analyzer" skill. Our cold email reply rate is 3%. Is that good, and which list and mailbox are pulling it down?

**Calling an A/B test**
Hey Claude, I just added the "outbound-campaign-analyzer" skill. We tested two subject lines on step 1. Is variant B really better, or do we need more sends?

**From a Google Sheet**
Hey Claude, I just added the "outbound-campaign-analyzer" skill. The campaign export is in the "Outbound October" tab of my connected Google Sheet. Analyse it and write the readout to a new tab.

## What you get

1. **The funnel:** contacts, delivered, human replies, positive replies and meetings, each with a 95% range.
2. **A verdict for each list or segment:** delivery, list, message, offer or ask, healthy, or not graded, with the numbers that decided it.
3. **A mailbox table** that shows any inbox replying far below its siblings on the same copy.
4. **Step and variant tables,** with "not decided" and the sends still needed when the ranges overlap.
5. **What to change first,** in order: delivery, then list, then message or offer, then follow-ups.
6. **The next test:** one variable, the metric, sends per arm, how long it takes at your volume, and when to stop.

## What it can change for you

With your yes, and only in Google Sheets, it can add a new tab and write the readout to it. It never touches your sending tool: pausing a mailbox or changing copy is yours to do.

## Tips

- Export after the last step has had a few days to collect replies, or late replies will make the last step look weak.
- Split out auto-replies if your tool can. Out-of-office replies inflate the reply rate.
- Run it again after each change to see whether the verdict moves.
