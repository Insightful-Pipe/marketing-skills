# How to Use This Skill

Hey Claude, I just added the "marketing-forecast" skill. Forecast next month's leads and revenue from my ad accounts, and explain how you got the number.

## What you need

- **Your monthly history, one of two ways.** Connect the InsightfulPipe MCP with at least one source that records leads or sales (Google Ads, Meta Ads, LinkedIn Ads, Microsoft Ads or GA4; Shopify or WooCommerce for a shop's orders in the annual forecast), and the skill pulls the history itself. Or paste or upload a monthly table: month, spend and leads per channel, plus value if you have it.
- **About a year of history or more.** It works with less, but the seasonal model needs at least 15 months, and the annual forecast is best with two or three years.
- **For an annual forecast,** your plan year, your targets if you have them, and any known events: a past one-off month (a heat wave, a viral post) or a change ahead (a launch, a price change) with your own estimate of its effect.
- **Your planned budget for the months ahead,** if you have one. It's the input that improves accuracy the most.
- **What a lead is worth,** if your ad accounts don't track real conversion value. A value per lead, or a close rate and an average deal size.

## Example requests

**Next month's leads**
Hey Claude, I just added the "marketing-forecast" skill. How many leads will Google Ads bring in next month?

**Forecast with a budget**
Hey Claude, I just added the "marketing-forecast" skill. We plan to spend $8,000 across Google and Meta in November. Forecast leads and revenue; each lead is worth about $150 to us.

**What-if on budget**
Hey Claude, I just added the "marketing-forecast" skill. If I raise next month's budget by 20%, how many more leads should I expect, and how sure are you?

**Annual forecast for budget season**
Hey Claude, I just added the "marketing-forecast" skill. It's budget season. Forecast 2027 by month and by channel: leads, spend and revenue, with low and high cases, and show the gap to our targets.

**From a pasted export, no connection**
Hey Claude, I just added the "marketing-forecast" skill. Here are 30 months of spend and leads by channel from our spreadsheet. Build a 12-month lead and revenue forecast; each lead is worth about $400.

**Explain the model**
Hey Claude, I just added the "marketing-forecast" skill. Explain in plain words how this forecast works, which model you chose and why the others lost.

## What you get

1. **The forecast for this month and next month:** leads with a range, expected spend, cost per lead, and revenue when a value is known.
2. **The real hit rate of that range,** for example "10 of 12 past months landed inside it".
3. **A check of the history:** the last 12 months, plus any tracking or cost-per-lead break that makes older months unreliable.
4. **A plain-words explainer:** what each model assumes, its arithmetic with your numbers, its average miss on your own past months, and why it was or wasn't chosen.
5. **What would make the forecast wrong,** tied to numbers from your account.
6. **In the annual forecast:** every month of the plan year by channel, with low, expected and high cases that widen the further out they go, totals by quarter and year, the gap to your targets with the spend that gap would need, and the effect of your known events shown separately.

## What it can change for you

Nothing in your ad accounts. It only reads them. If you ask, it saves the annual forecast to a new tab in your Google Sheets spreadsheet, only after you confirm. That needs a Read & Write connection.

## Tips

- Run it at the start of each month, after the last month's conversions have come in.
- Give it your budget. With a budget, the forecast follows the money instead of last month's pace.
- For next year's plan, run the annual forecast first without a budget. The gap to target tells you what the budget has to buy.
- If it reports a tracking break, check your conversion actions first. A forecast can't be better than the lead count behind it.
