# How to Use This Skill

Hey Claude, I just added the "incrementality-test-designer" skill. Design a test that tells me how many of my Google Ads leads I'd lose if I switched the ads off.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your ad account added.** Google Ads is the main path. The skill pulls 16 weeks of results by metro itself; you don't export anything.
- **Where every lead or sale is counted,** whatever its source: your CRM, intake log, orders, or GA4 key events. The test is read there, because the ad platform can't see leads in places where its ads are off. If your GA4 property is connected, the skill uses it.
- **What a truly new lead or sale is worth to you,** if you know it. Without it, the skill uses standard decision bands.
- **How much you can switch off,** and for how long. The defaults are 30% of the tested spend for up to 8 weeks.

## Example requests

**Is my search spend real?**
Hey Claude, I just added the "incrementality-test-designer" skill. Plan a geo test for my non-brand Google Ads campaigns. A new client is worth about $400 to us.

**Brand search**
Hey Claude, I just added the "incrementality-test-designer" skill. Would we lose leads if we stopped bidding on our own brand name? Tell me if we even have the volume to test it.

**Retargeting on Meta**
Hey Claude, I just added the "incrementality-test-designer" skill. Size a holdout for my Meta retargeting campaigns and tell me how big the control group has to be.

**Plan, then set it up**
Hey Claude, I just added the "incrementality-test-designer" skill. Design the test, then add the location exclusions on the start date. Show me the payloads first.

## What you get

1. **A verdict:** whether a test can work at your volume, which design, how long, and the smallest effect it can see.
2. **The hypothesis** the test checks, and what counts as success.
3. **Your baseline:** weekly spend and conversions in scope, the conversion lag, the weekday pattern and any recent edits that could skew it.
4. **The split:** which metros go dark and which stay on, chosen by scoring every possible split (or 500 random picks when more than 12 metros are usable) and back-tested on weeks where nothing changed.
5. **A dated test plan:** freeze and tracking check, launch, the days to skip, the read date, the cost, and the guardrails.
6. **The decision rule,** agreed before launch, with the formulas for incremental conversions and incremental CPA.
7. **The exact payloads** that start the test, marked "not run".

## What it can change for you

With your yes on the exact change and the start date, it can:
- exclude the holdout metros from the tested campaigns
- trim each tested campaign's daily budget by the holdout's share, so the budget doesn't flow into the control metros, and restore it after

It can't remove the location exclusions for you at the end; you do that in Google Ads. It never touches campaigns outside the test.

## Tips

- Fix conversion tracking first. A test on broken tracking can't be read.
- Don't change bids, budgets or ads in the tested campaigns while the test runs.
- If the skill says your volume is too low, believe it: a test that can't see the effect wastes weeks of leads. Test a bigger slice, or wait.
- Re-run it after the test to plan the next one in different metros.
