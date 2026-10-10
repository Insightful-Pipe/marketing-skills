# How to Use This Skill

Hey Claude, I just added the "spend-pacing-monitor" skill. Am I on track to spend my Google Ads budget this month, and how should I set daily budgets for the rest of it?

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls spend, budgets, budget edits and impression share itself. You don't need to export anything.
- **Your monthly target,** for the account or per campaign, if you have one. Without one, it paces you against what your current daily budgets allow (30.4 × their sum, the most Google bills in a month).
- **Known events,** if any: a promotion, a planned pause, a launch.

No Google Ads connection? Give it your target, the day of the month and your month-to-date spend (plus daily and per-campaign spend if you have them), and it does the math. It can't see why a campaign is behind, though.

## Example requests

**Quick check**
Hey Claude, I just added the "spend-pacing-monitor" skill. Our Google Ads budget is $25,000 for this month. Will we land on it?

**Which campaign stopped?**
Hey Claude, I just added the "spend-pacing-monitor" skill. Spend looks low this week. Is any campaign not spending, and why?

**Cost per conversion trend**
Hey Claude, I just added the "spend-pacing-monitor" skill. Show me cost per conversion by campaign, week by week, for the last 12 weeks, and tell me which campaigns are getting more expensive.

**Rest-of-month budgets**
Hey Claude, I just added the "spend-pacing-monitor" skill. We're overpacing. Tell me which daily budgets to cut so we land on $40,000, then make the changes once I say yes.

## What you get

1. **A status line:** on pace, underpacing or overpacing, judged against a tolerance that tightens as the month goes on.
2. **Budget edits this month,** and what they do to the pace.
3. **Three projections and a best estimate,** with the method shown and a confidence level.
4. **Every campaign classified:** stopped, capped by budget, can't spend its budget, or on budget. Each comes with its impression share lost to budget and to rank, so you know whether budget is the lever at all.
5. **Cost per conversion by campaign,** week by week for 12 weeks, marked rising, falling or flat, or "too few conversions to call" when either window has under 5.
6. **A daily table** against each weekday's normal spend, with unusual days flagged.
7. **A budget plan:** which daily budgets to change, by how much and why, the most each change could add, and three scenarios.

## What it can change for you

With your yes on the exact amounts, it can set campaign daily budgets with `update_campaign`. It warns you first when a budget is shared by several campaigns. It never pauses campaigns or changes bidding.

## Tips

- In the first week, pacing is rough. Read the best estimate and last month's landing, not the run rate.
- Run it weekly, or daily on big budgets. Problems are cheapest to fix before mid-month.
- If most of the gap sits in campaigns that can't spend, more budget won't help. Look at rank-lost impression share, bids and targeting instead.
- After changing budgets, run it again in about 7 days, and raise in steps of up to 30% at a time.
