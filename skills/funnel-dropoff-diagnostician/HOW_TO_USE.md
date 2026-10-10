# How to Use This Skill

Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. Build our funnel for the last 30 days, compare it with the 30 days before, and tell me where we lose the most people and what to fix first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property.** The skill pulls the events, pages and sessions for each step itself; you don't export anything.
- **Your ad accounts and Search Console (optional):** Google Ads, Meta Ads, LinkedIn Ads and Search Console add the steps above the site, from impression to click. Use the accounts of one business only.
- **Your funnel steps, if you have them.** Without them it picks a funnel from the events that fire, using GA4's recommended names (`form_start`, `generate_lead`, `sign_up`, `add_to_cart`, `begin_checkout`, `purchase`).
- **What one conversion is worth (optional),** so leaks can be priced in money, not only in conversions.
- **The date of any recent change (optional),** such as a redesign or a new form, for a before-and-after comparison.

## Example requests

**Where are we losing people?**
Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. Our traffic is fine but few visitors buy. Find the step that loses the most people and what it costs us each month.

**Full funnel, impression to revenue**
Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. Build our full funnel from ad impression to lead and revenue across Google Ads, Meta and GA4, and show where each channel leaks.

**SaaS signup funnel**
Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. Report on our signup funnel: visit, pricing page, signup started, signup completed and activated. Is any step worse than last month?

**Lead form report**
Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. Which pages get form starts but few submissions, and is mobile worse than desktop?

**Before and after a redesign**
Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. We changed the checkout on September 15. Compare the 3 weeks before and after, step by step. Did it help or hurt?

**Design a funnel**
Hey Claude, I just added the "funnel-dropoff-diagnostician" skill. We don't have a real funnel yet. Map one for our business from first visit to repeat customer, with ideas for each stage and the event that should measure it.

## What you get

1. **A summary:** the funnel, the windows, the source for each step, the overall rate, a health score and grade (or "not graded" and why), the biggest leak, its likely cause and the first fix.
2. **A trust check** before any diagnosis: is the goal measured, is tracking steady, do ad clicks reach the site, are the "leads" real leads. A failed check comes first in the fixes.
3. **The funnel map** from impression to conversion, with "not tracked" where the data stops.
4. **Each step against the prior period,** with a test that separates real drops from noise.
5. **Segments:** devices, channels, new or returning visitors, countries or regions, campaigns and landing pages, only where the gap is real.
6. **A priority matrix and the top 5 fixes,** each with its cost in conversions a month (and money, when a value is known), the likely cause, the evidence and the skill to go deeper.
7. **Tests** for the top leaks, with how much traffic each needs, and **alert lines** for each step and for the mobile-versus-desktop gap, to watch weekly.
8. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- mark your goal event (for example `generate_lead`) as a GA4 key event, when it fires but isn't one;
- create a GA4 audience of people who dropped off at a step (for example "started the form, didn't submit"), for remarketing.

These need a Read & Write connection, and an owner, admin or operator can switch them off. It never changes your site, ads, tags or forms; those it writes up as recommendations.

## Tips

- Give it at least 30 days. Steps with fewer than 30 sessions or clicks are shown but not graded.
- If a step has no event yet, the report says so and lists the event to add, so next month's run can see it.
- Tell it about recent changes (prices, forms, budgets, tracking) so it doesn't mistake a tracking break for a real drop.
- Without a connection, paste each step's counts for this period and the one before; it runs the same analysis and marks those figures "from your data, not checked".
