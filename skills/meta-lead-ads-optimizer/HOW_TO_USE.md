# How to Use This Skill

Hey Claude, I just added the "meta-lead-ads-optimizer" skill. Our Facebook lead ads bring plenty of leads but sales says half are junk. Which forms and audiences bring leads that turn into customers? Leads CSV and CRM export attached.

## What you need

- **Your leads and your costs.** Either the InsightfulPipe MCP connected to Claude with your Meta ad account added (the skill reads your instant forms, ads and spend itself), or two files: an Ads Manager report with spend and leads by ad, and the leads CSV you download from Meta.
- **What sales did with the leads:** a CRM export or sheet with one row per lead, its stage, and the stage dates. If your CRM is a Google Sheet and the Google Sheets MCP server is connected, the skill reads it directly. Without it, the skill stops at cost per lead and says so.
- **Optional:** your target cost per qualified lead, whether sales calls every lead, how often your CRM could send stages to Meta, and each form's type (more volume or higher intent) as Ads Manager shows it.

## Example requests

**Lead quality by form and audience**
Hey Claude, I just added the "meta-lead-ads-optimizer" skill. Here's our Meta leads CSV and the CRM export. Rank our instant forms and ad sets by cost per qualified lead, not cost per lead.

**Improve Facebook lead quality**
Hey Claude, I just added the "meta-lead-ads-optimizer" skill. Our Facebook leads don't answer the phone. Review our instant forms and tell me what to change.

**Higher intent or more volume**
Hey Claude, I just added the "meta-lead-ads-optimizer" skill. Should our instant forms use the higher intent type? Compare what each form type brings in booked appointments.

**Conversion leads optimization**
Hey Claude, I just added the "meta-lead-ads-optimizer" skill. Are we ready to optimize our Meta lead campaigns for qualified leads instead of form submits? Check Meta's requirements against our CRM.

**Rewrite a form**
Hey Claude, I just added the "meta-lead-ads-optimizer" skill. Rewrite our worst instant form and show me the new form before you create it.

## What you get

1. **A map** of every instant form, its type, and the ads and ad sets that feed it, with any leads that expired before anyone downloaded them.
2. **A check of every active form:** its type (more volume or higher intent), length, a question to qualify on, free-text questions, phone and the thank-you screen.
3. **Cost per lead and cost per qualified lead side by side,** by form, ad set and ad, with reached, qualified, booked and won rates.
4. **Rows that look cheap in Ads Manager but cost the most per qualified lead,** named first, and a winning form only once there are enough leads to be sure.
5. **Junk leads and speed to lead:** duplicates, bad emails and phones, and how much more often sales reaches leads called within the hour.
6. **A readiness check for conversion leads optimization** against Meta's published requirements.
7. **The weakest form rewritten,** with the exact body to create it, marked "not run" until you say yes.
8. **Up to 5 next moves,** each with the numbers behind it.

## What it can change for you

With your yes on the exact body, it can create the rewritten instant form on your Facebook Page. A new form collects nothing until an ad uses it; you point your ads at it in Ads Manager. It never edits or archives a live form, ad or ad set, and never changes budgets.

## Tips

- Give it at least 90 days of leads. Leads younger than 14 days aren't judged, because sales hasn't had time to work them.
- Make sure your CRM keeps Meta's lead id. It makes the join exact, and Meta's conversion leads optimization uses it too.
- Run it again a month after switching forms to see the cost per qualified lead move.
