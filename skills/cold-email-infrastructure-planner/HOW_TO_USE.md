# How to Use This Skill

Hey Claude, I just added the "cold-email-infrastructure-planner" skill. We want to send cold email to 400 new prospects a week. Plan the domains, mailboxes, DNS records and ramp so it stays out of spam.

## What you need

- **Your main domain** and the cold domains you already bought, if any.
- **Your weekly target** (new prospects a week) and your sequence (how many emails, how many sending days apart).
- **Your mailbox host:** Google Workspace or Microsoft 365.
- **Your DNS records,** pasted, if Claude can't run `dig` where you use it. In Claude Code it looks them up itself.
- **Optional:** last weeks' sent, bounce and spam figures if you already send cold, and your list's verification counts.
- **Optional:** the InsightfulPipe MCP with Google Sheets, to read your mailbox tracker and write the calendar to a new tab.

## Example requests

**Plan from scratch**
Hey Claude, I just added the "cold-email-infrastructure-planner" skill. How many domains and inboxes do I need to send 300 cold emails a day on Google Workspace? Give me the ramp calendar from Monday.

**Check my records**
Hey Claude, I just added the "cold-email-infrastructure-planner" skill. Here are the SPF, DKIM and DMARC records for my three cold domains. Check them line by line and give me the fixed versions.

**Something went wrong**
Hey Claude, I just added the "cold-email-infrastructure-planner" skill. Our bounce rate hit 3% last week and replies dropped. Here are the figures per mailbox. What do we pause, and what do we fix first?

**Write it to my sheet**
Hey Claude, I just added the "cold-email-infrastructure-planner" skill. Build the ramp calendar for my 12 mailboxes and put it in a new tab of my outbound tracker sheet. Show me the rows first.

## What you get

1. **The setup:** daily sends once fully ramped, mailboxes, cold domains, spare domains and how many to buy, with every default labelled as provider rule or practitioner convention.
2. **A DNS check** for the main domain and each cold domain: SPF, DKIM, DMARC, MX and tracking, each line pass, warn or fail, with the fixed record.
3. **List rules:** what to send, what to hold, what to remove, and when to verify the next list.
4. **A dated ramp calendar,** week by week, with follow-ups counted, and the first week your target fits.
5. **Stop rules:** the bounce and spam levels that hold, pause or stop a mailbox or domain, and the status of what you already run.

## What it can change for you

With your yes on the exact rows, it can add a tab to your Google Sheet and write the calendar into it. It never buys domains, edits DNS or sends email.

## Tips

- Buy the domains and set the records on day one: the warm-up clock starts when the mailboxes exist.
- Check again after any change at your DNS host; a second SPF record at the same name makes SPF fail for all your mail.
- Run it again before raising the weekly target. More volume means more mailboxes, not a higher cap.
