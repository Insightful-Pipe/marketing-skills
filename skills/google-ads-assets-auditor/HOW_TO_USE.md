# How to Use This Skill

Hey Claude, I just added the "google-ads-assets-auditor" skill. Audit every asset in my Google Ads account and show me which campaigns have gaps and what is broken.

## What you need

- **Best: the InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill reads every asset at account, campaign and ad group level itself, with its approval status and its own results, and checks each sitelink URL with the site crawler.
- **No connection? Paste the assets report instead.** In Google Ads, open Campaigns > Assets, switch to the table view, set the last 30 days, add the Level, Source, Status reason and Final URL columns, and download it. Paste it or upload the CSV.
- **A few facts, if you have them:** whether you take calls, whether customers visit an address, and your current offers and prices. Without them, the skill uses only what your approved ads and assets already say.

## Example requests

**Full assets audit**
Hey Claude, I just added the "google-ads-assets-auditor" skill. Audit all my Google Ads extensions for the last 30 days and rank the fixes.

**Sitelinks only**
Hey Claude, I just added the "google-ads-assets-auditor" skill. Which of my campaigns are short on sitelinks, which sitelinks point at broken pages, and what should replace them?

**Clean-up after a season**
Hey Claude, I just added the "google-ads-assets-auditor" skill. Find every promotion, callout and sitelink that mentions an old date or an offer that has ended.

**From an export**
Hey Claude, I just added the "google-ads-assets-auditor" skill. Here's my assets report as a CSV. Build the campaign grid and tell me what's missing.

## What you get

1. **A grid** of every Search and Performance Max campaign against every asset type, showing whether each campaign has its own assets, inherits the account's, or has none, with override traps marked (a small campaign set hiding a bigger account set).
2. **A ranked fix list:** broken now (disapproved, dead links), out of date, override traps, gaps, weak assets, Google-generated assets, and opportunities.
3. **Results for every asset,** compared only with assets of the same type.
4. **A link check** of every sitelink URL: status, redirects and where it lands.
5. **Drafted replacements,** each with its character count and where its facts came from.

## What it can change for you

With your yes on the exact change, it can add sitelinks, callouts, structured snippets, a call asset, a price asset or a lead form. Removing or editing an existing asset, adding promotions or images, and switching off Google-generated assets are done in Google Ads; the report tells you where.

## Tips

- Run it at the start of every season, and after any change to your website's pages.
- Fix the broken items first: a disapproved asset or a dead sitelink costs you today.
- If a campaign has a few sitelinks of its own, check the grid before adding account-level ones: the campaign's own set wins.
