# How to Use This Skill

Hey Claude, I just added the "google-ads-bulk-updater" skill. Our tune-up price goes from $89 to $99. Find every place it appears in my Google Ads account and show me the before-and-after sheet.

## What you need

- **Your change list,** in plain words: the old and new text, price or phone number, a map of old URLs to new ones, or the new tracking template or final URL suffix.
- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added,** for the live run. Add the crawler server and every new URL gets a status check before it goes into an ad.
- **No connection?** Export the account (or the campaigns in scope) from Google Ads Editor as a CSV and paste or upload it. The skill runs every step on the file and lists the new URLs for you to open.

## Example requests

**Price or offer change**
Hey Claude, I just added the "google-ads-bulk-updater" skill. Our tune-up price goes from $89 to $99 on November 1. Update it in every ad, sitelink, callout and price asset, paused ads included.

**Site move**
Hey Claude, I just added the "google-ads-bulk-updater" skill. We moved our site. Here is the old-to-new URL map. Change the final URLs in bulk across ads, keywords, sitelinks and Performance Max, and check every new page loads first.

**New phone number**
Hey Claude, I just added the "google-ads-bulk-updater" skill. Our main line changed from (303) 555-0142 to (303) 555-0187. Find it everywhere in the account.

**New tracking template**
Hey Claude, I just added the "google-ads-bulk-updater" skill. Set this as the account tracking template and tell me which campaigns, ad groups, ads or keywords override it.

**From a Google Ads Editor export**
Hey Claude, I just added the "google-ads-bulk-updater" skill. Here is my Google Ads Editor CSV. Find and replace "2025" with "2026" everywhere and give me the rows to import back into Editor.

## What you get

1. **Urgent items first:** live ads, keywords or sitelinks that already land on an error page.
2. **A URL check:** each old and new URL with its status and redirect chain, and whether it's safe to use.
3. **The before-and-after sheet:** one row per edit with the place, the old and new text or URL, the length against Google's limit, the checks, how the edit is made and what it does to review and history.
4. **Near misses** the strict matching skipped (a `$89` rule never touches `$899`), and assets that aren't linked anywhere.
5. **The payloads:** the exact connector calls and the Google Ads Editor import rows, with old values in `#Original` columns so Editor edits your existing ads and assets instead of making new ones.

## What it can change for you

Nothing until you say yes to the exact payloads. Then it can update responsive search ad text and final URLs, campaign and ad group tracking templates and final URL suffixes, and Performance Max landing pages, and write the sheet to a new tab in Google Sheets. It reads every changed item back afterwards to show it worked.

Ads with pinned lines, keyword URLs and assets go through the Editor import: the connector can't keep pins, and it has no action that edits a keyword's URL or an existing asset. It never pauses, enables or removes anything, and never touches bids or budgets.

## Tips

- Say yes to paused ads too. A paused ad with the old price comes back with it the day someone turns it on.
- Every ad you edit goes back to Google's review for up to a business day. Campaign and ad group tracking changes don't.
- Run it again once a held page is live: the held rows are swapped then.
- After the change, check the landing pages show the same price as the ads. The crawler checks a page loads, not what it says.
