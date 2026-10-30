# How to Use This Skill

Hey Claude, I just added the "facebook-ads-audience-builder" skill. Look at my Meta ad account and build me an audience plan: what to target cold, who to retarget, and which lookalikes to make.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta (Facebook) Ads account added.** The skill reads your audiences, pixel, linked Page and Instagram account, ad sets and 90 days of results itself. You don't export anything.
- **The result that counts:** purchases, leads, sign-ups or something else. Without it, the skill uses the goal most of your spend went to.
- **Your daily budget and countries,** if they differ from what the account runs today.
- **Your customer list size,** if you have one. Lists can't be read through the MCP, so the plan only knows about it if you say so.
- **Which linked Page and Instagram account are yours.** A Page linked to your ad account can belong to another business, so engagement audiences are built only from the ones you confirm.

## Example requests

**New or quiet account**
Hey Claude, I just added the "facebook-ads-audience-builder" skill. We've barely run Meta ads. Check what the account has and tell me which audiences to start with on $30 a day in the US.

**Advantage+ audience vs our own targeting**
Hey Claude, I just added the "facebook-ads-audience-builder" skill. Has Advantage+ audience done better than our interest and lookalike ad sets over the last 90 days? Show me the numbers.

**Rank our lookalikes**
Hey Claude, I just added the "facebook-ads-audience-builder" skill. Rank every lookalike we've run by cost per purchase and tell me which ones are wearing out.

**Lookalike from a customer list**
Hey Claude, I just added the "facebook-ads-audience-builder" skill. I have 4,000 customers with order values. Tell me exactly how to upload them and which lookalike to build, then set up a paused test ad set once it exists.

**Retargeting**
Hey Claude, I just added the "facebook-ads-audience-builder" skill. Spec the retargeting audiences we're missing and check that our prospecting ad sets exclude past buyers.

## What you get

1. **An inventory** of every audience, its size, window and health (too small, out of date), plus your pixel status and the seeds ranked from best to worst.
2. **What has worked:** Advantage+ audience against manual targeting, and your lookalikes ranked by cost per result. Ad sets with fewer than 10 results are shown but not graded.
3. **A cold, warm and hot plan** for your data stage, with sizes from Meta's reach estimate (an audience you haven't built yet shows as unknown until Meta can size it) and a budget share for each tier.
4. **Exact specs for the audiences to create,** in build order: retargeting rules and windows, customer-list segments, and lookalikes with seed, expected matched size, ratio and country.
5. **A setup checklist:** each step in order, what has to be true first, and when to run the skill again.
6. **Exclusion fixes** for each live ad set.
7. **Ready payloads** for any ad set change, marked "not run" until you say yes.

## What it can change for you

With your yes on the exact change, it can:
- create a test ad set with a new audience (the InsightfulPipe server always creates it paused)
- add exclusions to an ad set, or switch Advantage+ audience on or off

It can't create custom or lookalike audiences: you build those in Ads Manager from its specs (two minutes each), and it uses them from there. It can't turn ad sets on; you do that in Ads Manager.

## Tips

- Install the Meta pixel before anything else. Without it there are no website audiences and no website lookalikes.
- Run it again a month after a change, so the new audiences have results to rank.
- Name audiences the way the skill suggests. It reads the names next time to tell your tiers apart.
