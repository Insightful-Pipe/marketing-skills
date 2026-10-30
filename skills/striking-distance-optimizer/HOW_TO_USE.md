# How to Use This Skill

Hey Claude, I just added the "striking-distance-optimizer" skill. Find the keywords my site almost ranks for and tell me which pages to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Search Console property added.** The skill pulls the data itself; you don't need to export anything.
- **Your brand terms,** if they aren't obvious from your site name. Brand searches are left out so they don't swamp the list.
- **Optional:** a WordPress site connected with a Read & Write connection, if you want Claude to change titles for you after you approve them.
- **For the title tag and meta description audit, nothing has to be connected.** Paste your titles and descriptions, or a crawl export, plus a Search Console export if you have one. With Search Console connected, the crawler reads every page's tags, and with DataForSEO connected it also checks the title Google shows.

## Example requests

**Quick wins**
Hey Claude, I just added the "striking-distance-optimizer" skill. Show me the keywords on page two of Google that are closest to page one.

**Low-CTR pages**
Hey Claude, I just added the "striking-distance-optimizer" skill. Which of my pages get plenty of impressions but too few clicks for where they rank?

**Title rewrites**
Hey Claude, I just added the "striking-distance-optimizer" skill. Give me a priority list of page titles to rewrite, with the new title for each.

**Long-tail ideas**
Hey Claude, I just added the "striking-distance-optimizer" skill. Find the long-tail searches I show up for and tell me which ones deserve a new section or page.

**Title tag and meta description audit**
Hey Claude, I just added the "striking-distance-optimizer" skill. Audit the title tags, meta descriptions and social preview tags across my site, tell me which titles Google is rewriting, and write replacements from the searches each page shows for.

**Meta descriptions for a list of pages**
Hey Claude, I just added the "striking-distance-optimizer" skill. Here are 12 URLs with what each page offers and its target search. Write two title options and two meta descriptions for each, with their estimated width.

**A different band**
Hey Claude, I just added the "striking-distance-optimizer" skill. Use positions 4 to 15 instead, and leave out anything with "acme" in it as brand.

## What you get

1. **What the data covers:** non-brand impressions and clicks, the minimum share of your impressions that the query rows show (Google hides rare queries), and your site's own CTR at each position, with each figure labelled by the Search Console pull it came from.
2. **Striking-distance keywords:** queries at positions 8 to 20, grouped by the page that ranks for them, with the clicks at stake, whether each is rising or sliding, and any second page of yours competing for it.
3. **Low-CTR pages:** pages that get fewer clicks than your own site gets at the same position, and whether the problem is the snippet or the ranking.
4. **A title rewrite list:** the top 10 pages, the checks on each current title, and a new title where one is needed.
5. **Long-tail phrases:** grouped variants, each with the move to make: an FAQ, a comparison section, a stronger page or a new page.
6. **The top 5 actions,** ranked by clicks at stake.

The title tag and meta description audit gives you instead:
1. **A count of each problem:** missing, duplicated or cut-off titles and descriptions, pages with two title tags, incomplete Open Graph tags and missing X card tags.
2. **Titles Google rewrites:** the title you wrote next to the one Google shows, where Google's version likely came from, and why.
3. **A fix list,** most urgent first: the old and new title and description for each page with their estimated widths in pixels, and the social tags to add.
4. **A before and after read** for any page whose title changed: click-through on the same searches before and after, adjusted for position.

## What it can change for you

On a connected WordPress site, with your yes on the exact text, it can change a post or page title, and the meta description and social tags when your SEO plugin exposes them. On any other CMS, it gives you the old and new text to paste. It never changes URLs.

## Tips

- Run it monthly. Wait about 28 days after a title change before you judge it.
- Fix two pages competing for one query before you rewrite either of them.
- On a small site, start with the striking-distance list; CTR comparisons need more data.
- Wait at least 14 days after a title change before you ask for the before and after read; 28 is better.
