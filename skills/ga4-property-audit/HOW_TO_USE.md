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

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for eight areas:** property settings, streams and tag coverage, retention and privacy, key events, event coverage, custom definitions, attribution quality, and traffic quality.
3. **The top 5 fixes,** ranked by how much of your data each one makes trustworthy, each with the numbers behind it.
4. **A clean-up list:** test streams, test key events and unused custom definitions.
5. **A list of what couldn't be checked,** and why. The API can't read data filters, for example, so the skill tells you where to look.

## What it can change for you

With your yes on the exact change, it can:
- mark an event that already fires as a key event
- change how a key event counts (once per event or once per session)
- turn enhanced measurement events on or off on a web stream

These need a Read & Write connection. Retention, streams, filters, cross-domain settings and deletions stay with you in GA4 Admin; the skill tells you exactly what to change.

## Tips

- The audit ends its window two days before today, because GA4 is still processing the most recent days. A spike in the last two days is reported, marked provisional.
- Run it after any change to your consent banner, tag setup or site domains.
- Run it again after the fixes to see the grade move.
