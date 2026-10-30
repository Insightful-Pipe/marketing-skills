# How to Use This Skill

Hey Claude, I just added the "marketing-mix-model-builder" skill. Build a marketing mix model from our last two years of weekly sales and ad spend, and tell me what each channel really returns.

## What you need

- **Two years or more of weekly data (three is best):** total sales, orders or leads from every source, plus spend per channel. Paste or upload one weekly table, or let the skill pull it.
- **Or the InsightfulPipe MCP connected to Claude.** It pulls weekly spend from Google Ads, Meta, Microsoft Ads, LinkedIn, TikTok and Pinterest, and the outcome from Shopify, WooCommerce, Magento, BigQuery, Google Sheets or GA4. Weeks older than an API keeps (Pinterest keeps about 90 days) come from your exports, and so does spend from Snapchat, X, ads in ChatGPT and any channel without a connector.
- **Your promotion and event weeks:** sales, Black Friday, launches, price changes, stockouts.
- **Any lift tests you've run,** with the channel, dates, the incremental return and its interval. The model is calibrated with them.
- **Your total budget and limits,** if you want the split to respect them.

## Example requests

**What really drives sales**
Hey Claude, I just added the "marketing-mix-model-builder" skill. Here's our weekly revenue and spend by channel since 2023. Which channels really drive sales, and which ones are near their ceiling?

**Calibrate with a lift test**
Hey Claude, I just added the "marketing-mix-model-builder" skill. Pull our weekly spend and Shopify revenue and fit the model. We ran a Meta geo holdout in March that showed an iROAS of 1.7, between 1.3 and 2.0.

**Split the same budget**
Hey Claude, I just added the "marketing-mix-model-builder" skill. We spend about $21,000 a week across Google, Meta and TikTok. How should we split the same total, and what would it add?

**Is our data enough?**
Hey Claude, I just added the "marketing-mix-model-builder" skill. We're a small business with 15 months of data. Can we build a media mix model, or should we test instead?

**Export for Meridian or Robyn**
Hey Claude, I just added the "marketing-mix-model-builder" skill. Build the weekly dataset and give me CSV files ready for Meridian and Robyn.

## What you get

1. **A readiness check** before any fitting: weeks of data, whole-business outcome, missing weeks, spend share, spend movement, channels that move together and how many channels the weeks can separate. If the data can't carry a model, it says so and points to a lift test.
2. **The model:** carryover and diminishing returns per channel, with a check on 13 weeks it never saw, compared with a model that has no media at all.
3. **Calibration** against your lift tests, with the return before and after.
4. **Each channel's return as a range,** its marginal return at current spend, carryover half-life and how close it is to its ceiling.
5. **Response curves,** flagged where they go past any spend you've had.
6. **A budget split** for the same total, with limits, the extra weekly revenue as a range, and a two-step rollout.
7. **Two CSV exports** for Meridian and Robyn, including Robyn's calibration rows.

## What it can change for you

Nothing. It reads data and writes a report and two files. Budget changes stay with you.

## Tips

- Use total revenue or leads from your store or CRM, never the conversions an ad platform reports.
- Mark every promotion week. Without them, the model can credit a sale to the ads that ran beside it.
- Vary spend on purpose: a channel whose spend never moves can't be measured.
- Refit every quarter, and run a lift test on the channel with the widest range.
