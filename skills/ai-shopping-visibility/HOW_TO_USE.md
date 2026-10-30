# How to Use This Skill

Hey Claude, I just added the "ai-shopping-visibility" skill. Check which of my products ChatGPT and Google AI Overviews recommend when shoppers ask what to buy, and tell me why the others are missing.

## What you need

- **Your products.** Either a store connected through the InsightfulPipe MCP (Shopify, WooCommerce or Magento), or a product export or feed file. A typed list of products with prices works for a first look.
- **The questions shoppers ask,** if you have them. If not, the skill drafts 5 to 20 from your catalogue for you to confirm.
- **The answers.** With DataForSEO connected through InsightfulPipe, the skill pulls ChatGPT answers (with their product cards), Google AI Overviews and Claude, Gemini or Perplexity answers itself, after telling you how many paid calls that is. Without it, paste the answers you got from each assistant.
- **Optional:** Merchant Center and Search Console connected (or their exports), so it can check feed status and merchant listings.

## Example requests

**Full audit**
Hey Claude, I just added the "ai-shopping-visibility" skill. Draft 10 buying questions from my Shopify catalogue, run them on ChatGPT and Google AI Overviews, and show me which of my products get named and why the rest don't.

**From a paste**
Hey Claude, I just added the "ai-shopping-visibility" skill. Here's my product CSV and what ChatGPT and Perplexity answered for six questions. Match the answers to my products and find the data reason for every miss.

**A reseller wins the card**
Hey Claude, I just added the "ai-shopping-visibility" skill. ChatGPT shows my own product but sends shoppers to another store. Check which questions this happens on and what the cards show for price and stock.

**Rerun after fixes**
Hey Claude, I just added the "ai-shopping-visibility" skill. We fixed the feed prices and markup last month. Rerun the same questions and compare with the last run.

## What you get

1. **A scoreboard per assistant:** how many questions name one of your products, how many product chances you won, and on ChatGPT how often the card is your own store. Rival brands are counted beside you.
2. **A question table and a product table,** showing every product that fit a question and what happened to it on each assistant.
3. **The data reason for every miss:** not indexed, blocked to ChatGPT's crawler, missing from Merchant Center, a price or stock value that disagrees between feed, markup and store, missing markup, feed issues, no reviews, or a reseller's lower price.
4. **Fixes ranked** by how much they block and how many questions they win back.
5. **Drafts** of the supplemental feed rows and corrected Product markup, built only from your catalogue.
6. **The outside sites** the answers cite where rivals are named and you aren't.
7. **A list of what it couldn't see,** such as Google AI Mode or personalised answers.

## What it can change for you

Nothing. It's read-only. Feed rows, markup and robots.txt changes come as drafts for you or your developer to apply.

## Tips

- Keep the same questions between runs, so the numbers compare.
- Answers vary from run to run. Look at patterns across questions, not one answer.
- Give it your sale prices. A sale price that never reached the feed or markup can make a product look too expensive for an "under $N" question.
