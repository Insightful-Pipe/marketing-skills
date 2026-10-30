# How to Use This Skill

Hey Claude, I just added the "meta-recommendations-reviewer" skill. Here are the recommendations Meta shows in my Ads Manager. Which should I apply, test or skip?

## What you need

- **The recommendation list from Ads Manager.** Paste it or upload a screenshot: each card's title, the campaign, ad set or ad it names, and the points. Include any suggested budget Meta shows.
- **Your target cost per result or ROAS,** if you have one. Without it, the skill uses your account's own 30-day average.
- **Anything Meta can't know:** claims your ads must not make, audiences that must stay separate, tests already running.
- **Your account numbers, one of two ways:**
  - Connect the InsightfulPipe MCP with your Meta ad account, and the skill checks each recommendation against your ad sets, budgets, placement results and edit history itself.
  - Or export an ad set report for the last 30 days and the last 7 days from Ads Manager, plus the placement breakdown or the ad report if a placement or fatigue recommendation is on the list.

## Example requests

**Review the whole list**
Hey Claude, I just added the "meta-recommendations-reviewer" skill. Here's a screenshot of my Meta opportunity score and its recommendations. Our target is $35 per purchase. Which ones should I apply?

**One recommendation**
Hey Claude, I just added the "meta-recommendations-reviewer" skill. Meta says my retargeting ad set should use Advantage+ audience. Should I?

**Budget raises**
Hey Claude, I just added the "meta-recommendations-reviewer" skill. Meta keeps telling me two campaigns are limited by budget. Check whether raising them makes sense, and raise the ones that pass after I confirm.

**No connection**
Hey Claude, I just added the "meta-recommendations-reviewer" skill. I've pasted my Facebook Ads Manager recommendations and an ad set export for the last 30 and 7 days. Tell me which to dismiss.

## What you get

1. **A verdict for each recommendation:** apply, test first, skip or your call, with the numbers that decided it.
2. **The changes to apply,** each with the exact change for you to confirm.
3. **An A/B test plan for each test first item:** what to change on the copy, how long to run it, and when to keep the change.
4. **A list of what to dismiss,** with the reason for each.
5. **A dated order of changes,** so no ad set gets two changes in the same week.
6. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- raise a campaign or ad set budget, one step of 20% at most at a time
- pause the weaker of two similar ad sets and move its budget to the one you keep
- switch on Advantage+ audience for an ad set
- pause a tired ad once its replacement is live

Tests, new creatives, placement and goal changes, and Conversions API setup happen in Ads Manager or Events Manager. The skill gives you the steps.

## Tips

- Your opportunity score measures how many of Meta's suggestions you follow, not how well your ads perform. Skipping some is normal.
- Run it whenever new cards appear, and before applying several at once.
- Dismiss the cards the skill says to skip, so they stop coming back.
