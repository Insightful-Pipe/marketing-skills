# How to Use This Skill

Hey Claude, I just added the "google-ads-click-fraud-check" skill. Check whether my Google Ads account is paying for fake or accidental clicks, and tell me what to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** Add your GA4 property too: it is how the skill proves a suspect source with real visit data instead of guessing.
- **Your service area and when real customers contact you,** if you have them. Without them, the skill uses the campaigns' own targeted locations and treats every hour alike.
- **Your server or CDN logs,** only if you want IP exclusions or want to send Google an investigation request. Google Ads never shows click IP addresses.
- **No connection?** Paste or upload these Google Ads reports for the last 30 days instead: campaigns with the Invalid clicks and Invalid click rate columns (by day too, if you can), the network split (Google search vs search partners), "Where ads showed" for Display and Performance Max, locations with "targeted" vs "not targeted", hour of day and device. Add a GA4 export of paid sessions by campaign, network, city and device with engaged sessions and engagement time.

## Example requests

**Is it click fraud?**
Hey Claude, I just added the "google-ads-click-fraud-check" skill. Our clicks jumped last week and leads didn't. Is someone clicking our ads?

**Before buying a tool**
Hey Claude, I just added the "google-ads-click-fraud-check" skill. Do I need a click fraud protection tool, or is Google already filtering this?

**Competitor clicking**
Hey Claude, I just added the "google-ads-click-fraud-check" skill. I think a competitor keeps clicking our plumbing ads. Check the last 30 days and draft a report I can send to Google.

**From exports**
Hey Claude, I just added the "google-ads-click-fraud-check" skill. Here are my Google Ads campaign, location, placement and hour reports and a GA4 paid traffic export. Find the clicks that aren't real people.

## What you get

1. **Google's own numbers first:** invalid clicks and the invalid click rate for the account, each campaign and each day, with any spike day called out.
2. **Every suspect source checked:** search partners, Performance Max and Display apps and sites, people outside your area, night hours and devices, each with clicks, cost, leads and a verdict.
3. **Proof from GA4:** engaged visits and engagement time for the same paid traffic, next to your clean traffic, so a suspect source comes with evidence.
4. **Fixes ranked by the money at stake,** each with who can make the change.
5. **A ready-to-send investigation request for Google,** when your evidence says Google missed something, plus paste-ready exclusion lists.

## What it can change for you

With your yes on the exact change, it can:
- switch search partners off on a campaign
- switch a campaign's location matching to people in or regularly in your area

Placement exclusions, IP exclusions and the investigation request are handed to you ready to paste, because the connector can't write them.

## Tips

- Run it monthly, and right away after any day with a click spike. Google investigates only the last 60 days.
- A click fraud tool is worth considering only after the fixes here, and only if your GA4 proof still shows non-human visits that Google's invalid click rate doesn't reflect.
