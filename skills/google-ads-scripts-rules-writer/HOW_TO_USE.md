# How to Use This Skill

Hey Claude, I just added the "google-ads-scripts-rules-writer" skill. Write me a Google Ads script that stops spend when we hit our monthly budget, without touching Brand.

## What you need

- **Nothing, for an explain or fix job.** Paste the script or the error message and the skill works from that.
- **For a new script or rule, the InsightfulPipe MCP connected to Claude with your Google Ads account added** is best. The skill then reads your campaigns, labels, budgets and spend, sets each threshold from your own numbers and runs every query in the script before handing it over. Without it, give the campaign names and your numbers, or paste a campaigns report export, and the skill marks the queries "not tested".
- **Your numbers,** if you have them: the monthly cap, your target CPA, the campaigns a script must never pause, the alert email and, for an export, the Google Sheet URL.
- **Optional: Google Sheets connected,** so after your preview the skill can find the export tab, check its header row and count the rows the script wrote.

## Example requests

**Budget cap**
Hey Claude, I just added the "google-ads-scripts-rules-writer" skill. Pause our non-brand campaigns when the account reaches $14,000 this month, and turn them back on next month.

**Keywords with no conversions**
Hey Claude, I just added the "google-ads-scripts-rules-writer" skill. Set up an automated rule that flags keywords spending money with no conversions. Use my target CPA of $65.

**Search terms to a sheet**
Hey Claude, I just added the "google-ads-scripts-rules-writer" skill. Write a script that sends the last 30 days of search terms to this Google Sheet every Monday.

**Broken pages and spend jumps**
Hey Claude, I just added the "google-ads-scripts-rules-writer" skill. Email me when an ad's landing page breaks, and when a campaign spends far more than usual overnight.

**Fix a script**
Hey Claude, I just added the "google-ads-scripts-rules-writer" skill. This script worked last year and now errors. What is wrong with it? (paste the script)

## What you get

1. **Rule or script for each job,** with one line on why.
2. **The numbers behind every threshold,** from your account: the projected month against your cap, a keyword cost bar from your CPA, a spend jump ratio backtested on your last 60 days.
3. **The full script, or the rule's settings field by field,** with your real campaign names, ids and labels.
4. **What the preview should show today,** so you can tell at a glance whether it works.
5. **A change cap and an undo note** for every script that can change something.
6. **The query test results:** every query inside the script and how many rows it returned.

## What it can change for you

With your yes on the exact change, it can:
- create a label for a script's scope (for example "Budget cap: pause")
- apply that label to the campaigns you agree on

It never schedules or authorises a script and never creates a rule. You paste them into Google Ads under Tools, Bulk actions. Every script that can pause something starts switched off.

## Tips

- Click Preview before you schedule anything. A preview changes nothing in the account, but it does write to Google Sheets and send emails, so preview emails are marked.
- Run a new rule "one time" first, then switch it to a weekly schedule.
- Give each job its own script. One failing script then doesn't stop the others.
- Rerun the skill after a big change to campaigns or budgets, so the scope and thresholds still fit.
