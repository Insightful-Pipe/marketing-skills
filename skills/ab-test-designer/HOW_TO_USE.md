# How to Use This Skill

Hey Claude, I just added the "ab-test-designer" skill. Two ads have been running side by side in my top Google Ads ad group. Tell me if one really won, and design the next test.

## What you need

- **The InsightfulPipe MCP connected to Claude,** with Google Ads, GA4 or both added. The skill pulls baselines, daily traffic and test results itself; you don't need to export anything.
- **What you want to test,** or which ad group, campaign or page. If you don't say, it finds the ad groups that already have two ads running.
- **The smallest lift worth acting on,** if you know it. Without it, the skill shows what your traffic can detect in 8 weeks.
- **Not connected, or an email test?** Paste the numbers (visitors and conversions per version, delivered emails and unique clicks per version, or your baseline rate and daily traffic) and it runs the same math. Email results are always pasted; the skill doesn't pull them from your email tool.

## Example requests

**Who won?**
Hey Claude, I just added the "ab-test-designer" skill. Read out the two ads in my Criminal Defense ad group for the last 90 days. Is the gap real?

**Google Ads experiment readout**
Hey Claude, I just added the "ab-test-designer" skill. My Target CPA experiment ended last week. Read the results against the original campaign and tell me whether to apply it.

**Sample size and duration**
Hey Claude, I just added the "ab-test-designer" skill. I want to test a new headline on my pricing page. How much traffic do I need, and how long will it take with my GA4 numbers?

**Website copy variants**
Hey Claude, I just added the "ab-test-designer" skill. Write three headline variants for my top landing page, each changing one thing, and set up the test plan.

**Email subject line test**
Hey Claude, I just added the "ab-test-designer" skill. Subject line A was delivered to 6,000 people and got 240 unique clicks, subject line B to 6,000 and 285. Did B win, and how big a list do I need next time?

**Is this significant?**
Hey Claude, I just added the "ab-test-designer" skill. Version A had 4,210 visitors and 168 sign-ups, version B 4,180 and 201. Did B win?

## What you get

**For a finished test**
1. What actually differs between the versions, from the live ads, settings or pages.
2. Each metric per version with the lift, a 95% confidence interval and a p-value.
3. Checks: whether the split was even, whether both ran on the same days, how conversions are counted.
4. A device breakdown and a week-by-week view.
5. A verdict (winner, leaning winner, loser, inconclusive or invalid), what it is worth per month, and what to do next.

**For a new test**
1. A hypothesis built on your own numbers.
2. The control and the variants, each changing one thing.
3. A sizing table: sample size and days needed for 10%, 20%, 30% and 50% lifts, and whether the test is worth running.
4. The design, where to run it, the success and guardrail rules, the end date and a launch checklist.

## What it can change for you

With your yes on the exact ad, it can create the challenger responsive search ad in your Google Ads ad group. The ad is always created paused, so nothing goes live until you turn it on beside your current ad (a quick, observational test).

For a controlled split, Google Ads' ad variation experiment edits your current ad's text inside the experiment and doesn't use a separate ad. The skill gives you the exact text change to enter there, and you set it up in Google Ads.

It never pauses ads, creates Google Ads experiments or ad variations, sends emails or edits your website.

## Tips

- Ads rotating under Smart Bidding aren't a clean 50/50 test. The skill labels those results "observational"; use an ad variation experiment when the decision matters.
- Decide the end date before you start, and don't stop at the first good-looking day.
- Low traffic? Test bolder changes, or run the same change in several ad groups at once.
