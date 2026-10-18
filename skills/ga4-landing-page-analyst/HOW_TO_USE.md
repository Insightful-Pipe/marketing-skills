# How to Use This Skill

Hey Claude, I just added the "ga4-landing-page-analyst" skill. Review my landing pages in GA4 and tell me which ones lose the most visitors.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the data itself; you don't need to export anything.
- **Optional: Google Ads and Search Console in the same workspace.** They add ad cost per landing page and organic clicks per page.
- **Your main conversion,** if it isn't already a key event in GA4.
- **Your 404 page title,** if it doesn't contain "not found" or "404".

## Example requests

**Landing page review**
Hey Claude, I just added the "ga4-landing-page-analyst" skill. Show me my top landing pages for the last 30 days, how they changed from the month before, and which ones leak visitors.

**By ad source**
Hey Claude, I just added the "ga4-landing-page-analyst" skill. Compare landing page conversion rates for paid search, paid social and organic. Which pages work for paid traffic and which don't?

**Paid search quality**
Hey Claude, I just added the "ga4-landing-page-analyst" skill. Join my Google Ads cost to GA4 and tell me which paid landing pages cost the most per engaged visit.

**Organic landing pages**
Hey Claude, I just added the "ga4-landing-page-analyst" skill. Which pages bring in organic search visitors, and do the Search Console clicks match what GA4 records?

**Broken pages and site search**
Hey Claude, I just added the "ga4-landing-page-analyst" skill. Find the pages that return 404, show me which links point to them, and tell me what people search for on my site.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for six areas:** data health, landing page performance and leaks, traffic source fit, content engagement and scroll, broken pages, and site search.
3. **The top 5 page fixes,** ranked by the visitors or spend at stake.
4. **A landing page table** with sessions, change from the prior period, engagement, key event rate and a verdict for each page.
5. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- mark an event that already fires as a key event
- turn on scroll or site search tracking in enhanced measurement

It never edits your pages, redirects or ads.

## Tips

- GA4 has no exit-rate metric in its API, so "leaks" here means sessions that land and leave without engaging. The report says how many more than an average page would lose.
- If no key events fire yet, the ranking uses engaged sessions. Set up a key event first for a true conversion view.
- Run it monthly, and after you change a page, to see whether the change helped.
