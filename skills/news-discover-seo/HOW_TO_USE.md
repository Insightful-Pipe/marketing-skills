# How to Use This Skill

Hey Claude, I just added the "news-discover-seo" skill. Show me how to get more of our articles into Google Discover and Google News, and which fixes matter most.

## What you need

- **Either a Search Console export or a connection.** With no connection, paste or upload the Discover export (Pages and Dates tabs) for the last 28 days and the 28 before, plus the Google News export if you have one. With the InsightfulPipe MCP connected and your Google Search Console property added, the skill pulls the data itself.
- **The article checks need each page's head HTML,** pasted from view source, or the crawler connected through InsightfulPipe, or permission for Claude to fetch the pages.
- **Optional:** a GA4 landing page export, or GA4 connected, so the headline screen can compare Discover click-through with how long readers stay.
- **Your publication name,** exactly as readers see it, and up to 5 articles you expected to see in Discover and didn't.

## Example requests

**Get into Discover**
Hey Claude, I just added the "news-discover-seo" skill. How do we get on Google Discover? Check our top articles and tell me what's stopping them from showing as large cards.

**Discover traffic dropped**
Hey Claude, I just added the "news-discover-seo" skill. Our Discover clicks fell this month. Is it a real drop or noise, and which sections and articles lost it?

**Google News SEO**
Hey Claude, I just added the "news-discover-seo" skill. We're a local news site. Check our news sitemap, bylines and editorial pages for Google News, and compare this month's Google News clicks with last month.

**Articles that never showed up**
Hey Claude, I just added the "news-discover-seo" skill. These three articles never reached Discover. Check them and tell me whether anything on the page blocks them.

**Headlines and images**
Hey Claude, I just added the "news-discover-seo" skill. Screen our Discover headlines for clickbait and write three honest options for any that get flagged, plus image briefs for the articles with weak images.

**Working from an export**
Hey Claude, I just added the "news-discover-seo" skill. Here's our Search Console Discover export and the head HTML of our top 10 articles. Run the full review.

## What you get

1. **Discover and Google News at a glance:** clicks, impressions and CTR against the previous 28 days, each change marked real or noise, plus how concentrated Discover traffic is and how much comes from new stories.
2. **What wins:** a section table showing which parts of the site earn Discover clicks per article, and the headline traits that go with higher click-through.
3. **Article checks** on the top 10 Discover articles and the ones you named: indexing and canonical, the max-image-preview setting, image size, a representative image, Article markup and dates, and the byline.
4. **Site checks:** the news sitemap and the editorial pages Google News looks for.
5. **A headline screen** for clickbait, with three rewrites per flagged headline that stay true to the article.
6. **The top 5 fixes,** ranked by the Discover or Google News impressions at stake, with image briefs and a list of what couldn't be checked.

## What it can change for you

Nothing. It only reads. You get the fixes, headline options and image briefs to apply in your CMS.

## Tips

- Discover is never guaranteed. A clean check means nothing on the page blocks the article, not that Discover will pick it.
- Search Console shows Discover only once a site passes a minimum number of impressions. If you have no Discover report yet, the skill marks the traffic part not graded and still checks the articles you name.
- Fix section templates first: one robots line or image size setting can cover hundreds of articles.
- Run it monthly, and a few weeks after a template change to see whether the cards got bigger.
