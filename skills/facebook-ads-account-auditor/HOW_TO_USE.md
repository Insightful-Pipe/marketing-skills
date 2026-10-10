# How to Use This Skill

Hey Claude, I just added the "facebook-ads-account-auditor" skill. Audit my Meta Ads account and tell me what's broken and what it's costing me.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta Ads account added.** The skill pulls the data itself; you don't need to export anything.
- **The result you care about and its target cost,** if you have one (for example "leads at $40"). Without it, the skill uses your own 30-day cost per result.
- **Your naming convention,** if you have one. Without it, the skill works out the one your account already uses, or proposes one for you to approve.
- **Optional, from Meta's own screens:** Conversions API and deduplication status and Event Match Quality (Events Manager), and rejection reasons (Account Quality). The API doesn't expose these, so the skill asks or marks them unknown.

## Example requests

**Full audit**
Hey Claude, I just added the "facebook-ads-account-auditor" skill. Run a full audit on my Meta Ads account for the last 30 days. Our target is $40 per lead.

**CPA keeps rising**
Hey Claude, I just added the "facebook-ads-account-auditor" skill. My cost per purchase went up 40% this month and nothing obvious changed. Audit the account and show me where it's coming from.

**Billing and rejected ads**
Hey Claude, I just added the "facebook-ads-account-auditor" skill. Check whether a spend limit or billing problem is about to stop my ads, and list every rejected ad and policy issue.

**Before scaling**
Hey Claude, I just added the "facebook-ads-account-auditor" skill. I want to take this account from $5k to $20k a month. Is the structure ready, and what should I consolidate first?

**Naming clean-up**
Hey Claude, I just added the "facebook-ads-account-auditor" skill. Audit my campaign names against our convention "Funnel | Objective | Offer | Country | Month" and rename the ones that don't fit. Show me the list first.

## What you get

1. **A grade out of 100,** with the deductions shown (withheld when too little could be checked).
2. **A scorecard for eight areas:** account status and billing, ad review and policy, tracking, structure, audiences, budget efficiency, creative health and naming.
3. **Up to 5 top fixes,** ranked by the money at stake in the last 30 days, each with the numbers behind it.
4. **A consolidation plan:** which ad sets to merge, which to keep, and what the merged ad set would have delivered.
5. **A naming table:** each campaign name that breaks the convention, why, and a proposed new name.
6. **A policy list** of rejected, flagged or stuck ads, plus what couldn't be checked and why.

## What it can change for you

With your yes on the exact change, it can:
- rename campaigns, ad sets and ads to your convention
- pause ad sets emptied by a merge, and pause worn-out ads that have a backup in the same ad set

It never changes budgets, spend limits, bids or targeting, never deletes anything, and can't switch paused items back on (you do that in Ads Manager).

## Tips

- Run it monthly, before you raise budgets, and when you take over an account.
- If the account spent nothing in the last 30 days, you still get billing, policy, tracking and naming checks plus an inventory of audiences and ads by format; the performance areas are marked not graded.
- Run it again after the fixes to see the grade move.
