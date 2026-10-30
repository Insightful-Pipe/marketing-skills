# How to Use This Skill

Hey Claude, I just added the "html-email-template-builder" skill. Turn this copy into a responsive HTML email template that works in Gmail, Outlook and dark mode, using the brand from my website.

## What you need

- **Your content:** the copy, a screenshot or design of the email, or an existing HTML email to fix.
- **Your logo as a PNG or JPG** on a public link. SVG logos don't show in Gmail or classic Outlook.
- **Every link** the email should point to.
- **Optional: the InsightfulPipe MCP.** With it, the skill reads your brand colours, fonts and button style from your website, reads your Klaviyo or Mailchimp sender and postal address for the footer, and can save the finished email as a template. Without it, tell the skill your colours and fonts, or let it read them from your screenshot.

## Example requests

**From copy**
Hey Claude, I just added the "html-email-template-builder" skill. Here's the copy for our product announcement. Build the HTML email for Klaviyo with our brand from www.example.com.

**From a screenshot or design**
Hey Claude, I just added the "html-email-template-builder" skill. Rebuild this email design as HTML. Keep every word as live text, not images.

**Fix an existing email**
Hey Claude, I just added the "html-email-template-builder" skill. This email gets clipped in Gmail and the button breaks in Outlook. Check it and fix it.

**Build, then save**
Hey Claude, I just added the "html-email-template-builder" skill. Build a welcome email template and save it to Klaviyo when I say yes.

## What you get

1. **The brand kit** it used, with the source of each value and anything it changed (a darker button colour so the text is readable, a font stack for inboxes without your web font).
2. **The full HTML,** ready to paste: table layout, inline styles, an Outlook-safe button, dark-mode colours, alt text and the right footer tags for your platform.
3. **The plain-text version.**
4. **A 15-point check table with the measured numbers:** file size against Gmail's clipping limit, contrast for every colour pair, the smallest font, the button height and more.
5. **What to test before sending,** in which inboxes, and what can't be checked without a rendering service.

## What it can change for you

With your yes on the exact payload, it can:
- save the email as a Klaviyo template (with the plain text), or as a Mailchimp template
- update a Klaviyo template you name, when fixing an existing email
- upload your logo or images to Klaviyo

It never sends, schedules or sends tests, and never deletes a template.

## Tips

- Give it the real links up front; missing ones stay as named placeholders.
- Build one email, check it in your inboxes, then reuse it as the template for the rest of a series.
- If your brand colour fails the contrast check, the skill darkens it only as much as needed and shows you the before and after.
