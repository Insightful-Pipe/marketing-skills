# How to Use This Skill

Hey Claude, I just added the "app-store-localization" skill. Which countries should we localize our app listing for next? Write the App Store and Google Play metadata for them.

## What you need

- **Your app's App Store ID or Google Play package name.** Either one is enough to start.
- **Your current listing,** including the App Store keyword field, which only you can see. Without it, the skill reads what the stores show and marks the keyword field unknown.
- **Which localizations the listing already has, and which languages the app itself is in.** The stores don't show either.
- **Users by country,** from GA4 through the InsightfulPipe MCP, or pasted from App Store Connect or Play Console. With the MCP connected, the skill also checks your rank and ratings in each country's store and pulls local search volume.

## Example requests

**Pick the next markets**
Hey Claude, I just added the "app-store-localization" skill. Rank which countries we should localize our App Store and Google Play listing for next, using our GA4 users by country. App Store ID 1234567890.

**Localize for one market**
Hey Claude, I just added the "app-store-localization" skill. We're launching in Germany. Research what Germans search for apps like ours and write the German App Store and Google Play listing. Here is our English listing and keyword field.

**Fix a literal translation**
Hey Claude, I just added the "app-store-localization" skill. An agency translated our listing into French and Spanish word for word. Check which of those keywords people actually search and rewrite both locales.

**Work from a paste only**
Hey Claude, I just added the "app-store-localization" skill. Here are our App Store Connect downloads by territory and our current listing. Tell us which three languages to add and draft them.

## What you get

1. **A market ranking:** each candidate country with its users, sign-up rate against your home market, ratings and rank in that store, how crowded its results are, and a tier: covered, localize next, app first or later.
2. **A keyword table per locale:** literal translations, native phrasings, English loanwords and words rival apps use, with the evidence for each and literal terms nobody searches flagged.
3. **Ready-to-paste metadata** for the App Store and Google Play in each locale, every field counted against its limit, with an English back-translation of each line.
4. **An extra localization plan** for the additional languages Apple lists in some storefronts.
5. **A rank baseline** to check again 2 to 4 weeks after release.

## What it can change for you

Nothing. The store connections are read-only. You paste the drafts into App Store Connect and Play Console.

## Tips

- Ask a native speaker to read every visible line before release; the report lists the lines that are judgement calls.
- Add three locales per release at most, so you can keep screenshots, release notes and review replies current in each.
- Run the rank check again after the new listing has been live for a few weeks.
