# How to Use This Skill

Hey Claude, I just added the "javascript-seo-rendering-check" skill. Check whether Google and AI crawlers can read my JavaScript site, one URL per template, and tell me what to change.

## What you need

- **One URL per page template,** up to 10: home, a blog post, a product or feature page, a category or hub, a help article, pricing. Say roughly how many URLs each template serves.
- **One to three key facts per template** that must be findable: a price, a product name, the topic of the article.
- **How often each template changes,** and which pages are meant to stay out of search. The rendering fix depends on both.
- **Nothing to connect.** In Claude Code the skill fetches the raw HTML itself and, if Chrome is installed, the rendered page. Elsewhere, paste the page source (view-source) and the rendered HTML (DevTools, Copy outerHTML).
- **Optional: the InsightfulPipe MCP** with Search Console, PageSpeed, the crawler and DataForSEO (the DataForSEO path was untested at build time), to add Google's index status, Lighthouse SEO audits and soft-404 probes.

## Example requests

**A React or Next.js site**
Hey Claude, I just added the "javascript-seo-rendering-check" skill. Our site is built with React and Next.js. Here are six URLs, one per template. Can Google crawl the JavaScript, and what do AI crawlers see?

**Pages not indexed**
Hey Claude, I just added the "javascript-seo-rendering-check" skill. Our help center is a single-page app and none of its articles are in Google. Find out why and tell me the fix.

**AI answers get it wrong**
Hey Claude, I just added the "javascript-seo-rendering-check" skill. ChatGPT quotes old prices for us. Check whether our pricing page shows the prices before JavaScript runs.

**Pasted HTML, no connection**
Hey Claude, I just added the "javascript-seo-rendering-check" skill. Here is the view-source and the rendered HTML of our product page. Compare them and tell me what search engines miss.

## What you get

1. **A verdict per template for Google and for AI crawlers,** kept apart, because a page can be fine for Google and invisible to crawlers that don't run JavaScript.
2. **The raw-versus-rendered numbers:** visible words, internal links, key facts, title, description, canonical, robots and structured data, before and after JavaScript.
3. **Google's own view,** when Search Console is connected: index status and the canonical Google chose, read next to the cause.
4. **Fixes in order,** Google problems first, each with the evidence, the rendering approach (static, revalidated, server-side or a prerender stopgap) and the exact change in your framework.
5. **A list of the key facts AI crawlers can't see,** and what couldn't be checked.

## What it can change for you

Nothing. It reads and reports. It can draft the code change if you share the file, and rerun the check after you deploy.

## Tips

- Test the URL your visitors land on, not a staging copy: the HTML the production server sends is what crawlers get.
- Run it again after every framework upgrade or migration; a rendering setting can flip without anyone noticing.
- After a fix ships, use Test live URL in Search Console's URL Inspection to ask Google to look again.
