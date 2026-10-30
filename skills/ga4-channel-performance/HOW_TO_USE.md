# How to Use This Skill

Hey Claude, I just added the "ga4-channel-performance" skill. Show me how each GA4 channel performed last month, what my paid sources cost, and whether my referral and Direct traffic is real.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the reports itself; you don't need to export anything.
- **Your ad accounts, if you want cost and ROI.** Google Ads, Meta, LinkedIn, Microsoft Ads and TikTok each add their spend when connected. Without them you still get the channel, referral and Direct reviews.
- **Your date range,** if it isn't the last 30 days.

## Example requests

**Channel report**
Hey Claude, I just added the "ga4-channel-performance" skill. Give me a channel grouping report for the last 30 days compared with the 30 days before.

**ROI by source/medium**
Hey Claude, I just added the "ga4-channel-performance" skill. Build a source/medium table with ad spend from Google Ads, Meta and LinkedIn, and tell me which source costs the most per engaged visit.

**Referral review**
Hey Claude, I just added the "ga4-channel-performance" skill. Review my referral traffic for last quarter. Which referrers are real, and which are bots or my own tools?

**Direct spike**
Hey Claude, I just added the "ga4-channel-performance" skill. Direct traffic jumped last week. Find the day and tell me what caused it.

## What you get

1. **A grade out of 100** for how far your channel numbers can be trusted, with the math shown.
2. **A scorecard for four areas:** channel mix, source/medium ROI, referral quality and Direct spikes.
3. **A channel table** with sessions, engagement, key events and revenue, against the previous period.
4. **An ROI table** with spend, platform clicks, the GA4 sessions they turned into, and cost per engaged session, per key event and ROAS when those exist.
5. **A referral review** that labels each referrer: strong, normal, weak, one-day burst, suspected bot, internal or tool, ad network or AI assistant.
6. **A Direct spike diagnosis** comparing the spike day's pages, countries, browsers and hours with the four weeks before.
7. **The top 5 actions,** ranked by the sessions at stake.

## What it can change for you

With your yes on the exact change, it can create a custom channel group that gives AI assistant referrers (ChatGPT, Perplexity, Claude, Gemini, Copilot) their own channel, while all other traffic keeps its usual channel.

It never changes your tags, ad accounts or referral exclusions. It tells you what to change and where.

## Tips

- If GA4 shows no key events firing, the skill compares channels on engaged sessions and marks ROI as not graded. Fix the key events first for a full ROI table.
- Key events named with test, QA or debug are treated as setup checks, not conversions. The skill lists them apart and suggests removing them as key events.
- Connect every ad account that sends traffic to the site. Paid traffic from a platform that isn't connected shows up with an unknown cost.
- Run it monthly, and right after a launch or a mention that sends a burst of traffic.
