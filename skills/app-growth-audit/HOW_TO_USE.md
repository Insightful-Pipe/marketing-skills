# How to Use This Skill

Hey Claude, I just added the "app-growth-audit" skill. Audit my app on the App Store and Google Play against my top three competitors and tell me the five things that would grow installs most.

## What you need

- **The InsightfulPipe MCP connected to Claude.** The App Store and Google Play data is public, so you don't need a store login and you don't export anything.
- **Your app:** a store link, the Google Play package name, the Apple ID, or just the name.
- **Up to three competitors and up to eight keywords,** if you have them. Without them, the skill picks competitors from the store search and keywords from your title and category.
- **Optional:** your Google Ads, Meta and GA4 accounts connected, to add App campaigns, cost per install and the Android and iOS split.
- **For the listing writer:** your App Store subtitle, keyword field and promotional text (they aren't public), plus a Play Console search-term report or an Apple Ads search-terms export if you have one. It also works with nothing connected, from what you paste.

## Example requests

**Full audit**
Hey Claude, I just added the "app-growth-audit" skill. Audit Spotify on both stores against YouTube Music, Amazon Music and Pandora. Check the keywords music, podcasts, offline music and audiobooks.

**Keyword research**
Hey Claude, I just added the "app-growth-audit" skill. Where does my app rank in App Store and Google Play search for these six keywords, and which words do the top apps use in their titles that I don't?

**Did the release hurt us?**
Hey Claude, I just added the "app-growth-audit" skill. We shipped a new version last week. Compare its review ratings with the version before on both stores.

**What users ask for**
Hey Claude, I just added the "app-growth-audit" skill. Read our newest reviews and list the bugs and feature requests by how often they come up.

**Write my listing (ASO keyword and metadata writer)**
Hey Claude, I just added the "app-growth-audit" skill. Find the App Store and Google Play keywords my habit tracker can realistically win, pick the right categories, and rewrite my name, subtitle, keyword field, title and short and full description within the limits. Here is my current subtitle and keyword field, and our Apple Ads search terms export.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for six areas:** listing metadata, ratings health, release impact, review themes, keyword visibility, and paid and analytics.
3. **The top 5 actions,** each with the numbers behind it and who should do it.
4. **A review theme table:** the bugs and complaints in your 1-3 star reviews, plus the feature requests from reviews at any rating, counted and described in plain words. No review is quoted and no reviewer is named.
5. **A keyword table:** your rank and your competitors' on each store, plus the words competitors use in their titles that you don't.
6. **A competitor table,** and a list of what couldn't be checked and why.

From the listing writer you get:
1. **A term table:** each candidate's rank in both stores, the direct rivals and their ratings in the top 10, and a score built from relevance, winnability and demand, with the reason for each number.
2. **A category pick:** the App Store primary and secondary category and the Google Play category, with the counts behind them.
3. **The new listing:** App Store name, subtitle, keyword field and promotional text, and Google Play title, short and full description. Each field shows its character count against the limit, and the keyword field shows the repeated words it dropped.
4. **A rerun after the release,** showing which terms moved up, moved down or entered the top 10.

## What it can do for you

The store data is read only, so the skill changes nothing. When you ask, it drafts:
- the full store listing, in the listing writer mode
- release notes that name what changed
- replies to each review theme, for you to post

## Tips

- Run it after each major release, and again a week later when more reviews are in.
- App Store reviews have no dates in the feed, so the skill compares versions instead of weeks.
- For a big app, the newest 200 Google Play reviews can cover only a few hours. The report shows the window.
- Search volume is a Google web proxy. App stores don't publish their own, so use it to rank keywords against each other. An Apple Ads or Play Console search-term file gives a better signal for that store.
- After a listing change, wait at least a week before the rerun, and change fields again only after a second rerun agrees.
