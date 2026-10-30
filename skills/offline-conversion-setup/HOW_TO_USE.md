# How to Use This Skill

Hey Claude, I just added the "offline-conversion-setup" skill. Here is our CRM export. Set up offline conversions so Google Ads, Microsoft Ads and Meta learn which leads become customers.

## What you need

- **A CRM export of your leads from the last 180 days,** one row per lead: when it came in, where from, the entry path (form, quote tool, call), any click IDs the CRM stores, the date each stage was reached and the value of won deals. Paste it, upload it, or point to the Google Sheet or BigQuery table.
- **Your CRM stages in order,** and which ad platforms you run.
- **Optional: the InsightfulPipe MCP** with your ad accounts and GA4 added. The skill then reads your conversion actions, Google's upload results and your offline goals itself, and can create the actions and send the uploads once you say yes.

## Example requests

**Set it up from scratch**
Hey Claude, I just added the "offline-conversion-setup" skill. We have never sent CRM results back to the ad platforms. Here is our lead export. Build the whole setup.

**Capture the GCLID in a hidden form field**
Hey Claude, I just added the "offline-conversion-setup" skill. Write the script that keeps the GCLID, MSCLKID, FBCLID and UTMs in hidden fields on our forms, and tell me which forms are losing them.

**Fix uploads that get rejected**
Hey Claude, I just added the "offline-conversion-setup" skill. Our Google Ads offline import says most uploads failed. Find out why from our account and CRM export.

**Pick what the ads should bid on**
Hey Claude, I just added the "offline-conversion-setup" skill. Should Google Ads bid on qualified leads, booked meetings or closed deals? Decide from our own numbers and put a value on each stage.

**Upload a batch**
Hey Claude, I just added the "offline-conversion-setup" skill. Upload yesterday's qualified leads to Google Ads and Microsoft Ads. Show me the rows first.

## What you get

1. **A scorecard** for each platform: how many leads keep their click ID (and which entry path loses them), stage volumes, stage timing against each platform's window, upload health, and what bidding learns today.
2. **The stage each platform should bid on,** decided from your own monthly counts and timing, with the reason each deeper stage was ruled out.
3. **A value for every stage,** from your own win rates, with the math.
4. **The capture script** and the hidden fields to add, plus the fix for each leak.
5. **A stage map** of CRM stages to conversion actions on Google Ads, Microsoft Ads, Meta, LinkedIn, ChatGPT Ads and GA4.
6. **A daily upload runbook** with an example payload per platform, marked not run.
7. **A match check** to run one week after the first uploads.

## What it can change for you

With your yes on the exact change, it can create Google Ads upload actions and Microsoft Ads offline goals, raise a Google action's lookback window, upload batches to Google Ads and Microsoft Ads, create ChatGPT Ads event settings and send their conversion events, and create the GA4 Measurement Protocol secret and key event. For Meta and LinkedIn it writes the Conversions API spec for your developer or CRM integration.

## Tips

- Install the capture script first. Every later step depends on leads keeping their click IDs.
- Upload daily. Monthly uploads miss Meta's 7-day limit and let Google clicks expire.
- Keep the new stage secondary for 14 days before bidding moves onto it.
