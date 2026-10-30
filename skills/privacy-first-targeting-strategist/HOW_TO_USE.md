# How to Use This Skill

Hey Claude, I just added the "privacy-first-targeting-strategist" skill. Check how exposed my ads are to tracking loss and give me a plan to fix it.

## What you need

- **The InsightfulPipe MCP connected to Claude,** with the ad platforms you use: Google Ads, Meta, LinkedIn Ads or TikTok Ads. The skill reads your setup itself, so you don't need to export anything.
- **Optional but useful:** GA4, Google Tag Manager (the container your site loads) and Klaviyo. They fill in consent, server-side tagging, browser exposure and email lists.
- **Five quick answers,** if you know them:
  - your business model
  - where your customers are
  - where sales close (online, by phone, in a CRM)
  - roughly how big your customer email list is
  - whether a developer can work on your site, server or CRM

## Example requests

**Full plan**
Hey Claude, I just added the "privacy-first-targeting-strategist" skill. Score how ready my ad accounts are for less tracking and write me the roadmap.

**Meta drop**
Hey Claude, I just added the "privacy-first-targeting-strategist" skill. Our Meta results dropped and we think it's tracking. Check the pixel, our audiences and our targeting, and tell me what to fix first.

**Lead gen with offline sales**
Hey Claude, I just added the "privacy-first-targeting-strategist" skill. We're a home services company; most jobs are booked by phone. Check whether Google Ads is learning from the right signal and plan our first-party data.

**Build the audience**
Hey Claude, I just added the "privacy-first-targeting-strategist" skill. Set up a Customer Match list in Google Ads from our client list. Show me the payload first.

**App tracking opt-in**
Hey Claude, I just added the "privacy-first-targeting-strategist" skill. Only 22% of our iOS app users allow tracking. Here's our screen before the App Tracking Transparency prompt and our purpose string. Check them against Apple's rules, tell me what each extra point of opt-in is worth on Meta, and redesign the prompt.

## What you get

1. **A readiness score out of 100,** with the math, across six pillars:
   - signal source mix
   - server-side and matched data
   - consent
   - first-party audiences
   - targeting dependency
   - measurement resilience
2. **A current assessment:** your tracking setup row by row, your first-party data with sizes, and the current impact: how many conversions are exposed, which channels are hit hardest and how far you can trust the numbers.
3. **The top 5 moves,** in a fixed order, each with the numbers behind it and the share of spend it touches.
4. **The strategy:**
   - a tracking roadmap that marks which steps need a developer; when a Conversions API is part of it, the route (partner integration, server-side Tag Manager or direct API), the events to send and the match keys that raise Event Match Quality
   - a first-party data plan: collection rates to improve (email capture, account creation, consent opt-in), audience segments (high value, recent, lapsed, high intent, email engaged), where to use each, and lookalikes per platform
   - before-and-after targeting
   - recommendations for each connected platform
   - a measurement framework, with the cross-channel approach that fits your channels now
   - brand demand: your brand campaign's impressions and share of voice, plus the brand measures to check (brand search lift, direct traffic, brand lift surveys, social listening)
   - a timeline in four stages: weeks 1 to 2, weeks 3 to 4, month 2 and ongoing
5. **Unknowns:** what the APIs can't show (Event Match Quality, Conversions API status, consent rates), and how to fill each gap.

**In the app tracking opt-in mode** you get instead:
- what one more point of iOS tracking opt-in is worth on each ad platform: extra results the platform can see, your measured iOS cost per result now and at 5 and 10 more points, and how much your iOS retargeting audiences grow
- a check of your screen before the App Tracking Transparency prompt and your purpose string against Apple's rules (no rewards, one Continue button, no "Allow" on your own screen, no copy of the alert)
- a redesign: when to ask, the screen copy, the purpose string with a variant, what to show after a no, and the EU version of the prompt
- a before-and-after read of the opt-in rate by app version, with a range that says whether the change is real

This mode works from what you paste. Meta Ads, Google Ads app campaigns and GA4 app events make it fuller when connected.

## What it can change for you

With your yes on the exact change, it can do three things in Google Ads:
- create a Customer Match list
- upload consented customers to that list
- send closed deals from your CRM back to Google as offline conversions

These need a Read & Write connection, and an owner, admin or operator can switch them off. The skill never touches pixels, consent banners or Tag Manager; it tells you what to build there. The app tracking opt-in mode changes nothing; your app team ships the new screens.

## Tips

- Connect the Tag Manager container your site actually loads. Without it, consent and web enhanced conversions stay unknown.
- If you sell in the EU, EEA or UK, say so. Consent becomes a must, not a nice-to-have.
- Run it again a month after the fixes and watch the upload share and the score move.
- This is marketing strategy, not legal advice. Take consent and data questions to your lawyer.
