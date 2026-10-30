# How to Use This Skill

Hey Claude, I just added the "measurement-plan-builder" skill. Build a measurement plan for my business from what my analytics and ad accounts already track: a North Star, a KPI tree and a tracking plan.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** Search Console, Google Ads, Meta Ads, LinkedIn Ads and Google Tag Manager are optional; the more are connected, the more of the plan gets a real baseline.
- **Your business model,** if it isn't obvious: SaaS, lead generation, ecommerce or content.
- **Where conversions happen:** on your site, in an app on another domain, or offline in a CRM.
- **Numbers that only you have,** such as active accounts or revenue from your product database or billing. Without them, those KPIs are marked "outside connected sources".

## Example requests

**The full plan**
Hey Claude, I just added the "measurement-plan-builder" skill. We're a B2B SaaS and people sign up in our web app. Build our North Star, KPI tree, measurement plan and tracking plan from what we track today.

**Just the metric system**
Hey Claude, I just added the "measurement-plan-builder" skill. Help me pick a North Star metric for our lead generation business, with the inputs that drive it and the guardrails we shouldn't break.

**Just the tracking plan**
Hey Claude, I just added the "measurement-plan-builder" skill. Look at the events our GA4 property sends and write a tracking plan with a naming convention, the events we're missing and the ones to clean up.

**Plan, then write it down**
Hey Claude, I just added the "measurement-plan-builder" skill. Build the tracking plan and put it in a new tab of my Google Sheet. Show me the rows first.

## What you get

1. **What is measured today:** each connected source marked measuring, undercounting, not measuring, no activity or not connected, with the number behind it.
2. **A metric system:** one North Star tested against six rules, the inputs that move it and the guardrails.
3. **A KPI tree** up to 4 levels below the North Star, with a 28-day baseline and prior period on every node, or a status that says why it has none.
4. **A measurement plan:** definition, single source of truth, baseline, target, owner, cadence and the decision each KPI drives.
5. **A tracking plan:** naming rules, the event table, key events to keep or archive, custom definitions, and a conversion map across GA4, Google Ads, Meta and LinkedIn.
6. **A build order,** ranked by how many KPIs each tracking fix unblocks.

## What it can change for you

With your yes on the exact change, it can:
- mark a planned event that already fires as a GA4 key event
- register a planned event parameter as a GA4 custom dimension
- write the tracking plan into a new tab of your Google Sheet

Tags, triggers, consent and cross-domain settings, and pixels stay with you.

## Tips

- Run it again after each fix in the build order; nodes move from "not tracked" to "measured".
- If GA4 changed recently (a new tag or a consent fix), wait until it has 14 settled days before trusting its baselines. The skill tells you when.
- Targets are yours to set. The skill leaves them as "to set" rather than guessing.
