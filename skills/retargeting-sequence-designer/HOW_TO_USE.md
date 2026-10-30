# How to Use This Skill

Hey Claude, I just added the "retargeting-sequence-designer" skill. Can you design a retargeting sequence that brings back visitors who didn't convert?

## What you need

- **The InsightfulPipe MCP connected to Claude.** The skill reads GA4 for behaviour and pool sizes, Meta for the pixel, audiences and the funnel that's running, Google Ads for remarketing lists, and Klaviyo for email flows. Any one of them is enough to start; without GA4, you give page and event counts yourself. Parts without a source are marked unknown or not graded. For the other platforms it reads less, and what it reads differs: audience sizes come only from Pinterest and Snapchat; the pixel or tag is checked on Pinterest, TikTok, Snapchat and X; existing exclusions are read on LinkedIn, TikTok, Pinterest and Snapchat; and the LinkedIn Insight Tag is something you confirm yourself, because no call returns it. For pools without a platform size, it estimates from GA4 visitors and, on LinkedIn and TikTok, from video view and lead form counts, or uses the size you read off that platform's Ads Manager. Reddit, and any platform that isn't connected, works from those Ads Manager sizes.
- **Your conversion,** if it isn't obvious from your GA4 key events.
- **Your buying cycle,** roughly how long people take to buy. Without it, the skill uses 14 days for ecommerce, 30 for SaaS and lead generation, and 90 for high-value B2B.
- **Any offer you're willing to use.** Without one, the sequence answers objections instead of inventing a discount or a deadline.

## Example requests

**Full sequence**
Hey Claude, I just added the "retargeting-sequence-designer" skill. Size my retargeting pools from GA4 and design a full sequence for Meta and Google, from cart abandoners to blog readers.

**Cart abandonment**
Hey Claude, I just added the "retargeting-sequence-designer" skill. Most of my carts are abandoned. Design a cart retargeting sequence that pushes without annoying people, and tell me how often each person should see an ad.

**SaaS pricing and trial**
Hey Claude, I just added the "retargeting-sequence-designer" skill. Design sequences for people who saw our pricing page but didn't sign up, and for people who signed up but never set up the product.

**Lead generation**
Hey Claude, I just added the "retargeting-sequence-designer" skill. We run lead gen. Retarget people who started the form and didn't send it, and people who read our guides but never got in touch.

**Funnel check (TOF, MOF, BOF)**
Hey Claude, I just added the "retargeting-sequence-designer" skill. How is my Meta retargeting funnel doing? Show spend, frequency and cost per result for each stage, and what's missing.

**Email and paid overlap**
Hey Claude, I just added the "retargeting-sequence-designer" skill. Check whether my Klaviyo flows and my paid retargeting are hitting the same people at the same time, and fix the order.

**LinkedIn, TikTok, Pinterest, Snapchat and X**
Hey Claude, I just added the "retargeting-sequence-designer" skill. Plan LinkedIn retargeting for our pricing page visitors and lead form openers, and tell me whether our TikTok and Pinterest retargeting pools are big enough to run yet.

**Customers**
Hey Claude, I just added the "retargeting-sequence-designer" skill. Design upsell, cross-sell and win-back sequences for existing customers.

## What you get

1. **Readiness:** pixel, GA4 to Google Ads link, remarketing lists, email triggers, a converter event that fires and steady tracking, each checked and graded, with blocking problems first.
2. **The funnel now:** your Meta ad sets sorted into TOF, MOF and BOF, with spend, reach, frequency and cost per result for each stage, and checks for missing stages and exclusions.
3. **Email and paid overlap:** the flows and ad tiers that start on the same action, and the order to run them in.
4. **Pools:** each tier's real size over 7, 30 and 90 days, and whether Google Ads and Meta can serve it. Tiers too small to serve are merged.
5. **Sequence maps:** for each tier, the window, frequency, exclusions, and five message stages from reminder to last call.
6. **Creative briefs** for the hottest tier, plus setup notes for Meta and Google.
7. **Budget:** the split by tier and by phase, with a spend ceiling per tier when your CPM is known.
8. **KPIs and a launch checklist.**
9. **Other platforms, when you run ads there:** the site visitor, video viewer, engager, lead form and customer list pools on LinkedIn, TikTok, Pinterest, Snapchat, X and Reddit, each sized (a platform count, or a GA4 estimate with its match-rate range), checked against that platform's minimum, and given a window, formats, exclusions and a share of one frequency cap shared across platforms.

## What it can change for you

With your yes on the exact change, it can:
- create a GA4 audience for each tier
- add exclusions to an existing Meta ad set
- attach a Google Ads remarketing list to an ad group

It can't create Meta custom audiences, Klaviyo flows or Meta frequency caps. For those, it gives you the exact settings to use. On LinkedIn, TikTok, Pinterest, Snapchat, X and Reddit it changes nothing, and gives you the audience settings and exclusions to build in each Ads Manager.

## Tips

- Run it again 30 days after a tracking change. Pools sized on a few days of data are a projection, not a count.
- If a key conversion never fires in GA4, upload a customer list so converters can still be excluded.
- Launch the hottest tier first, then add warm tiers after a few days.
- No connection yet? Paste your page counts, audience sizes and ad set stats, and the skill designs the same way, marking those numbers as yours.
