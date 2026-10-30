# How to Use This Skill

Hey Claude, I just added the "app-store-conversion-analyst" skill. Here are my App Store Connect and Play Console exports for the last two months. Did our store conversion really drop, how many installs are paid, and what should we fix first?

## What you need

- **Your store exports.** From App Store Connect (Analytics, Acquisition): impressions, product page views and downloads by source type, and by territory for App Store search and browse. From Play Console (the store listings acquisition report): store listing visitors and acquisitions by traffic source, and by country for Google Play search. One store is enough. A pasted table or a screenshot works.
- **Two periods of the same length.** Without dates, the skill uses the last 28 complete days and the 28 days before.
- **What changed on the listing,** with dates: a new icon or screenshots, a title or subtitle change, a feature, a big release. "Nothing" is a fine answer.
- **Optional: the InsightfulPipe MCP connected to Claude.** With Google Ads, Meta, TikTok or Snapchat added, the skill pulls your app-campaign installs itself. With the App Store and Google Play servers, it reads your listing and up to 3 rivals. Apple Ads and AppLovin installs always come from an export or your numbers.

## Example requests

**Conversion dropped**
Hey Claude, I just added the "app-store-conversion-analyst" skill. Our App Store conversion rate fell from 10% to 8% this month. Here's the App Store Connect sources export for both months. Is the listing broken, or did our traffic change?

**Paid vs organic**
Hey Claude, I just added the "app-store-conversion-analyst" skill. How many of last month's Android installs were organic? Pull our Google Ads, Meta and TikTok app campaigns and compare them with this Play Console export.

**Which country to fix**
Hey Claude, I just added the "app-store-conversion-analyst" skill. Here are our App Store and Play conversion numbers by country. Which market converts worst for a reason we can fix, and what do the rival listings there do differently?

**After a listing change**
Hey Claude, I just added the "app-store-conversion-analyst" skill. We shipped new screenshots on Google Play on the 6th. Here are the store listing exports for the 28 days before and after. Did they hurt conversion?

## What you get

1. **The answer in three lines:** per store, whether conversion really changed or the traffic mix just shifted; the share of installs that is surely organic; the top fix.
2. **Conversion by source** for each store, previous and current, with a test that marks each change as real or noise.
3. **The mix and rate split:** how much of the blended change came from traffic moving between sources, and how much from sources converting differently.
4. **Paid vs organic installs,** with each network's claim placed in the store bucket where its installs land, and any network that claims more installs than the store recorded.
5. **Countries that convert below the rest,** with installs at stake, and rival listing differences only where they line up with a measured gap.
6. **Fixes ranked by installs at stake,** each tied to a listing element and the test to run before rolling it out.

## What it changes

Nothing. It reads your exports, your ad reports and public store listings. You make listing changes in App Store Connect or Play Console.

## Tips

- Export the same metrics in both periods: unique impressions and the same download metric (total or first-time).
- Give the dates of features and listing changes. A drop that starts with a change is a strong lead.
- Run it again 28 days after a fix, with the new period against the one before it.
