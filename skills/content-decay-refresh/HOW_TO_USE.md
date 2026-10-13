# How to Use This Skill

Hey Claude, I just added the "content-decay-refresh" skill. Find the pages on my site that are losing Google clicks, tell me why, and give me a refresh list in priority order.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Search Console property added.** The skill pulls the data itself; you don't export anything.
- **Optional sources that sharpen the result:**
  - GA4, for which decaying pages also bring sign-ups or sales
  - DataForSEO, to check whether demand fell and what the results page looks like now
  - Bing Webmaster, as a second search engine to compare against
  - WordPress, for when each post was last updated
- **Your brand terms,** if they aren't obvious from your domain.
- **Any big site changes** in the last six months (migration, redesign, URL changes), with dates.

## Example requests

**Refresh list**
Hey Claude, I just added the "content-decay-refresh" skill. Which blog posts should we refresh this month, and why each one?

**Traffic dropped**
Hey Claude, I just added the "content-decay-refresh" skill. Our organic clicks are down since June. Is it our content, lower demand, or Google?

**Update check**
Hey Claude, I just added the "content-decay-refresh" skill. Did the May core update or the June spam update hit our site? Show me the before and after.

**Search Console plus GA4**
Hey Claude, I just added the "content-decay-refresh" skill. Build a content refresh priority list from Search Console and GA4, and put the pages that convert first.

**Refresh, then fix (WordPress)**
Hey Claude, I just added the "content-decay-refresh" skill. Find the posts losing clicks to a weak title, draft new titles, and update the ones I approve.

## What you get

1. **The site trend** across the current, previous and quarter-ago 28-day windows.
2. **A refresh list in priority order.** Every page gets a cause: lost rank, lower click-through, another page of yours taking its queries, a redirect, a brand page, or lower demand. Each cause comes with the numbers behind it and a one-line fix.
3. **Refresh briefs** for the top three pages: the queries they lost, what the results page rewards now, and what to change.
4. **An update check** for each Google ranking update in the period. Each one is marked likely hit, possible hit, no clear effect or a gain, with the before, after and pre-trend numbers.
5. **What couldn't be checked,** and why.

## What it can change for you

With a WordPress site connected and your yes on the exact change, it can update a post's title, excerpt or content. It never publishes a rewrite you haven't read, and it doesn't change a post's URL unless you ask.

## Tips

- Run it monthly, and two weeks after any Google update finishes rolling out.
- Pages marked "watch: demand fell" usually don't need a rewrite. Fewer people are searching for them.
- If GA4 shows far fewer organic sessions than Search Console shows clicks, fix GA4 tracking first. Until then, the skill ranks by clicks only.
