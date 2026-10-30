# How to Use This Skill

Hey Claude, I just added the "meta-automated-rules-builder" skill. Build the automated rules my Meta ad account should run, test them on my last 13 weeks, and give me the settings for Ads Manager. My target is $30 a purchase.

## What you need

- **Your target cost per result** (cost per purchase, lead or install), or a ROAS target and your average order value.
- **Your data, one of two ways:**
  - The InsightfulPipe MCP connected to Claude with your Meta ad account added. The skill pulls 13 weeks of daily ad data, weekly ad set data, budgets and budget changes itself.
  - Or two Ads Manager exports: a daily report at ad level (day, ad set, ad, amount spent, impressions, results) and a weekly report at ad set level (with reach and frequency), plus your daily budgets.
- **The highest daily budget** you'd accept for each ad set (or campaign), so the raise rule has a ceiling.
- **Your current rules,** if you have any. Copy them from Ads Manager, Rules, Manage rules.

## Example requests

**Full rule set**
Hey Claude, I just added the "meta-automated-rules-builder" skill. Build stop, raise, alarm and overspend rules for my Meta account. Target $45 a lead, and no ad set should go over $300 a day.

**Stop rules only**
Hey Claude, I just added the "meta-automated-rules-builder" skill. How much should an ad spend before a rule turns it off? Test a few lines on my history and tell me which winners each would have killed.

**Check my existing rules**
Hey Claude, I just added the "meta-automated-rules-builder" skill. Here are the 4 automated rules we run in Ads Manager. Do any of them fight each other or kill good ads?

**Scaling rule**
Hey Claude, I just added the "meta-automated-rules-builder" skill. Write a rule that raises budgets on ad sets that keep beating target, without throwing them back into learning.

**From an export**
Hey Claude, I just added the "meta-automated-rules-builder" skill. I've attached a daily ad-level export and a weekly ad set export from Ads Manager. Our target ROAS is 3 and our average order is $90. Build our rules from these.

## What you get

1. **The rules, ready to enter:** for each one, what it applies to, the action, the conditions, the time range, the schedule, and for the raise rule the maximum budget and how often it may act.
2. **The replay:** four spend lines side by side, with the losers each would have stopped, the past winners each would have killed (by name), and the money saved, so you can see why the chosen line sits where it does.
3. **A review of your current rules:** what each would have done on your history, where rules fight each other, and whether to keep, change or replace each one.
4. **Today's check:** the ads the new rules would turn off now, the ones on watch, and the ad sets they'd raise tonight.

## What it can change for you

With your yes on the exact change, it can:
- turn off ads that already break a stop rule
- turn off an ad set that has already spent past its overspend guard today

It never changes budgets, bids or targeting, and it can't create rules for you: you enter them in Ads Manager from the settings it gives you.

## Tips

- Turn off any old rule the review replaces on the same day you add the new ones, so both sets never run together.
- Run it again every quarter, or after your target or budgets change: the lines move with them.
- Small accounts get fewer graded ads in 13 weeks. The skill says when a line is untested on your history.
