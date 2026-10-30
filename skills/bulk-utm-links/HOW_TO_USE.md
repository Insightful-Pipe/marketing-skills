# How to Use This Skill

Hey Claude, I just added the "bulk-utm-links" skill. Build the UTM links for our November launch from this list, and tell me which GA4 channel each one will land in.

## What you need

- **A list of the links,** pasted or typed: the page each link goes to, where it goes out (newsletter, post, ad, creator, partner, QR code) and the campaign. Nothing has to be connected.
- **Whether each creator or partner is paid,** and how (a flat fee, a commission, or unpaid). It decides the medium.
- **Optional, through the InsightfulPipe MCP:** GA4, so new links reuse the spellings your reports already hold; your team's Google Sheet, so rows go where the team keeps them; and your ad accounts, for live campaign names and a rename map.

## Example requests

**A launch**
Hey Claude, I just added the "bulk-utm-links" skill. Here are 20 links for our waitlist launch: the newsletter, social posts, three creators, two partners, a flyer QR code and our Meta, LinkedIn and TikTok ads. Build them all.

**A newsletter**
Hey Claude, I just added the "bulk-utm-links" skill. Tag every link in this week's newsletter by its position in the email.

**Creators and partners**
Hey Claude, I just added the "bulk-utm-links" skill. Make one link per creator and partner on this list. Two are paid a flat fee, one gets a commission.

**Naming and renames**
Hey Claude, I just added the "bulk-utm-links" skill. Name the campaigns for our new Meta and Google Ads launch, and give me a rename map for the campaigns that are live now. Don't change anything yet.

## What you get

1. **Every link, ready to send,** each with its source, medium, campaign and content.
2. **The values decided:** which spellings were reused from GA4 or your sheet, which were kept to avoid splitting a report row, and which are new.
3. **A channel check:** the GA4 default channel each link lands in, marked seen (GA4 already files it there) or predicted, with Unassigned links shown first.
4. **Warnings:** pages GA4 doesn't measure, old tags replaced, internal links left untagged, duplicates skipped.
5. **Names** for campaigns, ad sets or ad groups and ads on each platform, built from the same parts as the links.
6. **A rename map** for live campaigns, when you ask, with what each rename changes in GA4.
7. **The sheet rows,** written to your Google Sheet after you say yes, or as CSV to paste.

## What it can change for you

With your yes on the exact list, it can:
- add tabs to your Google Sheet and write the new rows below the existing ones
- rename campaigns, ad sets and ad groups in Google Ads, Meta and LinkedIn (TikTok and Microsoft Ads renames are untested until those accounts are connected)

It never changes budgets, status, targeting or ads, and never overwrites a filled sheet row.

## Tips

- Keep one sheet for all links. The skill reads it first, so the team's spellings and row numbers carry on.
- Use one campaign value for the whole launch. The source and medium already say where a click came from.
- After launch, check what GA4 received with `utm-auditor`, if installed.
