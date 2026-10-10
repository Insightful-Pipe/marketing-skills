# How to Use This Skill

Hey Claude, I just added the "form-cro" skill. Audit the demo request form on my site and tell me which fields to cut and what to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude,** with **DataForSEO** (it reads the form on the live page) and your **GA4 property** (form starts, submissions and tracking checks). You don't need to export anything or describe the form.
- **The form's page URL,** if GA4 doesn't already log `form_start` on it.
- **Which fields your team actually uses after a submit,** and whether anyone phones leads. Without that, the skill marks those fields "check with sales" instead of cutting them.
- **Any field you must keep for legal or policy reasons** (consent boxes, licence or eligibility questions), and, if you know them, what a lead is worth and whether you have field-level analytics. All three are optional; the skill says when it went without them.
- Optional: PageSpeed Insights and Screenshot (what the form looks like on mobile, and accessibility problems), Google Tag Manager (duplicate lead triggers) and Microsoft Clarity (behaviour hints; untested until a Clarity project is connected).

No connection? Paste the form's HTML or list its fields, plus your form views and submissions if you have them. The skill audits the fields and marks the rest unknown.

## Example requests

**Shorten a demo form**
Hey Claude, I just added the "form-cro" skill. Our demo request form feels long. Go through every field and tell me what to keep, cut or make optional. Sales only uses name, email and company size.

**Contact form that gets started but not finished**
Hey Claude, I just added the "form-cro" skill. Lots of people start our contact form and few send it. Check the funnel in GA4 by device and tell me where it breaks.

**Can I trust the form numbers?**
Hey Claude, I just added the "form-cro" skill. Check whether our form submissions are tracked properly in GA4 before we start changing the form.

**Multi-step or not**
Hey Claude, I just added the "form-cro" skill. Our quote form has 11 fields. Should it be multi-step, and how would you split it?

**Audit, then fix tracking**
Hey Claude, I just added the "form-cro" skill. Audit the form, then mark the submission as a key event in GA4. Show me the change first.

## What you get

1. **A grade out of 100** across six areas: measurement, funnel, field load, input quality, submit and trust, page and mobile.
2. **A field-by-field table:** every visible field with its type, whether it's required, its autofill setting, and a verdict (keep, make optional, merge, move after submit, cut, or check with sales or legal) with the reason.
3. **The funnel:** form page sessions, form starts and submissions by device, graded only when there's enough traffic to mean something.
4. **Up to five fixes,** tracking blockers first, then fields, then input details, then copy and trust.
5. **A test plan** written as "if we change X, then Y will move, because Z", or a plain note that your volume is too low for an A/B test.
6. **A short "check by hand" list** for what markup can't show (error messages, inline validation, email typos and aliases, international phone numbers, the success state).
7. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, and a Read & Write GA4 connection, it can:
- turn on GA4's form interaction tracking for your web stream
- mark the form submission event as a key event
- register `form_id` or `form_name` as a custom dimension, so GA4 can tell your forms apart

It never edits the form or your site. Field and copy changes are for you or your developer.

## Tips

- One DataForSEO call per form page. Audit your top 1–3 forms rather than every form on the site.
- If your form lives in an embed (HubSpot, Typeform, Calendly), give Claude the embed's own URL; the page around it can't see inside.
- A form that gets few visits can still be audited: the field, input and trust checks don't need traffic. The skill just won't grade the funnel.
- Run it again a month after the changes and compare completion rates.
