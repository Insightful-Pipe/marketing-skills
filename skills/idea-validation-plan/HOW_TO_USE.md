# How to Use This Skill

Hey Claude, I just added the "idea-validation-plan" skill. We're thinking about building a new add-on. Tell me if there's real demand, plan the cheapest tests that would prove it, and tell me what result means go or stop.

## What you need

- **The idea in one sentence, the buyer, and the price.** The rest has defaults the skill states.
- **Your gross margin and how long a customer may take to pay back,** if you know them. They set the pass and kill lines.
- **A test budget,** if you have one. The skill tells you what a readable test costs before you spend it.
- **Optional: the InsightfulPipe MCP** with DataForSEO for search demand and CPC, the ad libraries for who already advertises, and Google Ads, Meta, GA4, Search Console or Google Sheets for the test and the read-out. Without it, paste numbers from Keyword Planner and the Meta Ad Library, and the results from your ad platform and analytics. The DataForSEO calls were checked against the API schema but not run live when this skill was built; if one fails, it asks you for those numbers instead.

## Example requests

**Is there demand at all?**
Hey Claude, I just added the "idea-validation-plan" skill. I want to sell a bookkeeping service for dentists at $400 a month. Is there demand, and what's the riskiest thing I'm assuming?

**A fake door test**
Hey Claude, I just added the "idea-validation-plan" skill. Plan a fake door test for a new feature in our app, with the pass and kill numbers set before we launch it.

**Size a smoke test**
Hey Claude, I just added the "idea-validation-plan" skill. I have $2,000 to test this idea with Google Ads. How many clicks do I need to know if it works, and will $2,000 buy them?

**Read the results**
Hey Claude, I just added the "idea-validation-plan" skill. The waitlist test ended yesterday. Read the results against the plan and tell me: go, change or stop?

## What you get

1. **Desk demand:** searches for the problem in your buyer's words, the CPC advertisers pay, the 12-month trend, how many rivals already advertise, and who ranks.
2. **An assumption register,** scored, with the riskiest assumption named and the top three each given a test.
3. **Pass and kill lines from your own price and margin,** with the formulas, frozen with a date before anything runs.
4. **A sized test plan:** buyer conversations, a fake door or waitlist page with a paid smoke test, and a pre-sale, with visits needed, cost at 95% and 90% confidence, and the daily budget.
5. **A read-out** of each test against its lines, then the call: go, change or stop, and what to change.

## What it can change for you

With your yes on the exact payload, it can create the smoke test campaign in Google Ads or Meta. The campaign, ad groups and ads are created paused and the keywords go in paused, so nothing spends until you turn the campaign on. It never turns campaigns on or changes budgets.

## Tips

- Set the lines before you look at any result. A line moved afterwards proves nothing.
- Put the price on the test page. A sign-up without a price measures curiosity.
- Talk to buyers who don't know you. Friends and fans say yes to everything.
- If the paid test can't be afforded at 90% confidence, run the conversations and a pre-sale first; a half-sized test buys noise.
