---
name: ecommerce-ads-playbook
description: Comprehensive e-commerce advertising strategy covering Google Shopping, Meta catalog ads, Performance Max, and multi-channel funnel optimization. Triggers when user mentions "e-commerce ads," "online store advertising," "DTC ads," "Shopping campaigns," "product feed ads," or asks how to advertise their e-commerce store. Provides platform-specific tactics and full-funnel strategy for driving online sales.
---

# E-Commerce Ads Playbook

Selling products online has unique advertising dynamics. This playbook covers the complete e-commerce advertising strategy.

## Core Philosophy

**E-commerce is a full-funnel game.** You need awareness (prospecting), consideration (engagement), and conversion (retargeting) working together. Over-indexing on any single stage creates inefficiency.

**The Product Feed is Your Foundation.** Shopping ads, catalog ads, and Performance Max all rely on your product feed. A bad feed means bad ads, regardless of how clever your strategy is.

**ROAS is Not Profit.** A 4x ROAS sounds great until you factor in COGS, shipping, returns, and overhead. Think in terms of contribution margin, not revenue.

**Customer Acquisition vs. Customer Value:** Acquiring a customer who buys once at breakeven might be worth it if they have high LTV. Acquiring a discount-seeker at breakeven is just burning money.

**Channel Synergy Matters:**
- Google captures demand (high intent, searching)
- Meta creates demand (low intent, discovers)
- TikTok builds awareness and trends
- Email/SMS converts at near-zero marginal cost

---

## Required Context

### Must Have

**1. Business Fundamentals**
- Product catalog size (SKU count)
- Average order value (AOV)
- Target ROAS or CAC
- Current monthly revenue
- Monthly ad budget

**2. Product Feed Status**
- Platform: Shopify, WooCommerce, BigCommerce, etc.
- Feed quality: titles, descriptions, images, GTINs
- Google Merchant Center approval status
- Meta Catalog status

**3. Current Advertising**
- Channels currently running
- Campaign types active
- Current performance (ROAS, CPA, spend)
- Historical best performers

### Strongly Recommended

**4. Customer Data**
- Customer LTV or repeat purchase rate
- Purchase frequency
- Best-selling products
- Seasonal patterns

**5. Business Model**
- Direct-to-consumer only or wholesale too
- Margin structure
- Shipping economics
- Return rate

### Nice to Have

- Competitor advertising analysis
- Customer acquisition source breakdown
- Brand search volume trends
- Email/SMS performance data

---

## Full-Funnel Framework

### The E-Commerce Advertising Stack

```
┌─────────────────────────────────────────────────────────────────┐
│  AWARENESS (Top of Funnel)                                      │
│  Goal: Build brand, reach new audiences                         │
│  ├── Meta: Broad prospecting, Lookalikes                        │
│  ├── TikTok: Viral content, trends                              │
│  ├── YouTube: Brand videos, product discovery                   │
│  └── Display: Awareness campaigns                               │
│  Budget: 20-30% of total                                        │
├─────────────────────────────────────────────────────────────────┤
│  CONSIDERATION (Middle of Funnel)                               │
│  Goal: Engage interested users, build intent                    │
│  ├── Meta: Engaged audience retargeting                         │
│  ├── Google: Non-brand search, Shopping                         │
│  ├── YouTube: Product demos, reviews                            │
│  └── Email/SMS: Browse abandonment                              │
│  Budget: 30-40% of total                                        │
├─────────────────────────────────────────────────────────────────┤
│  CONVERSION (Bottom of Funnel)                                  │
│  Goal: Convert high-intent users                                │
│  ├── Google: Brand search, PMAX, Shopping                       │
│  ├── Meta: Cart abandoners, purchaser lookalikes                │
│  ├── Email/SMS: Cart abandonment, win-back                      │
│  └── Retargeting: Dynamic product ads                           │
│  Budget: 30-40% of total                                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Platform-Specific Strategies

### Google Ads for E-Commerce

**Campaign Type Hierarchy:**

| Priority | Campaign Type | Purpose | Expected ROAS |
|----------|---------------|---------|---------------|
| 1 | Brand Search | Capture branded demand | 5-15x |
| 2 | Performance Max | Full-funnel automation | 3-6x |
| 3 | Standard Shopping | Product-level control | 3-5x |
| 4 | Non-Brand Search | Category/product terms | 2-4x |
| 5 | Dynamic Remarketing | Cart/browse abandoners | 4-8x |
| 6 | Display Prospecting | Awareness | 1-2x |

**Performance Max Best Practices:**

| Setting | Recommendation | Why |
|---------|----------------|-----|
| Asset groups | By product category | Better creative relevance |
| Audience signals | Start broad, layer in | Signals are hints, not targeting |
| Final URL expansion | Off initially | Control landing experience |
| Brand exclusions | Add competitors, own brand | Prevent cannibalization |
| Search themes | Add 7-10 per asset group | Guide the algorithm |

**Shopping Feed Optimization Priorities:**

| Field | Impact | Optimization |
|-------|--------|--------------|
| Title | Critical | Front-load keywords, include attributes |
| Image | Critical | White background, no text, high quality |
| Price | High | Competitive, include sale prices |
| GTIN/MPN | High | Required for visibility |
| Product type | High | Use Google's taxonomy |
| Custom labels | Medium | Segment by margin, bestseller, season |
| Description | Medium | Include keywords, benefits |

**Shopping Campaign Structure:**

```
📁 Campaign: Shopping - High Priority (All Products)
  └── Ad Group: All Products
       └── Product Group: All Products

📁 Campaign: Shopping - Medium Priority (Category Breakout)
  ├── Ad Group: Category A
  │    └── Product Group: Category A products
  ├── Ad Group: Category B
  │    └── Product Group: Category B products
  └── Ad Group: Category C
       └── Product Group: Category C products

📁 Campaign: Shopping - Low Priority (SKU Level)
  └── Ad Group: Top Performers
       └── Product Group: Individual SKUs
```

---

### Meta Ads for E-Commerce

**Campaign Structure:**

| Funnel Stage | Campaign Type | Audience | Objective |
|--------------|---------------|----------|-----------|
| Prospecting | Advantage+ sales campaign | Broad / Lookalikes | Sales |
| Prospecting | Manual | Interest / Broad | Sales |
| Retargeting | Catalog Sales | Website visitors | Sales |
| Retargeting | Manual | Engagers, ATC | Sales |
| Retention | Catalog Sales | Past purchasers | Sales |

**Advantage+ Sales Campaigns (formerly Advantage+ Shopping):**

| Setting | Recommendation |
|---------|----------------|
| Budget | $100-500/day minimum |
| Existing customer cap | 20-30% |
| Country targeting | Single country |
| Creative | 10-15 ads of different formats |
| Attribution | 7-day click, 1-day view |

**Catalog Ads Best Practices:**

| Element | Optimization |
|---------|--------------|
| Primary text | Overlay benefit messaging |
| Headline | Dynamic: {{product.name}} |
| Description | Dynamic: {{product.price}} |
| Creative | Lifestyle images > white background |
| Collection format | Curate hero image + catalog grid |

**Retargeting Windows:**

| Audience | Window | Bid/Budget |
|----------|--------|------------|
| Cart abandoners | 1-7 days | Highest |
| Cart abandoners | 8-14 days | High |
| View content | 1-7 days | Medium |
| View content | 8-30 days | Lower |
| Past purchasers | 30-90 days | Varies |

---

### TikTok for E-Commerce

**When to Use TikTok:**

| Good Fit | Poor Fit |
|----------|----------|
| Visual products | Complex B2B |
| Younger demographic | 55+ target |
| Impulse purchases | High-consideration |
| Trend-friendly products | Boring necessities |
| <$100 price point | High-ticket items |

**TikTok E-Commerce Strategy:**

| Stage | Approach |
|-------|----------|
| Awareness | Spark Ads (boost organic), UGC content |
| Consideration | Product demos, reviews, tutorials |
| Conversion | TikTok Shop, direct response ads |

**TikTok Shop Integration:**

If available in your market:
- Link products to videos
- Enable live shopping
- Use affiliate creators
- Run Shop Ads campaigns

---

## Campaign Builds by Budget Level

### Starter: $5,000-$15,000/month

**Focus:** Profitable acquisition, limited testing

| Channel | % Budget | Campaign Types |
|---------|----------|----------------|
| Google | 60% | Brand Search, PMAX |
| Meta | 40% | Advantage+ sales, Retargeting |

**Strategy:**
- Let PMAX handle most prospecting
- Meta for catalog retargeting
- Build email list aggressively
- No TikTok, no YouTube yet

---

### Growth: $15,000-$50,000/month

**Focus:** Scaling winners, channel diversification

| Channel | % Budget | Campaign Types |
|---------|----------|----------------|
| Google | 50% | Brand, PMAX, Shopping, Non-brand |
| Meta | 40% | Advantage+ sales, Manual prospecting, Retargeting |
| TikTok | 10% | Testing / Prospecting |

**Strategy:**
- Segment PMAX by category
- Test manual Shopping for top products
- Meta manual campaigns for creative testing
- TikTok for younger demos / viral potential

---

### Scale: $50,000-$200,000/month

**Focus:** Full-funnel, multi-channel optimization

| Channel | % Budget | Campaign Types |
|---------|----------|----------------|
| Google | 45% | Full suite |
| Meta | 35% | Full suite |
| TikTok | 10% | Prospecting + Shop |
| YouTube | 5% | Awareness, Remarketing |
| Other | 5% | Pinterest, Snapchat (if relevant) |

**Strategy:**
- Incrementality testing to validate channels
- MMM or attribution modeling
- Creative testing program (weekly)
- International expansion

---

### Enterprise: $200,000+/month

**Focus:** Marginal efficiency, incrementality

| Channel | % Budget | Campaign Types |
|---------|----------|----------------|
| Google | 40% | Full suite + DSA |
| Meta | 30% | Full suite |
| TikTok | 10% | Full suite |
| YouTube | 10% | Awareness + Action |
| Programmatic | 5% | Display, CTV |
| Other | 5% | Emerging channels |

**Strategy:**
- Dedicated measurement team
- Marketing mix modeling
- Brand lift studies
- Retail media (Amazon, etc.)
- Influencer partnerships

---

## Key Metrics & Benchmarks

### E-Commerce KPIs

| Metric | How to Calculate | Benchmark |
|--------|------------------|-----------|
| ROAS | Revenue / Ad Spend | 3-5x target |
| CPA | Ad Spend / Purchases | <30% of AOV |
| CAC | Total Marketing / New Customers | <LTV/3 |
| AOV | Revenue / Orders | Varies |
| CVR | Purchases / Clicks | 1-3% |
| CTR | Clicks / Impressions | 1-2% |

### ROAS vs. Profit Reality Check

```
Revenue: $100
ROAS: 4x ($25 ad spend)
COGS: $40 (40%)
Shipping: $8
Returns: $5 (5% rate)
Payment processing: $3 (3%)
Ad spend: $25

Contribution margin: $100 - $40 - $8 - $5 - $3 - $25 = $19 (19%)

True unit economics matter more than ROAS.
```

### Channel Benchmarks (E-Commerce)

| Channel | Typical ROAS | Typical CPC | Typical CPM |
|---------|--------------|-------------|-------------|
| Google Brand | 5-15x | $0.50-1.50 | - |
| Google Shopping | 3-6x | $0.30-1.00 | - |
| Google PMAX | 3-5x | - | - |
| Meta Prospecting | 1.5-3x | $0.50-2.00 | $8-20 |
| Meta Retargeting | 4-10x | $0.30-1.50 | $10-25 |
| TikTok | 1.5-4x | $0.30-1.00 | $5-15 |

---

## Output Format

### E-Commerce Strategy Document

```
═══════════════════════════════════════════════════════════════════
E-COMMERCE ADVERTISING STRATEGY
═══════════════════════════════════════════════════════════════════
Brand: [Brand Name]
Monthly Budget: $[Budget]
AOV: $[AOV]
Target ROAS: [X]x
Created: [Date]
═══════════════════════════════════════════════════════════════════

📊 STRATEGIC OVERVIEW
────────────────────────────────────────────────────────────────────

CURRENT STATE:
- Monthly ad spend: $[X]
- Blended ROAS: [X]x
- Channels: [List]
- Key challenges: [List]

TARGET STATE:
- Monthly ad spend: $[X]
- Target ROAS: [X]x
- Channel mix: [Breakdown]
- Key objectives: [List]

═══════════════════════════════════════════════════════════════════

💰 BUDGET ALLOCATION
────────────────────────────────────────────────────────────────────

| Channel | Monthly Budget | % of Total | Primary Objective |
|---------|----------------|------------|-------------------|
| Google Ads | $[X] | [X]% | [Objective] |
| Meta Ads | $[X] | [X]% | [Objective] |
| TikTok | $[X] | [X]% | [Objective] |
| Other | $[X] | [X]% | [Objective] |
| **Total** | **$[X]** | **100%** | |

FUNNEL ALLOCATION:

| Stage | Budget | Channels |
|-------|--------|----------|
| Awareness (TOF) | $[X] ([X]%) | [Channels] |
| Consideration (MOF) | $[X] ([X]%) | [Channels] |
| Conversion (BOF) | $[X] ([X]%) | [Channels] |

═══════════════════════════════════════════════════════════════════

🎯 GOOGLE ADS STRATEGY
────────────────────────────────────────────────────────────────────

CAMPAIGN STRUCTURE:

| Campaign | Budget | Bid Strategy | Target |
|----------|--------|--------------|--------|
| Brand Search | $[X]/day | Target ROAS | [X]x |
| Performance Max | $[X]/day | Target ROAS | [X]x |
| Standard Shopping | $[X]/day | Manual / Target ROAS | [X]x |
| Non-Brand Search | $[X]/day | Target CPA | $[X] |

PMAX SETUP:
- Asset groups: [X] (by [category/product type])
- Audience signals: [List]
- Brand exclusions: [Yes/No] - [Details]
- Final URL expansion: [On/Off]

SHOPPING PRIORITIES:
1. [Top priority product category]
2. [Second priority]
3. [Third priority]

FEED OPTIMIZATION NEEDS:
- [Feed issue #1]
- [Feed issue #2]

═══════════════════════════════════════════════════════════════════

📱 META ADS STRATEGY
────────────────────────────────────────────────────────────────────

CAMPAIGN STRUCTURE:

| Campaign | Budget | Audience | Objective |
|----------|--------|----------|-----------|
| Advantage+ Sales - Prospecting | $[X]/day | Broad + signals | Sales |
| Catalog - Retargeting | $[X]/day | Website visitors | Sales |
| Manual - Testing | $[X]/day | [Audience] | Sales |

AUDIENCE STRATEGY:

| Stage | Audiences | Budget Split |
|-------|-----------|--------------|
| Prospecting | Broad, Lookalikes | [X]% |
| Retargeting | ATC 7d, VC 14d | [X]% |
| Retention | Purchasers 30-90d | [X]% |

CREATIVE STRATEGY:
- Formats: [UGC, Catalog, Static, Video]
- Test cadence: [X] new creatives/week
- Winning patterns: [List]

═══════════════════════════════════════════════════════════════════

📈 GROWTH ROADMAP
────────────────────────────────────────────────────────────────────

PHASE 1: Foundation (Weeks 1-4)
- [ ] [Action item]
- [ ] [Action item]
- [ ] [Action item]

PHASE 2: Optimization (Weeks 5-8)
- [ ] [Action item]
- [ ] [Action item]
- [ ] [Action item]

PHASE 3: Scale (Weeks 9-12)
- [ ] [Action item]
- [ ] [Action item]
- [ ] [Action item]

═══════════════════════════════════════════════════════════════════

📊 SUCCESS METRICS
────────────────────────────────────────────────────────────────────

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| Blended ROAS | [X]x | [X]x | [Weeks] |
| New Customer CPA | $[X] | $[X] | [Weeks] |
| Monthly Revenue | $[X] | $[X] | [Weeks] |
| CVR | [X]% | [X]% | [Weeks] |

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "Just starting with e-commerce ads"
**Recommendation:**
1. Fix your product feed first (titles, images, GTINs)
2. Start with Google PMAX + Brand Search
3. Add Meta retargeting for cart abandoners
4. Build email list from day one
5. Don't spread budget across too many channels

### Scenario 2: "Good ROAS but can't scale"
**Diagnosis:** Likely at diminishing returns on current channels
**Solutions:**
1. Add new channel (TikTok, YouTube)
2. Test new audiences on existing channels
3. Expand geographically
4. Launch new products
5. Improve AOV to afford higher CPAs

### Scenario 3: "Meta performance tanked after iOS 14"
**Adaptation:**
1. Implement Conversions API (CAPI)
2. Use Advantage+ sales campaigns
3. Broaden targeting (let algorithm optimize)
4. First-party data: email lists, CRM audiences
5. Longer attribution windows
6. Incrementality testing to validate true value

### Scenario 4: "Shopping campaigns not spending"
**Troubleshooting:**
1. Check Merchant Center for disapprovals
2. Review feed quality (missing GTINs, bad images)
3. Check bid/budget competitiveness
4. Review product eligibility
5. Check negative keywords aren't blocking

### Scenario 5: "High ROAS but low volume"
**Diagnosis:** Over-optimized for efficiency, missing growth
**Solutions:**
1. Increase budgets on winners
2. Loosen ROAS targets temporarily
3. Add prospecting campaigns
4. Test broader audiences
5. Accept lower efficiency for growth

---

## Limitations

**I can provide:**
- Full-funnel strategy framework
- Channel allocation recommendations
- Campaign structure guidance
- Benchmark data and targets
- Optimization priorities

**I cannot provide:**
- Product feed technical implementation
- Platform-specific pixel/API setup
- Actual campaign builds in platforms
- Creative production
- Real-time competitive analysis

**For best results, also involve:**
- Developer for tracking implementation
- Creative team for assets
- Platform specialists for complex setups

---

## Quality Checklist

Before delivering strategy:
- [ ] Budget allocation matches business stage
- [ ] Google and Meta strategies are complementary, not duplicative
- [ ] Feed optimization addressed
- [ ] Retargeting windows properly sequenced
- [ ] New customer vs. existing customer split considered
- [ ] ROAS targets realistic for margins
- [ ] Measurement plan included
- [ ] Phased roadmap with clear priorities
- [ ] Success metrics defined
