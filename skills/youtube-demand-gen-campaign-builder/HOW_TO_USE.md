# How to Use This Skill

Hey Claude, I just added the "youtube-demand-gen-campaign-builder" skill. Set up a YouTube campaign for sign-ups at $300 a day with a $40 target CPA. Pick the videos, check the assets and show me the payloads; don't create anything yet.

## What you need

- **A short brief:** the goal (conversions, video views or reach), a daily budget, and for conversions a target CPA. The landing page, locations, languages and brand terms help too.
- **Your videos and images:** YouTube links with each video's length and shape, and image links with their pixel sizes. With the connectors below, the skill reads most of this itself.
- **Optional, the InsightfulPipe MCP connected to Claude:**
  - **Google Ads:** conversion setup, live campaigns and CPA, your audience lists and their sizes, converting search terms, existing exclusions, past placements and the asset library.
  - **YouTube Analytics:** your channel's videos with their average view percentage, and the retention curve of the pick.
  - **GA4:** whether the landing page converts.
- **A Read & Write connection** if you want it to create the campaign after you approve the plan.

## Example requests

**Demand Gen from a brief**
Hey Claude, I just added the "youtube-demand-gen-campaign-builder" skill. Build a Demand Gen campaign for demo bookings in the US and Canada, $250 a day, target CPA $60, landing on our demo page.

**How to set up YouTube ads with no connection**
Hey Claude, I just added the "youtube-demand-gen-campaign-builder" skill. I want YouTube ads for more channel views. Here are three video links, a 45-second, a 2-minute and a 20-second vertical one. Budget is $50 a day. Plan it.

**Display remarketing**
Hey Claude, I just added the "youtube-demand-gen-campaign-builder" skill. Set up a Display remarketing campaign for people who visited our pricing page, using these two images and our logo. Check the image sizes first.

**Check my assets only**
Hey Claude, I just added the "youtube-demand-gen-campaign-builder" skill. Check these 9 images and 3 videos against Demand Gen specs and tell me what's missing.

## What you get

1. **The campaign type and bidding** for your goal, and why.
2. **A budget check** against Google's guidance (at least 10 times the target CPA, or $100 a day on Maximize conversions), with conversions a month, days to 50 conversions and how many ad groups the budget can feed.
3. **Audiences:** every list with its size and how it's used, a paste-ready custom segment from your own converting search terms, and the converters to exclude.
4. **Video picks** from your channel's retention, with the runner-ups and the hold at 5 seconds.
5. **An asset check:** each video, image and line of ad text against its spec, with character counts, and the gaps against Google's benchmark.
6. **Exclusions:** a paste-ready placement list from your own past placements, the exclusions you already have, content suitability and frequency.
7. **Every payload, marked not run,** plus the steps to finish in Google Ads.

## What it can change for you

With your yes on the exact plan, it can create a Demand Gen campaign (campaign, ad groups, audiences, image and video assets) or a Display campaign (campaign, ad group and responsive display ad), always paused, and add videos to your asset library. Turning anything on is a second, separate yes. It never changes a live campaign.

It can't create Video campaigns (Google's API doesn't allow it), Demand Gen ads, custom segments, placement exclusions or content suitability settings. For those it gives you paste-ready lists and the steps in Google Ads.

## Tips

- Give the skill a target CPA you can live with: the budget check depends on it.
- Run `display-video-demand-gen-auditor` 30 days after launch, if installed.
- Don't judge a Demand Gen campaign before it has 50 conversions; the plan gives you the date.
