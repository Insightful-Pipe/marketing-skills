# How to Use This Skill

Hey Claude, I just added the "cross-platform-budget-allocator" skill. Look at all my ad accounts and tell me how to split my budget across platforms.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your ad accounts added:** any of Google Ads, Meta, Microsoft Ads, LinkedIn, TikTok, Pinterest, Snapchat, X and OpenAI Ads. The skill pulls spend, results, budgets and saturation signals itself; you don't need to export anything.
- **GA4, if you have it.** The skill uses it to check whether a platform claims more results than your site recorded.
- **Your goal,** if you have one: a target CPA or ROAS, or "most results for the same money". Without it, the skill uses your own blended cost per result.
- **Your limits,** if any: a minimum or maximum per platform, a brand budget to leave alone, how much to keep for tests.

## Example requests

**Rebalance the current budget**
Hey Claude, I just added the "cross-platform-budget-allocator" skill. Meta's cost per lead went up this month while Google stayed flat. Should I move money between them, and how much?

**Next quarter's budget**
Hey Claude, I just added the "cross-platform-budget-allocator" skill. Build next quarter's ad budget by platform and month from the last 90 days of performance.

**Which channels to add**
Hey Claude, I just added the "cross-platform-budget-allocator" skill. We only run Google Ads. Build next quarter's budget by month, tell me where more money would work if we raised it, and which channel we should test next.

**A budget change**
Hey Claude, I just added the "cross-platform-budget-allocator" skill. Our ad budget goes from $30,000 to $45,000 a month. Where should the extra $15,000 go?

**The whole marketing budget**
Hey Claude, I just added the "cross-platform-budget-allocator" skill. We have $200,000 for marketing next year, $60,000 of it already committed to content and events. Plan the paid media part.

## What you get

1. **Current state:** every platform and campaign role (brand search, non-brand search, prospecting, retargeting, lead forms), or every campaign when you run one platform, with spend, results, cost per result, efficiency tier, trend, headroom, recent budget edits and the cost of the next result.
2. **A recommended split** with the reason for every change, plus conservative and aggressive alternatives and a naive reference.
3. **Projected results** and blended cost per result, with assumptions and a confidence level.
4. **A rollout in weekly steps** of at most 25% per budget, with the check before each step. Campaigns whose budget moved more than 20% net in the last two weeks, or whose bid strategy or target changed, wait until they settle; a smaller budget edit doesn't hold them back.
5. **Rebalancing triggers and risks,** and what couldn't be read.
6. For next quarter: **a monthly budget** adjusted for last year's seasonality, with a gate before each month and a list of where extra money would work. For a new channel: **a test budget** with continue and kill rules.

## What it can change for you

With your yes on the exact change, one step at a time, it can set:
- a Google Ads campaign's daily budget
- a Meta campaign's or ad set's daily budget

It never pauses, creates or removes campaigns, and never changes bid strategies. Budgets on other platforms are given as numbers for you to set.

## Tips

- Give the value of a result when channels or campaigns bring different kinds of results (a demo request against a newsletter sign-up, a large case against a small one). Without it, every result counts the same and cuts wait for you to confirm.
- Tag your ad links with UTM parameters so GA4 can check each platform's numbers.
- Rerun it after each rollout step, and whenever a rebalancing trigger fires.
