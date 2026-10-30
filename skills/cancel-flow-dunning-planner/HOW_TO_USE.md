# How to Use This Skill

Hey Claude, I just added the "cancel-flow-dunning-planner" skill. Look at our billing export and tell me how much we lose to cancellations versus failed payments, then plan the fixes.

## What you need

- **Your billing data,** in any of these forms:
  - Stripe connected through the InsightfulPipe MCP, and the skill reads subscriptions, invoices and failed charges itself
  - a subscription export from Stripe, Chargebee, Paddle, Recharge, App Store Connect or Google Play that you paste or upload
  - or, with no data at all, a description of how cancelling and failed payments work today
- **Your exit-survey answers,** if you collect them, and your save offer log if you show an offer today.
- **Your plans, prices and cost to serve each plan.** Without the cost, the skill plans pauses, plan changes and help, but no discount.
- **Screenshots of today's cancel screens and failed-payment emails,** if you have them.
- **GA4 or Klaviyo** connected, if you use them. GA4 shows how many people reach your cancel pages; Klaviyo shows any payment-failed flow you already run.

## Example requests

**Where the churn comes from**
Hey Claude, I just added the "cancel-flow-dunning-planner" skill. Here's our Stripe export for the last six months. How much of our churn is involuntary, and which exit reasons cost us the most?

**Design a cancellation flow**
Hey Claude, I just added the "cancel-flow-dunning-planner" skill. Right now people email support to cancel. Design a cancel flow with the right answer for each reason, and check every offer against our margins. Starter costs us $8 a month to serve, Growth $11.

**Dunning emails**
Hey Claude, I just added the "cancel-flow-dunning-planner" skill. Our failed payments mostly end in cancellations. Plan the retry window and write the dunning emails and in-app notices.

**Review our save offer**
Hey Claude, I just added the "cancel-flow-dunning-planner" skill. We offer everyone 30% off when they try to cancel. Here's the log. Is it working, and for which reasons?

**Load the drafts**
Hey Claude, I just added the "cancel-flow-dunning-planner" skill. Plan the dunning emails, then load them into Klaviyo as templates. Show me the drafts first.

## What you get

1. **The split:** lost monthly revenue from customers who chose to leave and from failed payments, with the involuntary share, and every cause ranked by money.
2. **Failed payments by type:** new card needed, customer approval needed, or try again later, each with its recovery rate and days to recover, and a retry window set from your own recoveries.
3. **Why people leave,** ranked by lost revenue, and a check of any save offer you show today against who was still paying 90 days later.
4. **A cancellation flow:** one optional reason question, one answer per reason (pause, cheaper plan, annual price, setup help, or a plain goodbye), every discount checked against the plan's gross margin, and a cancel button on every screen.
5. **A failed-payment plan:** retries, card-update emails on set days, in-app notices, and renewal reminders for annual plans.
6. **Every message written in full:** cancel screens, dunning emails, notices, the cancellation confirmation and the renewal reminders.
7. **A fairness check** against US, California and German cancellation rules, and the numbers to watch with today's baselines.

## What it can change for you

With your yes on the exact drafts, it can:
- load each written email into Klaviyo as an email template

It never builds or edits a flow, sends anything, creates coupons, or changes your billing tool. Your team applies the retry settings and the cancel screens from the report.

## Tips

- Give it at least six months of billing data. If fewer than 30 subscriptions ended, it reads a year.
- Include the cancel offer log if you have one: what people did 90 days after taking an offer matters more than how many took it.
- Run it again a quarter after the changes go live, and compare the recovery rates and the involuntary share with the baselines.
