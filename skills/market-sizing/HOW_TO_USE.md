# How to Use This Skill

Hey Claude, I just added the "market-sizing" skill. Size our market as TAM, SAM and SOM for this year, show the math, and tell me what share we can realistically win in three years.

## What you need

- **Who you sell to and where:** the kinds of business (or customer) you serve and their size, the countries you sell in today and the ones you can't serve yet, and your plans and prices (or average spend per customer).
- **Any figures you already have:** business or customer counts by segment, a published market figure with its publisher and date, your current customers, new customers in the last 12 months, churn and your sign-up to paid rate.
- **10 to 40 category search terms** a buyer would type, and your brand terms to leave out.
- **Optional, with the InsightfulPipe MCP connected:** DataForSEO for search volume by country, Search Console and Google Ads for your share of search and impression share, GA4 for the sign-up rate, and Shopify or WooCommerce for customers and orders if you run a store (the store paths were untested when this skill was built, because no store was connected, and the DataForSEO call returned no data on the login available then; you can paste Keyword Planner volumes instead).
- **No connection at all?** Paste the figures. Every step runs the same way, and anything missing is labelled assumed with a wide range.

## Example requests

**TAM, SAM and SOM from scratch**
Hey Claude, I just added the "market-sizing" skill. We sell scheduling software to dental practices in the US and Canada at $79 a month. Work out TAM, SAM and SOM for 2026 and label where every number comes from.

**How to calculate market size with my own data**
Hey Claude, I just added the "market-sizing" skill. Use our Search Console, Google Ads and GA4 plus search volumes for the UK and Ireland to check how big our market is and how much of it we can win.

**Check a number from a report**
Hey Claude, I just added the "market-sizing" skill. An analyst report says our category is worth $2.1 billion in 2023. Restate it to this year, cut it to our segment, and check it against a bottom-up count.

**A store**
Hey Claude, I just added the "market-sizing" skill. We run a Shopify store selling refillable cleaning products in the US. Size the market and use our customers and orders for the three-year share.

## What you get

1. **The answer first:** TAM, SAM and SOM in year 3 as low, base and high, and your share of SAM today.
2. **An inputs table:** every number labelled sourced (with link and date), measured, given or assumed, with its range.
3. **Three methods side by side:** bottom-up, top-down restated to the sizing year, and a demand check from search volume, with a verdict on whether they agree.
4. **Your share of search** by country, its trend, and the paid impression share lost to budget and rank.
5. **A three-year SOM** built year by year from your customers, retention, conversion rates and share of search.
6. **A sensitivity table** showing which inputs move the answer most, and what to research next.

## What it can change for you

With your yes on the exact change, it can add a "Market sizing" tab to a Google Sheet you name and write the model into it. It never writes to an existing tab, and it never changes campaigns, budgets, store data or Search Console.

## Tips

- Settle the scope grid first: mark each vertical, country and size band as SAM or TAM only, with the reason. A SAM that quietly counts a country you can't take payments in yet is the quickest way to inflate the answer.
- A search volume tells you people are looking, not how much they spend. The skill uses it to check buyer counts, never as a dollar figure.
- List search terms in every language your buyers use. A country that looks small in search often searches in a second language.
