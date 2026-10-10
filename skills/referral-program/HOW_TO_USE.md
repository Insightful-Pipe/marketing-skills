# How to Use This Skill

Hey Claude, I just added the "referral-program" skill. Design a referral or affiliate program for us from our own data, and tell me what to fix before we launch it.

## What you need

- **The InsightfulPipe MCP connected to Claude, with GA4 added,** for the full run. The skill pulls the data itself; you don't export anything.
- **Search Console, Klaviyo and an ad account** if you have them. Each one adds a part of the plan (brand search growth, where the ask lives in email, a paid CAC reference). Missing ones are listed as unknown.
- **What a customer is worth:** first-year revenue (or lifetime value) per customer and your gross margin. Without them the skill won't quote a reward amount.
- **The conversion you'd pay a reward on** (sign-up, first payment, purchase), if it isn't obvious.

No GA4? Describe your business, your customers, how they find you today and who already mentions you. The skill designs the program from your answers (and from Search Console or Klaviyo if those are connected), but the baseline, the traffic-based partner list and most readiness grades stay unknown until GA4 is connected.

## Example requests

**Start from scratch**
Hey Claude, I just added the "referral-program" skill. We have no referral program. Design one from our data. A customer brings in about $1,000 in the first year and our margin is 80%.

**Affiliate commission**
Hey Claude, I just added the "referral-program" skill. What commission and cookie window should our affiliate program offer, and which sites already sending us traffic should we invite first?

**A program nobody uses**
Hey Claude, I just added the "referral-program" skill. Our refer-a-friend program gets almost no shares. Check the tracking, the ask and the reward, and tell me what to change.

**Plan, then set up tracking**
Hey Claude, I just added the "referral-program" skill. Plan the program, then register the referral code in GA4. Show me the change first.

## What you get

1. **A readiness scorecard:** is the reward conversion tracked, can referrals be attributed, is sharing tracked, is there an email flow for the ask, is there real word of mouth, are there reward codes.
2. **Word of mouth today:** how much traffic other people and sites send, which senders engage, whether people first sent by others come back more, brand search growth, and searches for your program or codes.
3. **A recommendation:** customer referral, affiliate or partner, both, or foundation first, with the rule that chose it.
4. **Economics:** the break-even ceiling, the working budget per referred customer, the reward split and the affiliate commission.
5. **The program design:** trigger moments, incentive, share mechanics, referral landing page, tracking links and events, fraud rules and affiliate terms.
6. **Partner candidates** from your own traffic, with a drafted outreach note. When a video or social platform sends the visitors, GA4 names the platform, not the creator, so the skill tells you how to find the creators.
7. **Targets and a 90-day plan:** K-factor and the metrics to watch, each from your baseline or labelled as an assumption.

## What it can change for you

With your yes on the exact change, it can:
- register a `referral_code` custom dimension in GA4
- mark a referred sign-up event as a GA4 key event, once that event fires
- draft a referral ask email template in Klaviyo (it doesn't send anything)
- create a friend reward coupon in Klaviyo (ecommerce)

It never sends email, changes prices or pays rewards.

## Tips

- Fix the fails first. A program that can't see who referred whom can't pay the right person.
- Start small: 3 to 5 partners or 20 to 50 of your best customers, then open it up once 30 days of clean data exist.
- Run it again 60 days after launch to replace the planning assumptions with your own share and conversion rates.
