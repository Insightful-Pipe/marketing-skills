# How to Use This Skill

Hey Claude, I just added the "pricing-page-auditor" skill. Audit my pricing page with the last 30 days of GA4 data and tell me why visitors aren't picking a plan.

## What it does

It reads your GA4 property through the InsightfulPipe MCP and builds a behaviour report for the pricing page: how many visitors reach it, where they come from, how long they read, how many reach the bottom, what they open next, whether plan clicks and sign-ups are measured, and how mobile compares with desktop. Then it reads the page and scores eight pillars: tier architecture, price anchoring, value hierarchy, visual guidance, trust, urgency, objection handling and CTA clarity. You get a score out of 100, a grade, and fixes ranked by what the data shows.

## Example prompts

**Full audit**
Hey Claude, I just added the "pricing-page-auditor" skill. We have 3 plans and want more people on the middle one. Audit https://yoursite.com/pricing with our GA4 data.

**Behaviour report only**
Hey Claude, I just added the "pricing-page-auditor" skill. Give me a pricing page behaviour report for the last 30 days: reach, sources, scroll, next pages, devices.

**Too many plans?**
Hey Claude, I just added the "pricing-page-auditor" skill. We show 5 plans and I think it's too many. Should we merge some, and which?

**Psychology check**
Hey Claude, I just added the "pricing-page-auditor" skill. Am I anchoring well? Would a decoy plan help, or per-seat framing?

**Competitor comparison**
Hey Claude, I just added the "pricing-page-auditor" skill. Compare my pricing page with https://competitor.com/pricing and tell me what to borrow.

**Upgrade problem**
Hey Claude, I just added the "pricing-page-auditor" skill. 80% of our customers stay on the entry plan. What on the pricing page holds them back?

**Annual billing**
Hey Claude, I just added the "pricing-page-auditor" skill. Only 20% pick yearly billing. How do I present annual so more people choose it?

## What to have ready

- **GA4 connected** in the InsightfulPipe MCP (the skill finds the pricing page itself).
- **The plan you want most buyers to pick.** If you don't say, it uses the plan the page highlights.
- **Optional:** a competitor's pricing URL, your plan mix or upgrade rate, and any limits (prices fixed, names fixed).
- **Optional:** Microsoft Clarity connected, for rage and dead clicks on the page (untested until connected).

No GA4? It still audits the page and the competitor comparison, and marks the behaviour checks unknown.

## What you get

1. Score and grade, with the math
2. Executive summary: strength, blocker, quick win, and what's at stake in your own numbers
3. Scorecard: six behaviour checks and eight page pillars
4. Pricing page behaviour report
5. Critical issues and improvements, each with evidence
6. Tier-by-tier notes
7. Pricing psychology: what you use and what to test
8. Rewrites: plan taglines, button labels, FAQ questions
9. A/B tests with the GA4 event that will measure each one
10. Competitor comparison
11. Unknowns and limitations

## Fixes it can make (only after you say yes)

- Mark a plan-click or sign-up event as a GA4 key event, once that event is firing.
- Turn on scroll or outbound click tracking if they're switched off.

Both need a Read & Write connection, and an owner, admin or operator can switch them off. It never changes your prices, plans or page.

## Tips

- Small sites: under 100 pricing views a month, treat the behaviour findings as directional. Under 30, the skill audits the page alone.
- If your sign-up lives on a subdomain (app.yoursite.com), GA4 won't count clicks to it by default. The skill checks for this and explains the fix.
- Share a mobile screenshot if the screenshot service can't reach your page.
