# How to Use This Skill

Hey Claude, I just added the "performance-drop-investigator" skill. Our numbers dropped. Find out what changed and why.

## What you need

- **The InsightfulPipe MCP connected to Claude, with the source where the number lives:** Search Console and Bing Webmaster for organic search, GA4 for site traffic and key events, Google Ads, Meta or LinkedIn Ads for paid campaigns. The skill pulls the data itself; you don't export anything.
- **What moved, and roughly when you noticed.**
- **Anything you changed recently:** a site release, a price change, a budget or bid change, a tracking change. If you know the day, say it.
- **No connection?** Paste the exports for two date ranges instead. For Google Ads CPA or ROAS, the Campaigns report is the minimum (add Devices, Search terms, Landing pages and Change history if you have them), and the same dollar split runs on the pasted numbers. For other drops, paste the daily line of the number and the page, query or campaign reports for both ranges.
- **Auction insights:** Google withholds them from API access, so paste the Auction insights table for both date ranges if you want competitors named.

## Example requests

**What changed and why**
Hey Claude, I just added the "performance-drop-investigator" skill. Our organic clicks are down over the last two weeks. What changed and why?

**Leads fell on paid**
Hey Claude, I just added the "performance-drop-investigator" skill. Google Ads leads dropped this month while spend stayed the same. Where did they go?

**Google Ads cost per conversion went up**
Hey Claude, I just added the "performance-drop-investigator" skill. Our Google Ads cost per conversion went from about $45 to $57 over the last two weeks. Why did our CPA increase, and how many dollars does each cause account for?

**Campaign post-mortem**
Hey Claude, I just added the "performance-drop-investigator" skill. Our Meta lead campaign from March missed its target by half. Write the post-mortem: where did it fail and what should we do differently?

**Pricing change impact**
Hey Claude, I just added the "performance-drop-investigator" skill. We changed our pricing on the 1st. Did it change how many visitors sign up?

**Website redesign impact**
Hey Claude, I just added the "performance-drop-investigator" skill. We relaunched our product pages last month. Did the redesign hurt our search traffic?

## What you get

1. **A headline verdict:** what moved, by how much, between which dates, and the main cause with its grade.
2. **The change, sized and dated:** before and after on equal windows, whether it sits outside the last eight weeks' normal range, the day it started, and last year's same weeks when there is data.
3. **Measurement checks first:** whether GA4 still sees your search traffic, whether its daily line stepped, and whether a conversion stopped firing or a new one started, so a broken tag isn't blamed on the market.
4. **Where it went:** how much came from impressions, click rate or conversion rate, and which pages, queries, campaigns or devices carry the change, each labelled as lost ranking, lower demand, a weaker search result or a page that's gone.
5. **Every likely cause graded** as confirmed, likely, ruled out or can't tell, with the number that decided it.
6. **Up to three actions,** and a list of what couldn't be checked.

For a Google Ads CPA rise or ROAS fall, it first waits out your account's own conversion lag, then splits the extra cost into dollars of click cost, conversion rate and campaign mix, campaign by campaign, and gives each cause (new search terms, a bid target edit, competitors, Quality Score, a landing page, device, season, tracking) the dollars it explains, with the rest shown as unexplained.

For a redesign or pricing change, it compares the part you changed with a control the change didn't touch, so a site-wide trend isn't credited to your change. For a post-mortem, it names the first stage where the campaign failed: measurement, delivery, attention, landing or economics.

## What it changes

Nothing. It only reads your accounts.

## Tips

- Give the day of any change you suspect. A dated change turns a guess into a before-and-after with a control.
- Wait two weeks after a change before reading its impact. Under a week, the skill stops and tells you when to come back.
- If one brand holds several businesses, say which one to investigate. It never mixes two businesses in one report.
