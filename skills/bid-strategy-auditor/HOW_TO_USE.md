# How to Use This Skill

Hey Claude, I just added the "bid-strategy-auditor" skill. Check whether my Google Ads bid strategies are working, and tell me which targets to change.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls bidding settings, targets, conversion volume, change history and Google's bid simulations itself. You don't need to export anything.
- **Your target CPA or ROAS,** if it differs from what's set on the campaigns.
- **Whether your conversions are worth different amounts** (a call vs a form vs a sale). This shapes the value-based bidding advice.

No Google Ads connection? Paste a campaign report (strategy, target, status, cost, conversions, value, impression share lost to budget and rank) for the last 30 and prior 30 days, plus weekly conversions and your change history. The skill runs the same rules and marks what it couldn't check.

## Example requests

**Full audit**
Hey Claude, I just added the "bid-strategy-auditor" skill. I've had a $50 target CPA for six weeks, but my CPA is $68. Is Smart Bidding the problem?

**Choosing a strategy**
Hey Claude, I just added the "bid-strategy-auditor" skill. My campaigns get about 25 conversions a month. Should I use Target CPA, Maximize conversions or manual bidding?

**CPA creep**
Hey Claude, I just added the "bid-strategy-auditor" skill. My Maximize conversions campaign's CPA keeps rising month over month. What's going wrong?

**Google's recommendation**
Hey Claude, I just added the "bid-strategy-auditor" skill. Google keeps recommending Target ROAS. Am I ready for value-based bidding?

**Stuck in learning**
Hey Claude, I just added the "bid-strategy-auditor" skill. My campaign has shown "Learning" for three weeks. Is that normal, and what should I change?

**Portfolios**
Hey Claude, I just added the "bid-strategy-auditor" skill. Should my small campaigns share a portfolio bid strategy?

## What you'll get

1. **A scorecard** for six areas: conversion signal, data fit, target calibration, learning and stability, portfolios, and value-based readiness.
2. **A verdict for every campaign:** working, too early (with a re-check date), adjust target, change strategy, or budget is the limit.
3. **Target advice backed by Google's own bid simulations** where Google provides them, plus **red flags** the target ratio misses: CPA rising while impression share falls, weekly CPA swings on a target, value per conversion falling, and a target missed while budget-limited.
4. **Ranked recommendations,** each with a success check and a rollback rule.
5. **The exact changes as payloads.** It runs target edits, strategy switches, portfolio changes and conversion values only after you say yes.

## Tips

- Run it again on the re-check date it gives you. Changes made inside a settling window are judged too early.
- Make bid changes in one batch, not one a day. Every edit can restart learning.
- Writes need a Read & Write connection, and an owner, admin or operator can switch them off.
