# How to Use This Skill

Hey Claude, I just added the "facebook-ads-budget-allocator" skill. Look at my Meta ad account and tell me where to move budget, and how fast.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta ad account added.** The skill reads campaigns, ad sets, budgets, results and recent edits itself; you don't need to export anything.
- **Your target cost per result or ROAS** for each objective, if you have one. Without it, the skill uses your own 30-day average.
- **Your budget plan:** keep the total, raise it, or cut it. Without it, the total stays the same.
- **Any campaigns that must keep running,** and which custom audiences are your existing customers.

No Meta connection? Paste an ad set level export for the last 60 days and the skill runs the same checks, without recent edits, the budget floor or changes.

## Example requests

**Rebalance at the same total**
Hey Claude, I just added the "facebook-ads-budget-allocator" skill. Keep my Meta budget where it is, but move money from the ad sets that waste it to the ones that work. My target cost per purchase is $35.

**Scale the winners**
Hey Claude, I just added the "facebook-ads-budget-allocator" skill. Which of my ad sets can take more budget without the cost per lead blowing up? Draft the increases and show me before you change anything.

**Cut without losing the best results**
Hey Claude, I just added the "facebook-ads-budget-allocator" skill. I have to cut Meta spend by 30% next month. Tell me where to cut and what it will cost me in results.

**CBO or ad set budgets**
Hey Claude, I just added the "facebook-ads-budget-allocator" skill. Compare my campaign budget campaigns with my ad set budget campaigns and tell me which setup is working better.

**Where the money goes**
Hey Claude, I just added the "facebook-ads-budget-allocator" skill. Show me how my spend splits across objectives and funnel stages, and whether that split makes sense for a lead-gen business.

## What you get

1. **Objective mix:** spend, budget and cost per result by objective, with anything that looks off.
2. **Campaign vs ad set budgets:** which campaigns use which, how Meta splits each campaign budget, and a head-to-head when there's enough data.
3. **A grade for every live budget:** Star, Potential, Declining or Failing, from cost per result against target, the trend from the previous 30 days, frequency and CPM, marginal cost and the learning budget.
4. **The plan:** each move in dollars per day, from where to where and why, with the results it should gain or lose.
5. **A week-by-week rollout,** the risks, and what couldn't be graded.

## What it can change for you

With your yes on the exact change, it can:
- raise or lower an ad set budget
- raise or lower a campaign budget
- pause a failing ad set or campaign (switching it back on happens in Ads Manager)

It never raises a budget by more than 20% in one step. A cut is capped at 20% too, except for a failing budget, which can be cut by up to half or paused. It never goes below Meta's minimum budget, and it leaves anything edited in the last 7 days alone.

## Tips

- Run it every two weeks. A budget change needs about a week to show its effect.
- Give it a target per objective. A cost per click and a cost per purchase can't be compared, so the skill only moves money between budgets that optimise for the same event, and leaves moves across events to you.
- If your account has little spend, it will tell you so and show the setup rather than invent a plan.
