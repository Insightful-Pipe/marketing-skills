# How to Use This Skill

Hey Claude, I just added the "programmatic-seo" skill. We make an invoicing app for small service businesses. Should we build "[trade] invoice template" pages for our 40 trades, which ones first, and what should the template look like?

## What you need

- **The InsightfulPipe MCP connected to Claude, with DataForSEO added.** The skill pulls keyword volumes, SERPs, competitor folders and competitor pages itself; you don't need to export anything.
- **Search Console for your site** (optional), so the skill can see pages and queries you already have for the pattern, and check whether launched pages are indexed.
- **The head term and your list of variables** (cities, trades, tools, competitors). No list? The skill finds the variables people search.
- **What data you own per variable.** This decides whether the pages can be different from each other, so the skill will ask.

## Example requests

**Validate a pattern before building**
Hey Claude, I just added the "programmatic-seo" skill. We run a coworking marketplace. Is "coworking space in [city]" worth building for our 60 cities?

**Find the pattern**
Hey Claude, I just added the "programmatic-seo" skill. Our head term is "employee onboarding checklist". Which modifiers do people search, and which one should become a set of pages?

**Comparison or alternatives pages**
Hey Claude, I just added the "programmatic-seo" skill. Should we build "[competitor] alternatives" pages for the 12 tools we compete with? Show me who ranks now.

**Pages that don't rank or index**
Hey Claude, I just added the "programmatic-seo" skill. Our /integrations/ pages get almost no impressions. Check them in Search Console and tell me what's wrong with the template.

## What you get

1. **A verdict:** build, fix first or don't build, with five checks (demand, SERP openness, data per page, template uniqueness, business fit) and the number behind each.
2. **The pattern:** the modifier classes people search around your head term, and which one fits your data.
3. **Demand for every permutation:** total volume, the share of variables anyone searches, the CPC range, and phase 1, phase 2 and hold lists.
4. **The SERPs:** who ranks for the biggest variable, one from the lower half of phase 1 and one from phase 2, how many results are weak, where intent drifts, and the sub-modifiers and questions to cover.
5. **The incumbent teardown:** how many keywords its template folder ranks for, estimated traffic by page type, its page skeleton, and how much text its sibling pages share, which is the bar for yours.
6. **The page template:** URL, title, meta and H1 formulas, sections each tied to a data field, conditions, FAQ, internal links, structured data, a uniqueness target, an indexing plan, a data refresh plan, and the checks to run before you publish (unique titles and metas, one H1, self canonicals, robots.txt, noindex, sitemap).
7. **Your site** (with Search Console): existing pages and queries for the pattern, and the indexed share.
8. **Success metrics and risks:** an indexed-pages target, a 6-month traffic benchmark from the incumbent's pages, a conversion target if you give your conversion rate, and how the plan handles each risk.

## What it can change for you

With your yes, it can save the page matrix (one row per variable: keyword, volume, CPC, phase, URL, title) to a new tab in a connected Google Sheet. It never publishes pages or changes your site.

## Tips

- One run uses about 11 DataForSEO calls. The skill asks before going past 15.
- Give it your full variable list: the long tail is where you learn which pages not to build.
- After launch, ask it to check the folder in Search Console every week (impressions and crawl errors) and inspect the new URLs after 4 weeks.
- Running the pages as ad landing pages? Check that the call to action records a conversion, then A/B test where it sits.
