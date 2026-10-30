# How to Use This Skill

Hey Claude, I just added the "email-deliverability-auditor" skill. Our marketing emails are going to spam. Audit our deliverability and tell me what to fix first.

## What you need

- **Nothing connected is required.** Paste what you have: your DNS records (or let Claude Code look them up), the full headers of a test email sent to a Gmail address, any bounce messages, and your Google Postmaster Tools spam rate if you use it.
- **Your From address and email platform,** and roughly how many emails you send a day at peak.
- **Optional: the InsightfulPipe MCP with Mailchimp or Klaviyo added.** The skill then reads your bounces and complaints by mailbox provider itself. On Mailchimp it also reads whether your domain is authenticated, and which campaigns went to your whole audience.

## Example requests

**Why are my emails going to spam?**
Hey Claude, I just added the "email-deliverability-auditor" skill. Our newsletter started landing in spam at Outlook last month. Here are the headers of a test send and the bounce message we get.

**SPF, DKIM and DMARC check**
Hey Claude, I just added the "email-deliverability-auditor" skill. Check SPF, DKIM and DMARC for our domain and tell me whether they line up with the address we send from.

**Gmail and Yahoo bulk-sender rules**
Hey Claude, I just added the "email-deliverability-auditor" skill. Do we meet the Gmail, Yahoo and Microsoft rules for bulk senders? We send about 30,000 emails a week from Klaviyo.

**New domain or new platform**
Hey Claude, I just added the "email-deliverability-auditor" skill. We're moving our newsletter to a new sending subdomain next month. Give me a ramp-up schedule from our own list.

## What you get

1. **A grade out of 100,** with the math shown, over five areas: authentication and alignment, bulk-sender rules, bounces and complaints by provider, who is still being mailed, and sending domain and IP.
2. **A provider table:** Gmail, Microsoft, Yahoo, Apple and the rest, each with its bounces and complaints. Bounce rates are graded against Klaviyo's published targets, since no provider publishes a bounce limit. Yahoo and Microsoft complaint rates are graded against the 0.1% and 0.3% spam lines, and Gmail's spam rate comes from your Postmaster Tools data, never from the platform's complaint count. Apple and the rest show complaint counts without a grade. On Klaviyo, provider rows show counts and shares unless you paste the inbox-provider table from its deliverability hub.
3. **What your bounce codes mean,** and which fix each one points to.
4. **A dated repair sequence:** each step with who does it (DNS admin, email platform admin, marketer) and the check that proves it worked.
5. **A sunset rule** for people who never click, and a **ramp-up schedule** when your sending domain or IP is new.
6. **BIMI readiness:** whether your brand logo can show in the inbox yet, and what's missing.

## What it can change for you

With your yes, it can add your From domain to Mailchimp for verification and finish the verification with the code Mailchimp emails you. DNS records, platform settings and sending stay with you.

## Tips

- Send the test email to a Gmail address and paste the whole original message, not just the visible part. It answers most of the authentication questions at once.
- "Promotions tab" isn't spam. The skill tells you when that's all that's going on.
- Run it again a week after the DNS changes. The re-checks in the plan tell you what should have moved.
