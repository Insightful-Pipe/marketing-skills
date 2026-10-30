# How to Use This Skill

Hey Claude, I just added the "seo-content-planner" skill. Build a 12-week content plan for my site: what to write, what to upgrade and what to prune.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Search Console property added.** The skill pulls your queries, pages and sitemap itself.
- **DataForSEO, for the full plan.** It adds competitor topic gaps, search volumes and SERP checks, in about 6 calls a run.
- **GA4 and the crawler, if you have them.** GA4 protects pages that drive key events, and the crawler checks moved or broken URLs.
- **For a content audit, WordPress or your sitemap.** Connected WordPress gives every post with its dates, author, categories and text. Without it, the sitemap or a pasted crawl export works. DataForSEO adds referring domains per URL.
- **For content from customer conversations, the conversations.** Paste or upload call notes or transcripts, ticket or chat exports, reviews or lost-deal notes. Search Console, Bing Webmaster and DataForSEO add search demand when connected.
- **A few answers, if you know them:** what your site sells, your brand terms, one or two competitors, and how many pieces a week you can publish. Without them, the skill proposes defaults and asks you to confirm.

## Example requests

**A full content plan**
Hey Claude, I just added the "seo-content-planner" skill. Build a 12-week SEO content plan for example.com. We can publish two pieces a week.

**Content ideas from your own data**
Hey Claude, I just added the "seo-content-planner" skill. Find the queries we get impressions for but have no page for, and turn them into content ideas.

**Pillars and topical authority**
Hey Claude, I just added the "seo-content-planner" skill. Map our content pillars and show which topics we cover, which are weak and which are missing.

**Glossary pages**
Hey Claude, I just added the "seo-content-planner" skill. Which terms deserve a glossary or definition page on our site?

**Contrarian angles**
Hey Claude, I just added the "seo-content-planner" skill. Give me contrarian content ideas for our main topics, backed by our own numbers.

**Pruning**
Hey Claude, I just added the "seo-content-planner" skill. Which pages should we keep, refresh, merge or prune?

**Content audit**
Hey Claude, I just added the "seo-content-planner" skill. Run a content audit of our blog: list every post with its clicks, conversions and links over the last 12 months, and tell me which to keep, update, merge, redirect or remove.

**Content from customer conversations**
Hey Claude, I just added the "seo-content-planner" skill. Here are 40 sales call notes and last quarter's support tickets. Turn the questions buyers ask before they decide into a ranked list of pages and sections we're missing.

## What you get

1. **A plan summary:** the goal, the pillars, the cadence and how success is measured.
2. **A topical map:** each pillar's pages, clicks and impressions, and its covered, weak and missing topics.
3. **Week-1 fixes:** broken pages that still get impressions, and page sets Google is ignoring.
4. **A ranked new-page list,** from your own Search Console, competitor gaps and glossary terms, each with its demand, intent, difficulty and the page it links to.
5. **A ranked upgrade list:** existing pages to expand or refresh, with the queries behind each.
6. **A glossary plan,** and **contrarian angles** that each cite the SERP consensus and your own evidence.
7. **A pruning plan:** every content page sorted into keep, refresh, merge or inspect, with Google's indexing verdict where it was checked.
8. **A 12-week calendar** with a new-page slot and an upgrade slot each week.
9. **On request, a content audit:** one row per article with its facts, 12 months of clicks, key events, engagement and referring domains, freshness flags, and a keep, update, merge, redirect or remove verdict with its reason.
10. **On request, buyer questions turned into content:** each question in the buyer's words, how many buyers asked it, its search demand, whether a page already answers it, and the page or section to build.

## What it can change for you

With your yes on the exact change, it can save the plan or the audit to a new tab in a Google Sheet, and, on WordPress, change a post's title, excerpt, categories or tags. It never publishes, redirects, noindexes or deletes pages; it tells you which ones to change.

## Tips

- Run it once a quarter. The windows are the last 90 days and the 6 months before.
- Confirm the pillars and the off-product topics early. They decide what counts as a gap.
- Brief each new page with the `content-brief-writer` skill if you have it.
