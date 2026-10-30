# How to Use This Skill

Hey Claude, I just added the "meta-advantage-plus-auditor" skill. Audit my Meta Advantage+ campaigns, creative enhancements and catalog ads, and tell me what to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta ad account added.** The skill pulls campaigns, ad sets, insights, creatives, catalogs and product sets itself; you don't need to export anything.
- **Your main conversion event and target CPA or ROAS,** if you have them. Without them, the skill uses purchases or leads and your own average for the window.
- **One answer from Ads Manager,** if you can check: does any campaign carry the old "Advantage+ shopping campaign" or "Advantage+ app campaign" label? The API connection can't read that label, so the skill asks.

## Example requests

**Advantage+ shopping review**
Hey Claude, I just added the "meta-advantage-plus-auditor" skill. Review my Advantage+ sales campaigns for the last 30 days. Are they really in Advantage+, and do they beat my manual campaigns? My target ROAS is 3.

**Creative enhancements**
Hey Claude, I just added the "meta-advantage-plus-auditor" skill. Which Advantage+ creative enhancements are switched on in my ads, and are any of them making content I haven't checked?

**Catalog and dynamic ads**
Hey Claude, I just added the "meta-advantage-plus-auditor" skill. Check my product catalog and my catalog ads. Which products get the spend, and which ones spend without selling?

**Existing customers in Advantage+**
Hey Claude, I just added the "meta-advantage-plus-auditor" skill. How much of my Advantage+ sales spend goes to existing customers, and what do new customers really cost? My target is $38 per purchase.

## What you get

1. **A grade out of 100,** with the math shown. If three or more areas have nothing in scope, the grade is withheld and the findings are still listed.
2. **A scorecard for five areas:** Advantage+ setup, Advantage+ results and audience mix, creative enhancements, catalog health, and catalog ads.
3. **An Advantage+ table:** each sales, leads or app campaign with its budget, audience and placement settings, and whether all three put it in Advantage+.
4. **Up to 5 fixes,** ranked by the spend they touch, each with the numbers behind it and who does it.
5. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- switch on Advantage+ audience for an ad set that is one setting short of Advantage+
- pause a catalog ad whose product set is empty

It never changes budgets, bids, placements, creatives or your catalog. Those it recommends, and you change them in Ads Manager or Commerce Manager.

## Tips

- Run it after launching or restructuring an Advantage+ campaign, and before switching creative enhancements off across the account.
- Treat the enhancement and Advantage+ comparisons as leads, not proof: they compare different ads. Confirm a big gap with an A/B test.
- If the catalog check can't read your products, open Commerce Manager, choose the catalog and read the Issues tab, then tell Claude what it shows.
