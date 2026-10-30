# How to Use This Skill

Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Which of my marketing channels actually brings people in, and which only gets the credit at the end?

## What you need

- **The InsightfulPipe MCP connected to Claude, with GA4 added.** The skill pulls the data itself; you don't export anything.
- **Your ad accounts, if you run ads:** Google Ads, Meta, LinkedIn Ads, Microsoft Ads or TikTok Ads. They add spend and each platform's own conversion claims.
- **The outcome that matters** (a purchase, a lead, a sign-up) and its GA4 event name, if you know it. If the event sends a value (order value, lead value), the skill credits value as well as counts.
- **Spend on anything that isn't connected** (affiliates, sponsorships, other ad networks), if you want it in the cost side.

No GA4? Paste a channel table or a GA4 Conversion paths export instead, and the skill works from that.

## Example requests

**Which channel is really working**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Show me which channels start our customers' journeys and which ones close them, for the last 90 days.

**Is last-click misleading us**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Our Meta ads look expensive in last-click reports. Check whether they're starting journeys that other channels finish.

**Brand search taking the credit**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Brand search gets most of our conversions. Find out which channels are feeding it.

**Highest-value journeys**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Which channels and hand-offs bring our highest-value orders, not just the most orders? Show revenue per channel and the average order value for each.

**Platforms don't agree**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Google Ads and Meta together claim more purchases than GA4 records. Compare what each claims with what GA4 credits them.

**Where to move budget**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. We spend across Google, Meta and LinkedIn. Using multi-touch credit, which channel should get more money, and how should we test it?

**Working from an export**
Hey Claude, I just added the "cross-channel-attribution-analyst" skill. Here's our conversion paths export. Compare first touch, last touch, linear and position-based credit for each channel, for conversions and value, and show which channels mostly sit in the middle of paths.

## What you get

1. **A health rating** (GOOD, NEEDS WORK or NOT READY) with the checks behind it, so you know whether the credit numbers can be trusted.
2. **Three views of the same outcome from GA4:** first touch, last non-direct session and the property's own model, side by side per channel. When the outcome carries value: the value each channel brings and its average value per outcome.
3. **Channel roles:** openers, closers and balanced channels, plus a hand-off table of "found via X, came back via Y", with an assist ratio band for each channel and the hand-offs that bring the highest-value outcomes.
4. **Journeys:** how many outcomes come from returning visitors, and how many days after the first visit they happen.
5. **Paid platforms:** spend, the conversions and value each platform claims, CPA under each view and a blended CPA range, and ROAS under each view when there is value.
6. **Undervalued and over-credited channels,** each with its numbers, and platforms that may be claiming the same customers.
7. **A budget test,** capped at 20% of a channel's spend for four weeks, with a projection labelled as an upper bound.
8. **Tests to run** and the blind spots no attribution can see.

From a Conversion paths export you also get each channel's initiator, influencer (middle touch), closer and solo share, path length, and the most common and highest-value paths.

## What it can change for you

With your yes on the exact change, it can mark the event you choose as a GA4 key event, so future outcomes are credited. It never moves budgets or edits campaigns; those stay recommendations.

## Tips

- Use at least 90 days. Short windows cut off longer journeys and leave too few outcomes to compare.
- If GA4 has no key events firing, the skill says so first. You can run it on engaged sessions as a stand-in, but fix tracking before you move money.
- Keep brand and non-brand search apart: brand mostly closes what other channels started.
- A big gap between views is a reason to run a test, not to cut a channel overnight.
