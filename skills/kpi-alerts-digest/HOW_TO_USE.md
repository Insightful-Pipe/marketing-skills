# How to Use This Skill

Hey Claude, I just added the "kpi-alerts-digest" skill. Run this morning's health check on my marketing accounts and draft the daily digest for our Slack channel and our Telegram marketing channel.

## What you need

- **The InsightfulPipe MCP connected to Claude,** with your ad accounts, GA4 property and Search Console site added. The skill pulls the numbers itself.
- **Slack, Telegram or Notion connected,** only if you want the messages delivered there. Without them you still get the digest here in the chat.
- **A target ROAS or CPA,** if you have one. Without it, alerts compare each week with the week before.

## Example requests

**Daily digest to Slack**
Hey Claude, I just added the "kpi-alerts-digest" skill. Check yesterday's numbers across all my accounts and draft the digest for #marketing in Slack. Show it to me before you post.

**Daily digest to Telegram**
Hey Claude, I just added the "kpi-alerts-digest" skill. Send yesterday's KPI digest to our Telegram marketing channel once I've seen it.

**ROAS drop alert**
Hey Claude, I just added the "kpi-alerts-digest" skill. Our target ROAS is 3. Tell me if any ad account dropped below it this week and draft the alert for Slack.

**Week-over-week anomaly scan**
Hey Claude, I just added the "kpi-alerts-digest" skill. Scan last week against the week before across every platform and tell me what moved and why.

**Weekly client update**
Hey Claude, I just added the "kpi-alerts-digest" skill. Write this week's update for the client's shared Slack channel. Keep it client-friendly.

**Reminder, launch note, poll or meeting page**
Hey Claude, I just added the "kpi-alerts-digest" skill. Set a Slack reminder to review the weekly report every Monday at 9am, and make a Notion page for Tuesday's marketing meeting with this week's KPIs.

## What you get

1. **A health check** on the latest complete day: tracking alive, spend stopped or running away, clicks that never reach the site, stale data, unengaged traffic, and paid visits with no ad spend behind them.
2. **What moved:** each KPI against the median of the same weekday over the last four weeks, flagged only when it clears a floor, moves 40% or more and leaves its normal range.
3. **A weekly scan:** last 7 days against the 7 before, with the campaign or channel that drove each change.
4. **A ROAS or CPA alert** on rolling weeks, or a plain note that it can't be armed because nothing is tracked yet.
5. **Messages ready to send,** formatted for Slack or Telegram, each shown with its exact payload.

## What it can do for you

With your yes on the exact message and channel, it can:
- join a public Slack channel, then post a digest, alert or client update there
- set a Slack reminder to review a report
- send a digest, alert or campaign launch note to a Telegram chat
- send a poll to a Telegram channel
- create a Notion meeting notes page with a KPI snapshot

It never changes anything in your ad or analytics accounts.

## Tips

- Run it every morning on a schedule; each run reads the accounts fresh.
- Ask for "alerts only" if you want silence on normal days.
- For a full weekly or monthly report, use a reporting skill; this one is built to be short.
