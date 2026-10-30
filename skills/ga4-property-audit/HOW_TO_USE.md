# How to Use This Skill

Hey Claude, I just added the "ga4-property-audit" skill. Audit my GA4 property and tell me whether I can trust its numbers.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Analytics property added.** The skill reads the settings and reports itself; you don't need to export anything or send screenshots.
- **Search Console for the same site,** if you have it. The skill compares Google clicks with GA4 sessions to see how much of your traffic GA4 actually records.
- **Google Tag Manager,** if your GA4 tag runs through it. The skill then checks the tag itself.
- **Your other domains** (app, checkout, booking tool), so it can check cross-domain tracking.

## Example requests

**Full audit**
Hey Claude, I just added the "ga4-property-audit" skill. Run a full audit of my GA4 property for the last 30 days.

**Numbers look wrong**
Hey Claude, I just added the "ga4-property-audit" skill. GA4 shows far fewer visits than Search Console. Find out why.

**Before trusting conversions**
Hey Claude, I just added the "ga4-property-audit" skill. Check my key events and tell me which ones are real, which are broken and which are test leftovers.

**Clean-up after a handover**
Hey Claude, I just added the "ga4-property-audit" skill. I just took over this property. Audit it, then list everything that should be deleted or archived.

**Traffic quality**
Hey Claude, I just added the "ga4-property-audit" skill. Check my GA4 for bot traffic, spam hostnames, Unassigned traffic and missing internal traffic filters.

**Setting up a new property (setup mode)**
Hey Claude, I just added the "ga4-property-audit" skill. I just created a GA4 property for my Shopify store. Walk me through the GA4 setup checklist in order, check each step on the property, and fix what you can after I confirm.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for eight areas:** property settings, streams and tag coverage, retention and privacy, key events, event coverage, custom definitions, attribution quality, and traffic quality.
3. **The top 5 fixes,** ranked by how much of your data each one makes trustworthy, each with the numbers behind it.
4. **A clean-up list:** test streams, test key events and unused custom definitions.
5. **A list of what couldn't be checked,** and why. The API can't read data filters, for example, so the skill tells you where to look.

In setup mode you get a checklist instead of a grade: ten steps in order (time zone and currency, data retention, the web data stream, installing the tag, checking it landed, enhanced measurement, internal traffic and referrals, key events, and the Google Ads, Search Console and BigQuery links, then a final re-read), each marked done, done now, to do (with the click path), waiting on data, or not needed. Without a connection, send screenshots of the GA4 Admin screens and it fills the same checklist from them.

## What it can change for you

With your yes on the exact change, it can:
- mark an event that already fires as a key event
- change how a key event counts (once per event or once per session)
- turn enhanced measurement events on or off on a web stream
- in setup mode: set the time zone, currency and industry, keep event data for 14 months (when your connection allows that change), add the web data stream, and link Google Ads and BigQuery

These need a Read & Write connection. Filters, unwanted referrals, cross-domain settings, the Search Console link and deletions stay with you in GA4 Admin; the skill gives you the exact click path.

## Tips

- The audit ends its window two days before today, because GA4 is still processing the most recent days. A spike in the last two days is reported, marked provisional.
- Run it after any change to your consent banner, tag setup or site domains.
- Run it again after the fixes to see the grade move.
