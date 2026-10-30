# How to Use This Skill

Hey Claude, I just added the "indexing-monitor" skill. Check which of my pages Google and Bing have indexed, tell me why the rest aren't, and say what to submit.

## What you need

- **The InsightfulPipe MCP connected to Claude, with Google Search Console added.** The skill pulls the data itself; you don't need to export anything.
- **Bing Webmaster Tools,** if you want the Bing half. Without it, the report covers Google only and says so.
- **Your sitemap URL,** if it isn't the one in your robots.txt.
- **New pages you care about,** if you just published or moved some. Without a list, the skill finds them from your sitemap.

## Example requests

**Full check**
Hey Claude, I just added the "indexing-monitor" skill. Run an indexing check on my site for Google and Bing.

**Why aren't these pages indexed?**
Hey Claude, I just added the "indexing-monitor" skill. Inspect these URLs in Search Console and group the ones that aren't indexed by reason: [paste URLs].

**New pages**
Hey Claude, I just added the "indexing-monitor" skill. We published 12 new pages this week. Are Google and Bing picking them up?

**Sitemap check**
Hey Claude, I just added the "indexing-monitor" skill. Compare my XML sitemap with what Google and Bing last downloaded, and find pages that get impressions but are missing from it.

**Submit, after a look**
Hey Claude, I just added the "indexing-monitor" skill. Plan which URLs to submit to Bing today within my quota, and resubmit my sitemap to Google and Bing. Show me the payloads first.

## What you get

1. **A status line for each of seven areas:** sitemap health, Google coverage, not-indexed reasons, top pages, new pages, Bing coverage, and sitemap vs the pages the engines found.
2. **Google coverage:** how many sitemap URLs are confirmed indexed, from impressions and URL inspection.
3. **Not-indexed pages grouped by reason:** fix now, Google picked another page, crawled but not indexed, and not crawled yet, with orphan pages counted. Pages Google flagged months ago are rechecked today, and the ones that work again get their own "fixed since Google's last crawl" line, so you don't fix what's already fixed.
4. **New pages:** whether each one was crawled, indexed and linked from other pages.
5. **Bing coverage:** pages in Bing's index, crawl errors and the status of your sitemap there.
6. **A submission plan:** which URLs to submit to Bing within today's quota, and when to resubmit a sitemap.

## What it can change for you

With your yes on the exact payload, it can:
- submit or resubmit a sitemap to Google Search Console
- submit a sitemap to Bing
- submit URLs to Bing, one or a batch, within your daily quota

It never removes sitemaps or blocks URLs.

## Tips

- Run it a few days after you publish or move pages, then again a week later.
- Google's URL Inspection has a daily quota per property. The skill spends it on the pages that matter and tells you how many it used.
- A page Google chose not to index is often fine. The report says which ones to fix and which ones to leave.
