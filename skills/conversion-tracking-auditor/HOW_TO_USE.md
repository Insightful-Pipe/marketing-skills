# How to Use This Skill

Hey Claude, I just added the "conversion-tracking-auditor" skill. Check my conversion tracking and tell me whether I can trust the conversions Google Ads is bidding on.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the data itself; you don't need to export anything.
- **Optional: GA4, Google Tag Manager, Meta Ads and LinkedIn Ads.** Each one you connect adds checks: tags in the live container, key events that fire, pixels and Insight Tag conversions.
- **Your website address** and **what counts as a real conversion** for you (a sale, a booked call, a form). Without them, the skill uses what your accounts show.

## Example requests

**Full audit**
Hey Claude, I just added the "conversion-tracking-auditor" skill. Audit conversion tracking across Google Ads, GA4 and Tag Manager for the last 30 days.

**Primary and secondary actions**
Hey Claude, I just added the "conversion-tracking-auditor" skill. Which conversion actions does Google Ads actually count, and are any of them counting the same lead twice?

**Before Smart Bidding**
Hey Claude, I just added the "conversion-tracking-auditor" skill. I want to move my campaigns to Target CPA. Check the conversions are clean first.

**Conversions dropped**
Hey Claude, I just added the "conversion-tracking-auditor" skill. Our conversions fell off a cliff this week. Is a tag broken?

**Offline imports and enhanced conversions**
Hey Claude, I just added the "conversion-tracking-auditor" skill. Are my offline conversion uploads healthy, and am I ready for enhanced conversions?

**Set up the tags**
Hey Claude, I just added the "conversion-tracking-auditor" skill. Add a Conversion Linker and a Google Ads conversion tag for my thank-you page in GTM. Show me the tags before you create them.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for eight areas:** account setup, what counts, live signal, lag and windows, offline imports, enhanced conversions and consent, tags on the site, and GA4.
3. **The list of what Google Ads counts,** with counting, window, attribution, 30-day conversions and the last conversion date for each action.
4. **How many recent days to leave out** before you judge a CPA, from your own conversion lag.
5. **The top fixes,** ranked by the spend they steer.
6. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- set a duplicate or soft conversion action to secondary, hide a silent one, or lengthen a lookback window
- create a new conversion action
- add a Conversion Linker and a Google Ads conversion tag to your GTM workspace (you publish it)
- mark a GA4 event as a key event
- create a Meta custom conversion

It never deletes a conversion action and never publishes your GTM container.

## Tips

- Run it before any switch to Smart Bidding, after a site redesign, and after changing your form or call tracking.
- If you manage several sites, say which GTM container and GA4 property belong to this one.
- Run it again a week after the fixes to see the live-signal area recover.
