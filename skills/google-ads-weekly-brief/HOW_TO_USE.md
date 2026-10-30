# How to Use This Skill

Hey Claude, I just added the "google-ads-weekly-brief" skill. Write this week's Google Ads brief for my client as an email, and tell them what we changed and whether it worked.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the numbers and the change history itself; you don't export anything.
- **Who will read it:** a client, an executive, a marketing manager or your own team. The default is a client.
- **Your target CPA or ROAS, and a monthly budget,** if you have them. Without them, the skill uses your own 4-week average and today's daily budgets, and says so.
- **Anything the account can't know:** a promotion, a site outage, feedback from the sales team, how many leads became clients, or an Auction Insights export.

No Google Ads connection yet? Paste two weeks of campaign numbers (and the change history if you have it), and you get the same brief, minus the before/after verdicts.

**For the 90-day change history review,** the connection gives the last 30 days of changes with who made them and the old and new values. For older changes, download the change history from Google Ads as CSV (it keeps 2 years) and paste it. Without a connection, paste that CSV plus a campaign report by day for the same period and the 14 days before it.

## Example requests

**Client email**
Hey Claude, I just added the "google-ads-weekly-brief" skill. Write last week's brief for my client. Our target cost per lead is $45 and the monthly budget is $15,000.

**Executive summary**
Hey Claude, I just added the "google-ads-weekly-brief" skill. Give my CMO a 3-sentence summary of last week in Google Ads.

**Slack update**
Hey Claude, I just added the "google-ads-weekly-brief" skill. Format this week's Google Ads results as a Slack post for our #marketing channel.

**Did our changes work?**
Hey Claude, I just added the "google-ads-weekly-brief" skill. We changed budgets and bidding targets last week. Show what changed and whether it helped, campaign by campaign.

**A bad week**
Hey Claude, I just added the "google-ads-weekly-brief" skill. Leads dropped this week. Write an honest internal brief that explains why and shows the plan.

**Google Ads change history: who changed what, and did it work (90 days)**
Hey Claude, I just added the "google-ads-weekly-brief" skill. Pull our Google Ads change history for the last 90 days, tell me who made changes in the account, and which changes helped, which hurt, and which are worth undoing.

## What you get

1. **A headline:** how the week went, why, and what comes next.
2. **A scorecard:** this week, last week, the 4-week average and your target, coloured green, amber or red.
3. **Wins and concerns,** each with its number, its reason and the next step.
4. **What changed and did it work:** every change from the account's change history, net of repeat edits, with a verdict for each campaign compared against the same weekdays a week earlier.
5. **Campaign highlights:** the top performer and the campaign that needs attention.
6. **Next steps:** what was done, what's planned, and what needs your approval.
7. **Month pacing:** spend and conversions so far, and a projection.
8. **A tracking check:** whether a conversion action started or stopped counting.

From the change history impact review:

1. **Who changed what:** every net change of the last 90 days by person or source, type and month, with Google-side bursts set apart.
2. **A verdict per change:** helped, hurt, trade-off, no clear effect, too few conversions or too recent, read on equal windows before and after, once late conversions are in, and against campaigns nobody touched. Raw and adjusted numbers sit side by side.
3. **Worth undoing:** hurt changes still in place, with what keeping them cost and the exact undo, run only if you say yes.

## Formats

- **Email** (default): a subject line and the body
- **Slack:** a short post, with the detail in a thread
- **Slides:** one point per slide
- **Executive:** 3 sentences

## What it changes

The weekly brief changes nothing; it only reads your account. Budget, bidding and pause recommendations go under "Needs your approval" for you to decide. The change history review can undo a change it judged worth undoing, only after you confirm that exact change, and only on a Read & Write connection.

## Tips

- Run it on Monday, for the week that just ended.
- Tell it who the brief is for; length and wording change with the reader.
- Run it again a week after a big change, for the full-week verdict.
- Run the 90-day change history review once a month: it gives the settled verdict on changes the weekly brief could only call early.
