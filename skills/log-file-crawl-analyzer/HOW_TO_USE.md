# How to Use This Skill

Hey Claude, I just added the "log-file-crawl-analyzer" skill. Here are last week's access logs and our sitemap. Show me where Googlebot wastes crawl budget and which bots are fake.

## What you need

- **Your access logs,** 7 days at least and 30 days if you can. Apache, Nginx, Cloudflare, Fastly, CloudFront, Akamai and IIS exports all work, as does a CSV with time, client IP, URL with its query string, status code and user agent. If your site sits behind a CDN, send the CDN's edge log, not the origin server's.
- **Your sitemap,** uploaded or as a URL.
- **Optional:** the InsightfulPipe MCP connected to Claude with Google Search Console, Bing Webmaster Tools, the crawler and BigQuery. Each one adds a check; none is required.

## Example requests

**Full log file analysis**
Hey Claude, I just added the "log-file-crawl-analyzer" skill. Here are 30 days of Nginx logs and our sitemap. Run the full analysis and rank the crawl budget fixes.

**Fake Googlebot check**
Hey Claude, I just added the "log-file-crawl-analyzer" skill. Something calling itself Googlebot is hammering our search pages. Check which Googlebot hits in this log are real.

**AI crawlers**
Hey Claude, I just added the "log-file-crawl-analyzer" skill. What are GPTBot, ClaudeBot and PerplexityBot fetching on our site, and are they hitting dead pages?

**Crawled but no clicks**
Hey Claude, I just added the "log-file-crawl-analyzer" skill. Join this log with Search Console and show me which page types Google crawls that never earn a click.

**Logs too big to upload**
Hey Claude, I just added the "log-file-crawl-analyzer" skill. Our Cloudflare logs go to BigQuery in the table logs.http_requests. Analyse crawling for October 1 to 30.

**Analyse, then tell Bing**
Hey Claude, I just added the "log-file-crawl-analyzer" skill. Analyse this log, then tell Bing to ignore the sort and session parameters you find. Show me the list first.

## What you get

1. **Bot verification:** every Googlebot, Bingbot and AI crawler hit checked against the IP lists Google, Bing, OpenAI, Anthropic and Perplexity publish, with fake bots and the URLs they hit listed apart.
2. **A scorecard:** waste share, waste against money pages, server errors, redirects and fake share, each marked fine, watch or fix.
3. **Where Googlebot and Bingbot go:** hits by page type and status code, hits per day, how many of your product or category URLs were crawled, and the top waste URLs and parameters.
4. **Joins:** orphan candidates, page types crawled with no clicks, sitemap health, and Bing's own crawl count against the log.
5. **An AI crawler view:** one row per bot with its status codes, top page types, robots.txt group and share of dead URLs.
6. **Ranked fixes:** each with the verified bot hits a week it addresses and who does it.
7. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can tell Bing Webmaster Tools to ignore a query parameter (one call per parameter). Everything else, from robots.txt and redirects to sitemaps and CDN rules, it drafts for you to apply.

## Tips

- Crawl budget matters most on sites with more than about 10,000 URLs. On a smaller site the skill still finds fake bots, errors and dead URLs, and says crawl budget is unlikely to be what holds you back.
- Run it again two to four weeks after a robots.txt or redirect change to see the waste share fall.
- Google's Crawl Stats report isn't in the Search Console API. Paste it in if you want Google's own count set against the log.
