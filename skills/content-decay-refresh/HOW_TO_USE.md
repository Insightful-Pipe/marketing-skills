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
- **For the AI Overview impact check with nothing connected:** a Search Console export comparing two periods (Performance, set the date filter to Compare, Queries tab, Export), plus any queries where you've seen an AI Overview, or a rank-tracker export with an AI Overview column.

## Example requests

**Refresh list**
Hey Claude, I just added the "content-decay-refresh" skill. Which blog posts should we refresh this month, and why each one?

**Traffic dropped**
Hey Claude, I just added the "content-decay-refresh" skill. Our organic clicks are down since June. Is it our content, lower demand, or Google?

**Update check**
Hey Claude, I just added the "content-decay-refresh" skill. Did the May core update or the June spam update hit our site? Show me the before and after.

**Search Console plus GA4**
Hey Claude, I just added the "content-decay-refresh" skill. Build a content refresh priority list from Search Console and GA4, and put the pages that convert first.

**AI Overview impact (impressions up, clicks down)**
Hey Claude, I just added the "content-decay-refresh" skill. Our impressions are up but clicks are down year over year. How much of that is AI Overviews, and which queries should we defend?

**AI Overview impact from a pasted export**
Hey Claude, I just added the "content-decay-refresh" skill. Here's our Search Console query export comparing the last 28 days with the same period last year, and the queries where I saw an AI Overview. Split the click drop into AI Overviews, rankings and demand, and write a short note I can send my boss.

**Refresh, then fix (WordPress)**
Hey Claude, I just added the "content-decay-refresh" skill. Find the posts losing clicks to a weak title, draft new titles, and update the ones I approve.

## What you get

1. **The site trend** across the current, previous and quarter-ago 28-day windows.
2. **A refresh list in priority order.** Every page gets a cause: lost rank, lower click-through, another page of yours taking its queries, a redirect, a brand page, or lower demand. Each cause comes with the numbers behind it and a one-line fix.
3. **Refresh briefs** for the top three pages: the queries they lost, what the results page rewards now, and what to change.
4. **An update check** for each Google ranking update in the period. Each one is marked likely hit, possible hit, no clear effect or a gain, with the before, after and pre-trend numbers.
5. **What couldn't be checked,** and why.

The AI Overview impact check returns its own report: the click change on your non-brand queries split into demand, rank, other results-page changes, AI Overviews (cited and not cited), unknown status and dropped-out queries, with the formula for each line; the queries where impressions held but clicks fell; since when each big query has shown an overview; which queries to defend and which pages to steer toward clicks a summary can't satisfy; and a four-sentence note for stakeholders. It uses at most 10 DataForSEO calls.

## What it can change for you

With a WordPress site connected and your yes on the exact change, it can update a post's title, excerpt or content. It never publishes a rewrite you haven't read, and it doesn't change a post's URL unless you ask.

## Tips

- Run it monthly, and two weeks after any Google update finishes rolling out.
- Pages marked "watch: demand fell" usually don't need a rewrite. Fewer people are searching for them.
- Compare the same weeks a year apart for the AI Overview check, so seasonality doesn't pass for an AI Overview effect.
- If GA4 shows far fewer organic sessions than Search Console shows clicks, fix GA4 tracking first. Until then, the skill ranks by clicks only.
