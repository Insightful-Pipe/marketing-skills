# How to Use This Skill

Hey Claude, I just added the "google-ads-delivery-troubleshooter" skill. Find out why my Google Ads aren't showing and tell me what to fix first.

## What you need

- **Best: the InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill reads every status, reason, policy note, negative, schedule and target itself, in one pass.
- **Or nothing connected:** paste the Status column with its hover text, screenshots, or a campaign or keyword export with the Status and Status reasons columns. The skill runs the same checks on what you send and marks the rest unknown.
- **Where and when your ads should run,** so it can tell a deliberate setting from a mistake.
- **An Ad Preview and Diagnosis screenshot** if the question is "I searched and didn't see my ad". Google doesn't make that tool available through the API.

## Example requests

**Ads not showing**
Hey Claude, I just added the "google-ads-delivery-troubleshooter" skill. My Google Ads aren't showing since Tuesday. Find out why.

**Eligible (limited)**
Hey Claude, I just added the "google-ads-delivery-troubleshooter" skill. Two of my campaigns say Eligible (limited). What does that mean for each one, and what should I change?

**Not spending the budget**
Hey Claude, I just added the "google-ads-delivery-troubleshooter" skill. My Fitness campaign has a $100 daily budget but only spends about $30. Why?

**No connection**
Hey Claude, I just added the "google-ads-delivery-troubleshooter" skill. Here's a screenshot of my campaigns with the Status column. Tell me what's blocking delivery.

## What you get

1. **A one-line answer:** how many things stop delivery, how many hold it back, and what to fix first.
2. **The blockers, ranked:** each with Google's own reason, the numbers behind it, the money at stake over 7 days, the fix, and whether the skill can make it for you.
3. **A campaign table:** status, reasons, budget use, impression share and what each campaign loses to budget and to rank.
4. **What's simply out of demand:** campaigns and keywords that win most of the searches there are, where a bigger budget would change nothing.
5. **What was checked and found fine, and what couldn't be checked.**

## What it can change for you

With your yes on the exact change, it can:
- turn a paused ad group, ad or keyword back on
- raise a manual keyword bid
- move a campaign's start or end date
- loosen a target CPA or ROAS, or raise a CPC cap
- point disapproved ads at a landing page that works

Billing, policy appeals, removing negative keywords and turning a whole campaign back on stay with you in Google Ads.

## Tips

- Say what changed recently, if you know. The skill also reads the last 14 days of change history.
- Fix one blocker at a time when it touches bidding. Every target change restarts learning.
- Run it again a day after a fix. Google's status can take a few hours to update.
