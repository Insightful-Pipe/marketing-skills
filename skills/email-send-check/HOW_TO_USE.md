# How to Use This Skill

Hey Claude, I just added the "email-send-check" skill. Check my email before it goes out and tell me whether it's safe to send.

## What you need

- **The email.** Paste or upload the HTML, or connect Klaviyo or Mailchimp through the InsightfulPipe MCP and name the campaign. A screenshot works too, but then links, tags and size can't be checked.
- **Who it should go to,** and who must not get it.
- **The UTM tags you agreed,** for example `klaviyo / email / spring_sale`. Without them, the skill uses the source and medium your GA4 already records for email.
- **Where the main button should land,** and the send time with its time zone.

Connecting the site crawler, PageSpeed Insights and GA4 lets it request every link, time the landing pages on a phone and check your tags against what GA4 records. Without them it reads the links from the HTML and tells you which to open yourself.

## Example requests

**A Klaviyo campaign**
Hey Claude, I just added the "email-send-check" skill. Proof the "Spring sale" Klaviyo campaign before tomorrow's 9am send. It should go to VIP customers only, excluding anyone who bought this week. Tags are klaviyo / email / spring_sale_2026.

**A Mailchimp draft**
Hey Claude, I just added the "email-send-check" skill. Run the pre-send checklist on my Mailchimp draft "October newsletter", including Mailchimp's own send checklist.

**Pasted HTML, nothing connected**
Hey Claude, I just added the "email-send-check" skill. Here is the HTML of our launch email. Check the links, tag fallbacks, alt text, size, footer and plain text before I send it.

**A flow email**
Hey Claude, I just added the "email-send-check" skill. QA the second email of our welcome flow. The template is called "Welcome 2" and every link should carry utm_campaign=welcome_flow.

**Check, then fix**
Hey Claude, I just added the "email-send-check" skill. Check this campaign, then save the corrected template and send a test to me at my own address. Show me every change first.

## What you get

1. **A verdict:** Go, Go after fixes, or Hold, with the count of blockers, fixes, notes and unknowns.
2. **Blockers and fixes,** numbered, each with the evidence and the exact change.
3. **A link table:** status, redirect hops, final page, whether the UTM tags survived, and mobile load time.
4. **A tag table:** every personal-data tag, where it sits and its fallback.
5. **What passed, and what couldn't be checked,** including how the email renders in Outlook or the Gmail apps, which is described from the HTML rather than shown.

## What it can change for you

With your yes on the exact change, it can:
- save the corrected template in Klaviyo, or the corrected HTML and plain text in Mailchimp
- put the corrected template on the Klaviyo campaign, or fix its subject and preview text
- send a Mailchimp test email to your own address

It never sends to your list, schedules a campaign, or changes an audience.

## Tips

- Run it after the email is final and the audience is set, so the audience and timing checks mean something.
- Name your landing pages. A link that answers 200 can still land on the wrong page.
- Run it again after the fixes; the verdict should move to Go.
