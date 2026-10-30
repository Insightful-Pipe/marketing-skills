# How to Use This Skill

Hey Claude, I just added the "keyword-cannibalization-fixer" skill. Find the pages on my site that compete for the same Google queries and tell me how to fix each one.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Search Console property added.** The skill pulls the query and page data itself; you don't need to export anything.
- **Your brand terms,** if they aren't obvious from your domain. Brand searches often show several of your pages at once, and that's fine, so they're left out.
- **Pages that must keep their URL,** if any, such as a page you send paid traffic to.
- Optional: DataForSEO, to check what the US results page shows today, and GA4, to break ties with conversions.

## Example requests

**Find cannibalization**
Hey Claude, I just added the "keyword-cannibalization-fixer" skill. Which of my pages are competing for the same queries in Search Console?

**Wrong page ranking**
Hey Claude, I just added the "keyword-cannibalization-fixer" skill. Google keeps ranking my blog post instead of my product page for our main keyword. Find out why and tell me what to change.

**Query-to-page map**
Hey Claude, I just added the "keyword-cannibalization-fixer" skill. Build me a map of my top 25 queries and the one page that should own each, so new content doesn't overlap.

**Check past fixes**
Hey Claude, I just added the "keyword-cannibalization-fixer" skill. We redirected some old posts last month. Check whether Google has picked up the redirects and whether anything is still split.

## What you get

1. **A header** with the dates, the share of clicks Google shows queries for, and a count of conflicts by status.
2. **A fix list:** each open conflict, with the page that should own it, why, and the exact change (a redirect, a new title or a link), plus the internal links to update.
3. **What's already handled:** redirects that are live, and whether Google has caught up.
4. **A query-to-page map** for your top 25 queries.
5. **Unfocused pages:** pages pulling in lots of unrelated queries, if any.
6. **Unknowns:** anything that couldn't be checked, and why.

## What it can change for you

Nothing on its own. Search Console can't change your site, so you make the redirects, title changes and links in your CMS. The skill gives you each change ready to copy.

## Tips

- Run it again 2–4 weeks after you ship the fixes, to see the pairs move to fixed.
- Run it before you plan new content, and use the query-to-page map as the brief.
- On a big site, ask for one folder at a time (for example `/blog/`), so each pull stays under 25,000 rows.
