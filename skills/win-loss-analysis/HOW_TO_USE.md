# How to Use This Skill

Hey Claude, I just added the "win-loss-analysis" skill. Here is our closed-deals export and our call notes for the last 12 months. Tell me why we win and lose, by competitor and channel, and what each team should fix.

## What you need

- **A deal export:** every deal created or closed in the window, open ones included, with created and close dates, status, amount, segment, company size, lead source, competitor and the reason logged at close. A list amount (or your price list) lets the skill measure discounts. Paste it, upload a CSV, or point to a Google Sheet or BigQuery table.
- **Call notes and buyer interviews,** each line with its deal id and date. Notes alone work; interviews make the reasons sharper.
- **Optional, for the channel check:** the InsightfulPipe MCP with GA4, Google Ads, LinkedIn Ads or CallRail connected, so the skill pulls lead counts itself. Without it, paste the lead counts per channel.

There is no CRM connector: the deals come from an export, a sheet or a BigQuery table.

## Example requests

**Full win-loss analysis**
Hey Claude, I just added the "win-loss-analysis" skill. Run a win-loss analysis on the attached export and notes for the last 12 months. Our deal size bands are under $10k, $10k to $30k and $30k and up.

**One competitor**
Hey Claude, I just added the "win-loss-analysis" skill. We keep losing to one competitor. Show me our win rate against them by company size, why we lose, and what our reps should say.

**Interview questions**
Hey Claude, I just added the "win-loss-analysis" skill. Write our win loss interview questions for next quarter, and tell me which buyers to call based on these closed deals.

**Which channels bring winnable deals**
Hey Claude, I just added the "win-loss-analysis" skill. Our deals are in a Google Sheet. Compare the lead source on our deals with Google Ads, LinkedIn Ads and GA4 leads, and tell me which channels bring deals we actually win.

## What you get

1. **Headline findings,** each with its numbers and the team it is for.
2. **Win rates** by competitor, segment, company size, deal size, lead source and sales-cycle length, each with its deal count, and any cut under 20 decided deals marked directional.
3. **Time to close and discount depth** for won and lost deals, including the pocket where you lose most.
4. **The reason logged at close next to what the buyer said,** with how often they agree.
5. **The main reasons for losing,** ranked, each with the note or interview lines behind it and a fix for product, pricing, messaging or sales.
6. **Themes to use against each competitor:** when you win, when you lose, what to say, what to prove it with, what to avoid.
7. **A channel check** of CRM lead source against platform lead counts.
8. **A buyer interview guide** and a deal log template for the next round.

## What it changes

Nothing. It reads your export, sheet or table and your platform reports, and it never edits the CRM, the sheet or an ad account.

## Tips

- Export at least a year of deals. With fewer than 20 decided deals in a cut, the skill can only call it directional.
- Log a competitor on every deal. Deals with none sit under "Not logged" and teach nothing about competitors.
- Keep the deal log template from the report and fill it in as deals close; next quarter's run reads it directly.
