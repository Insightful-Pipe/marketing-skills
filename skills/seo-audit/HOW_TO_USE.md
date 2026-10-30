# How to Use This Skill

Hey Claude, I just added the "seo-audit" skill. Audit my website's SEO and tell me the five fixes that matter most.

## What you need

- **The InsightfulPipe MCP connected to Claude, with Google Search Console added.** The skill pulls the data itself; you don't need to export anything or run a desktop crawler.
- **For a fuller audit, also add** PageSpeed Insights, DataForSEO, Bing Webmaster Tools, Google Analytics 4 and the Crawler. Anything missing shows up as "unknown" in the report instead of a guess.
- **Your most important pages,** if they aren't your top pages in Google already.
- **For the E-E-A-T and helpful content review,** no connection is needed: give it your URLs or paste the page text, and tell it who writes and checks your content. Search Console adds each page's click trend.

## Example requests

**Full audit**
Hey Claude, I just added the "seo-audit" skill. Run a full SEO audit on my site for the last 28 days and give me a grade.

**Traffic dropped**
Hey Claude, I just added the "seo-audit" skill. Our organic clicks fell this month. Audit the site and show me where the problem is.

**Indexing problems**
Hey Claude, I just added the "seo-audit" skill. Find which of my sitemap pages Google hasn't indexed, and tell me why.

**Broken links and redirects**
Hey Claude, I just added the "seo-audit" skill. Find the 404s people still land on and any redirect chains, and tell me where each should point.

**On-page check**
Hey Claude, I just added the "seo-audit" skill. Check titles, meta descriptions, H1s, canonicals and image alt text on my top pages.

**Content inventory**
Hey Claude, I just added the "seo-audit" skill. Give me a content inventory of my site by section, with impressions, clicks and how much of each section is indexed.

**E-E-A-T plan**
Hey Claude, I just added the "seo-audit" skill. Audit my site's trust signals and give me an E-E-A-T improvement plan.

**E-E-A-T and helpful content review**
Hey Claude, I just added the "seo-audit" skill. Run the E-E-A-T and helpful content review on my top 10 articles: check bylines, author pages, sources and dates, flag anything that looks mass-produced, show which pages are losing clicks, and write the author bios from the facts I give you.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for eight areas:** crawl access, indexation, broken and redirected URLs, on-page tags, content depth, speed, search performance, and authority and trust.
3. **The top 5 fixes,** failing areas first, ranked by the Google impressions at stake, each with the numbers behind it.
4. **A content inventory** by site section, with an estimate of how much of each section Google has indexed. It doubles as a map of the site's structure.
5. **A page table** for your top pages and your About page: title and description length, H1s, word count, canonical, load time, impressions and position.
6. **Lists you can act on:** 404s with their traffic, pages Google hasn't indexed, pages Google has never found, and snippet rewrites with the clicks at stake.
7. **A list of what couldn't be checked,** and why, and the next step for each finding the audit can't fix by itself.

In the **E-E-A-T and helpful content review** you get a table of your key pages with their click trend, what each one shows about who wrote it, how it was made, its sources and its dates, any helpful content or scaled content flag with the evidence, and an act now, fix soon or keep label. Then drafted author bios, a reviewer line, About page sections and Person and Organization markup, written only from facts you confirm, with a list of the facts still needed. There is no made-up E-E-A-T score.

## What it can change for you

With a Read & Write Bing Webmaster connection and your yes on the exact change, it can:
- resubmit your sitemap to Bing
- ask Bing to crawl pages you've fixed

Everything else (redirects, titles, content, speed) is a change to your site, so the skill writes it as a precise instruction for you or your developer.

## Tips

- Run it monthly, and after a migration, a redesign or a big content change.
- If you have international versions, say so, and the audit adds an hreflang check and a country breakdown.
- Run it again after the fixes to see the grade move.
