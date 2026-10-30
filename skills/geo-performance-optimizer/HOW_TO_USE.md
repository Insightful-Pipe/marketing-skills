# How to Use This Skill

Hey Claude, I just added the "geo-performance-optimizer" skill. Show me where, on which devices and at what hours my Google Ads money is working, and what I should change.

## Example prompts

**Locations**
Hey Claude, I just added the "geo-performance-optimizer" skill. Which states, metros or cities spent money in the last 90 days without bringing conversions? We only serve Texas and Oklahoma.

**Location bid adjustments**
Hey Claude, I just added the "geo-performance-optimizer" skill. Give me location bid adjustments from real CPA. My target CPA is $60 on the Plumbing campaign and $90 on Remodeling.

**Devices**
Hey Claude, I just added the "geo-performance-optimizer" skill. Should I lower bids on mobile or tablets, or exclude a device anywhere?

**Day-parting and ad schedule**
Hey Claude, I just added the "geo-performance-optimizer" skill. Run a day-parting analysis and draft an ad schedule I can apply. Our customers are on Eastern time.

**Expansion**
Hey Claude, I just added the "geo-performance-optimizer" skill. Is there any evidence I should target new areas?

## What it does

1. Finds your Google Ads account through the InsightfulPipe MCP (or asks which one if you have several).
2. Reads each campaign's bid strategy, location settings, current exclusions, bid adjustments and ad schedules.
3. Pulls 90 days of performance by state and metro, by device, and by day and hour, and names every location. For each metro on the act or watch list it drills into cities to show where that spend came from.
4. Grades each slice against its own campaign's CPA (or the target you give; ROAS on campaigns that bid on value), with a confidence level from the conversion count.
5. Picks the lever that the campaign's bid strategy actually uses. Smart Bidding ignores location and schedule bid adjustments, so there it recommends exclusions and schedule hours instead.
6. Returns the report. Location and device changes can be made for you, but only after you say yes to the exact change.

## What to tell it (all optional)

- Target CPA or ROAS per campaign. Without one, each campaign's own CPA over the window is the benchmark.
- Your service area: places you can and can't serve.
- Your customers' time zone, if it differs from the account's. Campaigns that target a whole country across several time zones are shown in account time only.
- A different window than the last 90 days.

## What you get

- A health light for locations, devices and schedule
- A bid strategy map: which levers work on each campaign
- Settings checks: presence vs interest matching, spend from outside your targeted areas, bid adjustments your strategy ignores, current schedules
- An "act now" list with the change, the money a month and who makes it
- A watch list, the strongest slices, and what to do about them
- A city drill-down for every metro on the act or watch list
- A bid adjustment sheet (only for campaigns whose strategy uses one) and an ad schedule draft, ready for Google Ads Editor
- Evidence-based expansion ideas, or "none found"
- An estimate of the money freed, labelled as an estimate

## Changes it can make (after you confirm)

- Exclude or add a location: `add_location_targeting`
- Stop targeting a location: `update_campaign_targeting`
- Switch location matching to presence: `update_campaign`
- Exclude or adjust a device: `set_campaign_device_targeting` or `set_device_bid_modifier`

These need a Read & Write connection, and an owner, admin or operator can switch any of them off. Ad schedules and location bid percentages have no MCP action yet, so the skill drafts them for you to paste into Google Ads.

## Not connected?

Export the Locations, Devices and "Day & hour" reports from Google Ads for the same dates, by campaign, with cost, clicks and conversions, and tell it each campaign's bid strategy. It runs the same grading on the exports.
