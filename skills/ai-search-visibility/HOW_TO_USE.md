# How to Use This Skill

Hey Claude, I just added the "ai-search-visibility" skill. Check how visible my site is in AI search and tell me what to do to get cited more.

## What you need

- **The InsightfulPipe MCP connected to Claude.** The skill pulls the data itself; you don't need to export anything. It uses whichever of these you have connected:
  - Google Analytics (GA4) for AI assistant referrals
  - Google Search Console for question and zero-click queries
  - Bing Webmaster Tools (optional) for Bing questions
  - DataForSEO for mentions in Google AI Overviews and ChatGPT
  - the crawler for robots.txt, llms.txt and structured data
- **2 to 5 competitor domains,** if you know them. Without them, the skill suggests the sites that outrank you.
- **3 questions you most want to be the answer to.** Without them, it picks your top question queries from Search Console.

## Example requests

**Full check**
Hey Claude, I just added the "ai-search-visibility" skill. Run a full AI search visibility check on my site. My competitors are competitor-a.com and competitor-b.com.

**Share of voice**
Hey Claude, I just added the "ai-search-visibility" skill. How often do ChatGPT and Google AI Overviews mention us compared with our three biggest competitors?

**AI referral traffic**
Hey Claude, I just added the "ai-search-visibility" skill. How much traffic do we get from ChatGPT, Perplexity, Claude and Gemini, and which pages do they send people to?

**FAQ from real questions**
Hey Claude, I just added the "ai-search-visibility" skill. Find the questions people search for that we almost rank for, and draft an FAQ section for each page.

**Crawler readiness**
Hey Claude, I just added the "ai-search-visibility" skill. Check whether AI crawlers can read our site, and whether our llms.txt and schema are set up.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for six areas:** measurement and AI referrals, answer coverage, zero-click queries, share of voice in AI answers, AI Overviews and ChatGPT on your priority questions, and AI crawler readiness.
3. **A share of voice table** for you and your competitors.
4. **The top 5 actions,** each with the numbers behind it and the page or query it targets.
5. **An FAQ draft** built from questions people really asked, with the page each one belongs on.
6. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes, it can ask Bing to recrawl the pages you just updated. Everything else, like answers, FAQ blocks, schema and robots.txt, is a change to your website: it drafts those for you to publish.

## Tips

- It makes 7 paid DataForSEO calls per run, plus one for each extra question you add. Competitors share one call (up to 10 domains in all), so they add none. It asks before adding either.
- AI answers change from run to run. Run it monthly, or 4 to 6 weeks after you publish changes, and compare.
- If GA4 shows far fewer Google visits than Search Console clicks, fix tracking first. Until then, AI referral numbers are a floor.
