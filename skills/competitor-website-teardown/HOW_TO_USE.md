# How to Use This Skill

Hey Claude, I just added the "competitor-website-teardown" skill. Tear down my two main competitors' websites against mine and tell me the five moves worth copying.

## What you need

- **The InsightfulPipe MCP connected to Claude,** with the DataForSEO, PageSpeed Insights and Crawler sources, plus YouTube for the channel benchmark. The skill reads the sites itself; you don't need to export anything.
- **Your domain and one to four competitor domains.**
- **YouTube channel IDs** (they start with `UC`), if you want channels compared. A handle like `@brand` won't work. You'll find the ID on the channel's About panel under "Share channel", "Copy channel ID".
- **Pricing page URLs,** if they aren't at `/pricing`.

## Example requests

**Full teardown**
Hey Claude, I just added the "competitor-website-teardown" skill. Compare competitor-a.com and competitor-b.com with mysite.com: structure, pricing pages, speed and YouTube.

**Pricing pages only**
Hey Claude, I just added the "competitor-website-teardown" skill. Compare our pricing page with these three competitors' pricing pages and tell me what they have that we don't.

**Speed benchmark**
Hey Claude, I just added the "competitor-website-teardown" skill. Benchmark mobile speed on our home and pricing pages against competitor-a.com and competitor-b.com.

**Where their traffic comes from**
Hey Claude, I just added the "competitor-website-teardown" skill. Which kinds of pages bring competitor-a.com its search traffic, and which of those are we missing?

**YouTube benchmark**
Hey Claude, I just added the "competitor-website-teardown" skill. Compare our YouTube channel with this competitor's. Our channel ID is UC... and theirs is UC...

## What you get

1. **A scoreboard** naming the leader in five areas: search footprint, structure, pricing page, speed and YouTube.
2. **Search footprint:** estimated monthly organic visits, ranking keywords and paid visits for each site.
3. **Structure:** each site's ranking pages grouped by type (blog, integration pages, best-of lists, templates, free tools and more), with the gaps you have and the types where you're far behind.
4. **Home page positioning:** title, headline, length and which sections each home page has.
5. **Pricing pages side by side:** plans, entry price, what the price scales with, discounts, how you can start, done-for-you tiers, comparison tables, FAQs and cost anchors.
6. **Mobile speed** on each home and pricing page, rated good, needs improvement or poor.
7. **YouTube:** subscribers, uploads per week and median views per video.
8. **The top 5 moves,** each with the numbers behind it and the competitor pages to study.
9. **A list of what couldn't be measured,** and why.

## Good to know

- It only reads. It never changes your site, your channel or any account.
- Traffic numbers are DataForSEO estimates for US Google searches, not your analytics.
- A run makes about 10 DataForSEO calls for three sites (1 + 3 per site), plus a retry for a pricing page whose prices load by JavaScript.
- Speed numbers come from single mobile lab runs, so small differences are called a tie.

## Tips

- Run it quarterly, and after a competitor relaunches its site or changes its pricing.
- Pair it with the pricing page auditor to rewrite your own pricing page once you've seen theirs.
