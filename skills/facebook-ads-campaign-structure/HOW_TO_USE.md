# How to Use This Skill

Hey Claude, I just added the "facebook-ads-campaign-structure" skill. Look at my Meta ad account and tell me how my campaigns should be structured.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Meta ad account added.** The skill reads your campaigns, ad sets, ads, results, pixel, audiences, Pages and lead forms itself. You don't need to export anything.
- **Your goal and monthly budget.** Without a budget, it uses your last 30 days of spend.
- **Your target cost per result (or ROAS),** if you have one. Without it, it uses your own 30-day average. A new account has no average, so give your best guess, or give your price, margin and (for leads) close rate and the skill works the target out for you. With a ROAS target, add your average order value: the skill turns ROAS into a cost per purchase (average order value ÷ ROAS) before it sizes anything.
- **Your products and markets:** one offer or several, the countries and the ad languages.
- **For a new build:** the landing page, offer, the images or videos to use (or their URLs) and your copy angles.

No connection yet? Paste a campaign and ad set export from Ads Manager plus your brief. You'll get the same structure and names, but nothing is created. The budget planner needs no export: describe your price, margin, goal and country.

## Example requests

**Clean up a messy account**
Hey Claude, I just added the "facebook-ads-campaign-structure" skill. I have 15 campaigns and it's a mess. Show me what to merge and how to move over without losing performance.

**New account setup**
Hey Claude, I just added the "facebook-ads-campaign-structure" skill. I'm starting Meta ads for my online store with $5,000 a month, a target ROAS of 3 and an average order of $90. What structure should I use?

**CBO or ABO**
Hey Claude, I just added the "facebook-ads-campaign-structure" skill. Check my campaigns and tell me which should use a campaign budget and which should keep ad set budgets.

**Build from a brief**
Hey Claude, I just added the "facebook-ads-campaign-structure" skill. Build a lead-gen campaign for our B2B service: US only, $3,000 a month, $60 per lead, four ads from the copy below. Show me the payloads before you create anything.

**How much to spend on Facebook ads**
Hey Claude, I just added the "facebook-ads-campaign-structure" skill. I'm launching Meta ads for a $120 product with a 60% margin, selling in the US, and I can put in about $3,000 a month. How much do I need to spend per ad set, is $3,000 enough, and what's the minimum budget Meta allows?

**Fix the naming**
Hey Claude, I just added the "facebook-ads-campaign-structure" skill. Give me one naming convention for this account and the new names for every live campaign.

## What you get

1. **Your current structure as a tree,** with results per ad set and checks for fragmentation, budget type, funnel separation, exclusions, duplicate audiences, ads per ad set and naming.
2. **A readiness check** for a new build: pixel and events, Page, Instagram, audiences, lead forms, catalog, creative and minimum budget, with blockers first.
3. **The recommended structure,** with the math on how many results a week each ad set can reach, and audience sizes from Meta's estimate.
4. **A naming convention** and the actual names.
5. **A budget split** by campaign and by funnel stage.
6. **A migration plan,** if the account already spends: what to keep, merge or retire, week by week.
7. **The exact payloads** for the campaign, ad sets, creatives and ads, each marked "not run".
8. **A starting budget,** when you ask how much to spend or start a new account: your break-even and target cost per result from price and margin, the weekly budget each ad set needs for about 50 results, Meta's minimum for your currency, whether your budget is enough (and which earlier event to optimise for if it isn't), and a low, base and high case for what it buys.

## What it can do for you

With your yes on the exact payloads, it can create the campaign, ad sets, creatives and ads, and upload an image from a URL. Everything is created **PAUSED**: you review it and switch it on in Ads Manager. At the end of a migration it can also pause old campaigns or ad sets, or rename them. It can't switch anything on.

## Tips

- Start simpler than you think you need. One ad set that gets all the results learns faster than three that split them.
- Keep prospecting and retargeting in separate campaigns.
- Want to test 10 audiences? Group them into 3-4 types, or test them one after another.
- The structure helps Meta learn; it doesn't guarantee results. Treat the templates as starting points.
- Set up the pixel before a sales or sign-up campaign. Without it, the skill builds the plan but marks the ad sets as blocked.
- Run it again after a month to see whether each ad set reaches about 50 results a week.
