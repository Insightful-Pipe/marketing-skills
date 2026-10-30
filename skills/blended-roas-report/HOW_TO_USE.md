# How to Use This Skill

Hey Claude, I just added the "blended-roas-report" skill. Show me blended ROAS and CAC across all my ad platforms for last month, and which channel earns its share of the budget.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your ad accounts added:** Google Ads, Meta, LinkedIn, TikTok, Microsoft, Pinterest, Snapchat, X or OpenAI Ads, whichever you use. The skill finds them and pulls the data itself.
- **GA4, if you have it.** It gives the site-side view that doesn't count the same customer twice.
- **Your revenue and new-customer count for the period,** from your store, billing system or CRM. Without them the skill falls back to GA4 revenue and first-time purchasers, and says so.
- **What counts as a result** (purchase, lead, sign-up, booked call), and your monthly budgets if you want pacing.
- **For a marketing ROI report:** your gross margin, and each cost that isn't ad spend (agency and freelance fees, tools, content and creative, events, team time). The skill asks for each one by name.
- **No connection?** Paste each platform's spend, clicks and results, or type the totals. The ROI report runs on typed numbers alone.

## Example requests

**Blended ROAS and CAC**
Hey Claude, I just added the "blended-roas-report" skill. Revenue last month was $84,000 from 310 new customers. Give me blended ROAS and CAC across every ad platform, and CAC by channel from GA4 first-time purchasers.

**Spend share vs revenue share**
Hey Claude, I just added the "blended-roas-report" skill. Show me each channel's share of spend against its share of revenue for this quarter.

**Pacing**
Hey Claude, I just added the "blended-roas-report" skill. Our October budget is $20,000 on Google, $12,000 on Meta and $5,000 on LinkedIn. Are we on pace?

**Marketing ROI for the board**
Hey Claude, I just added the "blended-roas-report" skill. Calculate our marketing ROI for Q3 against Q2 for the board, with the agency fee, tools, the trade show and our marketing manager's salary in the cost, on a 44% gross margin, with payback.

**Google Ads vs Meta**
Hey Claude, I just added the "blended-roas-report" skill. Compare Google Ads and Meta head to head on purchases for the last 30 days.

**Google Ads vs Microsoft Ads**
Hey Claude, I just added the "blended-roas-report" skill. Is Microsoft Ads cheaper per lead than Google Ads for us?

**Meta vs TikTok prospecting**
Hey Claude, I just added the "blended-roas-report" skill. Compare our Meta and TikTok prospecting campaigns for last month.

**LinkedIn vs Google for B2B leads**
Hey Claude, I just added the "blended-roas-report" skill. Which brings cheaper B2B leads, LinkedIn or Google non-brand search? We had 14 qualified leads from LinkedIn and 9 from Google.

## What you get

1. **Blended numbers:** total ad spend, revenue, blended ROAS, new customers and blended CAC, against the period before.
2. **A row per channel:** spend and share, what the platform claims, what GA4 saw from that platform's tagged clicks, the site-side cost per result, CAC by channel (spend over the first-time purchasers GA4 saw from that channel, for stores), and whether the channel earns more or less than its share of spend.
3. **An over-claim ratio:** the platforms' claims added together, divided by what your site actually recorded from their clicks. It is the one place the claims are added up; they are never shown as a total.
4. **Checks before conclusions:** untagged ads, missing results, mixed currencies, accounts outside a platform's data window.
5. **Pacing or a head-to-head,** when you ask for one, with a verdict only when both sides have enough results to call it.
6. **A marketing ROI report,** when you ask for one: every cost line by quarter, ROI on gross margin next to ROI on revenue, ROI by channel with the shared costs kept on their own line, full-cost CAC, the payback period, and the formulas written out for finance.
7. **Up to three next steps,** each tied to a finding.

## What it can change for you

Nothing. It only reads your accounts. Budget moves go to the cross-platform budget allocator skill or to you.

## Tips

- Give it your real revenue and customer count. Platform numbers alone can't tell you what a customer costs.
- Tag every ad link with UTM parameters, so GA4 can credit each visit to the platform that paid for it.
- For a board report, give it your gross margin. Revenue ROI makes marketing look better than it is.
- Small numbers come back as "too small to call". That's on purpose: a channel with four results hasn't proved anything yet.
