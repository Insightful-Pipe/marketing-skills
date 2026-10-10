# How to Use This Skill

Hey Claude, I just added the "negative-keyword-implementer" skill. Check my negatives for conflicts, build new ones from the last 30 days of search terms, and show me the plan before you add anything.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill reads your negatives, keywords and search terms itself; you don't need to export anything.
- **A Read & Write connection** if you want it to add the negatives. On a read-only connection it still runs every check and hands you the list.
- **Your target CPA,** if you have one. Without it, the skill uses your own 30-day average.
- **Anything it can't know:** competitor names you bid on deliberately, and services, places or languages you don't serve.

## Example requests

**Find conflicts**
Hey Claude, I just added the "negative-keyword-implementer" skill. Are any of my negative keywords blocking my own keywords?

**Negatives from search terms**
Hey Claude, I just added the "negative-keyword-implementer" skill. Go through the last 30 days of search terms, find what I should block, and show me the negatives with match types before adding them.

**Roll a list out**
Hey Claude, I just added the "negative-keyword-implementer" skill. Make sure every search campaign has our negative keyword list, and tell me if anything on it would block a keyword.

**Add a list you already have**
Hey Claude, I just added the "negative-keyword-implementer" skill. Add these as phrase negatives to my DUI campaign: jobs, salary, school. Check them first.

**After Search Term Gold Miner**
Hey Claude, I just added the "negative-keyword-implementer" skill. Take the negatives from the search term analysis above and add the safe ones.

## What you get

1. **Every negative already in force,** counted by campaign, ad group and shared list, and which campaigns each list covers.
2. **Conflicts:** negatives that block your own live keywords, with the fix. Deliberate routing between campaigns is counted separately, as information.
3. **New negatives,** each with its match type, level, reason, the search term behind it, the spend it would have blocked in 30 days, and the five safety checks it passed.
4. **What it left alone:** terms already covered, a watch list of relevant terms that spent more than your target CPA without converting, and questions only you can answer.
5. **Lists to campaigns:** which campaigns are missing a negative list, and which items would conflict there.
6. **The exact calls,** marked "not run" until you say yes.

## What it can change for you

With your yes on the exact list, it adds negatives with `add_negative_keywords`, one call per campaign or ad group per match type, then checks what landed. It never removes negatives and never touches bids, budgets or keywords. Linking a shared negative list is done by you in Google Ads; the skill tells you where.

## Tips

- Run it after every search-term review, and again 7 to 14 days later to confirm the blocked terms are gone.
- Don't block price, "near me" or "best" searches on spend alone. They are usually buyers; the skill keeps them, and lists them on the watch list only when they spend more than your target CPA without converting.
- Negatives don't cover plurals or synonyms. If the report shows both forms, block both.
