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
- **For the brand accuracy check:** your pricing, product and about pages (it reads them and asks you to confirm the facts), two rivals and your main use case. Nothing connected? Paste the answers you got from ChatGPT, Gemini, Claude or Perplexity.
- **For prompt research:** two seed terms, and any questions your sales or support team hears. Nothing connected? Paste the questions or describe the product.

## Example requests

**Full check**
Hey Claude, I just added the "ai-search-visibility" skill. Run a full AI search visibility check on my site. My competitors are competitor-a.example and competitor-b.example.

**Share of voice**
Hey Claude, I just added the "ai-search-visibility" skill. How often do ChatGPT and Google AI Overviews mention us compared with our three biggest competitors?

**AI referral traffic**
Hey Claude, I just added the "ai-search-visibility" skill. How much traffic do we get from ChatGPT, Perplexity, Claude and Gemini, and which pages do they send people to?

**FAQ from real questions**
Hey Claude, I just added the "ai-search-visibility" skill. Find the questions people search for that we almost rank for, and draft an FAQ section for each page.

**AI brand monitoring: is what ChatGPT says about us right?**
Hey Claude, I just added the "ai-search-visibility" skill. Check what ChatGPT, Gemini, Claude, Perplexity and Google AI Overviews say about our brand, flag anything wrong or out of date against our own pages, and tell me where to fix each one.

**Prompt research: which prompts should we track?**
Hey Claude, I just added the "ai-search-visibility" skill. Build a list of the prompts we should track in AI search, sized with AI search volume and tagged by funnel stage. Here are the questions our sales team hears most: ...

**Crawler readiness**
Hey Claude, I just added the "ai-search-visibility" skill. Check whether AI crawlers can read our site, and whether our llms.txt and schema are set up.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for six areas:** measurement and AI referrals, answer coverage, zero-click queries, share of voice in AI answers, AI Overviews and ChatGPT on your priority questions, and AI crawler readiness.
3. **A share of voice table** for you and your competitors.
4. **The top 5 actions,** each with the numbers behind it and the page or query it targets.
5. **An FAQ draft** built from questions people really asked, with the page each one belongs on.
6. **A list of what couldn't be checked,** and why.

The brand accuracy check gives you instead: the fact sheet it judged against, accuracy by engine, every wrong, outdated or missing claim with its likely source, a correction plan (which page, markup field or listing to fix) and a rerun date. Prompt research gives you a list of 30 to 100 prompts, each with its source, AI search volume, funnel stage, persona and intent, the reason it's in, and which brands showed up in a live sample.

## What it can change for you

With your yes, it can ask Bing to recrawl the pages you just updated, and save the accuracy run log or the prompt list to a new tab in a Google Sheet. Everything else, like answers, FAQ blocks, schema and robots.txt, is a change to your website: it drafts those for you to publish.

## Tips

- The full check makes 7 paid DataForSEO calls per run, plus one for each extra question you add. Competitors share one call (up to 10 domains in all), so they add none. It asks before adding either.
- The brand accuracy check makes 10 paid calls (two prompts to each of four assistants, plus stored and current AI Overview answers), and prompt research makes 8.
- Answers pulled through the API can differ from what you see in the ChatGPT or Gemini app, which knows your account and location. Before acting on a harmful claim, check it in the app too.
- AI answers change from run to run. Run it monthly, or 4 to 6 weeks after you publish changes, and compare.
- If GA4 shows far fewer Google visits than Search Console clicks, fix tracking first. Until then, AI referral numbers are a floor.
