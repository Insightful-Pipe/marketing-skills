# How to Use This Skill

Hey Claude, I just added the "junk-lead-investigator" skill. Half our leads this month were junk. Here is our CRM export. Find where the spam and bad leads come from and what to fix first.

## What you need

- **Your lead list** for the last 30 days: submit time, source or UTM tags (or the click ID), landing page, form, email, phone and what sales decided about each lead. A CSV from your CRM or form tool is fine. With CallRail connected through InsightfulPipe, the skill reads form submissions itself.
- **Spend by campaign and network or placement** for the same days, pasted, or pulled through the InsightfulPipe MCP from Google Ads, Microsoft Ads, Meta and LinkedIn.
- **What your form asks,** and whether it already has a hidden honeypot field or a CAPTCHA.
- **Timing fields if you have them:** seconds to submit, scroll and clicks before submit. Without them the speed and interaction checks are skipped and the report says so.

## Example requests

**Spam leads on the website form**
Hey Claude, I just added the "junk-lead-investigator" skill. We get fake form submissions every night. Here is the form export. Tell me if they're bots and how to stop them without a CAPTCHA.

**Google Ads spam leads**
Hey Claude, I just added the "junk-lead-investigator" skill. Google Ads reports 60 conversions but sales says most are junk leads. Check which campaigns and networks they come from and what Google is counting.

**Meta instant form leads that never answer**
Hey Claude, I just added the "junk-lead-investigator" skill. Our Facebook lead form leads don't pick up the phone. Here is the lead download with our call outcomes. Are these accidental taps, and which placements bring them?

**Lead quality across every channel**
Hey Claude, I just added the "junk-lead-investigator" skill. Grade last month's leads from Google, Microsoft, Meta and LinkedIn and show the spend that bought junk on each source.

**No lead list yet**
Hey Claude, I just added the "junk-lead-investigator" skill. I don't have a CRM export. Use GA4 and the ad accounts to look for bot patterns in our lead events.

## What you get

1. **A verdict on every lead:** bot or script, accidental tap, real but wrong fit, qualified, or can't tell, with the signs and outcome behind it.
2. **A source table:** spend, leads, verdict counts, junk share, spend that bought junk and cost per qualified lead for every campaign and network or placement, with leaks marked.
3. **The same counts by landing page and by form.**
4. **What your ad platforms count as a conversion,** and how much junk they counted.
5. **Fixes ranked by the spend tied to the leads they address,** each saying whether it saves ad spend, sales time or the bidding signal.
6. **A list of checks that couldn't run,** and why.

## What it can change for you

With your yes on the exact change, it can:
- add negative keywords in Google Ads taken from the search terms behind wrong-fit leads
- make a raw form conversion secondary in Google Ads, once a qualified lead import has run for 30 days

Everything else (networks, placements, location settings, the form itself) comes as exact steps for you or your developer.

## Tips

- Ask sales to record a reason on every disqualified lead. "Not the homeowner" or "outside the area" tells the skill which fix to write.
- Add a hidden timing field to your form even before you fix anything. It turns a guess about bots into a measurement.
- Run it again two weeks after the fixes to see the junk share move.
