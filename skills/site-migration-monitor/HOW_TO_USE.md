# How to Use This Skill

Hey Claude, I just added the "site-migration-monitor" skill. We moved our site yesterday and set up redirects. Check the migration and tell me what to fix today.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Search Console property added.** The crawler comes with it. The skill pulls the data itself; you don't export anything.
- **The move date,** planned or done.
- **What moved and where to:** a pattern such as `/blog/*` or the old domain, and a redirect map or a rule such as "same path on the new domain".
- **Optional:** GA4, Bing Webmaster and DataForSEO. GA4 adds visits and 404 views, Bing adds a second search engine and inbound links per page, and DataForSEO finds the old pages other sites link to (1 paid call per run).
- **Nothing connected?** The launch check and the redirect map builder work from two crawl exports or two pasted URL lists. Add a Search Console performance export and they rank pages by real clicks.

## Example requests

**Before the move**
Hey Claude, I just added the "site-migration-monitor" skill. We're moving the blog from /resources to /blog on November 10. Build the baseline, draft the redirect map and run the checklist.

**The day after**
Hey Claude, I just added the "site-migration-monitor" skill. We switched from oldbrand.com to newbrand.com yesterday. Check every important old URL redirects to the right page.

**A few weeks in**
Hey Claude, I just added the "site-migration-monitor" skill. We relaunched on a new CMS three weeks ago. Has Google picked up the move, and has traffic recovered?

**Before a redesign goes live (launch check)**
Hey Claude, I just added the "site-migration-monitor" skill. Our redesign is on staging.example-shop.example and launches next Tuesday. Here are crawl exports of staging and the live site. Run the website redesign SEO checklist and tell me what the new build lost on the pages that get clicks.

**A brand-new site**
Hey Claude, I just added the "site-migration-monitor" skill. We launch our new website on Monday. Run the SEO checklist for a new website: indexing, sitemap, Search Console, Bing and analytics.

**Redirect map with no clean rule**
Hey Claude, I just added the "site-migration-monitor" skill. We're moving from WordPress to Shopify and every URL changes. Here are the old and new URL lists. Build the 301 redirect map, flag the ones I should check by hand and give me the Shopify import file.

**Traffic dropped after a redesign**
Hey Claude, I just added the "site-migration-monitor" skill. Organic traffic fell after our redesign on September 1. Check whether the migration is the cause.

## What you get

**Before the move:**
1. **A baseline:** every old URL with search clicks, GA4 visits or backlinks, and a priority list of up to 50 to protect.
2. **A pre-move crawl:** old URLs that already redirect or are broken, so the new redirects don't chain.
3. **A redirect map draft,** with gaps, chains and home-page dumps flagged.
4. **The migration checklist,** with each item marked verified, to do, or by hand.

**Launch check:**
1. **A verdict:** hold the launch, launch after fixes, or clear to launch.
2. **A page-by-page diff** of the pages that earn clicks: titles, H1s, text, canonicals, noindex, internal links and structured data, live against test.
3. **The usual launch traps:** leftover noindex, canonicals on the test host, robots.txt blocking CSS and JavaScript, missing analytics.
4. **For a brand-new site,** the go-live list instead.

**Redirect map:**
1. **Every old URL matched** to its best new page, with how it was matched and how sure the match is.
2. **A review list** of the valuable URLs a human should check, plus chains, loops, home-page dumps and 410 candidates.
3. **A ready file** for Apache, Nginx, Cloudflare, Shopify or CSV.

**After the move:**
1. **An overall status:** on track, watch or act now, with the stage of the move (first week, settling, settled).
2. **Eight checks:** redirects, untouched pages, new pages, robots.txt, sitemaps, search engine pickup, traffic and tracking. Each one is graded only when enough time has passed to judge it.
3. **A redirect table:** every problem URL with its clicks and backlinks.
4. **The next check dates,** and what each one will grade.

## What it can change for you

With your yes on the exact change, it can:
- resubmit your sitemap to Bing
- ask Bing to crawl your new pages

It never changes redirects, robots.txt or your site; the redirect file is yours to install. Search Console has no sitemap submit through the MCP, so it tells you when to resubmit there yourself.

## Tips

- Run it once before the move, then on day 1, 7, 14, 28 and 90.
- Search Console data lags 3 to 4 days, so traffic can only be judged from about day 11. The redirect checks work on day 1.
- If GA4 changed on the same day as the move, the skill says so and leans on Search Console instead.
