# How to Use This Skill

Hey Claude, I just added the "scaling-roadmap-builder" skill. We spend about $5,500 a month on Google Ads. Plan how to get to $10,000 a month over the next 6 months without our cost per lead going over $40.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls the data itself, so you don't need to export anything.
- **Your target:** a monthly spend or a number of conversions, and a timeline. If you don't have one, the skill shows how far the account can grow efficiently.
- **Your maximum CPA.** Without it, the skill uses your own CPA over the last 6 months (or the months you have). If you think in ROAS, give your minimum ROAS instead: the skill turns it into a maximum CPA using your average conversion value, shows the math, and plans on that CPA.
- **How many more leads or orders your team can handle**, if you know.

## Example requests

**Full roadmap**
Hey Claude, I just added the "scaling-roadmap-builder" skill. Build me a plan to take Google Ads from $8K to $25K a month. Our max CPA is $60.

**Am I ready?**
Hey Claude, I just added the "scaling-roadmap-builder" skill. Before I raise budgets, check whether my Google Ads account is ready to scale and tell me what to fix first.

**Where should the next dollar go?**
Hey Claude, I just added the "scaling-roadmap-builder" skill. If I add $2,000 a month to Google Ads, which campaigns should get it, and what will each extra lead cost?

**Stuck at a plateau**
Hey Claude, I just added the "scaling-roadmap-builder" skill. Every time I raise my budget, CPA jumps. Find where I can still grow and where I've hit the ceiling.

**New account**
Hey Claude, I just added the "scaling-roadmap-builder" skill. Our Google Ads account launched 2 months ago and leads cost about $45. How fast can we scale it?

**Aggressive timeline**
Hey Claude, I just added the "scaling-roadmap-builder" skill. I need to double spend in 3 months. Is that realistic for this account? Show me the plan and the risks.

## What you get

1. **A readiness score out of 5:** tracking, efficiency and its trend, data volume, structure and landing pages, each backed by a number.
2. **A campaign scaling map:** which campaigns to scale now, fix first, watch, or grow only with new keywords.
3. **Headroom:** how much more each campaign can spend before the *next* conversion costs more than your max. This comes from Google's budget simulations and recommended budgets, checked against impression share lost to budget.
4. **An expansion list:** converting search terms that aren't keywords yet, and Keyword Planner ideas graded by whether you can afford the click.
5. **A phase-by-phase roadmap:** daily budgets per campaign, actions, success criteria, risk responses and checkpoints.
6. **A month-by-month projection:** an expected and a low case, labelled as estimates, with a simple text chart of spend and conversions.
7. **Pause triggers** and a checklist to clear before each new phase.

## What it can change for you

When a phase starts, and only with your yes to the exact change, it can:
- set a campaign's new daily budget
- add your converting search terms as keywords

It never changes bid strategies or targets, and never creates or pauses campaigns.

## If you haven't connected Google Ads

Paste a 30-day campaign report: spend, conversions, clicks, impression share, impression share lost to budget and to rank, bid strategy and daily budget. Add monthly totals for the last 6 months. The skill builds the same roadmap from it, with lower confidence, and without the simulations or the Keyword Planner check.

## Tips

- Be honest about your max CPA. The plan scales only while the next conversion costs less than that number.
- A newer account works too. With under 6 months of history the skill compares the months you have, and with under 2 it says the trend is unknown and keeps confidence at Medium or lower.
- Run it again at every checkpoint. The next phase is based on what the last one actually did.
- Fix tracking first. A budget raised on double-counted conversions buys fewer real leads than the plan shows.
