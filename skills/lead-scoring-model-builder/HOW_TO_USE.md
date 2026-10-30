# How to Use This Skill

Hey Claude, I just added the "lead-scoring-model-builder" skill. Here's our CRM leads export: build a lead scoring model from our real wins and losses and pick the MQL threshold.

## What you need

- **A leads or deals export from your CRM** (HubSpot, Salesforce, Pipedrive or any other), as a CSV, an Excel file or a Google Sheet. One row per lead with the created date, the outcome (won, lost or open), the close date, the company traits you track, and the dates of actions such as demo requests, pricing visits, email clicks, webinars and trial starts.
- **The date sales first reviews each lead,** if the export has it. That is the moment the score is used.
- **Your current scoring rules and MQL threshold,** if you have them, for the audit.
- **About how many hours a rep spends on each lead they work** (default: 1), so wasted time on losers can be weighed against wins.
- **Optional, through the InsightfulPipe MCP:** the GA4 BigQuery export for per-lead page views, Klaviyo or Mailchimp for email clicks, GA4 for which pages come before lead events, and Google Sheets to read the export or receive the finished rules.

## Example requests

**Build a model from deal history**
Hey Claude, I just added the "lead-scoring-model-builder" skill. Here's 12 months of HubSpot leads with outcomes. Build a lead scoring model from what our wins actually did, and tell me the MQL threshold.

**Audit the model we have**
Hey Claude, I just added the "lead-scoring-model-builder" skill. Our sales team says MQLs are junk. Here are our scoring rules and last year's leads. Check every rule against what really happened and tell me what to change.

**Fit sales capacity**
Hey Claude, I just added the "lead-scoring-model-builder" skill. Our two reps can work about 40 new leads a month. Build the score and set the threshold so they get the 40 most likely to close.

**Score trial users (PQL)**
Hey Claude, I just added the "lead-scoring-model-builder" skill. Here's our trial sign-ups with what each account did in its first week and who paid. Build a product-qualified lead score.

**Add page visits from BigQuery**
Hey Claude, I just added the "lead-scoring-model-builder" skill. Our GA4 export is in BigQuery and we send the CRM lead id as user_id. Pull each lead's pricing and demo page visits, join them to this export and build the model.

## What you get

1. **A trait table:** every company trait and action with its leads, wins, win rate, lift over your base win rate and the points it earns. Traits seen on fewer than 30 leads are flagged, not scored.
2. **A leakage check:** actions that happened after sales reviewed the lead are left out, with the points they would have wrongly earned.
3. **A decay rule** fitted from how win rates fall as the newest action gets older.
4. **A threshold table** with wins caught, losers flagged and sales hours spent on losers at each cut-off. The threshold starts where it still catches 80% of past wins (or the share you set), then drops step by step only while each extra win costs fewer sales hours on losers than working every lead would.
5. **A check on later leads** the model never saw, with a clear verdict.
6. **An audit of your current rules,** rule by rule, with the old and new model side by side.
7. **The rules ready to set up in your CRM,** plus the open leads above the threshold right now.

## What it can change for you

With your yes, it can write the rules and the scored open leads into a new tab of a Google Sheet. It never changes your CRM, your email platform or GA4; you enter the rules in your CRM's scoring tool. BigQuery's `run_query` is listed as a write action because it accepts any SQL, so it needs a Read & Write connection, but this skill only sends it SELECT queries.

## Tips

- Export every lead, not only MQLs. Leads your old model never passed are how the new one finds the wins it would have missed.
- Dates beat counts. An export with the date of each action lets the skill drop actions that happened after the sales call.
- Rerun it each quarter, or after as many new wins as the first model was built on.
