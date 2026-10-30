# How to use Buyer Persona Builder

Hey Claude, I just added the "buyer-persona-builder" skill. Build buyer personas from my real customer data and tell me which ones the evidence actually supports.

## What you need

- The InsightfulPipe MCP connected to Claude.
- At least one of: Search Console, GA4, LinkedIn Ads, Meta Ads, YouTube, Klaviyo, Google Business Profile or Facebook Pages. More sources give stronger personas.
- Optional: customer text to paste (reviews, support tickets, call notes, survey answers). It's the best input for pains and sentiment.
- For the interview planner, the voice of customer analysis and the segment ranking, nothing has to be connected: paste or upload the text or the export. Connected stores, email lists, review and comment sources, Google Sheets or BigQuery let Claude pull it instead.

## Example prompts

- "Who are my customers really? Build personas from my data."
- "Build an ICP from my LinkedIn Ads and Search Console data."
- "Segment my audience and tell me which segment to target first."
- "Here are 40 support tickets. What are the main pains, and how do people feel about us?"
- "Write an interview script and a survey to test my personas."
- "Let me talk to the clinic-manager persona."
- "We want to sell to dental clinics. What would our ICP look like there?"
- "Plan 12 customer interviews: who to invite from my Klaviyo list, a screener, the interview questions and the consent wording."
- "Here are 30 call transcripts and our Google Play reviews. Run a voice of customer analysis by plan and by quarter."
- "Here's our CRM export of closed deals. Which customer segments win most often, pay most and stay longest?"

## What you get

1. **Evidence coverage:** which sources were used, which were missing and why.
2. **Segments,** each with its size and the sources behind it.
3. **Up to 3 personas and 1 anti-persona.** Each has who they are, their job to be done, trigger, pains, alternatives, where to reach them, the words they use, and a confidence rating.
4. **An ICP scorecard** with fit criteria and disqualifiers.
5. **A jobs and pains map,** with sentiment when there's enough customer text.
6. **A validation kit:** an interview script and a survey aimed at the weakest claims.
7. **A role-play mode,** where the persona answers only from the evidence.
8. **A customer interview plan,** when you ask for one: invite pools with counts, how many interviews per segment, a screener, a discussion guide built around the moment they switched, consent wording and a note template.
9. **A voice of customer theme table,** when you ask for one: themes counted by person, split by segment and quarter, tied to customer value where it can be, and checked against search demand and your own ad and site wording.
10. **A best-fit segment ranking,** when you ask for one: segments ranked on win rate, average value and retention together, the ones with too little data held back, and how your ad reach compares with who actually buys.

## What it can change for you

If you say yes to the exact change, it can save a persona as a GA4 audience, or write the interview shortlist (ids only), the theme table or the ranking to a new tab of your Google Sheet. It never changes ad targeting or lists, and never sends invites or other messages to customers.

## Tips

- Tell it what counts as a customer (a key event, a purchase, a lead). Without conversion data, the personas describe engaged audiences, and the report says so.
- Paste 20 or more pieces of customer text if you can. Below that, you get quotes but no sentiment percentages.
- Run it again each quarter, or after you launch in a new market.
