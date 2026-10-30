# How to Use This Skill

Hey Claude, I just added the "klaviyo-flow-auditor" skill. Audit my Klaviyo flows and tell me what is missing and who is unengaged.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Klaviyo account added.** The skill reads flows, reports, lists, segments, profiles and events itself; you don't need to export anything.
- **Or, for the other modes:** Mailchimp, Shopify or WooCommerce connected through InsightfulPipe, or the exports from any email platform and store (flow report, campaign report, list size, abandoned checkouts and orders). Nothing connected works too: paste the exports.
- **Your business model,** if it isn't obvious: online store, subscription, or lead and SaaS. It decides which flows you should have.
- **How long counts as unengaged** for you. Without it, the skill uses 180 days with no click, open or site visit after at least 5 emails.

## Example requests

**Full audit**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. Run a full audit of my Klaviyo account for the last 90 days. We're an online store.

**Flow gap check**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. Which of the core flows (welcome, abandoned cart, browse, post-purchase, winback) am I missing, and which ones could I build today with the data I already track?

**Flow performance**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. Rank my flows by revenue per recipient and show me the email in each flow that needs rewriting.

**Unengaged subscribers and winback**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. How many of my subscribers are unengaged? Build me a winback and sunset plan from the numbers.

**Abandoned cart recovery review**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. What's my real abandoned cart recovery rate, measured from Shopify orders rather than Klaviyo's attribution? Which channel brings people back, and is my checkout flow's timing, discount and SMS step set up well?

**Email marketing audit on Mailchimp, with dollar figures**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. We're on Mailchimp. Run an email marketing audit and tell me what each missing or weak automation is worth per month, with the math shown.

**Clean-up**
Hey Claude, I just added the "klaviyo-flow-auditor" skill. Find profiles that bounced or marked us as spam but can still get email, and show me the list before suppressing them.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for five areas:** flow coverage, flow performance, lists and segments, engagement, and deliverability and consent.
3. **A flow map** of the six core flows: live, not live, missing (with or without the data to build it), or not applicable.
4. **The top 5 fixes,** each with the numbers behind it.
5. **A re-engagement plan** sized from your own unengaged count, plus the exact segment to build in Klaviyo.
6. **A list of what couldn't be checked,** and why.
7. **In the recovery review:** your recovery rate by count and value from the store's own orders, the split by channel (email, text, paid, on its own) next to what the email platform claims, how fast people come back on their own, a step-by-step check of the flow, and the shoppers who only buy with a code.
8. **In the any-platform audit:** the same five areas on Mailchimp or your exports, plus a money view: email revenue from flows against campaigns, value per subscriber, and a monthly range for each missing or weak flow, built from your own trigger volume with its assumption printed.

## What it can change for you

With your yes on the exact change, it can:
- put unengaged profiles on a new list so you can review them
- suppress profiles that bounced or complained and can still receive email
- set a flow you've reviewed from draft to live

It never writes or sends emails, builds flows, or deletes profiles. Klaviyo doesn't let segments be created through the API, so it gives you the segment definition to build in Klaviyo.

## Tips

- Run it monthly, and after launching or changing a flow.
- For the recovery review, leave 7 days after the window so every abandoned checkout has had its time to come back.
- Treat the house starting ranges in the money view as placeholders: once a flow has run for a few months, its own rate replaces them.
- Open rates are inflated by mail privacy features, so the skill judges flows on clicks and revenue.
- On a very large account, build the unengaged segment in Klaviyo first; the skill can then read its size instead of pulling every email event.
