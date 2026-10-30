# How to Use This Skill

Hey Claude, I just added the "north-star-metric-builder" skill. Help me choose a North Star metric for my product and break it into input metrics my teams can own.

## What you need

- **A short description of your product** and what customers get from it. That's enough for a pre-launch product.
- **Your monthly history, if you have it:** customers kept and revenue per month, and any product counts you already track. Paste a table or upload a CSV.
- **Optional: the InsightfulPipe MCP connected to Claude,** with GA4 or a BigQuery export of GA4 (or of your product data). The skill then pulls the monthly and weekly numbers itself.
- **Optional: a 90-day goal** for the North Star, and the teams that will own each input.

## Example requests

**Choose the metric**
Hey Claude, I just added the "north-star-metric-builder" skill. We run booking software for salons and clinics. Here are 12 months of paying customers, customers kept and revenue. Which metric should be our North Star?

**Test what we already report**
Hey Claude, I just added the "north-star-metric-builder" skill. Our dashboard leads with monthly active users. Check it against our retention and revenue history and tell me if it's the right North Star.

**Build the tree from BigQuery**
Hey Claude, I just added the "north-star-metric-builder" skill. Our GA4 export is in BigQuery. Use it to test our candidates, then give me the input metrics with baselines and 13-week targets.

**Pre-launch**
Hey Claude, I just added the "north-star-metric-builder" skill. We launch a home-cleaning marketplace in January. Pick a North Star and tell me which events to track from day one.

**Into a sheet**
Hey Claude, I just added the "north-star-metric-builder" skill. Build the metric tree, then put the weekly check in a new tab of my planning spreadsheet. Show me the layout first.

## What you get

1. **The North Star,** in one sentence, with the evidence: how strongly it moved ahead of your retention and revenue, month by month.
2. **Every candidate you considered,** with the rule it broke or its test result, so you can explain the choice to your team.
3. **The input tree:** 3 to 5 inputs with formulas that multiply back to the North Star, and a check that they add up.
4. **Owners, baselines and 13-week targets,** each with the formula behind it.
5. **How each weekly number gets computed:** the calculation, where it runs (GA4, BigQuery or your product database), and whether the events behind it are recorded today.
6. **A weekly check layout** with the target path at weeks 4, 8 and 13.

## What it can change for you

With your yes on the exact layout, it can add a new tab to a Google Sheet you choose and fill in the weekly check. It never overwrites a tab, and it never changes GA4, BigQuery or your product.

## Tips

- Give it at least 6 complete months of history for the test; 12 to 24 is better.
- Keep the same unit throughout: if the North Star counts accounts, give retention by account too.
- Rerun it each quarter. Targets move, and a pick labeled "unproven" or "early" gets a real test once more months are in.
