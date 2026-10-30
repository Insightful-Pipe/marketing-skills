# How to Use This Skill

Hey Claude, I just added the "agency-client-health" skill. Check the health of every client I have connected and tell me which ones need attention first.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your clients' sources added:** ad accounts (Google Ads, Meta, LinkedIn, TikTok, Microsoft, Pinterest, Snapchat, X or OpenAI Ads), GA4, Search Console and Bing Webmaster, whichever each client uses. The skill finds them and pulls the data itself; you don't export anything.
- **A minute to confirm the client map.** The skill groups your connected accounts into clients and asks you to check the grouping before it grades anything.
- **Each client's main result and target cost per result,** if you have them. Without them, it uses each ad platform's own conversions and grades the trend.
- **For budget pacing:** your monthly budgets per client and platform, from a connected Google Sheet or pasted, and each client's tolerance (10% either side if you don't say). With no ad account connected, paste month-to-date and last-7-day spend per line instead.
- **For the access audit:** the list of who should have access, who is leaving, and the user lists the connector can't read (GA4, Tag Manager, Search Console, Meta Business settings, LinkedIn, TikTok, Shopify, Klaviyo), pasted or as screenshots. Google Ads users and manager links, and the Meta account's owner and partners, are read live, and so are LinkedIn Page admins and Merchant Center users when those are connected.

## Example requests

**Portfolio overview**
Hey Claude, I just added the "agency-client-health" skill. Give me a health overview of all my clients for the last 30 days, worst first.

**Churn risk**
Hey Claude, I just added the "agency-client-health" skill. Which of my clients are most likely to leave? Show me the signals and a save plan for each.

**New client onboarding**
Hey Claude, I just added the "agency-client-health" skill. We just signed a new client and they connected their accounts. Audit every connected source and tell me what's missing before we start.

**Account takeover**
Hey Claude, I just added the "agency-client-health" skill. We're taking over this client's Google Ads account from another agency today. Freeze the baseline and tell me what the last team left behind.

**Budget pacing across clients**
Hey Claude, I just added the "agency-client-health" skill. Our monthly budgets are in the pacing sheet I connected. Show me every client's spend against budget, where each one lands by month end, which campaigns went dark, and the daily budgets to fix today.

**Access and offboarding audit**
Hey Claude, I just added the "agency-client-health" skill. Our old agency stopped working with this client last month. Check who still has access to the client's Google Ads and Meta accounts, and here are the GA4, Tag Manager and Shopify user lists. Give me the clean-up list and an offboarding checklist.

## What you get

1. **A client map:** every connected source grouped by client, with its access level and status, confirmed by you.
2. **Seven checks per client:** connections and access, tracking, results, cost per result, spend, organic demand and account activity, each green, amber or red with the numbers behind it.
3. **A health score out of 100 and a churn risk level** for each client, with the math shown.
4. **The shape you asked for:** a portfolio table, a churn-risk report with save plans, an onboarding audit with missing sources and a baseline, a takeover audit with a frozen baseline and the last team's change history, a budget pacing board with a fix-today list, or an access map with ranked risks and an offboarding checklist.
5. **Next steps,** pointing to the right skill for a deeper look.

## What it can change for you

Only budgets, and only when you say yes. The pacing board drafts new daily budgets, and it can apply the Google Ads and Meta ones one at a time after you confirm each. Everything else is read only, and the access audit never adds or removes anyone: you make those changes in each platform with its checklist.

## Tips

- Run the portfolio overview every Monday, and the churn-risk report before each client's monthly call.
- Tell the skill what the data can't see: a contract ending, a new contact on the client side, slow replies. It raises the churn risk for each one you confirm.
- Run the takeover audit on day one, before anyone changes the account, and save the baseline it gives you.
- Run the pacing board twice a week, and every day in the last week of the month.
- Run the access audit whenever an employee, freelancer or agency leaves, and once a quarter for every client.
