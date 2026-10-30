# How to Use This Skill

Hey Claude, I just added the "seo-forecast" skill. Here are the keywords our SEO plan targets and what it costs. Forecast the traffic, leads and revenue, and tell me when it pays for itself.

## What you need

- **Your target keywords,** each with the position you aim for, the page (an existing URL or "new") and the month the work on it ships.
- **What a lead is worth:** how many leads become customers, and what a customer pays (once, or each month with your churn). Add your gross margin if you want the return on profit, not revenue.
- **The cost of the work:** one-off amounts and monthly fees, with the months they run.
- **Best results: the InsightfulPipe MCP connected to Claude, with Google Search Console added.** Then the skill measures your own click-through rate at each position. GA4 adds your own organic conversion rate, and DataForSEO adds keyword volumes and seasonality.
- **No connection?** Paste your Search Console Queries export and keyword volumes from any SEO tool. With only a keyword list, it still runs, on a placeholder click curve it labels as such.

## Example requests

**Price an agency quote**
Hey Claude, I just added the "seo-forecast" skill. An agency quoted $3,000 a month for 12 months to rank these 15 keywords. Will it pay back, and when?

**SEO ROI for a budget request**
Hey Claude, I just added the "seo-forecast" skill. I need an SEO ROI case for our CFO: conservative, base and stretch, with the break-even month.

**Traffic forecast for new content**
Hey Claude, I just added the "seo-forecast" skill. We're publishing 8 new pages next quarter. Forecast the organic traffic they'll bring over the next year, month by month.

**From a pasted list**
Hey Claude, I just added the "seo-forecast" skill. Here's a keyword list with volumes, our current positions and the goals. Nothing is connected. Give me a 12-month SEO traffic forecast.

**Check a forecast someone gave you**
Hey Claude, I just added the "seo-forecast" skill. Our consultant says this plan will triple organic leads in 6 months. Test that against our own Search Console and GA4 numbers.

## What you get

1. **The answer in three lines:** base-case extra clicks, leads and customers over 12 months, the break-even month, and the conservative to stretch range.
2. **Every assumption in one table,** each tagged measured, from you, or assumption.
3. **Your own click curve:** the click-through rate your site gets at each position, from Search Console, with brand searches left out.
4. **A backtest:** last year's curve tested against this year's real clicks, and what that does to the conservative case.
5. **One row per keyword:** volume, peak month, where it ranks now, where it lands in each scenario, and the extra clicks it brings.
6. **Three scenarios** with 12-month clicks, leads, customers, revenue, cost and return, plus the 24-month net and the break-even month.
7. **Month by month for the first year,** then by quarter, with the money to date in each scenario.
8. **What has to be true** to pay back sooner, and how much the case rests on its top 3 keywords.
9. **A confidence rating** (high, medium or low) with the checks behind it.

## What it can change for you

Nothing. It only reads Search Console, GA4 and DataForSEO, and writes the forecast in the chat.

## Tips

- Give it the real cost, including your own team's time. A forecast without the cost can show traffic but not a return.
- Run it again each quarter with fresh data, and compare the actual clicks with the base case.
- If your new pages usually take longer (or less time) to rank than the skill assumes, tell it. It uses your experience over its defaults.
- Leave brand keywords out of the target list. SEO work doesn't create searches for your name.
