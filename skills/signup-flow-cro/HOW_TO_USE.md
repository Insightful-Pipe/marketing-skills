# How to Use This Skill

Hey Claude, I just added the "signup-flow-cro" skill. Audit our signup flow and tell me where we lose people between the signup button and a working account.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the numbers itself; you don't need to export anything.
- **Your signup page URL,** if it isn't obvious from your site's signup links.
- **Your activation event,** if you have one: the first action that shows a new user got value (for example connecting an account or creating a first project).
- **Where else signup is tracked,** such as a product analytics tool, so gaps in GA4 can be explained.

Without GA4, the skill still tears down your signup page and builds the funnel from numbers you give it.

## Example requests

**Full audit**
Hey Claude, I just added the "signup-flow-cro" skill. Audit our signup flow for the last 30 days. Our signup page is https://app.example.com/signup and activation is the create_project event.

**Signups dropped**
Hey Claude, I just added the "signup-flow-cro" skill. Signups fell this month. Show me which step lost people and on which device.

**Page review only**
Hey Claude, I just added the "signup-flow-cro" skill. Review our create-account page: the sign-in options, the fields, the password rules and what's distracting people.

**Tracking first**
Hey Claude, I just added the "signup-flow-cro" skill. Check whether GA4 can even see our signups, and tell me what to fix in the tracking before anything else.

**Policy questions**
Hey Claude, I just added the "signup-flow-cro" skill. Should we require email verification before people get in, and should we ask for a card at signup? Use our data.

## What you get

1. **A measurement grade** (measured, partly measured or not measured), with the checks behind it.
2. **The path into signup:** the pages that carry the signup button, their sessions, their recorded signup clicks and the device split.
3. **The funnel** from signup page to `sign_up` to your activation event (with email verification as a step when your app sends an event for it), by step, sign-in method and device, against the previous period. When GA4 can't see the signup, the report says where its view stops and why, and never estimates signups from page views.
4. **A teardown of the rendered signup page:** sign-in options, fields, field setup, password rule, clicks to the first field, distractions, value line, button text, bot protection, legal line, labels and load time, each scored with the evidence.
5. **Up to 5 fixes,** ranked with tracking first and then by the visitors each step touches, and **3 test ideas** with a hypothesis each.
6. **What couldn't be checked,** such as the verification email and the first screen after signup, which the skill never signs up to see.

## What it can change for you

With your yes on the exact change, it can update GA4:
- make `sign_up` a key event
- turn on outbound-click and form-interaction tracking
- register a signup parameter as a custom dimension

It never changes your signup page or app, and never creates an account.

## Tips

- If your app lives on another domain or subdomain, say which tool tracks it. GA4 often sees only the marketing site.
- Run it again a month after a change to see the step rates move.
- For what happens after signup, follow up with the `onboarding-cro` skill, if you have it installed.
