# How to Use This Skill

Hey Claude, I just added the "linkedin-ads-b2b-optimizer" skill. Show me which seniorities, job titles, company sizes and industries are worth paying for on LinkedIn, and fix what's wasting money.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your LinkedIn Ads account added.** The skill pulls campaigns, ads, placements and the audience breakdowns itself; you don't export anything.
- **Your buying committee,** if it differs from what your campaigns already target: the seniorities, job functions, company sizes and industries that can buy.
- **Your target cost per qualified lead,** if you have one. Without it, the skill uses your own blended cost per lead.
- **CRM counts, optional:** qualified leads by seniority, title, company size or industry for the same dates. With them, "qualified" means what your sales team says; without them, it means a lead from the buying committee with a valid work email.
- **To make changes:** a Read & Write connection. An owner, admin or operator can switch write actions off.

Not connected yet? Give it the Campaign Manager campaign export and the Demographics tab exports (seniority, job title, job function, company size, industry). It runs the breakdowns from them, but it can't check bids against LinkedIn's live suggested bids or change anything.

## Example requests

**Cost per qualified lead by seniority**
Hey Claude, I just added the "linkedin-ads-b2b-optimizer" skill. Break down my LinkedIn cost per qualified lead by seniority for the last 90 days. Our buyers are directors and above.

**Titles, company sizes and industries**
Hey Claude, I just added the "linkedin-ads-b2b-optimizer" skill. Which job titles, company sizes and industries are driving my LinkedIn leads, and which ones are just spending?

**Pause the weak ads**
Hey Claude, I just added the "linkedin-ads-b2b-optimizer" skill. Find the LinkedIn ads with low click-through rates and pause them. Show me the list first.

**Bids and budgets**
Hey Claude, I just added the "linkedin-ads-b2b-optimizer" skill. Check my LinkedIn bids and daily budgets against LinkedIn's suggested bids, and update the ones that are off.

**Plan the next quarter**
Hey Claude, I just added the "linkedin-ads-b2b-optimizer" skill. Plan our LinkedIn ABM and lead gen campaigns for next quarter from what has worked, and tell me how much to spend.

## What you get

1. **A status for six areas:** delivery and placement, cost per qualified lead by seniority, job titles and functions, company size and industry, ads, and bids and budgets.
2. **Audience breakdowns** ranked by cost per qualified lead (or, with no leads yet, by cost per click, clearly labelled), with the spend that leaks outside your targeting.
3. **Ads to pause,** compared only with the other ads in the same campaign.
4. **Bids and budgets** checked against LinkedIn's live suggested bids for each campaign's own audience, with daily pacing.
5. **Up to 5 changes,** ranked by the spend they touch, each with its evidence and the exact payload.
6. **A plan:** objectives, audiences, campaign structure, formats, offers, lead form basics, a daily and monthly budget priced on your real audiences, a two-month roadmap and what to measure.

## What it can change for you

With your yes on the exact payload, it can:
- pause a low-CTR ad
- change a campaign's bid or daily budget
- turn off the LinkedIn Audience Network on a campaign
- tighten a campaign's targeting (add a seniority or company size layer, add an exclusion), one layer per change
- restart a paused campaign and its campaign group, when you ask

It never changes a campaign's bidding type, objective or ad copy, and it never runs a change you haven't approved.

## Tips

- Run it monthly, or after any campaign has 2–4 weeks of delivery.
- Give each campaign 2–4 ads so the ad check has something to compare.
- Job titles, functions and industries come back from LinkedIn as ids. Tell Claude the names you use in Campaign Manager if you want them in the report.
- For the full account health check, use the LinkedIn Ads Auditor skill; for lead form design, the LinkedIn Lead Gen Form Optimizer.
