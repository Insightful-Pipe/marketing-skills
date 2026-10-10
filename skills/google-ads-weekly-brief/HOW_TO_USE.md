# How to Use This Skill

Hey Claude, I just added the "google-ads-weekly-brief" skill. Write this week's Google Ads brief for my client as an email, and tell them what we changed and whether it worked.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the numbers and the change history itself; you don't export anything.
- **Who will read it:** a client, an executive, a marketing manager or your own team. The default is a client.
- **Your target CPA or ROAS, and a monthly budget,** if you have them. Without them, the skill uses your own 4-week average and today's daily budgets, and says so.
- **Anything the account can't know:** a promotion, a site outage, feedback from the sales team, how many leads became clients, or an Auction Insights export.

No Google Ads connection yet? Paste two weeks of campaign numbers (and the change history if you have it), and you get the same brief, minus the before/after verdicts.

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

## What you get

1. **A headline:** how the week went, why, and what comes next.
2. **A scorecard:** this week, last week, the 4-week average and your target, coloured green, amber or red.
3. **Wins and concerns,** each with its number, its reason and the next step.
4. **What changed and did it work:** every change from the account's change history, net of repeat edits, with a verdict for each campaign compared against the same weekdays a week earlier.
5. **Campaign highlights:** the top performer and the campaign that needs attention.
6. **Next steps:** what was done, what's planned, and what needs your approval.
7. **Month pacing:** spend and conversions so far, and a projection.
8. **A tracking check:** whether a conversion action started or stopped counting.

## Formats

- **Email** (default): a subject line and the body
- **Slack:** a short post, with the detail in a thread
- **Slides:** one point per slide
- **Executive:** 3 sentences

## What it changes

Nothing. The skill only reads your account. Budget, bidding and pause recommendations go under "Needs your approval" for you to decide.

## Tips

- Run it on Monday, for the week that just ended.
- Tell it who the brief is for; length and wording change with the reader.
- Run it again a week after a big change, for the full-week verdict.
