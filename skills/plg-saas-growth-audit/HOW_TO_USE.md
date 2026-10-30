# How to Use This Skill

Hey Claude, I just added the "plg-saas-growth-audit" skill. Audit our self-serve funnel from first visit to churn and tell me which leak costs us the most MRR.

## What you need

- **A short description of the business:** plans and prices, whether new users start on a trial (with or without a card) or a free plan, the trial length, and how much sales is involved.
- **Your activation event:** the first action that shows a new account got value. If you don't have one yet, name the action you believe matters most.
- **Your numbers, in any of these forms:**
  - pasted monthly figures (sessions, signups, activated, paid, and your MRR movements)
  - a billing export from Stripe, Chargebee, Paddle, Recurly or similar, and a product export with one row per new account
  - or the InsightfulPipe MCP connected to Claude with GA4, Google Ads, Meta Ads, LinkedIn Ads, BigQuery or Stripe, so the skill pulls them itself
- **Targets,** if you have any. Without them, the skill uses the average of your own three best months.

## Example requests

**Full audit**
Hey Claude, I just added the "plg-saas-growth-audit" skill. Here are our Stripe export and our signup export. Audit the whole funnel for the last six months and rank the leaks by MRR.

**Growth stalled**
Hey Claude, I just added the "plg-saas-growth-audit" skill. Our MRR growth slowed this summer. Find which stage changed and when.

**PLG metrics check**
Hey Claude, I just added the "plg-saas-growth-audit" skill. Compare our activation, signup to paid and churn with published SaaS benchmarks, and tell me which ones are actually a problem for us.

**Before a planning meeting**
Hey Claude, I just added the "plg-saas-growth-audit" skill. We can work on one growth problem next quarter. Which one is worth the most, and which skill should take it from here?

## What you get

1. **Trust checks first:** whether the MRR movements add up, whether signup counts agree across sources, and whether the latest cohort is old enough to judge.
2. **A scorecard for seven stages:** visit to signup, signup to activated, activated to paid, expansion, cancellations and downgrades, failed payments, and referral. Each shows six months of rates, your target and where it came from, and a sourced benchmark where a trustworthy one exists.
3. **Ranked fixes,** each with the MRR at stake per month, the formula with your numbers in it, the month the gap opened, and who does the fix.
4. **Acquisition cost by ad platform:** cost per paying customer and months to pay it back.
5. **Unknowns:** what couldn't be measured and what would fill it.

## What it changes

Nothing. It reads your data and writes a report. Each fix points to the skill that does it, such as onboarding-cro, signup-flow-cro, pricing-strategy or referral-program, if installed.

## Tips

- Six complete months gives the best targets; three is the minimum for targets from your own months. With less, only activation and combined churn get a target, from published SaaS benchmarks.
- Tell it about recent changes (a new onboarding, a billing move, a price change) and their month. The audit names them when a gap opens in the same month.
- Run it again a month after a fix to see whether that stage's MRR at stake fell.
