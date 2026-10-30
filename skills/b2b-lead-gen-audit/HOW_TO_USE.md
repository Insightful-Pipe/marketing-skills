# How to Use This Skill

Hey Claude, I just added the "b2b-lead-gen-audit" skill. Audit how my business gets leads, from search and ads to the form, and tell me the fixes worth the most.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** GA4 is the one source the audit can't run without.
- **Search Console** for the search demand check, and **LinkedIn Ads, Google Ads or Meta** for the paid checks. The audit skips any source you haven't connected and says so.
- **Your business type:** B2B, real estate or legal services. It changes what counts as a lead, which searches show buying intent and how audience fit is judged.
- **Your target cost per lead,** if you have one. Without it, the skill uses your own blended cost per lead.
- **Optional CRM numbers** for the same period: leads, qualified leads, clients won and how fast you answer a new lead. Without them, lead quality is graded only from what GA4 records.

## Example requests

**B2B audit**
Hey Claude, I just added the "b2b-lead-gen-audit" skill. We sell software to finance teams. Audit our lead generation for the last 90 days across GA4, Search Console and LinkedIn Ads. Our target cost per demo request is $250.

**Real estate**
Hey Claude, I just added the "b2b-lead-gen-audit" skill. I'm a real estate agent in Austin. Audit where my buyer and seller leads come from and where the website loses them.

**Legal services**
Hey Claude, I just added the "b2b-lead-gen-audit" skill. We're a personal injury firm in Ohio. Audit our lead flow, calls and forms, and tell me what our cost per case lead really is.

**Leads dropped**
Hey Claude, I just added the "b2b-lead-gen-audit" skill. Our demo requests fell this quarter. Audit the whole lead path and show me where it breaks.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for seven areas:** lead tracking, lead sources, search demand, lead pages and forms, paid lead cost, audience fit, and lead quality and follow-up.
3. **The top 5 fixes,** ranked by how many leads or how much spend they touch, each with the numbers behind it.
4. **A list of what couldn't be checked,** and why.
5. **Next steps,** pointing to the right skill for a deeper look at each area.

## What it can change for you

With your yes on the exact change, it can:
- mark a lead event that already fires in GA4 as a key event, so GA4 counts it as a conversion
- switch a lead key event to count once per session, so a double submit counts as one lead

It never changes campaigns, budgets, bids, tags or your website.

## Tips

- Run it every quarter, and after any change to your forms, tracking or ad accounts.
- Give it your CRM counts: lead volume without lead quality is half an audit.
- If you run ads for several brands, say which GA4 property and ad account belong to the business you want audited.
