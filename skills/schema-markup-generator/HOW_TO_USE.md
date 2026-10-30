# How to use Schema Markup Generator

Hey Claude, I just added the "schema-markup-generator" skill. Audit the structured data on my site, tell me which rich results we earn, and write the JSON-LD we're missing.

## What you need

- For the full audit: the InsightfulPipe MCP with Google Search Console connected for your site.
- Optional: the Web Crawler server, to read the markup on each page. If it can't read your pages, Claude says so and uses the page source instead. You can also paste the source.
- Optional: Bing Webmaster, so Claude can ask Bing to recrawl the pages once the new markup is live.
- For video pages: the Video indexing report from Search Console (Indexing, then Video pages), pasted or exported. YouTube helps Claude read each video's real length, date and chapters.
- For location pages: Google Business Profile, so the markup matches each profile. Without it, paste each location's address, phone and hours.
- No connection at all? Paste the page source and Claude writes the markup from that.

## Other ways to ask

- "Which rich results does my site get in Google, and on which pages?"
- "Why don't my product pages show prices or stars in search results?"
- "Write Organization and Breadcrumb schema for my home page and pricing page."
- "Check the schema on this blog post and fix the author markup."
- "Do I get product snippets or merchant listings? Which pages?"
- Video pages: "Search Console says my videos aren't indexed. Here's the Video indexing report; fix the video SEO on these pages and write the VideoObject markup with key moments."
- Location pages: "Write LocalBusiness schema for our 6 location pages and check it matches our Google Business Profiles."

## What you get

1. The rich results your site earned in the last 28 days, from Search Console.
2. A table of your page types: what Google detected, what markup each page has, and a status for each rich result on each page.
3. The top fixes, ranked by the search impressions at stake, each with a JSON-LD block ready to paste.
4. A short list of markup that isn't worth adding, and why.
5. Anything that couldn't be checked, and why.

In video mode you get the pages that earn video results, a fix for each reason in your Video indexing report, and a VideoObject block (with key moments when your player supports them) plus video sitemap entries. In location mode you get a field-by-field comparison of each location page against its Business Profile and one LocalBusiness block per location.

## What it can change for you

It can't edit your site. You or your developer paste the markup. Once it's live, and only with your yes on the exact URLs, it can ask Bing to recrawl those pages.

## Tips

- Tell Claude about real ratings, reviews or prices you want in the markup. It never makes them up.
- Test each block in Google's Rich Results Test before it goes live.
- Run it again a week or two after deploying to see whether Google picked up the new markup.
