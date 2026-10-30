# How to Use This Skill

Hey Claude, I just added the "conversion-rate-benchmark" skill. Is our store's conversion rate good for our industry, and is any gap worth a CRO project?

## What you need

- **Your numbers, one of two ways.** Paste or upload sessions, users, conversions and revenue by channel, device and new or returning visitors (a GA4 Explore export or a Shopify sessions report works). Or connect GA4 through the InsightfulPipe MCP and the skill pulls them itself.
- **Your industry,** in plain words: fashion, beauty, home and furniture, SaaS, legal.
- **What counts as a conversion:** purchases for a store, or the one lead or sign-up action that matters.
- **Optional:** your store's order count for the same dates (or a connected Shopify or WooCommerce store), so the skill can check GA4 isn't missing orders before it compares anything.

## Example requests

**The everyday question**
Hey Claude, I just added the "conversion-rate-benchmark" skill. What is a good conversion rate for an online fashion store, and how does ours compare? Use GA4 for the last 30 days.

**From a paste, no connection**
Hey Claude, I just added the "conversion-rate-benchmark" skill. Here are our sessions and orders by channel and device for September. We sell home furniture. Are we behind the industry, and where?

**Landing pages**
Hey Claude, I just added the "conversion-rate-benchmark" skill. Our SaaS demo landing pages get paid search, paid social and email traffic. Benchmark each channel against the right figure.

**A drop to explain**
Hey Claude, I just added the "conversion-rate-benchmark" skill. Our conversion rate fell this month. Tell me whether the site got worse or we just bought more cold traffic.

## What you get

1. **A two-sentence answer:** your rate, the benchmark it was compared with (source and year), and whether you are behind, in range or ahead.
2. **Your rates done properly:** per session and per user, by channel, device, visitor type and landing page type, each with a 95% interval so small segments aren't over-read.
3. **A fair benchmark:** an estimate of the industry figure at your own device mix, with its assumption stated, and channel figures only where a source publishes them for the same kind of page, compared with the same measure (per visitor for landing pages).
4. **Mix against rate:** how much of any change came from a different traffic mix, and how much from the site itself.
5. **Money on every gap,** and a ranked list of the gaps that justify a CRO project.
6. **Every source,** with the year of its data and the date it was read.

## What it changes

Nothing. It reads your data and reports.

## Tips

- Under about 10,000 sessions a month, ask for 90 days so each segment has enough traffic to judge.
- If you have your own benchmark from an agency or a paid report, paste it with its source and year; the skill will use it alongside the built-in table.
- Store-wide and landing page rates are different numbers. Say which one you mean, or the skill will ask.
- For landing pages, give their paths or the prefix they share (such as /lp/), so only sessions that start on them are judged.
