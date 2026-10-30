# How to Use This Skill

Hey Claude, I just added the "trial-to-paid-optimizer" skill. Here's our billing export. Work out why our free trial users don't pay and give me the plan to fix it.

## What you need

- **A billing or subscription export** from Stripe, Paddle, Chargebee or RevenueCat, with trial start, trial end and the first paid date. With Stripe connected through the InsightfulPipe MCP, the skill pulls subscriptions and paid invoices itself.
- **The date each trial activated,** from a product usage export or the GA4 export in BigQuery, so it can compare trials that got value with those that didn't. Without it, you still get the cohort, source and touch parts.
- **Your trial setup:** length, card rule (card up front, no card or reverse trial), what happens at the end, and your activation event.
- **The touches running today,** with the day each one goes out. Connect Klaviyo or Mailchimp and it reads the emails and their results.
- **Who can call trials,** and how many calls a week they can take, if anyone.

## Example requests

**Find out why trials don't pay**
Hey Claude, I just added the "trial-to-paid-optimizer" skill. Our 14-day free trial converts at about 10%. Here's the Stripe export with activation dates. Tell me why trials don't pay and what to fix first.

**Is our free trial conversion rate good?**
Hey Claude, I just added the "trial-to-paid-optimizer" skill. We run a 7-day trial with a card up front. Compare our trial-to-paid rate with the published benchmarks and tell me where we stand.

**Card or no card, and how long**
Hey Claude, I just added the "trial-to-paid-optimizer" skill. Should we shorten our 30-day trial or ask for a card? Use our activation timing to decide, and tell me what you can't judge from this data.

**Check the trial emails**
Hey Claude, I just added the "trial-to-paid-optimizer" skill. Read our trial flow in Klaviyo, lay it out day by day and tell me where the gaps are.

**When should sales step in**
Hey Claude, I just added the "trial-to-paid-optimizer" skill. We have two account executives. Which trials should they call, and on what day?

**Plan the tests**
Hey Claude, I just added the "trial-to-paid-optimizer" skill. We get about 40 trials a week. Which trial tests can we actually run, and how long does each one take?

## What you get

1. **Your trial-to-paid rate** over 12 weeks of finished trials, week by week.
2. **The activation split:** how much more often trials that activated pay, when activation happens, and how many more paying accounts 10 points of activation would bring.
3. **The source split:** which channels bring trials that pay, and which bring trials that never start using the product.
4. **A benchmark** against published card-required and no-card ranges, with source and year.
5. **A day-by-day touch calendar:** what runs today, five gap checks, and the touches to add, split by activated and not.
6. **Length, type and sales verdicts,** each with the numbers behind it.
7. **A target rate** and **a test plan** sized to your weekly trial volume, saying which tests are too slow to run as A/B tests.

## What it changes

Nothing. It reads your data and writes the plan. Emails, flows and trial settings stay as they are.

## Tips

- Join activation to billing on your account id. Email addresses change; account ids don't.
- Give it at least 12 weeks of trials that have ended, so every trial counted has had its full chance to pay.
- Rerun it 12 weeks after the changes ship, on the new trials, to see the rate move.
