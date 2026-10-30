---
name: trial-to-paid-optimizer
description: Works out why free trial users don't pay and plans the fix for the whole trial. Measures trial-to-paid conversion from a billing or subscription export (Stripe, Paddle, Chargebee, RevenueCat) or from Stripe through the InsightfulPipe MCP, splits trials by whether they activated and by acquisition source, compares the rate with published card-required and no-card benchmarks, checks the day-by-day touches (email from Klaviyo or Mailchimp, in-app, calls), decides trial length and type (card up front, no card, reverse trial) and when a person should step in, then sets a target rate and a test plan sized to the product's own trial volume. Use when someone asks about free trial conversion rate, trial-to-paid, why trials don't convert, SaaS free trial best practices, trial length, card or no card, or how to improve free trial conversion. Changes nothing in any account.
---

# Free Trial Conversion Optimizer

A trial converts or fails on four things: who starts it, what they do inside it, what they hear while it runs, and whether a person talks to them. This skill measures each one on the product's own trials, finds the one that moves the rate most, and turns it into a plan with a target and tests the product has the volume to run.

Every number in the report comes from the user's export or a call below. Where the data can't answer a question, the report says so instead of guessing.

## Before you start

Ask for these, and use the defaults when the user doesn't know:

1. **The trial today.** Length in days, the card rule (card up front, no card, or a reverse trial that starts on a paid plan and drops to a free plan), and what happens at the end (charged, locked, or moved to a free plan).
2. **The activation event.** The action inside the product that shows a trial got real value: a first report shared, a first client booking, a first invoice sent. No default: if the user can't name one, run the cohort and source parts, mark the activation split **not graded**, and point to Onboarding CRO (if installed) to find one.
3. **Plans and monthly prices,** to put money on the findings.
4. **Who can talk to trials.** A sales or success team and how many calls a week it can take, or none.
5. **The touches running today.** For each email, in-app message or call: the trial day it goes out, who gets it (everyone, or only some), and what it asks the user to do. With Klaviyo or Mailchimp connected, the skill reads the messages and their results; Klaviyo's report doesn't return the send day of a message, so ask for it.

**Data, from the strongest to the weakest:**

| What | Best source | Fallback |
|---|---|---|
| Trials and payments | Billing export uploaded as CSV (Stripe, Paddle, Chargebee, RevenueCat), or Stripe through the MCP | The user's own counts: trials started and trials paid per week |
| Activation per trial | Product usage export with the account id and activation date, joined to billing on that id | GA4 export in BigQuery with `user_id` set to the account id |
| Source per trial | Signup source in the product or CRM export | GA4 first-user channel, source level only |
| Touches | Klaviyo or Mailchimp through the MCP | The user's list of touches |

Whatever the source, build one row per trial with these fields: trial id, trial start, trial end, source, activation date (blank if none), first paid date (blank if none), plan and monthly price paid, and any plan-size signal the product records at signup (seats, staff, locations).

**Window.** Use 12 complete Monday to Sunday weeks of trial starts. The last week ends on the latest Sunday where Sunday + trial length + grace days falls on or before today, so every trial in the window has had its full chance to pay. Default grace: 7 days after the trial ends, to catch late plan picks and payment retries. Print the window, the grace and the date every trial settled by.

## How to run the calls

Only needed when a platform is connected through InsightfulPipe; otherwise work from the uploaded or pasted files. Call `query_contexts` with `request="accounts"` for each platform to get `workspace_id`, `brand_id` and the account ids, then `request="actions_details"` for the actions below, and follow the body shapes it returns. If a call fails, mark the part it feeds **unknown**, say which call failed and why, and keep going.

**Stripe: trials and payments** (untested until a Stripe account is connected; body shapes from the action details).
```json
{"action": "get_subscriptions", "status": "all", "created[gte]": <unix seconds 30 days before the window starts>, "limit": 100, "auto_paginate": true}
```
```json
{"action": "get_invoices", "status": "paid", "created[gte]": <unix seconds of the window start>, "limit": 100, "auto_paginate": true}
```
- A trial is a subscription with `trial_start` set. `trial_start` and `trial_end` are Unix timestamps.
- `status` defaults to subscriptions that aren't canceled; `"all"` is needed, or every trial that ended without paying disappears.
- A trial paid when an invoice for that `subscription` has `amount_paid` above 0. Stripe opens a trial with a 0 invoice, so never count the first invoice by itself as a payment.
- If the product creates the Stripe subscription only when someone pays (common with no-card trials), Stripe can't see trials at all. Take the trial starts from the product's signup export and the payments from `get_invoices`, joined on the customer.

**BigQuery: activation and source per trial** (the GA4 export, when the product sets `user_id` to its account id).
```json
{"action": "list_datasets"}
```
```json
{"action": "run_query", "max_rows": 50000, "query": "SELECT user_id, ANY_VALUE(traffic_source.source) AS first_source, ANY_VALUE(traffic_source.medium) AS first_medium, MIN(IF(event_name = '<activation event>', TIMESTAMP_MICROS(event_timestamp), NULL)) AS activated_at FROM `<dataset>.events_*` WHERE _TABLE_SUFFIX BETWEEN '<YYYYMMDD>' AND '<YYYYMMDD>' AND user_id IS NOT NULL GROUP BY user_id"}
```
- `traffic_source` in the GA4 export is the user's first-touch source, which is what this split needs.
- Rows come back as `rows[].f[].v`, every value a string, in the order of `schema.fields`. Read them by position.
- Every table the query touches must sit in the connected project (Google's public datasets excepted). If `list_datasets` shows no `analytics_` dataset, the GA4 export isn't linked; use a product export instead.

**GA4: source-level view** (when there is no per-trial join).
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["firstUserDefaultChannelGroup", "eventName"], "metrics": ["totalUsers"],
 "start_date": "<window start>", "end_date": "<window end + trial length>",
 "dimensionFilter": {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["<trial start event>", "<activation event>", "<paid event>"]}}}}
```
This gives users per event per first channel. It can't tell whether the users who activated are the users who paid, so with GA4 alone the activation split is **not graded** and the source split shows rates per channel only. Call `list_key_events` first to see which of these events the property records.

**Klaviyo: the trial emails.**
- `get_flows` with `filter` `equals(status,'live')`: the live flows. Pick the ones that trial users enter.
- `get_metrics`: find the metric that records a paid plan starting, and pass its id as `conversion_metric_id`. Left out, Klaviyo counts its "Placed Order" metric, which a software trial usually never fires.
- `get_flow_report` with `timeframe` `{"key": "last_90_days"}`, `group_by` `["flow_id", "flow_message_id", "flow_name", "flow_message_name"]` and `statistics` `["recipients", "delivered", "open_rate", "click_rate", "conversions"]`. Rates come back as fractions. One row per message.

**Mailchimp: the trial emails** (untested until a Mailchimp account is connected).
- `list_automations`, then `list_automation_emails` with the `workflow_id` of each trial automation. If the response includes each email's delay, use it as the send day; otherwise ask.

## The analysis

### 1. Cohort

- **Trial-to-paid rate** = trials that paid on or before trial end + grace ÷ trials that started in the window.
- Show the rate per start week. Flag a week with 30 or more trials whose rate is above 1.5x or below half the 12-week rate, and ask the user what happened that week (a promotion, an outage, a pricing change) before reading anything else.
- Trials per week = trials in the window ÷ 12. Every test in step 9 is sized with it.

### 2. Activation split: where to push

- A trial **activated** when its activation date is on or before its trial end. Activation after the end doesn't count for the split; report how many there were.
- Report the activation rate, the trial-to-paid rate of activated and of non-activated trials, and how many times more often activated trials pay.
- Report the median and the 80th percentile trial day of activation (day 0 is the trial start).
- **Check the definition.** It holds when activated trials pay at least 2x as often as the rest and at least 60% of paying accounts activated first. If not, say the definition is weak; every later step leans on it.
- **Size the lever:** extra paying accounts per 12 weeks if activation rose 10 points = trials × 0.10 × (activated rate − non-activated rate). Multiply by the average monthly price of the plans paid for the revenue it adds.

### 3. Source split

- Per source: trials, share of trials, activation rate, trial-to-paid rate, share of paying accounts.
- A source with fewer than 30 trials in the window is **too few to judge**. Show it, don't rank it.
- Call out the source whose share of trials is well above its share of paying accounts, and the source with the best rate per trial. A source that brings many trials that never activate is a first-run or targeting problem, not a trial problem; say which.

### 4. Benchmark

Compare the rate with the published band for the product's card rule, always naming the source and year:

| Source | Bands |
|---|---|
| ChartMogul, The SaaS Conversion Report by Kyle Poyar (survey January 2026, 200 software products) | No card: GOOD 4-6%, GREAT 10-15%. Card required: GOOD 25-35%, GREAT 50-60%. Reverse trial: GOOD 4-6%, GREAT 8-12%. |
| Lenny's Newsletter, "What is a good free-to-paid conversion rate" by Kyle Poyar and Lenny Rachitsky (August 2023, 1,000+ products) | Free trials: GOOD 8-12%, GREAT 15-25%, counting accounts that pay within 6 months of signup. |

Say where the rate sits in each, and say that the two sources count differently and disagree. A rate counted to trial end + 7 days reads lower than a 6-month count. The band is context; the product's own weekly rate is the scoreboard.

### 5. Touch calendar

Lay the touches on a day 0 to day (trial length + grace) line, with who gets each one. Then run these checks and mark each **ok** or **gap**:

1. **Activation nudge early.** A touch in days 0 to 2 that asks for the activation step and goes only to trials that haven't activated.
2. **Branch on activation.** At least one touch that activated and non-activated trials receive differently. Telling a trial that already got value how to get value wastes the message.
3. **Ending notice.** A touch in the last 3 days of the trial saying what happens at the end. With a card on file, the notice says when the charge comes and how much.
4. **After the end.** A touch in the grace days to trials that didn't pay. A locked account with no message is the quietest place to lose a trial that activated.
5. **A person, where the sales rule says so** (step 7).

Then propose the calendar: keep what passes, fix each gap, and say which touches go to whom. With Klaviyo data, show each message's recipients, open rate and click rate next to it, and note that the report's 90 days aren't the trial window. The skill plans the touches; Email Sequence Builder (if installed) writes them.

### 6. Trial length and type

**Length,** from the activation timing:
- If the 80th percentile activation day + 3 is at most half the trial length, a shorter trial is worth testing (most trials that will activate already have).
- If more than 20% of activations (counting those after the end) land in the last 2 trial days or after the end, activation is too slow for the trial. Fix activation first; a longer trial only delays the same stall.
- Otherwise keep the length.

**Type:**
- **Card up front** raises trial-to-paid because fewer, keener people start, so trial-to-paid can't judge it. Judge it on paying accounts per 1,000 visitors to the signup page, in a split test, and only after activation is fixed. Without signup-page visitors in the data, say it can't be sized.
- **Reverse trial** needs a free plan to drop to. Recommend testing it only when the product has one and the paid features show their value within the trial.
- **No card** stays when the activation split holds and the touches still have gaps: those are cheaper fixes.

### 7. When a person steps in

- Pick the segment from a signal recorded at signup that points to the higher plans (seats, staff, locations, company size). Compare its trial-to-paid rate with the rest.
- Offer a person (a setup call, a named contact) to that segment when its trials per week fit the team's weekly capacity. If they don't, narrow the segment until they do.
- Timing: before the median activation day for trials that haven't activated, so the call removes the stall instead of explaining it afterward.
- With no one to make calls, skip this step and say so.

### 8. Target

Target rate = (activation rate + 10 points) × activated trial-to-paid rate + (the rest) × non-activated rate, with both group rates held at today's values. State the formula, the starting rate, and that it's judged on the trials that start in the 12 weeks after the changes ship. If the definition check failed, give no target.

### 9. Test plan, sized to the product's volume

For each change worth testing:
- Name the change, who gets it, the metric (activation within the trial for activation changes; trial-to-paid for changes aimed at payment), the baseline from step 1, 2 or 3, and the lift to detect (10 points by default).
- **Trials per arm** for a two-sided test at 95% confidence and 80% power: n = (1.96 × √(2p̄(1−p̄)) + 0.8416 × √(p₁(1−p₁) + p₂(1−p₂)))² ÷ (p₂ − p₁)², where p₁ is the baseline, p₂ the baseline plus the lift and p̄ their average. Round up.
- **Weeks needed** = 2n ÷ eligible trials per week, rounded up.
- 12 weeks or less: run it as a 50/50 A/B test. More than 12: too slow at this volume. Ship it to every trial it targets, compare the 8 weeks after with the 8 weeks before, and label the result weaker evidence.
- Two kinds of change ship without a test: a touch that fills an empty slot and reaches only trials that didn't pay (an after-the-end email when nothing goes out today), and narrowing a touch that exists to the trials it fits (tips only to trials that activated).

Test design detail lives in A/B Test Designer (if installed).

## The report

1. **Summary:** the rate, the window, the biggest lever with its size, the target.
2. **Cohort:** the rate and the weekly table.
3. **Activation split:** the two rates, the multiple, the timing, the definition check, the lever.
4. **Source split:** the table and the two call-outs.
5. **Benchmark:** both bands, where the rate sits, the caveat.
6. **Touch calendar:** today, the five checks, the proposed calendar.
7. **Length and type:** each verdict with its numbers.
8. **Sales rule:** the segment, its rate, the weekly load against capacity.
9. **Target** and **test plan** with sizes and verdicts.
10. **Not checked,** and why.

## Fixes this skill can run

None. It reads data and plans. Emails, flows, pricing and trial settings stay as they are until the user changes them.

## Rules

- Count only settled trials. A trial still running, or inside its grace days, is neither paid nor lost.
- Never fill a missing activation or source with a guess. Mark the part **not graded** and say what data would grade it.
- Every benchmark carries its source and year. Never quote a band without them.
- Keep the user's own currency and plan names.
- Customer emails and ids from an export stay in the analysis; the report shows counts and rates, never a list of people.

## Go deeper

- **Onboarding CRO** (if installed): find a better activation event and design the first run.
- **Pricing Strategy** (if installed): whether a free plan, a trial or both fits the product.
- **Email Sequence Builder** (if installed): write the trial emails this plan calls for.
- **A/B Test Designer** (if installed): set up and read the tests in step 9.
