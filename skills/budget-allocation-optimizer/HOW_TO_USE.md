# How to Use This Skill

Hey Claude, I just added the "budget-allocation-optimizer" skill. Can you look at my Google Ads campaigns and tell me where to move budget?

## Example prompts

**Fixed total**
Hey Claude, I just added the "budget-allocation-optimizer" skill. My Google Ads total can't go up. Split it across my campaigns to get the most conversions.

**With a target**
Hey Claude, I just added the "budget-allocation-optimizer" skill. My target CPA is $50. Which campaigns are overfunded and which deserve more?

**Different values per campaign**
Hey Claude, I just added the "budget-allocation-optimizer" skill. A lead from my enterprise campaign is worth three times one from my SMB campaign. Use $150 and $50 as targets and rebalance.

**Capped winner**
Hey Claude, I just added the "budget-allocation-optimizer" skill. My best campaign runs out of budget most days. Where should the extra money come from?

**Room to grow**
Hey Claude, I just added the "budget-allocation-optimizer" skill. I can add $1,000 a month. Which campaigns should get it, and what will it buy?

## What it reads for you

Through the InsightfulPipe MCP it pulls, from the connected Google Ads account:
- each campaign's budget, spend, conversions, and impression share lost to budget and to rank over the last 30 days
- daily spend, and the budget changes of the last 30 days, so each day is measured against the budget that was actually in force
- Google's budget simulations and budget recommendations, which show what more or less budget would have bought
- 12 weeks of weekly results, for the trend

You only need to say your target CPA (or ROAS), whether the total is fixed, any campaign to leave alone, and any minimum or maximum daily budget a campaign must keep. Without a target it uses the CPA of your non-brand campaigns.

## What you get

1. **A campaign table,** ranked by efficiency: CPA against target, tier, how much of the budget was used, days capped, share lost to budget and to rank, the cost of the next conversion and where that figure comes from, trend, and a verdict (fund, cut, trim or hold) with the reason.
2. **Recent budget changes** and how they affect the reading.
3. **The moves:** from which campaign to which, how much a day and a month, and the conversions gained and lost.
4. **Before and after:** budgets, conversions, CPA and spend change, with the confidence and assumptions.
5. **A week-by-week rollout** with the checks to pass before each next step: each recipient spends its new budget at the expected CPA without losing impression share, each donor stays stable, and total conversions hold.
6. **Where extra money would go** if the total can grow.
7. **Risks and limits,** including any campaign that loses more than 30% of its impression share to rank, which more budget won't fix.

## What it can change for you

With your yes on each step, it can set the new daily budgets with `update_campaign`. It never pauses campaigns or changes bid strategies.

## Tips

- If your campaigns sell things of different value, give each its own target. One target treats every conversion as equal.
- Move in steps. The rollout raises a campaign by at most 30% of its budget a week.
- Run it again two weeks after the last step, and after any big change to budgets or bidding.
- Not connected? Paste a 30-day campaign export with budget, cost, conversions and lost impression share. It will work from that, with lower confidence.
