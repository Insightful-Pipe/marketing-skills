# How to Use This Skill

Hey Claude, I just added the "facebook-ads-creative-tester" skill. Plan a proper creative test for my Meta ads, sized on my own account's numbers.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta ad account added.** The skill reads your baseline, formats, budgets and limits itself; you don't need to export anything.
- **What you want to test,** if you know. If not, the skill picks the weakest step in your numbers (hook, hold, click or conversion).
- **A daily budget per variant,** if you have one. Without it, the plan tells you the budget the test needs.
- **A Read & Write connection,** only if you want it to set the test up for you.

## Example requests

**Plan a hook test**
Hey Claude, I just added the "facebook-ads-creative-tester" skill. I want to test a question hook against a bold-claim hook on my video ads. Tell me how many impressions, days and dollars that takes on my account.

**Which format works for us?**
Hey Claude, I just added the "facebook-ads-creative-tester" skill. Compare video, single image, carousel and collection ads on my account for the last 90 days, and tell me which differences are real.

**Did my test win?**
Hey Claude, I just added the "facebook-ads-creative-tester" skill. My image vs UGC test has run for 9 days. Read both ads and tell me if there's a winner or if I need to wait.

**Set the test up**
Hey Claude, I just added the "facebook-ads-creative-tester" skill. Take the two videos in my media library, upload them to my ad account and build the test campaign. Show me every payload before you create anything.

**See dynamic creative results by asset**
Hey Claude, I just added the "facebook-ads-creative-tester" skill. My flexible ad mixes 3 headlines, 3 texts and 4 images. Tell me which ones Meta is really using, which are winning, and which never got a fair run.

## What you get

1. **Your baseline:** hook rate, hold rate, link CTR, click-to-result rate and CPM from your own ads, or "unknown" when there's too little data.
2. **A format comparison,** with flexible ads split by their video and image assets, and a significance check between the top two formats.
3. **A one-variable test plan:** hypothesis, variants, an isolation check, primary metric, sample size per variant, length, budget, structure and winner rules, all agreed before launch.
4. **A test read:** lift, p-value, progress against the planned sample, and a verdict (or "too early").
5. **An asset report** for flexible and dynamic creative ads: every headline, text, image and video ranked by spend and cost per result, with "barely delivered" kept apart from "lost", and what to keep, replace or move into an ad of its own.
6. **The launch payloads:** upload, campaign, ad sets, creatives and ads, ready to run once you say yes.
7. **A test log row** to record what you learned.

## What it can change for you

With your yes on the exact payloads, it can:
- store creatives from URLs in your InsightfulPipe Media Library
- upload images and videos to your ad account
- create the test campaign, one ad set per variant, the creatives and the ads

Everything is created paused. You switch the test on in Ads Manager. It never switches ads on, changes a running test or touches ads outside the test.

## Tips

- New account with little delivery? The skill won't guess a baseline. It runs a 7-day calibration week and then sizes the rest of the test from what that week shows.
- Test one thing at a time. If two things change, you'll know which ad won but not why.
- Keep both variants in the same shape (for example both 1:1), or the test measures placement as well as creative.
- Don't call a winner before day 7, even when one ad looks far ahead.
