# How to Use This Skill

Hey Claude, I just added the "product-market-fit-assessment" skill. Here is our product-market fit survey export. Do we have product-market fit, and who should we focus on?

## What you need

- **Your survey answers:** a CSV, a pasted table, or a Google Sheet (Google Forms and many survey tools write there). No answers yet? The skill drafts the survey, who to send it to and when to close it.
- **A usage column,** such as logins, bookings or orders in the last 14 days, so only real users count. Without one, the skill says the score is unfiltered.
- **Optional, for the behaviour checks:** the InsightfulPipe MCP with GA4 (a property that tracks the product itself), Search Console, BigQuery, Shopify or WooCommerce. Or paste a cohort table, brand-search clicks and new users by channel.

## Example requests

**Score a survey**
Hey Claude, I just added the "product-market-fit-assessment" skill. Our PMF survey is in the "Responses" tab of this sheet. Score it, and only count people who used the product twice in the last two weeks.

**Run the Sean Ellis test from scratch**
Hey Claude, I just added the "product-market-fit-assessment" skill. We have 600 active users and no survey yet. Set up the Sean Ellis test for us: who to ask, what to ask and when to read it.

**Check the survey against behaviour**
Hey Claude, I just added the "product-market-fit-assessment" skill. 44% said very disappointed. Before we raise prices and scale ads, check our GA4 cohorts and brand search and tell me if usage agrees.

**Find the segment**
Hey Claude, I just added the "product-market-fit-assessment" skill. Our score is stuck at 30%. Which customers already love the product, and what would move the ones who almost do?

## What you get

1. **The score with its margin of error:** the share of qualified users who would be very disappointed, a 95% interval, and a verdict against the 40% bar (clears, at the bar, below, or too few to read under 40 answers).
2. **The cleaning counts:** duplicates, lapsed users and answers that failed the usage rule.
3. **Every segment scored,** with the core segment (where the fit already is) and the promising ones that need more answers.
4. **What core users value** and **what holds back** the users who are one fix away, with short quotes.
5. **Behaviour checks:** whether retention cohorts flatten, whether earned channels bring a rising share of new users, and whether brand search grows.
6. **One overall read** and a plan of up to five moves that narrows the target before adding features, plus a re-survey date.

## What it can change for you

Nothing. It reads your data and drafts the survey and the plan. It never sends a survey, emails users or edits a sheet or a store.

## Tips

- Keep question 1 worded the same every time, so scores compare.
- Re-run it about 12 weeks after a change to targeting or the product.
- If your GA4 property mixes the marketing site and the app, give it BigQuery or a product export for retention instead.
