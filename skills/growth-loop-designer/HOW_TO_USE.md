# How to Use This Skill

Hey Claude, I just added the "growth-loop-designer" skill. Map the growth loops we could run, put numbers on each one, and tell me which loop to build first and what to track.

## What you need

- **A short description of your product** and how it reaches people who don't use it yet: invites, things users share or publish, public pages, your blog, paid ads.
- **A few numbers from your product database or admin panel** for the last 30 days: new accounts, outputs published and live (split by plan or setting if you can), invites sent and accepted, and how many invites created a new account rather than a seat.
- **Your economics,** if you want the paid loop judged: the share of new accounts that pay, revenue per paying account per month, gross margin, and the longest payback you accept (12 months if you don't say).
- **Optional, for measured numbers instead of pasted ones:** the InsightfulPipe MCP with GA4, Search Console, Google Ads, Meta Ads or a BigQuery GA4 export connected. Each one replaces numbers you would otherwise paste.

## Example requests

**Pick the first loop**
Hey Claude, I just added the "growth-loop-designer" skill. We have five ways new users find us. Work out which growth loop gives us the most new sign-ups in the next 90 days.

**No connection, just numbers**
Hey Claude, I just added the "growth-loop-designer" skill. Here are our sign-ups, invites and shared documents for last month. Build the loop math from these and show me the weak step in each loop.

**Is our invite feature a loop?**
Hey Claude, I just added the "growth-loop-designer" skill. Our users invite a lot of teammates. Tell me whether that brings in new companies or only adds seats.

**Paid reinvestment**
Hey Claude, I just added the "growth-loop-designer" skill. Check whether our Google Ads and Meta spend pays back fast enough to reinvest, using our margin and a 12-month limit.

**Tracking first**
Hey Claude, I just added the "growth-loop-designer" skill. List the events and parameters we need so every growth loop we run can be measured in GA4.

## What you get

1. **A loop map:** each loop's output per cycle (k for user loops, r for paid), cycle time in days, sign-ups it brings now, its weak step and whether it passes the gates.
2. **The math for each loop,** step by step, with where every number came from and a check that the steps multiply out to the measured result.
3. **The fix for each weak step,** sized as extra sign-ups per month, in 90 days and in 12 months, with build days and lag counted.
4. **One loop to build first,** the order for the rest, and the date the first result can be read.
5. **A tracking plan:** the events, parameters, link tags and GA4 dimensions each loop needs.

## What it can change for you

With a Read & Write connection and your yes on the exact change, it can register loop parameters (such as `invite_type` or the sign-up `method`) as GA4 custom dimensions, and make `sign_up` a key event when it isn't one yet. It never changes your product, budgets, campaigns or links.

## Tips

- Split your product numbers by the setting you suspect (plan, default on or off, linked or not). The skill finds the weak step by comparing your own segments, so a split is what lets it size a fix.
- Staff or teammate invites usually add seats, not new customers. If you want a reward program for customers who bring other businesses, use the referral-program skill if you have it.
- Rerun it 30 days after the first fix ships to see the loop's k move.
