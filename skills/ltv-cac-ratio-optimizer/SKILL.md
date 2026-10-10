---
name: ltv-cac-ratio-optimizer
description: Analyzes customer lifetime value (LTV) and customer acquisition cost (CAC) to optimize advertising profitability. Calculates true acquisition economics, identifies high-value customer segments, and recommends bid/budget strategies based on customer value. Triggers when user asks about "LTV," "CAC," "customer lifetime value," "unit economics," "payback period," or wants to move beyond ROAS to profitability-based advertising.
---

# LTV:CAC Ratio Optimizer

ROAS tells you if you made money this month. LTV:CAC tells you if you're building a profitable business.

## Core Philosophy

**ROAS is a snapshot. LTV:CAC is the movie.** A customer acquired at 2x ROAS might seem unprofitable, but if they have 5x LTV, you're printing money.

**Not all customers are equal.** A $50 first purchase from a customer who will spend $500 over 3 years is worth more than a $200 one-time purchase. Treat them differently.

**CAC only matters relative to LTV.** A $100 CAC is terrible if LTV is $80. A $100 CAC is incredible if LTV is $500. The ratio is everything.

**The 3:1 Rule:** Generally, LTV should be at least 3x CAC for a healthy business. Below 3:1, you're vulnerable. Above 5:1, you're likely under-investing in growth.

**Payback period matters too.** Even with great LTV:CAC, if it takes 2 years to recoup CAC, you need deep pockets. Cash flow constraints are real.

---

## Required Context

### Must Have

**1. Customer Value Data**
- Average first order value
- Repeat purchase rate
- Average order value (overall)
- Customer lifespan or retention rate
- OR: Cohort revenue data over time

**2. Acquisition Cost Data**
- Total marketing spend
- Number of new customers acquired
- Channel-level spend and acquisition (if available)
- Attribution methodology used

**3. Time Period**
- Analysis period (usually 12 months)
- Cohort definition (when customers were acquired)

### Strongly Recommended

**4. Gross Margin Data**
- COGS or product margin
- Shipping costs
- Returns rate
- Payment processing fees

**5. Segmentation Data**
- Channel of acquisition
- First product purchased
- Customer demographic
- Marketing campaign source

### Nice to Have

- Full cohort analysis by month/quarter
- Customer segment breakdowns
- Blended vs. new customer CAC
- Paid vs organic acquisition split

---

## Analysis Framework

### Step 1: Calculate LTV

**Simple LTV Formula:**
```
LTV = Average Order Value × Purchase Frequency × Customer Lifespan
```

**Example:**
- AOV: $75
- Purchase Frequency: 3x per year
- Customer Lifespan: 2 years

LTV = $75 × 3 × 2 = **$450**

---

**Gross Margin-Adjusted LTV (More Accurate):**
```
LTV (GM) = LTV × Gross Margin %
```

**Example:**
- LTV: $450
- Gross Margin: 60%

LTV (GM) = $450 × 0.60 = **$270**

---

**Cohort-Based LTV (Most Accurate):**
Track actual revenue from customer cohorts over time.

| Cohort | Month 1 | Month 3 | Month 6 | Month 12 | Month 24 |
|--------|---------|---------|---------|----------|----------|
| Jan 2024 | $60 | $85 | $120 | $180 | $260 |
| Feb 2024 | $55 | $78 | $110 | $165 | - |
| Mar 2024 | $62 | $88 | $125 | - | - |

**Projected LTV:** Use curves from mature cohorts to project newer cohorts.

---

**LTV Calculation Methods:**

| Method | Complexity | Accuracy | Best For |
|--------|------------|----------|----------|
| Simple formula | Low | Low | Quick estimates |
| Gross margin adjusted | Low | Medium | Margin-aware businesses |
| Cohort-based | High | High | Subscription, repeat purchase |
| Predictive modeling | Very High | Highest | Enterprise, data teams |

---

### Step 2: Calculate CAC

**Basic CAC:**
```
CAC = Total Marketing Spend / Number of New Customers Acquired
```

**Example:**
- Marketing Spend: $50,000
- New Customers: 500

CAC = $50,000 / 500 = **$100**

---

**Fully Loaded CAC (More Accurate):**
```
Fully Loaded CAC = (Marketing Spend + Sales Costs + Marketing Team Costs) / New Customers
```

Include:
- Ad spend
- Agency fees
- Marketing tools/software
- Marketing team salaries (portion)
- Sales team costs (if applicable)
- Discounts given to acquire

---

**Channel-Specific CAC:**

| Channel | Spend | New Customers | CAC |
|---------|-------|---------------|-----|
| Meta Ads | $25,000 | 200 | $125 |
| Google Ads | $15,000 | 180 | $83 |
| TikTok Ads | $5,000 | 40 | $125 |
| Influencer | $3,000 | 50 | $60 |
| Organic | $0 | 100 | $0 |
| **Total Paid** | **$48,000** | **470** | **$102** |
| **Blended** | **$48,000** | **570** | **$84** |

---

**Blended vs. Paid CAC:**

| Metric | What It Measures | When to Use |
|--------|------------------|-------------|
| Paid CAC | Cost per customer from paid channels | Channel efficiency |
| Blended CAC | Total marketing / all customers | Overall efficiency |
| Marginal CAC | Cost of the NEXT customer | Scaling decisions |

**Important:** Don't conflate blended and paid CAC. Blended CAC includes organic customers who cost $0 to acquire, making it artificially low.

---

### Step 3: Calculate LTV:CAC Ratio

**Formula:**
```
LTV:CAC Ratio = LTV / CAC
```

**Example:**
- LTV (GM-adjusted): $270
- CAC: $100

LTV:CAC = $270 / $100 = **2.7:1**

---

**LTV:CAC Benchmarks:**

| Ratio | Assessment | Interpretation |
|-------|------------|----------------|
| <1:1 | Critical | Losing money on every customer |
| 1:1 - 2:1 | Poor | Barely breaking even |
| 2:1 - 3:1 | Fair | Sustainable but tight |
| 3:1 - 5:1 | Good | Healthy unit economics |
| 5:1 - 8:1 | Excellent | Strong efficiency |
| >8:1 | Very High | Potentially under-investing in growth |

**The Sweet Spot:** 3:1 to 5:1 typically indicates healthy growth-oriented businesses.

---

### Step 4: Calculate Payback Period

**Payback Period:**
```
Payback Period = CAC / (Average Monthly Revenue per Customer × Gross Margin)
```

**Example:**
- CAC: $100
- Monthly Revenue per Customer: $30
- Gross Margin: 60%

Payback = $100 / ($30 × 0.60) = $100 / $18 = **5.6 months**

---

**Payback Period Benchmarks:**

| Payback | Assessment | Cash Flow Implications |
|---------|------------|------------------------|
| <3 months | Excellent | Can scale aggressively |
| 3-6 months | Good | Healthy, sustainable |
| 6-12 months | Fair | Need working capital |
| 12-18 months | Concerning | Cash flow challenges |
| >18 months | Problematic | Requires significant funding |

---

### Step 5: Segment Analysis

**Analyze LTV:CAC by Segment:**

| Segment | LTV | CAC | LTV:CAC | Action |
|---------|-----|-----|---------|--------|
| Meta - Lookalikes | $320 | $90 | 3.6:1 | Scale |
| Meta - Interests | $240 | $95 | 2.5:1 | Optimize |
| Google - Non-Brand | $380 | $85 | 4.5:1 | Scale |
| Google - Brand | $420 | $25 | 16.8:1 | Protect |
| TikTok - Prospecting | $180 | $110 | 1.6:1 | Audit |
| Influencer | $400 | $65 | 6.2:1 | Expand |

---

**Segment by First Purchase:**

| First Product | LTV | % of Customers | Recommendation |
|---------------|-----|----------------|----------------|
| Product A | $520 | 25% | Feature in ads |
| Product B | $340 | 40% | Maintain |
| Product C | $180 | 20% | De-prioritize in ads |
| Bundle | $680 | 15% | Promote bundles |

---

**Segment by Customer Demographics:**

| Segment | LTV | CAC | LTV:CAC |
|---------|-----|-----|---------|
| Age 25-34 | $290 | $85 | 3.4:1 |
| Age 35-44 | $410 | $95 | 4.3:1 |
| Age 45-54 | $350 | $120 | 2.9:1 |
| Age 55+ | $280 | $140 | 2.0:1 |

**Insight:** Focus acquisition on Age 35-44 (highest LTV:CAC).

---

## Output Format

### LTV:CAC Analysis Report

```
═══════════════════════════════════════════════════════════════════
LTV:CAC ANALYSIS REPORT
═══════════════════════════════════════════════════════════════════
Business: [Business Name]
Analysis Period: [Date Range]
Cohort: [Customers acquired in X period]
Prepared: [Date]
═══════════════════════════════════════════════════════════════════

📊 EXECUTIVE SUMMARY
────────────────────────────────────────────────────────────────────

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| LTV (Revenue) | $[X] | - | - |
| LTV (Gross Margin) | $[X] | - | - |
| Blended CAC | $[X] | - | - |
| Paid CAC | $[X] | - | - |
| LTV:CAC Ratio | [X]:1 | 3:1 | 🟢/🟡/🔴 |
| Payback Period | [X] months | <6 months | 🟢/🟡/🔴 |

OVERALL ASSESSMENT:
[One paragraph summary of unit economics health]

KEY FINDING:
[Single most important insight]

═══════════════════════════════════════════════════════════════════

💰 LIFETIME VALUE ANALYSIS
────────────────────────────────────────────────────────────────────

LTV CALCULATION:

| Component | Value | Notes |
|-----------|-------|-------|
| Average Order Value | $[X] | [Period] |
| Purchase Frequency | [X]x/year | [Method] |
| Customer Lifespan | [X] years | [Method] |
| **LTV (Revenue)** | **$[X]** | |
| Gross Margin | [X]% | |
| **LTV (GM-Adjusted)** | **$[X]** | Use this for ratio |

LTV BY COHORT:

| Cohort | M1 | M3 | M6 | M12 | Projected LTV |
|--------|----|----|----|----|---------------|
| [Month 1] | $[X] | $[X] | $[X] | $[X] | $[X] |
| [Month 2] | $[X] | $[X] | $[X] | $[X] | $[X] |
| [Month 3] | $[X] | $[X] | $[X] | - | $[X] |

LTV TRENDS:
- [Observation about LTV trends]
- [Observation about retention/frequency]

═══════════════════════════════════════════════════════════════════

📈 CUSTOMER ACQUISITION COST ANALYSIS
────────────────────────────────────────────────────────────────────

CAC CALCULATION:

| Component | Amount |
|-----------|--------|
| Total Ad Spend | $[X] |
| Agency/Contractor Fees | $[X] |
| Marketing Tools | $[X] |
| **Total Marketing Spend** | **$[X]** |
| New Customers (Paid) | [X] |
| New Customers (All) | [X] |
| **Paid CAC** | **$[X]** |
| **Blended CAC** | **$[X]** |

CAC BY CHANNEL:

| Channel | Spend | New Customers | CAC | LTV:CAC |
|---------|-------|---------------|-----|---------|
| [Channel 1] | $[X] | [X] | $[X] | [X]:1 |
| [Channel 2] | $[X] | [X] | $[X] | [X]:1 |
| [Channel 3] | $[X] | [X] | $[X] | [X]:1 |
| [Channel 4] | $[X] | [X] | $[X] | [X]:1 |
| **Total Paid** | **$[X]** | **[X]** | **$[X]** | **[X]:1** |

CHANNEL EFFICIENCY RANKING:

| Rank | Channel | LTV:CAC | Recommendation |
|------|---------|---------|----------------|
| 1 | [Best] | [X]:1 | Scale |
| 2 | [Second] | [X]:1 | Scale |
| 3 | [Third] | [X]:1 | Maintain |
| 4 | [Fourth] | [X]:1 | Optimize/Cut |

═══════════════════════════════════════════════════════════════════

⏱️ PAYBACK PERIOD ANALYSIS
────────────────────────────────────────────────────────────────────

PAYBACK CALCULATION:

| Component | Value |
|-----------|-------|
| CAC | $[X] |
| Monthly Revenue/Customer | $[X] |
| Gross Margin | [X]% |
| Monthly GM/Customer | $[X] |
| **Payback Period** | **[X] months** |

PAYBACK BY CHANNEL:

| Channel | CAC | Monthly GM | Payback |
|---------|-----|------------|---------|
| [Channel 1] | $[X] | $[X] | [X] months |
| [Channel 2] | $[X] | $[X] | [X] months |
| [Channel 3] | $[X] | $[X] | [X] months |

CASH FLOW IMPLICATION:
[Analysis of what payback period means for cash flow and growth]

═══════════════════════════════════════════════════════════════════

🎯 SEGMENT ANALYSIS
────────────────────────────────────────────────────────────────────

BY ACQUISITION SOURCE:

| Segment | LTV | CAC | LTV:CAC | % of Customers |
|---------|-----|-----|---------|----------------|
| [Segment 1] | $[X] | $[X] | [X]:1 | [X]% |
| [Segment 2] | $[X] | $[X] | [X]:1 | [X]% |
| [Segment 3] | $[X] | $[X] | [X]:1 | [X]% |

BY FIRST PRODUCT:

| First Product | LTV | % of Customers | Action |
|---------------|-----|----------------|--------|
| [Product 1] | $[X] | [X]% | [Action] |
| [Product 2] | $[X] | [X]% | [Action] |
| [Product 3] | $[X] | [X]% | [Action] |

HIGH-VALUE CUSTOMER PROFILE:
[Description of what high-LTV customers have in common]

═══════════════════════════════════════════════════════════════════

💡 OPTIMIZATION RECOMMENDATIONS
────────────────────────────────────────────────────────────────────

IMMEDIATE ACTIONS:

1. [Action #1]
   - Current: [Metric]
   - Target: [Metric]
   - Expected Impact: [Impact]

2. [Action #2]
   - Current: [Metric]
   - Target: [Metric]
   - Expected Impact: [Impact]

3. [Action #3]
   - Current: [Metric]
   - Target: [Metric]
   - Expected Impact: [Impact]

BUDGET REALLOCATION:

| Channel | Current Spend | Recommended | Change |
|---------|---------------|-------------|--------|
| [Channel 1] | $[X] | $[X] | +[X]% |
| [Channel 2] | $[X] | $[X] | -[X]% |
| [Channel 3] | $[X] | $[X] | +[X]% |

BIDDING STRATEGY CHANGES:

| Campaign/Audience | Current Target | Recommended | Rationale |
|-------------------|----------------|-------------|-----------|
| [Campaign 1] | $[X] CPA | $[X] CPA | Higher LTV justifies |
| [Campaign 2] | [X]x ROAS | [X]x ROAS | Lower LTV requires |

LTV IMPROVEMENT OPPORTUNITIES:

1. [Opportunity #1 - e.g., increase AOV]
2. [Opportunity #2 - e.g., improve retention]
3. [Opportunity #3 - e.g., cross-sell]

CAC REDUCTION OPPORTUNITIES:

1. [Opportunity #1 - e.g., improve conversion rate]
2. [Opportunity #2 - e.g., better targeting]
3. [Opportunity #3 - e.g., channel mix optimization]

═══════════════════════════════════════════════════════════════════

📊 TARGET SETTING
────────────────────────────────────────────────────────────────────

BASED ON LTV:CAC ANALYSIS:

| Metric | Current | Target (3:1 ratio) | Target (5:1 ratio) |
|--------|---------|--------------------|--------------------|
| Max Paid CAC | $[X] | $[LTV/3] | $[LTV/5] |
| Min ROAS (first order) | [X]x | [X]x | [X]x |
| Target CPA by channel | Varies | [Calc] | [Calc] |

CHANNEL-SPECIFIC TARGETS:

| Channel | LTV | Target CAC (3:1) | Current CAC | Gap |
|---------|-----|------------------|-------------|-----|
| [Channel 1] | $[X] | $[X] | $[X] | [+/-X]% |
| [Channel 2] | $[X] | $[X] | $[X] | [+/-X]% |
| [Channel 3] | $[X] | $[X] | $[X] | [+/-X]% |

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "ROAS looks bad but I think customers are valuable"
**Analysis needed:**
1. Calculate true LTV (not just first purchase)
2. Compare LTV:CAC to ROAS
3. If LTV:CAC is healthy but ROAS is low, you're likely acquiring good customers inefficiently-looking

**Common finding:** First-purchase ROAS of 1.5x with LTV:CAC of 4:1 means the channel is actually very profitable.

### Scenario 2: "Which channel should I scale?"
**Framework:**
1. Calculate channel-specific LTV (do customers from different channels have different LTV?)
2. Calculate channel-specific CAC
3. Rank by LTV:CAC ratio
4. Scale highest ratio channels first (assuming they have headroom)

**Watch out for:** Channel saturation - highest LTV:CAC might not be scalable.

### Scenario 3: "What CPA can I afford?"
**Calculation:**
```
Max CPA = LTV (GM-adjusted) / Target LTV:CAC Ratio
```

**Example:**
- LTV (GM): $300
- Target Ratio: 3:1
- Max CPA: $300 / 3 = $100

**By Channel:** If channel-specific LTV varies, max CPA should vary too.

### Scenario 4: "LTV:CAC is great but we're not growing"
**Possible issues:**
1. Underinvesting in marketing (LTV:CAC >8:1 suggests this)
2. Channel saturation (can't find more customers at current CAC)
3. Operational constraints (can't fulfill more orders)

**Solution:** Gradually increase CAC tolerance until ratio approaches 3:1-5:1.

### Scenario 5: "How do I improve LTV:CAC ratio?"
**Two levers:**
1. **Increase LTV:**
   - Increase AOV (bundles, upsells)
   - Increase frequency (subscription, replenishment)
   - Increase retention (loyalty, experience)

2. **Decrease CAC:**
   - Improve conversion rate
   - Better targeting
   - Channel mix optimization
   - Improve ad creative performance

---

## Limitations

**I can provide:**
- LTV:CAC calculation frameworks
- Benchmark comparisons
- Segmentation analysis
- Strategic recommendations
- Target-setting methodology

**I cannot provide:**
- Actual data calculations (you need to input data)
- Predictive LTV models (need data science)
- Real-time CAC tracking
- Attribution model recommendations
- Financial forecasting

**For deeper analysis, you'll need:**
- Clean customer data (purchases, dates, revenue)
- Marketing attribution system
- Analytics/BI tool for cohort analysis
- Potentially: data science support

---

## Quality Checklist

Before delivering analysis:
- [ ] LTV calculation method clearly explained
- [ ] CAC includes all relevant costs
- [ ] Blended vs. paid CAC distinguished
- [ ] LTV:CAC ratio interpreted correctly
- [ ] Payback period calculated and contextualized
- [ ] Segment analysis reveals actionable insights
- [ ] Recommendations tied to specific data
- [ ] Target CPAs derived from LTV:CAC math
- [ ] Cash flow implications addressed
- [ ] Limitations of analysis noted
