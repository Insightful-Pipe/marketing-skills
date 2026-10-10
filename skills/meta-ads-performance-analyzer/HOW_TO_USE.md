# How to Use This Skill

Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Can you analyze my Meta Ads account for the last 28 days and tell me what's working, what's broken and what to do?

## What it needs

- The InsightfulPipe MCP with your Meta ad account connected (Facebook Ads). Claude pulls campaigns, ad sets, ads, daily results, breakdowns and the change history itself. You don't export anything.
- Optional: your target cost per result (cost per purchase, lead or other event) and target ROAS. Without them, Claude uses the account's own 28-day averages and says so.
- Pauses and budget changes need a Read & Write connection, and an owner, admin or operator can switch write actions off. Claude never makes a change until you confirm the exact payload.

## Example requests

**Full analysis**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Analyze my Meta account: health dashboard, campaign tiers, creatives, audiences and an action plan. Our target cost per purchase is $35 and target ROAS is 3.

**Why did cost per result jump?**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. My cost per lead went from $25 to $45 in two weeks. Find the spike, tell me whether CPM, CTR or conversion rate drove it, and what changed in the account around then.

**Creatives: winners and fatigue**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Which ads are winning, which are fatigued, and what's the hook rate on my videos?

**Breakdown reports**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Break down the last 28 days by placement, age and gender, country, device and hour of day, flag the segments that cost too much, and tell me whether Advantage+ placements beat my manual ones.

**Learning phase and spend alerts**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Which ad sets look stuck in learning, and did any day in the last two weeks spend far more or less than normal?

**Attribution and optimisation choices**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Compare 1-day click, 7-day click and 1-day view results, and tell me whether value optimisation is beating purchase optimisation.

**Lead ads**
Hey Claude, I just added the "meta-ads-performance-analyzer" skill. Show me cost per lead by instant form, and which forms have too many questions.

## What you get

1. A health dashboard: six traffic lights (CPM, CTR, cost per link click, cost per result, ROAS, frequency), trend arrows and a health score out of 100 with the math shown.
2. Campaign tiers: Winners, Performers, Borderline and Losers, with an action for each.
3. Creative analysis: top and bottom ads, fatigue alerts, Meta's quality rankings, format mix and video hook rates.
4. Audience analysis: Advantage+, lookalike, retargeting, interest and broad ad sets, with possible overlap and fragmentation flags.
5. Breakdowns by placement, age and gender, country, region, device and hour, flagging expensive and efficient segments, plus Advantage+ (automatic) placements compared with manual placements.
6. Trends: this window against the last one, cost-per-result spikes split into CPM, CTR and conversion rate, and daily spend anomalies matched to account edits.
7. Inferred learning status per ad set, the attribution comparison, value vs conversion optimisation, the add-to-cart and checkout funnel, and lead form costs.
8. A root-cause chain, an action plan (this week, next 2 weeks, next month), the expected impact as a labelled estimate, and a monitoring checklist with red flags.

## Tips

- 28 days is the default. Ask for a different length if you need one, and Claude compares it with the same number of days before it. Under 7 days is too short to judge most ad sets.
- Tell Claude what a result is if your ad sets optimise for something other than what you care about. For example, landing page views when you sell.
- Learning status is inferred from results and edits, because the connector can't read Meta's learning label. Confirm it in the Delivery column in Ads Manager.
- Don't react to one day. Spikes are judged on 3-day stretches, and the last 2 days are never called a spike because conversions are still coming in.
- Not connected? Paste an ad set and ad export for the last 28 days. Claude runs what it can and marks the rest unknown.
