# How to Use This Skill

Hey Claude, I just added the "seo-blog-writer" skill. Find the best blog post opportunity in my Search Console and write the draft.

## What you need

- **The InsightfulPipe MCP connected to Claude, with Google Search Console and DataForSEO added.** The skill pulls the data itself; you don't need to export anything.
- **WordPress (optional),** if you want the draft saved there as a draft. This step is untested until a WordPress site is connected.
- **A web fetch tool in your client (recommended),** so the skill can read your sitemap's URLs. It costs no DataForSEO call. Without one, the skill matches against the pages in your Search Console data and marks each opportunity unconfirmed.
- **Your brand terms,** if they aren't obvious from your site name.
- **Nothing connected?** Paste a keyword and the results you see for a new post, or paste a page, your questions and the AI answers you see (with their links) for a rework.

## Example requests

**From Search Console**
Hey Claude, I just added the "seo-blog-writer" skill. Find a query cluster in my Search Console that has impressions but no page of its own, and write the post.

**Best-of roundup**
Hey Claude, I just added the "seo-blog-writer" skill. Write a "best project management tools" roundup for our blog. We make one of the options.

**X vs Y comparison**
Hey Claude, I just added the "seo-blog-writer" skill. Write a comparison page for "Asana vs Trello" with facts from each vendor's own pages.

**Alternatives page**
Hey Claude, I just added the "seo-blog-writer" skill. Write an alternatives page for people leaving Mailchimp.

**Headlines only**
Hey Claude, I just added the "seo-blog-writer" skill. Give me 6 title options, a meta description and a slug for "standing desk for small spaces".

**Answer-first rewrite**
Hey Claude, I just added the "seo-blog-writer" skill. Rewrite https://example.com/blog/my-post so every section answers its heading first.

**AI answer page optimizer**
Hey Claude, I just added the "seo-blog-writer" skill. Optimize https://example.com/blog/my-guide for AI Overviews and ChatGPT: find the questions it should answer, check which pages the AI answers cite today, and show me a section-by-section before and after.

## What you get

1. **The opportunity:** your top query clusters with impressions, clicks and position, and which ones need a new post rather than a refresh.
2. **The target keyword,** with its volume next to your own impressions.
3. **A SERP snapshot** and the format the query asks for.
4. **The options to cover** and a facts table, every fact sourced from the product's own page.
5. **Six headline options** with checks, plus the meta description, H1 and slug.
6. **The draft in Markdown,** answer first, with an FAQ and dated sources.
7. **A self-check** of the draft against every rule, and the internal links to add.

For a page rework you get the page's questions, a citation snapshot (which pages AI Overviews, ChatGPT and Perplexity cite today), a question-to-section map, a section-by-section before and after with every unsourced figure marked, a markup draft that matches the visible text, and a recheck date 4 to 6 weeks out.

## What it can change for you

With your yes on the exact payload, it can save the draft to WordPress as a draft. A reworked page is saved as a new draft; the live post is never changed. It never publishes or schedules a post.

## Tips

- Add your own first-hand evidence where the draft says `[ADD: ...]`. That's what makes a roundup worth ranking.
- If the skill finds that a page already covers the cluster, refresh that page instead of writing a second one.
- About 10 DataForSEO calls per post. The skill asks before going past 12.
