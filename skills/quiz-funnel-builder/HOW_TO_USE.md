# How to Use This Skill

Hey Claude, I just added the "quiz-funnel-builder" skill. Build a quiz funnel for my store from what people actually buy, with the follow-up emails for each result.

## What you need

- **What you sell and who buys it.** A store link, a product list or a services page is enough.
- **The goal:** more subscribers, sales from the quiz itself, or qualified leads for a call.
- **Your customer groups, with numbers, if you have them.** Connect Shopify, WooCommerce, Klaviyo, Mailchimp or GA4 through the InsightfulPipe MCP and the skill reads them itself, or paste a sales-by-product export, segment sizes or audience sizes. Without numbers it still builds the quiz, and marks the results "not measured".
- **The deepest discount you'll give.** Without it, no email offers a percent off.
- **To check a quiz you already have:** its questions, its answers and the points or result each answer gives.

## Example requests

**Product recommendation quiz from Shopify**
Hey Claude, I just added the "quiz-funnel-builder" skill. Build a product finder quiz from our Shopify sales, write the result pages and three emails per result, and tell me what to track in GA4. We never go above 10% off.

**Lead generation quiz for a service business**
Hey Claude, I just added the "quiz-funnel-builder" skill. We run a physiotherapy clinic. Design a lead generation quiz that sorts people by their problem and sends each group the right follow-up. Here are our Klaviyo segments and their sizes.

**Self-assessment scorecard**
Hey Claude, I just added the "quiz-funnel-builder" skill. Turn our onboarding checklist into a scorecard quiz for agencies: score bands matched to our Klaviyo segments for small, growing and large agencies, a result for each band, and emails that lead to a call.

**Check a quiz you already have**
Hey Claude, I just added the "quiz-funnel-builder" skill. Here are our quiz questions and the result each answer leads to. Check whether every result can be reached and none takes over, fix the scoring with the smallest change, and tell me what the funnel is missing.

**Read the drop-off after launch**
Hey Claude, I just added the "quiz-funnel-builder" skill. Our quiz has been live for a month. Pull the quiz events from GA4 and show me which question loses the most people.

## What you get

1. **A table of your customer groups,** showing which became results and which are add-ons, with the numbers behind each.
2. **The quiz:** questions, answers, points and the tie order.
3. **A path check:** every answer combination counted, so each result is reachable and none takes over the quiz. For a scorecard it also sets the band cut-offs so each band gets a fair share of paths.
4. **The email screen:** where it goes for your goal, what it asks for and the consent line.
5. **A result page and three emails per result,** each tied to the products or offer that result leads to.
6. **The tracking plan:** the GA4 events, the custom dimensions and key event to add, and the email platform setup.
7. **The quiz as a JSON data file** for any quiz tool, and a single HTML file when you ask for one.

## What it can change for you

With your yes on the exact change, it can:
- add the GA4 custom dimensions and mark `generate_lead` as a key event
- create a Klaviyo list for quiz takers and the follow-up emails as Klaviyo templates
- create a Mailchimp quiz result field and the emails as Mailchimp templates

It never sends emails, starts flows, publishes pages or creates discount codes.

## Tips

- Give it 12 months of sales if you can; a shorter window over-weights whatever was on promotion.
- Keep the quiz to 5 to 8 questions. Every extra question loses people.
- Run the drop-off read once the quiz has 100 starts, then rewrite or cut the question that loses the most people.
