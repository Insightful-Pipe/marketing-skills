# How to Use This Skill

Hey Claude, I just added the "pmax-asset-group-analyzer" skill. Review my Performance Max campaign and tell me which asset groups and assets to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls asset groups, assets, signals, search terms and the channel split itself; you don't need to export anything.
- **Your target CPA or ROAS,** if you have one. Without it, the skill uses the campaign's own 30-day figure.
- **Your brand terms and any competitor names you bid on on purpose,** if they aren't obvious from your account.

## Example requests

**Why isn't PMax working?**
Hey Claude, I just added the "pmax-asset-group-analyzer" skill. My Performance Max campaign is above my $60 target CPA. Find out why and rank the fixes.

**One asset group takes all the budget**
Hey Claude, I just added the "pmax-asset-group-analyzer" skill. One asset group gets most of my PMax spend. Is that a problem, and what should I do with the others?

**Weak assets**
Hey Claude, I just added the "pmax-asset-group-analyzer" skill. Which headlines and images in my asset groups barely serve, and what should replace them?

**Brand cannibalisation**
Hey Claude, I just added the "pmax-asset-group-analyzer" skill. Is PMax taking clicks from my brand Search campaign? Show me the brand share of its search terms.

**Where the money goes**
Hey Claude, I just added the "pmax-asset-group-analyzer" skill. Break down my PMax spend by network and show me the placements it bought.

**No PMax yet**
Hey Claude, I just added the "pmax-asset-group-analyzer" skill. We don't run Performance Max yet. Check whether the account is ready and draft a first campaign, but don't create anything.

## What you get

1. **A route:** a full review if PMax spent in the last 30 days, a structure review if it didn't, or a readiness check and draft if there is no PMax at all.
2. **A scorecard** for campaign health, asset groups, assets, signals and search themes, search terms, and channels and placements.
3. **A diagnosis:** the main problem, traced from symptom to root cause.
4. **Up to 5 fixes,** ranked by the money at stake, each with the numbers behind it and a suggested week.
5. **Asset groups in tiers** (star, on target, behind, problem, too early) and the assets that barely serve, with replacement ideas taken from your own converting search terms and ads.
6. **Search term findings:** brand share, wasted spend, competitor terms, and how much of the spend Google actually shows.
7. **For a new account:** a paused campaign draft built from your best Search campaign, with every payload shown and marked not run.

Google no longer shares the old Best / Good / Low asset labels through its API, so the skill judges each asset by how often it serves and converts.

## What it can change for you

With your yes on the exact change, it can:
- add search themes and audience signals to an asset group
- upload images or add YouTube videos and link them to an asset group, then unlink the asset they replace
- create a new asset group, or pause, rename or re-point one
- merge thin asset groups: create one combined group, then pause the old ones
- add negative keywords to a PMax campaign (not yet tested there; if Google refuses, it tells you the Google Ads route)
- create the drafted campaign (always paused), then set its bidding, locations and audiences

Brand exclusions, placement exclusions and account-level negative lists stay in Google Ads; the skill tells you where. It never changes budgets or bidding on a live campaign.

## If Google Ads isn't connected

You can paste exports instead: asset group performance, the asset list per group, search themes and audience signals, the search terms insight report and the channel performance report. The skill runs the same checks on them and offers no changes.

## Tips

- Leave two weeks between changes to the same asset group, so you can read each one.
- Under 30 conversions a month, read every verdict as a direction, not a final answer.
- Run it monthly, and two weeks after any change to assets or signals.
