# How to Use This Skill

Hey Claude, I just added the "consent-mode-auditor" skill. Check our cookie banner and Consent Mode v2 setup, and tell me how much data the banner costs us in GA4 and Google Ads.

## What you need

- **A few browser recordings of your site.** In Chrome, open an incognito window, open DevTools, tick "Preserve log" on the Network tab, load the site and save it as a HAR file. Make one with no click, one after Reject all, one after Accept all, and one return visit, from a country where your banner must ask. If you can't make HAR files, paste the Consent tab from Tag Assistant instead.
- **Your consent platform's report** for the last 28 days, if it has one: how many saw the banner, accepted, rejected, made custom choices or ignored it, by country and device.
- **Optional: the InsightfulPipe MCP** with Google Tag Manager, GA4, Search Console and Google Ads connected. The skill then reads the live container and puts a number on the loss from your own data. Anything you don't connect is skipped, not failed.

## Example requests

**Consent mode v2 check**
Hey Claude, I just added the "consent-mode-auditor" skill. Here are four HAR files from our site, recorded from Germany. Check that Consent Mode v2 is set up right.

**What the banner costs**
Hey Claude, I just added the "consent-mode-auditor" skill. How many visitors decline our cookie banner, and how many GA4 sessions and Google Ads conversions does that hide? Our consent platform report is attached.

**Modelling**
Hey Claude, I just added the "consent-mode-auditor" skill. Do we qualify for Google's conversion modelling and GA4 behavioural modelling in each European country we advertise in?

**After a banner change**
Hey Claude, I just added the "consent-mode-auditor" skill. We switched consent platforms last week. Check nothing fires before a choice and that Accept all sends all four signals.

## What you get

1. **A scorecard for seven areas:** before a choice, default and update signals, regions, the Tag Manager cause, what declines cost, modelling eligibility, and personal data in URLs.
2. **A signal table** decoding the consent state on every Google hit in your recordings.
3. **The cost per country:** decline share, unseen GA4 sessions and unseen Google Ads conversions, each marked as an estimate.
4. **Ranked fixes:** breach risks first, then signal gaps, then data recovery, each with the evidence and who does it.
5. **Banner suggestions** that lift acceptance within the rules, only where your report supports them.

## What it can change for you

With your yes on the exact change, it can add a consent requirement to a non-Google tag in your Google Tag Manager workspace. It never publishes the container, and it never changes your consent platform or site code; it gives you the exact change to make there.

## Tips

- Record from a country where the banner must ask. A VPN or your consent platform's geo preview works.
- Run it again after every consent platform or GTM change, and after you add a new country to your ads.
- This is a technical check against Google's rules, not legal advice.
