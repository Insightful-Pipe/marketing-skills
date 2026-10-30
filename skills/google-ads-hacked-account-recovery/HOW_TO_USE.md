# How to Use This Skill

Hey Claude, I just added the "google-ads-hacked-account-recovery" skill. I think our Google Ads account was hacked: there's a campaign I didn't make and spend jumped. Check it and tell me how to lock it down.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill reads users, invitations, manager links, billing, change history, URLs and spend itself.
- **No connection?** Paste the Users and Managers tabs from Admin > Access and security, and upload the Change history CSV from Tools > Change history. Add spend by day and a Locations report if you have them.
- **Your list of who should have access:** the email addresses and the role each should have, plus the ids of your own and your agency's manager accounts. Without it, the skill lists everyone and asks you to mark each one.
- **Your landing page domains and the countries you sell to,** if they aren't obvious from your campaigns.

## Example requests

**Spend is running away now**
Hey Claude, I just added the "google-ads-hacked-account-recovery" skill. Someone is spending thousands in our Google Ads account right now. Find the campaigns they made and help me stop them first.

**Unknown manager account**
Hey Claude, I just added the "google-ads-hacked-account-recovery" skill. An unknown manager account is linked to our Google Ads account. Check what else changed and who has access.

**Unauthorized charges**
Hey Claude, I just added the "google-ads-hacked-account-recovery" skill. We got unauthorized charges on Google Ads. Work out how much to report to Google and what evidence to send.

**Routine takeover check**
Hey Claude, I just added the "google-ads-hacked-account-recovery" skill. Check our Google Ads account for signs of a takeover. Only dana@ and marco@ at our company and our agency's manager account should have access.

## What you get

1. **A verdict:** taken over, suspicious (needs your answer), or no sign of takeover in what Google records.
2. **A findings table** from seven checks: users, invitations, manager links, billing, change history, campaigns and URLs, and spend by day and country. Each finding names the change, user or link behind it, with its date when Google records one.
3. **The unauthorised spend** to report, split into intruder campaigns, budgets an intruder raised, and off-target countries to confirm.
4. **A lock-down plan in order:** save evidence, stop the spend, cut access, secure the logins that were used, report to Google, claim the spend, harden.
5. **The evidence for Google's compromised-account form,** and what the check can't see.
6. **A watch plan** with four dates over the next 30 days.

## What it can change for you

With your yes on the exact change, it can:
- pause a campaign an intruder created
- put back a budget, tracking template or final URL suffix an intruder changed
- pause an ad that sends people to an unknown domain

It never deletes anything, because Google needs those records. Removing users, cancelling invitations, unlinking manager accounts, billing, passwords and 2-Step Verification are steps you take in Google Ads; the plan says exactly where.

## Tips

- Download the Change history before anyone cleans up the account.
- When Google sends the change log, choose to clean up the account. Restoring it as is makes the spend ineligible for reimbursement.
- Rerun the check on the watch-plan dates; intruders often come back through a pending invitation or a manager link.
