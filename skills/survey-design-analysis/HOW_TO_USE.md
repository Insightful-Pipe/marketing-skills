# How to Use This Skill

Hey Claude, I just added the "survey-design-analysis" skill. Analyse our customer survey answers, tell me which results are real, and fix the questions for next time.

## What you need

- **The decision the survey is for,** such as which feature to build next or why customers cancel.
- **Either a draft survey, or the answers.** Paste the questions, or upload the response file (CSV or spreadsheet) from Google Forms, Typeform, SurveyMonkey, Mailchimp or any other tool.
- **The size of the audience,** and its mix by plan, industry or whatever segments you care about. The skill uses it for the sample size and to check who answered.
- **Optional: the InsightfulPipe MCP,** with Google Sheets (where a Google Form saves its answers), Mailchimp or BigQuery for the answers, and Klaviyo, Mailchimp, Shopify or WooCommerce for the send list. Nothing has to be connected. The BigQuery query action is filed with the write actions, so reading from BigQuery may need a Read & Write connection.

## Example requests

**Write a survey**
Hey Claude, I just added the "survey-design-analysis" skill. Write a short customer satisfaction survey for our 1,800 active customers. We want to know whether onboarding is the reason people stall.

**Check a draft**
Hey Claude, I just added the "survey-design-analysis" skill. Here are my draft customer survey questions. Check them for bias and rewrite the weak ones.

**Sample size**
Hey Claude, I just added the "survey-design-analysis" skill. We have 650 customers who bought in the last 90 days. How many answers do we need, and how many invites should we send?

**Analyse results**
Hey Claude, I just added the "survey-design-analysis" skill. Here's the CSV from our NPS survey. Give me NPS with its range, compare plans, and code the comments.

**From Google Sheets**
Hey Claude, I just added the "survey-design-analysis" skill. Our Google Form saves to the sheet "Q4 customer survey". Analyse it and tell me what's real and what isn't.

## What you get

1. **A question audit:** each question passed or failed against a bias list, with a rewrite for every failure.
2. **Sample size math:** the completes and invites you need, and the margin of error you'll actually get.
3. **A cleaning log:** duplicates, speeders and incompletes removed, with counts.
4. **A check of who answered** against your customer base, with a reweighted headline when the mix is off.
5. **Results with ranges:** every percentage with its margin of error, and NPS with its confidence range.
6. **Tested segment comparisons,** adjusted for the number of tests, so a lucky gap isn't sold as a finding.
7. **A MaxDiff ranking** scored by simple counts, with ties marked.
8. **Coded open answers** with counts and one quote per theme.
9. **A one-page findings summary,** and fixes for the next wave.

## What it can do for you

With your yes on the exact payload, it can draft the survey invite as a Klaviyo or Mailchimp campaign to the segment you choose, and save the coded open answers to a new tab in your Google Sheet. Drafts stay drafts: you add the survey link and send them yourself. It never sends an email or changes your lists.

## Tips

- Give each survey one decision. A second question goes into its own survey.
- Decide the segment comparisons before you send. A cut you pick after seeing the answers is exploratory.
- If a segment matters, plan for about 100 answers in it; a large population needs about 385 for plus or minus 5 points.
- Join plan, tenure and industry from your account data instead of asking for them.
