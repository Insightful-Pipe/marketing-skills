# How to Use This Skill

Hey Claude, I just added the "audience-overlap-analyzer" skill. Check whether my Meta ad sets and Google Ads campaigns are reaching the same people, and tell me what to exclude or merge.

## Example prompts

**Full overlap check**
Hey Claude, I just added the "audience-overlap-analyzer" skill. Go through my live Meta ad sets and Google campaigns, find every pair that targets the same people, and rank them by how much they cost me.

**Rising frequency or CPM**
Hey Claude, I just added the "audience-overlap-analyzer" skill. Frequency and CPM have been climbing on three prospecting ad sets for a month. Is it overlap, saturation, or both?

**Custom audiences and lookalikes**
Hey Claude, I just added the "audience-overlap-analyzer" skill. I run 1%, 1-3% and 3-5% lookalikes from my purchasers, plus a lookalike of my top customers. How much do they share, and how should they be set up?

**Is this audience used up?**
Hey Claude, I just added the "audience-overlap-analyzer" skill. Check whether my retargeting and interest audiences are saturated: how much of each we've reached and how fast results are fading.

**Retargeting exclusions**
Hey Claude, I just added the "audience-overlap-analyzer" skill. Check that my prospecting ad sets exclude buyers and site visitors, and that my retargeting tiers exclude each other properly.

**Google campaigns fighting over terms**
Hey Claude, I just added the "audience-overlap-analyzer" skill. Which search terms show up in more than one of my Google Ads campaigns, and which campaign should own each one?

## What it needs

The InsightfulPipe MCP with a Meta ad account, a Google Ads account, or both. It reads everything itself:
- **Meta:** ad sets and their targeting, custom audiences and lookalikes, 30 days of delivery, 90 days of weekly trends, and Meta's reach estimates.
- **Google:** 30 days of search terms, campaign spend, keywords, locations and audience segments.

It asks three things up front, with defaults if you don't know: the result that counts and its target cost, which audiences are buyers and which are warm, and your brand terms.

No connection? Paste the ad set list with targeting, 30-day spend, reach and frequency, plus campaign and account reach for the same 30 days. You can add Meta Audience Overlap tool results and a Google search terms export with the campaign column. Figures from your export are marked as unchecked.

## What you get

1. **Overall health:** healthy, at risk or critical.
2. **Overlap matrix:** each pair among the live ad sets with the most spend (up to 8), with the overlap share and where it came from: the settings, a reach estimate, or not measured. People actually reached twice are counted per campaign and for the whole account, because that figure can't say which pair caused it.
3. **Pairs ranked worst first:** each with an Overlap Score from 0 to 100, its factors, the cause and the fix.
4. **Saturation table:** audience size, share already reached, 7-day frequency, CPM and CTR trend, and a verdict.
5. **Google findings:** terms served by several campaigns, which are by design (split by location) and which aren't, the owner for each, brand leakage and duplicate keywords.
6. **Exclusion and consolidation plan:** an exclusion order from buyers down to broad, which ad sets to merge, and the structure before and after.
7. **Action plan** for this week and the next two weeks, plus what couldn't be checked.

## What it can change for you

With your yes on the exact change, it can:
- add exclusions to a Meta ad set (it sends the full targeting with the exclusions merged in)
- pause a duplicate Meta ad set after you merge it
- add exact-match negatives so a Google campaign stops serving a term another campaign owns

It never creates audiences, changes budgets or sets frequency caps. Those stay in Ads Manager and Google Ads.

## Tips

- Run it before scaling a budget, after adding new audiences, and monthly.
- The same term in two Google campaigns is fine when they target different places. The skill checks locations before it calls anything overlap.
- Overlap between two custom audiences or lookalikes uses Meta's reach estimate on both together. That path hasn't yet been run on large audiences, and Meta gives no estimate for audiences that are too small; the report then marks the pair unknown instead of guessing.
- Meta's rate limit is shared by every tool on the account. If Meta pauses the calls, the skill can do Google first.
