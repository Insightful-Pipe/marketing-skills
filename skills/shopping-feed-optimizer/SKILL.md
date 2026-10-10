---
name: shopping-feed-optimizer
description: Audits and optimizes product feeds for Google Shopping, Meta Catalog, and other platforms. Identifies feed quality issues, provides title/description optimization, and recommends feed structure improvements. Triggers when user asks about "product feed," "shopping feed," "Merchant Center," "catalog ads," "feed optimization," or has Shopping campaign performance issues. Essential for e-commerce advertisers.
---

# Shopping Feed Optimizer

Your feed is the foundation. Bad feed = bad ads. No amount of bidding or targeting fixes a broken feed.

## Core Philosophy

**The Feed IS Your Ad.** For Shopping and Catalog ads, you don't write ad copy, your product data becomes the ad. Every field matters.

**Google/Meta Are Matching Engines.** When someone searches "blue running shoes size 10," the algorithm matches that to product data. If your title doesn't say "blue running shoes," you won't show up.

**Garbage In, Garbage Out.** Platform algorithms optimize based on your feed data. Missing attributes, poor images, and bad titles limit what the algorithm can do.

**Feed Quality = Impression Share.** Google explicitly uses feed quality as a ranking factor. Better data = more visibility at the same bid.

**The Title Is 80% of the Battle.** Users see the title first. Google matches queries to titles first. Optimize titles before anything else.

---

## Required Context

### Must Have

**1. Feed Access or Sample**
- Export of current product feed (CSV, XML, or Google Sheet)
- OR sample of 10-20 products with all attributes
- OR Merchant Center / Catalog Manager screenshots

**2. Product Category**
- What type of products (apparel, electronics, home goods, etc.)
- Google Product Category taxonomy used

**3. Current Performance**
- Click-through rate by product/category
- Impression share data (if available)
- Disapproved products count
- Top performing vs underperforming products

### Strongly Recommended

**4. Platform Context**
- Which platforms: Google Shopping, Meta, Pinterest, etc.
- Country/market targets
- Language requirements

**5. Competitive Context**
- Competitor pricing (if known)
- Category competition level

### Nice to Have

- Search query data from Shopping campaigns
- Historical feed changes and results
- Merchandising priorities (what to push)
- Inventory levels and availability data

---

## Feed Audit Framework

### Audit Area 1: Required Attributes

**Google Shopping Required Fields:**

| Field | Requirement | Common Issues |
|-------|-------------|---------------|
| id | Unique per product | Duplicates, changes causing re-learning |
| title | ≤150 chars, accurate | Too short, missing keywords |
| description | Accurate, detailed | Thin, duplicate, keyword stuffed |
| link | Valid product page | Broken links, wrong pages |
| image_link | High quality, valid URL | Small images, wrong aspect ratio |
| price | Accurate, matches landing | Mismatch errors |
| availability | in_stock/out_of_stock | Not synced with website |
| brand | Accurate brand name | Missing, generic |
| gtin | Valid UPC/EAN/ISBN | Missing (major issue) |
| condition | new/refurbished/used | Missing when required |

**GTIN Importance:**

| GTIN Status | Impact |
|-------------|--------|
| Valid GTIN | Full visibility, all placements |
| Missing GTIN | Reduced visibility, limited placements |
| Invalid GTIN | Disapproval risk |

**Meta Catalog Required Fields:**

| Field | Requirement |
|-------|-------------|
| id | Unique identifier |
| title | Product name |
| description | Product description |
| availability | in stock / out of stock |
| condition | new / refurbished / used |
| price | Amount + currency |
| link | Product URL |
| image_link | Product image URL |
| brand | Brand name |

---

### Audit Area 2: Title Optimization

**Title Formula by Category:**

| Category | Recommended Structure |
|----------|----------------------|
| Apparel | Brand + Gender + Product Type + Attributes (Color, Size, Material) |
| Electronics | Brand + Product Line + Model + Key Specs |
| Home & Garden | Brand + Product Type + Material + Key Feature + Size |
| Beauty | Brand + Product Line + Product Type + Size/Volume |
| Generic | Brand + Product Type + Key Differentiator + Variant |

**Title Best Practices:**

| Do | Don't |
|----|-------|
| Front-load important keywords | Start with brand if not well-known |
| Include color, size, material | Use ALL CAPS or excessive punctuation |
| Match search intent | Stuff keywords unnaturally |
| Be specific (150 chars available) | Be generic ("Nice Shirt") |
| Include model numbers for electronics | Include promotional text ("Sale!") |

**Title Optimization Examples:**

| Before (Weak) | After (Optimized) |
|---------------|-------------------|
| Running Shoes | Nike Air Zoom Pegasus 40 Men's Running Shoes - Black/White - Size 10 |
| Blue Dress | Zara Women's Midi Wrap Dress - Navy Blue - Size Medium - Cotton Blend |
| Laptop | Apple MacBook Pro 14" M3 Pro - 18GB RAM - 512GB SSD - Space Gray |
| Face Cream | CeraVe Moisturizing Cream - 16oz - Daily Face and Body Moisturizer for Dry Skin |

**Title Scoring:**

| Score | Criteria |
|-------|----------|
| ⭐⭐⭐⭐⭐ | Brand + Type + 3+ Attributes + Key Differentiator |
| ⭐⭐⭐⭐ | Brand + Type + 2 Attributes |
| ⭐⭐⭐ | Brand + Type + 1 Attribute |
| ⭐⭐ | Just brand + type |
| ⭐ | Generic name only |

---

### Audit Area 3: Image Quality

**Google Shopping Image Requirements:**

| Requirement | Specification |
|-------------|---------------|
| Minimum size | 100x100px (non-apparel), 250x250px (apparel) |
| Recommended size | 800x800px or higher |
| Format | JPEG, PNG, GIF, BMP, TIFF |
| Background | Prefer white/light solid background |
| Product visibility | Product should fill 75-90% of frame |

**Image Quality Checklist:**

| Factor | Pass | Fail |
|--------|------|------|
| Resolution | ≥800px longest side | <250px, blurry |
| Background | White/clean | Busy, watermarks |
| Product focus | Product clearly visible | Product too small |
| Accuracy | Matches the variant | Generic image |
| Professionalism | Clean, well-lit | Amateur, dark |
| Text/overlays | None or minimal | Promotional text, logos |

**Image Optimization Priority:**

1. **Top sellers** - Best images first where it matters most
2. **High-margin products** - Worth the investment
3. **Competitive categories** - Stand out visually
4. **Underperformers** - Image might be the issue

---

### Audit Area 4: Pricing & Availability

**Price Accuracy:**

| Issue | Impact | Check |
|-------|--------|-------|
| Price mismatch (feed vs site) | Disapproval | Daily sync verification |
| Missing sale_price | Lost opportunity | Add when on sale |
| Currency mismatch | Disapproval | Match target country |
| Price too low/high | Suspension risk | Verify accuracy |

**Availability Sync:**

| Status | Feed Value | When to Use |
|--------|------------|-------------|
| In stock | in_stock | Available to ship |
| Out of stock | out_of_stock | Not available |
| Preorder | preorder | Future availability |
| Backorder | backorder | Ships when available |

**Availability Best Practices:**
- Sync feed at least daily (hourly for fast-moving inventory)
- Remove products that won't be back in stock
- Use availability_date for preorders

---

### Audit Area 5: Custom Labels Strategy

**Custom Label Use Cases:**

| Label | Use Case | Example Values |
|-------|----------|----------------|
| custom_label_0 | Margin tier | high_margin, medium_margin, low_margin |
| custom_label_1 | Bestseller status | bestseller, rising, standard, clearance |
| custom_label_2 | Seasonality | spring, summer, fall, winter, evergreen |
| custom_label_3 | Promotion status | promo_eligible, full_price |
| custom_label_4 | New arrival | new_arrival, core, legacy |

**Why Custom Labels Matter:**

- **Bid differently** by margin (bid higher on high-margin)
- **Segment campaigns** by performance tier
- **Prioritize budgets** to bestsellers
- **Seasonal control** for inventory management
- **Reporting** by business category

---

### Audit Area 6: Product Type & Categories

**Google Product Category:**
- Use the most specific category available
- Required for some categories (apparel, media)
- Improves matching accuracy

**Product Type (Your Taxonomy):**
- Use your internal categorization
- Format: Category > Subcategory > Sub-subcategory
- Example: `Apparel > Men's > Shoes > Running Shoes`

**Category Optimization:**

| Issue | Impact | Fix |
|-------|--------|-----|
| Too generic | Poor matching | Use most specific available |
| Missing | Limited optimization | Always include |
| Incorrect | Wrong auctions | Audit and correct |

---

### Audit Area 7: Additional Attributes

**Apparel-Specific (Required):**

| Attribute | Values |
|-----------|--------|
| gender | male, female, unisex |
| age_group | adult, kids, toddler, infant, newborn |
| color | Actual color name |
| size | Standardized sizing |
| size_type | regular, petite, plus, tall, big, maternity |
| size_system | US, UK, EU, etc. |

**Optional But Valuable:**

| Attribute | Benefit |
|-----------|---------|
| additional_image_link | Multiple angles, lifestyle shots |
| product_highlight | Bullet points for comparison |
| product_detail | Additional specs |
| material | Filtering, matching |
| pattern | Filtering, matching |
| item_group_id | Groups variants together |
| shipping | Override account-level shipping |

---

## Output Format

### Feed Audit Report

```
═══════════════════════════════════════════════════════════════════
SHOPPING FEED AUDIT REPORT
═══════════════════════════════════════════════════════════════════
Feed: [Feed Name / Source]
Products Analyzed: [X]
Platforms: [Google / Meta / etc.]
Audit Date: [Date]
═══════════════════════════════════════════════════════════════════

📊 FEED HEALTH SCORE: [X/100]

| Category | Score | Priority |
|----------|-------|----------|
| Required Attributes | [X/25] | [P0/P1/P2] |
| Title Quality | [X/25] | [P0/P1/P2] |
| Image Quality | [X/20] | [P0/P1/P2] |
| Pricing & Availability | [X/15] | [P0/P1/P2] |
| Additional Attributes | [X/15] | [P0/P1/P2] |

TOP 3 ISSUES:
1. [Critical issue] - Affecting [X] products
2. [Issue #2] - Affecting [X] products
3. [Issue #3] - Affecting [X] products

QUICK WIN:
[Single highest-impact fix]

═══════════════════════════════════════════════════════════════════

📋 REQUIRED ATTRIBUTES AUDIT
────────────────────────────────────────────────────────────────────

| Attribute | Coverage | Quality | Issues |
|-----------|----------|---------|--------|
| id | [X]% | ✅/⚠️/❌ | [Issue description] |
| title | [X]% | ✅/⚠️/❌ | [Issue description] |
| description | [X]% | ✅/⚠️/❌ | [Issue description] |
| link | [X]% | ✅/⚠️/❌ | [Issue description] |
| image_link | [X]% | ✅/⚠️/❌ | [Issue description] |
| price | [X]% | ✅/⚠️/❌ | [Issue description] |
| availability | [X]% | ✅/⚠️/❌ | [Issue description] |
| brand | [X]% | ✅/⚠️/❌ | [Issue description] |
| gtin | [X]% | ✅/⚠️/❌ | [Issue description] |
| condition | [X]% | ✅/⚠️/❌ | [Issue description] |

CRITICAL GAPS:
- [Gap #1]: [X] products affected
- [Gap #2]: [X] products affected

═══════════════════════════════════════════════════════════════════

📝 TITLE OPTIMIZATION ANALYSIS
────────────────────────────────────────────────────────────────────

TITLE QUALITY DISTRIBUTION:

| Rating | Count | % of Feed |
|--------|-------|-----------|
| ⭐⭐⭐⭐⭐ Excellent | [X] | [X]% |
| ⭐⭐⭐⭐ Good | [X] | [X]% |
| ⭐⭐⭐ Average | [X] | [X]% |
| ⭐⭐ Weak | [X] | [X]% |
| ⭐ Poor | [X] | [X]% |

COMMON TITLE ISSUES:

| Issue | Frequency | Example |
|-------|-----------|---------|
| Missing brand | [X]% | "[Example title]" |
| No color/size | [X]% | "[Example title]" |
| Too short (<50 chars) | [X]% | "[Example title]" |
| Missing key attributes | [X]% | "[Example title]" |

TITLE OPTIMIZATION EXAMPLES:

| Product ID | Current Title | Optimized Title |
|------------|---------------|-----------------|
| [ID] | [Current] | [Recommended] |
| [ID] | [Current] | [Recommended] |
| [ID] | [Current] | [Recommended] |

═══════════════════════════════════════════════════════════════════

🖼️ IMAGE QUALITY ANALYSIS
────────────────────────────────────────────────────────────────────

IMAGE QUALITY DISTRIBUTION:

| Quality | Count | % of Feed |
|---------|-------|-----------|
| High quality | [X] | [X]% |
| Acceptable | [X] | [X]% |
| Needs improvement | [X] | [X]% |
| Poor/Problematic | [X] | [X]% |

IMAGE ISSUES IDENTIFIED:

| Issue | Frequency | Impact |
|-------|-----------|--------|
| Low resolution | [X] products | Reduced CTR |
| Busy background | [X] products | Distraction |
| Text overlays | [X] products | Policy risk |
| Wrong variant image | [X] products | Returns, disapprovals |

PRIORITY PRODUCTS FOR IMAGE UPDATE:
1. [Product] - [Reason]
2. [Product] - [Reason]
3. [Product] - [Reason]

═══════════════════════════════════════════════════════════════════

💰 PRICING & AVAILABILITY AUDIT
────────────────────────────────────────────────────────────────────

PRICING:
- Products with price: [X]%
- Products with sale_price: [X]%
- Price mismatches detected: [X]

AVAILABILITY:
- In stock: [X] products ([X]%)
- Out of stock: [X] products ([X]%)
- Sync frequency: [Daily/Weekly/Unknown]

ISSUES:
- [Issue #1]
- [Issue #2]

═══════════════════════════════════════════════════════════════════

🏷️ CUSTOM LABELS STRATEGY
────────────────────────────────────────────────────────────────────

CURRENT USAGE:
| Label | In Use | Values | Recommendation |
|-------|--------|--------|----------------|
| custom_label_0 | ✅/❌ | [Values] | [Recommendation] |
| custom_label_1 | ✅/❌ | [Values] | [Recommendation] |
| custom_label_2 | ✅/❌ | [Values] | [Recommendation] |
| custom_label_3 | ✅/❌ | [Values] | [Recommendation] |
| custom_label_4 | ✅/❌ | [Values] | [Recommendation] |

RECOMMENDED LABEL STRATEGY:
- custom_label_0: [Use case + values]
- custom_label_1: [Use case + values]
- custom_label_2: [Use case + values]

═══════════════════════════════════════════════════════════════════

🎯 OPTIMIZATION ROADMAP
────────────────────────────────────────────────────────────────────

IMMEDIATE (This Week):

1. [ ] [Action] - [Expected impact]
2. [ ] [Action] - [Expected impact]
3. [ ] [Action] - [Expected impact]

SHORT-TERM (Next 2 Weeks):

1. [ ] [Action] - [Expected impact]
2. [ ] [Action] - [Expected impact]

ONGOING:

1. [ ] [Process to establish]
2. [ ] [Process to establish]

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "Shopping campaigns not spending"
**Feed Checks:**
1. Merchant Center disapprovals?
2. Missing GTINs on majority of products?
3. Image quality issues?
4. Price/availability mismatches?
5. Product data quality warnings?

**Fix Priority:** Disapprovals → GTINs → Images → Data quality

### Scenario 2: "Low CTR on Shopping ads"
**Likely Feed Issues:**
1. Weak titles (missing keywords, too generic)
2. Poor images (low quality, wrong variant)
3. Price not competitive
4. Missing ratings/reviews

**Fix Priority:** Titles → Images → Competitive pricing

### Scenario 3: "High impressions, low clicks"
**Diagnosis:** Showing for queries but not compelling
**Check:**
1. Title relevance to search queries
2. Image quality vs competitors
3. Price comparison
4. Missing promotional annotations

### Scenario 4: "Products disapproved"
**Common Causes by Type:**
| Disapproval | Common Cause | Fix |
|-------------|--------------|-----|
| Price mismatch | Feed/site not synced | Improve sync frequency |
| Image quality | Too small, watermarks | Upgrade images |
| GTIN issue | Invalid or missing | Add/correct GTINs |
| Policy violation | Prohibited content | Review product content |
| Availability mismatch | OOS on site, in stock in feed | Sync inventory |

### Scenario 5: "How often should I update my feed?"
**Recommendations:**
| Business Type | Minimum Frequency | Ideal |
|---------------|-------------------|-------|
| Fast inventory changes | Every 4 hours | Hourly |
| Standard e-commerce | Daily | Twice daily |
| Stable catalog | Daily | Daily |
| Flash sales / promos | Before and after sale | Hourly during sale |

---

## Limitations

**I can provide:**
- Feed quality assessment
- Title optimization recommendations
- Attribute gap identification
- Custom label strategy
- Priority-based action plan

**I cannot provide:**
- Direct feed editing/uploads
- Merchant Center account access
- Automated feed generation
- Real-time disapproval resolution
- Competitor feed analysis

**For implementation, you'll need:**
- Feed management tool (Feedonomics, DataFeedWatch, GoDataFeed)
- OR direct platform access
- Developer resources for custom feeds

---

## Quality Checklist

Before delivering audit:
- [ ] All required attributes assessed
- [ ] Title quality scored and examples provided
- [ ] Image quality evaluated
- [ ] Pricing/availability issues identified
- [ ] Custom label strategy recommended
- [ ] Specific product examples included
- [ ] Optimization actions prioritized
- [ ] Platform-specific requirements noted
- [ ] Realistic timeline for improvements
