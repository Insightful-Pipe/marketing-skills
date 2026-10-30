# How to Use This Skill

Hey Claude, I just added the "robots-llms-txt-builder" skill. Check my robots.txt and sitemap, then write corrected versions and an llms.txt for my site.

## What you need

- **Your site's address,** exactly as visitors see it (`https://www.yoursite.com`).
- **Your current robots.txt and a list of your URLs,** pasted or exported (a sitemap, a CMS export, a crawl export or a Search Console Pages export). Or connect the InsightfulPipe MCP and the skill reads them itself, along with Search Console clicks and Bing crawl issues.
- **The paths you want kept away from crawlers,** such as your app, API, internal search or staging copies.
- **Your view on AI crawlers.** The skill explains the three kinds (model training, AI search, user fetch) before it asks.

## Example requests

**Fix and rebuild everything**
Hey Claude, I just added the "robots-llms-txt-builder" skill. Fix our robots.txt, rebuild the XML sitemap and write an llms.txt. We want to show up in ChatGPT and Perplexity answers, but not in AI training data.

**Block AI training only**
Hey Claude, I just added the "robots-llms-txt-builder" skill. Block AI training bots like GPTBot and ClaudeBot without hurting our Google or ChatGPT visibility. Here's our robots.txt.

**Generate an XML sitemap**
Hey Claude, I just added the "robots-llms-txt-builder" skill. Generate an XML sitemap from this crawl export. Leave out anything that redirects, is noindex or 404s.

**Why did a page lose traffic?**
Hey Claude, I just added the "robots-llms-txt-builder" skill. Our template page stopped getting Google clicks after we edited robots.txt. Test the file against our URLs and fix it.

**Write an llms.txt**
Hey Claude, I just added the "robots-llms-txt-builder" skill. Write an llms.txt (and llms-full.txt) for our docs site from the pages people actually visit.

## What you get

1. **A test of your live robots.txt:** every URL from your sitemap and every page with Search Console clicks, checked for Googlebot, Bingbot and each AI crawler, with the rule that decided it and the clicks at stake.
2. **A dated AI crawler table** split by purpose, and the policy you chose for each.
3. **A corrected robots.txt** with a line-by-line diff, retested on the same URLs, and a 4-check gate it must pass before you ship it.
4. **An XML sitemap** of only live, indexable, canonical pages, with every dropped URL and the reason, and the pages it was missing.
5. **An llms.txt** built from your key pages and the guides that earn clicks, with every link checked.
6. **How to ship** each file on your platform (WordPress, Shopify, Next.js, Wix, Webflow, Squarespace).

## What it can change for you

Nothing on your site. You publish the files. After you've deployed the new sitemap and say yes, it can tell Bing about it.

## Tips

- Paste a crawl export with status code, canonical and noindex columns if you have one. It makes the sitemap check exact.
- Google needs no llms.txt for AI Overviews. Treat llms.txt as a low-cost extra, not a ranking lever.
- Run it again after any site migration, new section or CMS change, and a week after shipping to read what Google and Bing downloaded.
