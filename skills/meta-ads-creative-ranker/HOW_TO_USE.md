# How to Use This Skill

Hey Claude, I just added the "meta-ads-creative-ranker" skill. Rank my Meta ads from the last 30 days and tell me which ones to keep, scale and switch off.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta ad account added.** The skill pulls ad results, creatives and engagement itself; you don't need to export anything.
- **Your target cost per result or ROAS,** if you have one. Without it, the skill uses your account's own average for the window.
- **The result that counts,** if it isn't the one your ad sets optimise for (for example purchases when the ad sets optimise for landing page views).
- **For partnership ads:** the creators' Instagram handles, if your ad names don't carry them. Meta returns the creator's account id, not the handle. With the Instagram MCP server connected too, the skill also reads each creator's recent public posts.

No connection yet? Paste an ad-level export from Ads Manager and the skill runs the same steps on it. For the variety check, add thumbnails or screenshots of your live ads if you want them grouped by look as well.

## Example requests

**Weekly creative review**
Hey Claude, I just added the "meta-ads-creative-ranker" skill. Rank last week's Meta ads by cost per lead. Our target is $40 a lead.

**Kill list**
Hey Claude, I just added the "meta-ads-creative-ranker" skill. Which of my running Meta ads are losing money? Give me a kill list and pause them once I've checked it.

**Copy angles**
Hey Claude, I just added the "meta-ads-creative-ranker" skill. Compare the copy angles in my Meta ads over the last 90 days. Do problem-led ads beat benefit-led ones on cost per purchase?

**Engagement and social proof**
Hey Claude, I just added the "meta-ads-creative-ranker" skill. Show me which ads get the most reactions, comments and shares, and whether that engagement turns into sales.

**Creative variety after the Andromeda update**
Hey Claude, I just added the "meta-ads-creative-ranker" skill. Is my Meta creative varied enough for Andromeda? Find ads that reuse the same image or video or are near-copies, show how much of each ad set's spend sits on one concept, and tell me which concepts to make next.

**Partnership ads review**
Hey Claude, I just added the "meta-ads-creative-ranker" skill. Compare my Instagram partnership ads with the ads from our own handle, rank the creators by cost per purchase and show each one's hook rate, and tell me which creator posts to put more money behind and how much.

## What you get

1. **Six tiers,** from stars to bleeders, measured against your target, with ads that haven't had a fair chance marked "too early".
2. **A leaderboard** of your best ads with the reason each one works.
3. **A kill list** of running ads to pause, with the money they cost and how much of your spend went to losers.
4. **Patterns** by copy angle, format, video length and call to action, each marked firm, directional or too few to call.
5. **Engagement and social proof** per ad and per post, the engagement-vs-results matrix, and Meta's relevance labels.
6. **The video funnel:** hook rate, hold rate, click-through and click-to-result for each video ad.
7. **Red flags and up to three tests to run next,** each tied to something the ranking found.
8. **Creative variety (the Andromeda check):** how many distinct concepts you really run, exact copies (the same image or video under different ad names) and near-copies, each ad set's spend share on its top one and two concepts with a verdict, and the angle and format pairs to make next.
9. **Partnership ads:** partnership ads against your own handle on cost per result, CTR, CPM and hook rate, a creator ranking, a 20% daily-spend step for each in-target creator's best post, and, with Instagram connected or their post links pasted, up to two of their recent posts to run next. If you run none, it says so in one line.

## What it can change for you

With your yes on the exact list, it can pause the ads on the kill list. It tells you first when an ad is the last one running in its ad set. Pausing can't be undone through the connection: you switch an ad back on in Ads Manager. It never changes budgets, creates ads or edits creative: the variety check and the partnership review only read.

## Tips

- Run it weekly with a 30-day window, or with 7 days on a big account.
- Ask for one mode only ("just the variety check", "just my partnership ads") and the skill still sets your target and tiers first, then reports only that section.
- A target from your margins beats the account average: with the average, half your ads look bad by definition.
- If few ads have enough data, ask for the 90-day window. If nothing spent in 90 days, the skill shows each ad's lifetime numbers, creative and engagement once and stops there.
