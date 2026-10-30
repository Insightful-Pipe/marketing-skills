# How to Use This Skill

Hey Claude, I just added the "b2b-lead-enrichment" skill. Clean my inbound lead sheet, enrich every company, and rank the leads by fit with our ICP.

## What you need

- **The InsightfulPipe MCP connected to Claude.** The enrichment crawlers are built in. Add Google Sheets if your leads live in a sheet, or Airtable if they live in a base (the Airtable path is untested until a base is connected).
- **Your ICP:** core and adjacent industries, an employee range, the regions you sell to, and up to 8 technologies that signal a good fit. Leave out what you don't know; that part of the score is skipped.
- **Domains to exclude:** your own, current customers and competitors.
- **For the weekly watch:** your target accounts (name and domain), the deals sales is already working, the team your product serves, and last week's watch table if you have one. Connections are optional: you can paste what you saw instead.
- **For a pre-call brief:** the company's name or website, what you sell and the main problems it solves, and who is in the meeting.

## Example requests

**Clean and dedupe**
Hey Claude, I just added the "b2b-lead-enrichment" skill. Clean the "Inbound" tab of my leads sheet: remove duplicates, bad addresses and personal emails, and group leads by company.

**Enrich and score**
Hey Claude, I just added the "b2b-lead-enrichment" skill. Enrich and score these leads. Our ICP is logistics software companies with 100 to 1,000 employees in North America.

**Tech stack and funding for target accounts**
Hey Claude, I just added the "b2b-lead-enrichment" skill. Look up the tech stack and latest funding for these five target accounts, with a source for every fact.

**Decision-makers and outreach**
Hey Claude, I just added the "b2b-lead-enrichment" skill. For the tier A accounts, map the decision-makers by role and draft a 3-email cold sequence for each.

**Weekly buying signal watch**
Hey Claude, I just added the "b2b-lead-enrichment" skill. Here are my 15 target accounts, our open deals and last week's watch table. Check them for buying signals this week (new ads, hiring in marketing, new pricing or product pages, app releases, leadership hires) and give me the short list with a first line for each.

**Pre-call account brief**
Hey Claude, I just added the "b2b-lead-enrichment" skill. I have a first call with northwind-logistics.example on Thursday. We sell route planning software. Build me a one-page research brief with discovery questions and an opening angle.

**Write it back**
Hey Claude, I just added the "b2b-lead-enrichment" skill. Score my leads, then write the enriched list to a new tab in the same sheet. Show me the rows first.

## What you get

1. **A cleaning summary:** rows in, invalid, duplicates, personal addresses, excluded, and unique companies.
2. **A ranked account list:** each company with an ICP score out of 100, a tier (A to D), a confidence level, and the math behind it.
3. **Account cards:** industry, headquarters, employees, funding, technologies and growth signals, each with its source.
4. **A decision-maker map** for tier A accounts, by buying role.
5. **Cold email drafts:** 3 short emails per tier A account, each built on a fact from the enrichment.
6. **Unknowns and conflicts:** what nobody published, and where sources disagreed.
7. **In the weekly watch:** this week's short list of accounts with dated, linked signals, a priority score with the math, what changed since last week, a first line for each, and the table to keep for next week.
8. **In the pre-call brief:** a one or two page brief on one company that opens with what to say in the first minute, then dated changes, how it markets itself, the leaders it publishes, likely priorities, problems to test and discovery questions.

## What it can change for you

With your yes on the exact change, it can:
- write the enriched list to a new tab in your Google Sheet (it never overwrites your source tab)
- save each week's signal watch table to a new tab, so next week's run can show what changed
- write scores back to Airtable records, or add new accounts there (untested until a base is connected)

It never sends email and never guesses personal contact details.

## Tips

- Enrichment runs per company, not per lead, so ten leads from one company cost the same as one.
- Each crawler call takes 20 seconds to 2 minutes. For long lists, run the top 25 companies first.
- "Unknown" means nobody published it where the crawlers looked. Fill it in yourself and ask for a rescore.
- Third-party numbers are labelled as estimates. Check them before you quote them to a prospect.
- Run the watch on the same day each week. A signal counts in full for 30 days, at half for days 31 to 90, then drops out.
- The watch never puts website-visit or ad-engagement data into a first line. It uses them to decide who to write to, not what to say.
