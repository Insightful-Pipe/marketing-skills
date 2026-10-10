---
name: pricing-strategy
description: Builds a pricing strategy on live market data through the InsightfulPipe MCP. Reads your rivals' pricing pages itself (plans, prices, pricing metric, entry offer, enterprise gate, add-ons), prices every rival at the customer sizes you care about, measures how searchers shop on price (free-seeking share, rival price checks, switching searches, segment CPCs), optionally adds your own Search Console, GA4 and Stripe signals, then applies stated decision rules to recommend a value metric, entry offer, tiers, price points, value ladder and annual discount, with a perception review, a validation survey plan and pricing experiments. Use when someone asks what to charge, how to package or tier a product, whether to offer a free plan or a trial, how their prices compare, how to build a value ladder or offer stack, how buyers perceive their pricing, or how to plan a price increase.
---

# Pricing Strategy

A pricing plan built from what the market actually charges and how buyers actually search, not from a template. Every market finding comes from a page this skill reads or a call it runs, and every recommendation names the rule and the numbers behind it.

Pricing has three parts, and most teams only argue about the third:
1. **Packaging:** what each plan includes (features, limits, support, controls).
2. **Pricing metric:** the unit you charge for (seat, location, usage band, contacts, transactions, flat).
3. **Price point:** the amount, and how monthly and annual billing differ.

## Before you start

You need the InsightfulPipe MCP connected. DataForSEO is the main data source (pricing pages and search demand). Search Console, GA4 and Stripe are optional and add your own signals. Without DataForSEO, see "Without a connection" at the end.

1. Call `query_contexts` with `request="accounts"` for `platform="dataforseo"`, and for `google-search-console`, `google-analytics` and `stripe` if the user has them. Note `workspace_id`, `brand_id`, the Search Console `site_url` and the GA4 `property_id`.
2. Call `query_contexts` with `request="actions_details"` for `onpage_content_parsing` and `kw_google_ads_search_volume` (dataforseo), plus `search_analytics`, `get_report`, and `get_products`, `get_prices`, `get_subscriptions`, `get_coupons` (stripe) when those are connected. Follow the body shapes it returns.
3. Ask the user for these, and use the defaults if they don't know:
   - **Product and buyer:** what it does, who pays, self-serve or sales-led. Default: infer it from their site and say so.
   - **Current pricing,** or "new". Default: read their own pricing page in Step 1.
   - **3 to 5 rivals' pricing page URLs.** Default: propose the category leaders and confirm them before reading anything (each page is a paid call).
   - **Reference customer profiles:** 2 or 3 sizes measured in the unit that drives cost in the category (staff, seats, contacts, locations, orders). Default: smallest buyer, typical buyer, large buyer; for example 1, 3 and 10 staff.
   - **Goal:** growth (more customers), revenue (more per customer) or margin. Default: growth for a new product, revenue for an existing one.
   - **Value inputs (optional):** what one customer gains per month (extra revenue, hours saved times hourly cost, loss avoided) and your monthly cost to serve one. Without them, the value check in D8 is not run.
   - **Market (optional):** country and language. Default: United States, English (`location_code` 2840, `language_code` "en").

State the date the pages were read, the market and the rivals at the top of the report.

## How to run the queries

Every body goes through `query_data` with the `platform` it names. Rules:
- **DataForSEO costs money.** One call per pricing page plus one keyword call: about 5 to 7 paid calls for a run. Never loop or retry a paid call more than once.
- **Pages localise.** A page can come back in another language or currency depending on where it is fetched from. Always send `"accept_language": "en-US"` (or the user's market). Record the currency you got and keep other currencies out of the price math unless the user gives an exchange rate.
- If a call fails, keep going. Mark what it would have shown **unknown**, say which call failed and why, and never fill the gap with a guess.

## Step 1. Market price map

Read each rival's pricing page, and the user's own if they have one:
```json
{"platform": "dataforseo", "action": "onpage_content_parsing", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "url": "<PRICING_URL>", "accept_language": "en-US"}
```
The text is in `data[0].page_content.main_topic` (and `secondary_topic`); structured offers, when the page has them, are in `page_content.offers`.

**When prices are missing.** Many pricing pages draw their prices with scripts, and the parsed text then has plan names but no amounts. If a plan has no price in the parsed text:
1. Read the page with your own web fetch tool, if you have one, and take the amounts from the visible text next to each plan name and its billing label.
2. Otherwise ask the user for the amounts.
3. Otherwise mark the price **unknown**. Never estimate a price.

Note the source of every price (parsed page, web fetch or user) in the map. `"enable_javascript": true` is accepted but did not recover script-drawn prices in testing, so don't pay for a second call to try it.

**Record, per rival and plan, only what the page says:**

| Field | What to record |
|---|---|
| Plans | Plan names in order, including free and "contact us" plans |
| Price | The amount shown, the billing basis (annual-billed per month, or monthly) and the currency. When both are shown, keep both. |
| Metric | What the price multiplies by: per seat or user, per location, a band of calendars or contacts, included usage (bookings, emails, credits), transaction fees, or flat |
| Limits | The stated limits that decide which plan a buyer needs (users, calendars, locations, usage) |
| Entry offer | Free plan (and its cap), trial length, and whether a card is needed |
| Enterprise gate | "Contact us" or "starts at" plans, and the threshold that sends you there |
| Add-ons | Anything sold on top: credits, extra seats, setup services, assistants |
| Presentation | The default billing toggle, badges ("most popular", "best value"), anchors ("starts at $X"), annual saving shown |

Feature tables built from check-mark images parse as empty cells. Don't infer which plan has a feature from an empty cell; leave it out or ask.

## Step 2. Price every rival at your reference profiles

For each profile, find each rival's cheapest plan whose **stated limits** fit it, and compute the monthly price on annual billing (seat price × seats, band price, or price per location). If a rival only shows monthly billing, use that and say so.

- A plan with no stated limit for the profile's unit fits.
- A free plan counts at $0. Say what it costs instead, if the page says so (card fees, usage fees).
- A rival in another currency, or one whose metric can't be mapped to the profile (for example included bookings when the profile is staff), stays in the map but out of this table. Say why.

This table shows how each metric scales: seat pricing climbs with team size, band pricing climbs in steps, location pricing and fee-funded models stay flat.

## Step 3. Search demand and price sensitivity

One call with 20 to 30 keywords built from the category, the rivals and the segments:
```json
{"platform": "dataforseo", "action": "kw_google_ads_search_volume", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "keywords": ["<KEYWORD_1>", "<KEYWORD_2>"], "location_code": 2840, "language_code": "en"}
```
Each row gives `search_volume` (monthly average), `cpc` and `competition`. Build the list from these groups (C = category phrase, R = a rival, S = a segment):

| Group | Patterns |
|---|---|
| Head | "C", "C app" |
| Price research | "C pricing", "C cost", "R pricing" for every rival |
| Free-seeking | "free C", "free C app", "cheap C", "is <leader> free", "<leader> free plan" |
| Switching | "R alternative" for the 2 biggest rivals |
| Segment | "C for S", "S C" for each segment the user sells to |
| Enterprise | "enterprise C", "C for teams" |

Send both segment patterns for every segment the user names, and the whole list in one call. A keyword with no volume returns null: list it as "no data" and count it as 0 in the sums. Google Ads can merge close variants: two phrasings ("salon booking software", "booking software for salons") may come back with the same volume, CPC and monthly trend. List both, but count the pair once in a group's sum. Then compute:
- **Free-seeking share** = free-seeking volume ÷ (free-seeking + price-research volume). How strongly the market expects a no-cost way in.
- **Leader free check** = the leader's free-seeking volume ÷ "<leader> pricing" volume. How often buyers ask whether the leader is free before (or instead of) asking what it costs.
- **Segment CPC index** = a segment keyword's CPC ÷ the CPC of the highest-volume head keyword. What advertisers pay for that buyer relative to the average buyer, a proxy for how much that segment is worth.
- **Switching volume** per rival, and **enterprise volume**.

## Step 4. Your own signals (optional, when connected)

**4a. How searchers find your pricing (Search Console).** Last 90 complete days:
```json
{"platform": "google-search-console", "action": "search_analytics", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "site_url": "<SITE_URL>", "dimensions": ["query"], "start_date": "<START>", "end_date": "<END>", "row_limit": 1000}
```
Keep queries with a price word: price, pricing, cost, free, cheap, discount, coupon, plan, subscription, trial, vs, alternative. Group them like Step 3 and report impressions and clicks per group. This pull stops at 1,000 rows; when it returns exactly 1,000, say the shares are of the visible rows.

**4b. Does pricing traffic convert (GA4).** Last 30 complete days:
```json
{"platform": "google-analytics", "action": "get_report", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "property_id": "properties/<PROPERTY_ID>", "dimensions": ["pagePath"], "metrics": ["screenPageViews", "activeUsers", "sessions", "keyEvents"], "start_date": "<START>", "end_date": "<END>", "dimensionFilter": {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "pric"}}}, "limit": 20}
```
```json
{"platform": "google-analytics", "action": "get_report", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "property_id": "properties/<PROPERTY_ID>", "dimensions": ["eventName"], "metrics": ["eventCount", "totalUsers", "keyEvents"], "start_date": "<START>", "end_date": "<END>"}
```
Report sign-up or purchase key events per 100 pricing page viewers. If no key event fired in the window, the rate is **unknown**: a defined event that never fires measures nothing. The page itself (layout, anchors, objections) belongs to the Pricing Page Auditor skill.

**4c. What customers actually pay (Stripe).** Untested until a Stripe account is connected; the bodies follow the helper schema:
```json
{"platform": "stripe", "action": "get_products", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "active": true, "auto_paginate": true}
```
```json
{"platform": "stripe", "action": "get_prices", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "active": true, "auto_paginate": true}
```
```json
{"platform": "stripe", "action": "get_subscriptions", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "status": "all", "auto_paginate": true}
```
```json
{"platform": "stripe", "action": "get_coupons", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "auto_paginate": true}
```
From these: plan mix (active subscriptions per price), average revenue per customer, share on annual billing, share with a discount, trialing count, and cancellations in the last 90 days per plan. Amounts are in the smallest currency unit (cents): divide by 100.

**Signs you are underpriced** (any two): most customers sit on the cheapest paid plan while using it heavily; prospects rarely push back on price; you are well under the paid median at the typical profile (Step 2); cancellations rarely cite price; rivals raised prices recently. **Signs you are overpriced:** cancellations cluster on one plan, heavy discount use (over a third of active subscriptions), and pricing traffic that doesn't convert while other pages do.

## Step 5. Decisions

Apply each rule, show the numbers that triggered it, and say when the user's business makes a rule wrong. The thresholds are starting points.

| # | Decision | Rule |
|---|---|---|
| D1 | Entry offer | **Free plan** when the free-seeking share is 40% or more and at least half the rivals cost $0 at the smallest profile: cap it at the smallest profile. **Trial only** when the share is under 25% and fewer than half the rivals are free. In between, test a free plan against a reverse trial (everything unlocked for a set time, then the free plan). Trial length follows time to first value: 7 days when value shows in the first session, 14 as the default, 30 when setup takes days. A card up front gets fewer, more serious starts. Overrule the numbers when the product says otherwise: a free plan suits a product that spreads through use and costs little per free user; a trial suits one that needs setup before it shows value. |
| D2 | Value metric | Pick the unit that (a) grows as the customer gets more value, (b) the buyer can predict, (c) is hard to game, (d) you can measure, and (e) the category already accepts. Use Step 2 to show how each rival's metric scales across the profiles, and where seat pricing gets expensive. |
| D3 | Price points | **Core plan:** at or under the median paid rival price at the typical profile. **Growth plan:** at or under the median paid price at the large profile. Going above a median needs a named advantage buyers pay for, and a test. Adjacent paid plans sit 1.3× to 3× apart: under 1.3× they blur together, over 3× they leave a gap a middle plan should fill. |
| D4 | Plan count | Three rungs (entry, core, growth) by default, plus a contact-us rung when D5 says so. Use four or more only when the median paid price at the large profile is 5× or more the median paid price at the typical profile. |
| D5 | Enterprise rung | Add a contact-us rung when at least half the rivals show one, or the user has deals that need contracts or security reviews. Don't lead with it when enterprise search volume is under 100 a month. What enterprise buyers expect: single sign-on, audit logs, admin controls, an uptime commitment, security documents and a named contact. |
| D6 | Annual billing | Take one saving per rival: the largest the page shows (its "save up to" figure). Leave out rivals with no annual option or an amount with no billing label. Match the median of those savings, kept within 15% to 25%. Show annual prices by default only when most rivals do. Savings and the default toggle are not amounts, so rivals in any currency count in both. |
| D7 | Segment package | Test every segment the user names. A segment keyword with a CPC index of 2 or more and 100 or more searches a month is a segment worth a dedicated package. Price it against the rival plan that names the same segment, if there is one: at or under that plan, and 1.3× to 3× the plan it builds on. Compare all three in one unit: if the rival charges per location and your plans charge per account, compare at one location, say what each extra location costs at the rival, and say where a second location goes in your ladder. |
| D8 | Value ceiling | Only with value inputs: the price should stay at or under 10% to 25% of the monthly value one customer gets, and above the cost to serve. The floor that matters to the buyer is the next best alternative (Step 2), not your cost. Not run without the inputs; say so. |

## Step 6. Value ladder and offer stack

Lay out the rungs a customer climbs, from the first free or cheap step to the most expensive plan, and the add-ons around them:
- **Entry:** removes the reason not to start (D1).
- **Core:** where most customers should land; the plan you badge.
- **Growth:** for the large profile; adds capacity and the controls bigger teams need.
- **Band edges** (when the metric is a band): each paid rung covers up to twice the profile it is priced for, so a growing customer has headroom before the next step. With profiles of 1, 3 and 10 staff: entry 1, core 2 to 6, growth 7 to 20.
- **Segment package or custom rung:** D7 and D5.
- **Add-ons:** only ones the market already sells (Step 1): usage credits, setup or migration services, extra capacity, assistants. Each add-on should answer "what does a customer who outgrows this plan buy next?"

Separate rungs with the levers buyers understand: usage limits (staff, bookings, contacts), features, support level, and access and control (API, single sign-on, audit logs, admin roles). Limits that track the value metric (D2) make the best upgrade triggers.

Flag gaps: adjacent rungs more than 3× apart, a rung with no reason to upgrade into it, or an add-on that costs more than the next plan.

## Step 7. Perception and packaging review

From the pages (Step 1) and search (Steps 3 and 4a):
- **Price endings:** prices ending in 9 read as value; round prices read as premium and simple. Note what the category does.
- **Badges and anchors:** which plan rivals badge, and any "starts at" or high plan that makes the middle look reasonable (an anchor), or a weaker plan placed so the badged one looks like the obvious pick (a decoy).
- **Billing framing:** annual by default or monthly, and how the saving is shown (percent, months free, or per-month price). Small daily framing ("under $1 a day") makes a low price feel smaller; it doesn't help a premium position.
- **Entry wording:** how plainly rivals say "free" or "no card needed", and whether searchers are asking (leader free check).
- **Plan names:** names that say who the plan is for beat names that only say size.
- **Readable prices:** when a page draws its prices with scripts (Step 1 needed the fallback), search engines and AI assistants may not see them either. If the user's own page does this, recommend putting the prices in the page text.
- **Your page (if you have one):** the same checks on your plans, and the 4a query groups: many "free" or "cheap" queries landing on your pricing means the entry offer needs to be clearer, not cheaper.

## Step 8. Validate before you ship

The market map tells you where you can sit; buyers tell you what they will pay. Recommend at least one of these:
- **Van Westendorp price sensitivity survey:** ask each respondent four prices (too cheap to trust, a bargain, getting expensive, too expensive to consider). Plot the cumulative answers; the crossings give an acceptable range and a point of least resistance. Read at least 100 answers per segment you want to price separately, and show the product description, not just the name.
- **Gabor-Granger ladder:** ask "would you buy at $X?" and move up after a yes, down after a no. Ladder: the lowest, median and highest paid rival price at the typical profile, plus one rung 25% above the highest.
- **Conjoint:** for a big repackaging; buyers pick between plan bundles, which prices each feature and limit. Use it when plans differ on many features.

**Pricing experiments:**

| Test | Measure |
|---|---|
| Free plan vs reverse trial (D1) | Paid conversion by day 30 and 90, not sign-ups |
| Core price at two ladder points | Paid conversion and revenue per visitor to pricing |
| Annual default on vs off | Annual share and first-year revenue |
| Metric: seat vs band | Expansion revenue at 90 days |
| Plan names | Plan mix |

Test on new customers only, one change at a time, for at least one full billing cycle. If traffic is too thin for a split test, run the prices in sequence and compare like-for-like periods, or vary quotes in sales calls and track close rates.

**Before launch:** the pricing page and plan limits match, billing is set up for every plan and the annual option, sales and support know the new prices and the upgrade triggers, and the FAQ answers "what happens to my current plan?"

## Changing prices you already charge

Use this when Step 4 shows you are underpriced, or the user asks to raise prices:
1. **Pick the approach:** new customers only (existing ones keep their price, simplest, leaves money behind); existing customers at renewal with 60 to 90 days' notice and an option to lock the old price by switching to annual; a new plan with new value at the new price, which existing customers may choose; or a full restructure that maps each customer to the nearest new plan.
2. **Write the notice** with: what is changing and from when, what was added since they joined, exactly what it means for this customer, what they can do before the date, and who to contact. No surprises in the invoice.
3. **Watch** paid conversion on the pricing page (4b) and cancellations per plan (4c) for two billing cycles.

## Pricing and acquisition economics

Higher prices only help if retention holds. Lifetime value = monthly revenue per customer × gross margin ÷ monthly churn. Keep lifetime value at about 3× the cost to acquire a customer or better; a higher price gives more room to pay for ads, a lower price needs cheaper acquisition. For the full calculation on live ad spend, use the LTV:CAC Ratio Optimizer skill.

Advertise each rung to the buyer it fits: the entry offer to broad, problem-aware audiences; the core plan to high-intent searches ("<category> pricing", "<rival> alternative"); a segment package to the segment terms D7 found; the contact-us rung to named accounts.

## Report format

1. **Headline:** the recommended metric, entry offer, plans and prices in three lines, with the market, the rivals and the date the pages were read.
2. **Market price map:** one row per rival and plan, with each price's source.
3. **Price at your profiles:** the Step 2 table, plus who was left out and why.
4. **Demand signals:** free-seeking share, leader free check, segment CPC indexes, switching and enterprise volume, with the keyword table.
5. **Your own signals:** 4a to 4c, or "not connected" / "not run" with the reason.
6. **Decisions D1 to D8:** each with the rule, the numbers and the verdict.
7. **Recommended plans:** rung, metric, price ceiling, who it's for, the limit that moves a buyer up.
8. **Value ladder and gaps.**
9. **Perception review.**
10. **Validation plan and experiments.**
11. **Unknowns:** every price, check or signal that couldn't be read, and why.

## What this skill never changes

It changes nothing. It reads pages and data and returns a plan. It never edits prices, products or coupons in Stripe, and never edits your pricing page.

## Without a connection

If DataForSEO isn't connected, ask the user to paste each rival's plan names, prices, limits and entry offer (or read the pages with your web fetch tool), and to share any keyword volumes they have. Run Steps 2 and 5 to 8 on that, label the demand checks **unknown**, and say the market map came from the user.

## Go deeper

- **Pricing Page Auditor:** how the prices are presented and whether visitors act on them.
- **Marketing Psychology:** anchoring, decoys and price framing in more depth.
- **LTV:CAC Ratio Optimizer:** whether the new prices pay for acquisition.
- **Signup Flow CRO:** the free plan or trial start you chose in D1.

## Rules

- Never invent a price, limit or volume. Unknown is an answer.
- Quote rivals' facts in your own words, with the source per price.
- Keep currencies apart; never mix amounts in different currencies in a median (percentages such as annual savings carry no currency).
- Every recommendation names the decision rule and numbers behind it.
- A recommendation to go above the market median needs a named reason and a test.
- No more than about 7 paid DataForSEO calls per run without asking.
