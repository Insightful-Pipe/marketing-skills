# How to Use This Skill

Hey Claude, I just added the "on-page-seo-optimizer" skill. Optimize this page for its target keyword and give me every edit as before and after text.

## What you need

- **The target query,** one per run, in the words people type.
- **The page:** a live URL, or the draft pasted as HTML, Markdown or text.
- **Best with the InsightfulPipe MCP connected,** with DataForSEO (to read the live top 10), Google Search Console (for the page's own queries and your link sources) and the crawler (to read your page). Add WordPress if you want the approved edits pushed for you.
- **Without any connection,** it still works: paste the page or draft, and Claude reads the top 10 with its own web search or from URLs you paste. Paste a Search Console Queries export for the page if you have one.

## Example requests

**A live page**
Hey Claude, I just added the "on-page-seo-optimizer" skill. Optimize https://www.example.com/blog/reduce-no-shows/ for "how to reduce no-shows". Keep the numbered tactics.

**A draft before it goes live**
Hey Claude, I just added the "on-page-seo-optimizer" skill. Here's a draft for "salon cancellation policy". Check it against what ranks today before I publish.

**A page that slipped**
Hey Claude, I just added the "on-page-seo-optimizer" skill. Our pricing guide dropped to page two for "booking software pricing". What does the top 10 have that we don't?

**Optimize, then push**
Hey Claude, I just added the "on-page-seo-optimizer" skill. Optimize our deposits post for "no-show deposit", show me the edits, then apply the ones I approve in WordPress.

## What you get

1. **A two-line verdict:** does the page fit what Google ranks for the query, and how many of the must-cover subtopics it has.
2. **The top 10 as read today,** with each result's format and length, and which ones were dropped (videos, blocked forums) and why.
3. **What the ranking pages cover,** subtopic by subtopic, with how many pages cover each and whether yours does.
4. **Your page checked:** title, H1, intro, meta description, heading order, your own Search Console queries and whether each one is answered, links in and out, the terms most ranking pages use (as a range, never a target), images and markup.
5. **The edits, in order of impact,** each with the current text, the new text and the evidence.
6. **The WordPress payload,** ready and marked "not run", if WordPress is connected.

In the sample, a blog post for an invented booking software company fit the intent but lacked 4 of 9 must-cover subtopics, used the target phrase more often than any ranking page, and had a title tag without the query's main words. The run produced 17 edits.

## What it can change for you

With your yes on the exact edits, on a WordPress site it can:
- apply the body edits to the post or page (new sections, intro, headings, links, alt text)
- add a link to the page from other posts or pages, once you approve the sentence
- change the title tag and meta description, only when your SEO plugin exposes those fields

It never changes a URL, a slug, a publish date or a post's status. On other sites, you get the text to paste.

## Tips

- Run it on the page that already gets impressions for the query. If a second page of your site gets a large share, sort that out first.
- Fill the `[your number]` placeholders with your own figures before you publish. The skill never invents a statistic.
- Run it again a few weeks after the edits go live, against a fresh top 10.
