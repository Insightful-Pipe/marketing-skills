# How to Use This Skill

Hey Claude, I just added the "email-list-cleaner" skill. Clean this contact file before I import it into Klaviyo, and give me keep, re-confirm and remove files.

## What you need

- **The contact file.** A CSV or Excel upload, pasted rows, or a Google Sheet tab. Only an email column is required; a source, an opt-in date and method, and a last click or purchase date make the checks sharper.
- **Nothing else to start.** It runs with no connection. In Claude Code it also looks up each domain's mail server with `dig`.
- **Optional: the InsightfulPipe MCP** with Klaviyo or Mailchimp, so the file is checked against the addresses your platform has already unsubscribed, bounced or suppressed. With Google Sheets connected, it can read the file from a tab and write the results back.

## Example requests

**Before an import**
Hey Claude, I just added the "email-list-cleaner" skill. Here's the contact export from our CRM. Clean it before I import it into Mailchimp.

**Trade show leads**
Hey Claude, I just added the "email-list-cleaner" skill. These are badge scans from last week's expo. Remove invalid emails and duplicates, and tell me which rows have no record of consent.

**An old list**
Hey Claude, I just added the "email-list-cleaner" skill. We haven't emailed this list since 2023. How do I clean it, and should I use it at all? Quiet window: 18 months.

**Clean, then write back**
Hey Claude, I just added the "email-list-cleaner" skill. Clean the "Leads" tab in my Contact imports sheet and write keep, re-confirm and remove tabs next to it. Show me what you'll write first.

## What you get

1. **One line with the verdict,** for example "Keep 14 of 45 rows, re-confirm 9 and remove 22", or "Do not mail this file" when most of it is bought.
2. **Three files,** keep, re-confirm and remove, with the original row number, a reason and a next step on every row.
3. **The checks:** syntax, duplicates (including case, Gmail dot and plus variants), addresses already blocked in your platform, bought sources, missing consent, throwaway domains, domains that take no mail, never-read and role addresses, misspelt domains such as gmial.com with a suggested fix, and contacts quiet longer than your window.
4. **What couldn't be checked,** and why, for example a domain whose lookup timed out.

## What it can change for you

With your yes on the exact change, it can:
- write the three files to new tabs in a Google Sheet
- suppress throwaway, dead-domain and never-read addresses that already sit in Klaviyo
- tag members in Mailchimp as "list-clean remove" or "list-clean re-confirm"

It never imports, deletes or emails anyone.

## Tips

- It doesn't probe mailboxes. For a list nobody has mailed in two years or more, run a paid verification service on the keep and re-confirm files too.
- A bought list can't be cleaned into a safe one. The skill removes those rows.
- Misspelt domains are never fixed silently: confirm the right address with the person first.
