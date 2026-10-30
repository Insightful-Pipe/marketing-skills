# How to Use This Skill

Hey Claude, I just added the "expansion-revenue-planner" skill. Work out our net revenue retention for the last 12 months and tell me which customers are ready to upgrade.

## What you need

- **Your price list:** plans, what each includes (seats, allowances, features), add-ons and their prices.
- **A billing export** with each account's plan, seats, add-ons and MRR at the start and end of the last 12 months. Stripe, Chargebee, Paddle, Recurly or a spreadsheet all work.
- **A usage export** by account for the last three months: active seats, blocked invites, allowance used, clicks on locked features, your core usage count and payment status.
- **Optional: the InsightfulPipe MCP** with BigQuery, Stripe, Klaviyo, Mailchimp or GA4 connected, so the skill pulls the data and checks your upgrade emails itself.

## Example requests

**Net revenue retention**
Hey Claude, I just added the "expansion-revenue-planner" skill. Here's our Stripe export. Calculate our NRR and GRR for the last 12 months by plan and by signup year, and show me the formula with our numbers.

**Who to upsell**
Hey Claude, I just added the "expansion-revenue-planner" skill. Here's our usage export and price list. Which accounts are ready to upgrade, add seats or buy an add-on, and what is each one worth?

**The full expansion plan**
Hey Claude, I just added the "expansion-revenue-planner" skill. We launch upgrade prompts on November 2. Plan the moments, the emails and the account-manager steps, with targets and a read-out date.

**From BigQuery and Klaviyo**
Hey Claude, I just added the "expansion-revenue-planner" skill. Our billing and product events are in BigQuery and our emails are in Klaviyo. Pull them, work out expansion revenue, and tell me which upgrade emails are missing.

## What you get

1. **NRR, GRR and expansion rate,** with the math, by plan and by signup cohort, and expansion split into upgrades, seats and add-ons.
2. **A ready list:** every account pressing on a limit, with the evidence, the next step, its price and the MRR it adds.
3. **A watch list,** plus the accounts held back because payment is failing or usage is falling.
4. **An upgrade moments plan:** the in-product prompt, the email and the account-manager step for each moment, and which emails already run.
5. **Targets:** a floor from your own past expansion rate, the points it adds to NRR, and a read-out date.

## What it can change for you

Nothing. It never touches plans, prices, subscriptions or emails. The prompts and emails come as briefs for you to build.

## Tips

- Include blocked invites and locked-feature clicks in the usage export. They are the strongest signals.
- Rerun it at the read-out date with fresh exports to see which moments hit their floor.
