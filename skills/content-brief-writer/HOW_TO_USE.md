# How to Use This Skill

Hey Claude, I just added the "content-brief-writer" skill. Write a content brief for "how to write a press release" for my site.

## What you need

- **The InsightfulPipe MCP connected to Claude, with DataForSEO added.** The skill pulls the Google top 10, People Also Ask, related searches and keyword data itself.
- **Search Console for your site,** so the skill can tell you whether you already rank for the keyword and should refresh a page instead of writing a new one.
- **One target keyword,** and the market if it isn't the United States in English.

## Example requests

**A brief for a new article**
Hey Claude, I just added the "content-brief-writer" skill. Write a brief for "best standing desk" for the UK market.

**Refresh a page that isn't ranking**
Hey Claude, I just added the "content-brief-writer" skill. Our page for "sourdough starter" sits on page 4. Build a refresh brief from the current top 10.

**Harvest the questions**
Hey Claude, I just added the "content-brief-writer" skill. Pull every People Also Ask and question query for "how to start a podcast" and tell me which ones to answer.

**An outline only**
Hey Claude, I just added the "content-brief-writer" skill. Give me just the H2 and H3 outline for "cold brew ratio", with how many top-10 pages cover each section.

## What you get

1. **A verdict:** write a new page, or refresh the one you already have, and the format the top 10 rewards.
2. **A SERP snapshot:** the features on the page, the domains the AI overview cites, and related searches.
3. **A competitor table:** each top-10 page's type, word count and heading count.
4. **An outline:** title, meta description, H1, and the H2s with the H3s under each. Every H2 shows how many top-10 pages cover it.
5. **The questions to answer,** merged from People Also Ask, keyword suggestions, your Search Console queries and competitor headings, with duplicates dropped. Each shows its sources and where it goes: an H2, an H3 or an FAQ item.
6. **Secondary keywords** with volume, difficulty and the section each belongs in.
7. **The angle to win:** subtopics the top 10 barely covers, and the first-hand material to add.
8. **Internal links** from your own pages that already show up for the topic.

## What it changes

Nothing. It only reads, and it never publishes or edits a page.

## Tips

- Give it the exact phrase people search, not a topic. Run it once per keyword.
- It uses about 10 DataForSEO calls per brief (5 in the sample; about 10 on a day the crawler is down) and tries the free crawler first; blocked pages, forum threads and videos are never sent to the paid parser.
- Re-run it before a refresh: the top 10 changes, and so does the brief.
