# How to Use This Skill

Hey Claude, I just added the "search-term-gold-miner" skill. Mine my Google Ads search terms from the last 30 days: what should I block, which terms should become exact keywords, and what should I expand into?

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the search terms, your keywords and every negative list itself; you don't export anything.
- **Your target CPA or ROAS,** if you have one. Without it, the skill uses your own non-brand CPA for the last 30 days.
- **Your brand terms and any competitor names you bid on,** if they aren't obvious from your account name.

No connection yet? Paste a search terms export (term, campaign, ad group, match type, clicks, cost, conversions) and the skill applies the same rules. It marks the checks it can't run without the account as unknown.

## Example requests

**Full mining run**
Hey Claude, I just added the "search-term-gold-miner" skill. Review my last 30 days of search terms and tell me what to negate and what to promote. My target CPA is $45.

**Quick waste hunt**
Hey Claude, I just added the "search-term-gold-miner" skill. Find the search terms wasting money that I can safely block today, and give me a copy-paste negative list.

**N-gram analysis**
Hey Claude, I just added the "search-term-gold-miner" skill. Break my search terms into one, two and three-word phrases and show me which phrases convert and which only spend.

**Keyword expansion**
Hey Claude, I just added the "search-term-gold-miner" skill. Find converting search terms that aren't keywords yet, add them as exact match once I confirm, and suggest new keywords based on what already converts.

## What you get

1. **A health light,** your visible share of search spend, and the money going to terms with no conversions.
2. **Negatives to add today:** exact-match terms and phrase-match patterns, each checked against your 90-day conversions, your own keywords and the negatives you already have, plus a copy-paste list.
3. **"Considered, not negated":** costly terms the skill held back on purpose, and why.
4. **Keywords to promote:** converting terms to add as exact match, with the ad group each one belongs in.
5. **Ad group themes and new keyword ideas** from Keyword Planner, filtered against what you already run.
6. **A watchlist** with a review date, plus n-gram, long-tail, hidden-traffic and competitor-search tables.
7. **Ready payloads** for the keywords and negatives. The skill runs them only after you say yes.

## Tips

- Run it monthly, and again two weeks later for the watchlist.
- Give it your real target CPA. The waste scores and the promotion rule scale with it.
- If you bid on competitor names on purpose, say so. The skill never blocks or promotes them without asking.
