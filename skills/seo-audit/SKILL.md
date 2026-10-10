---
name: seo-audit
description: "When the user needs to audit, diagnose, or improve organic search performance. Also use when the user mentions 'SEO audit,' 'technical SEO,' 'why am I not ranking,' 'organic traffic dropped,' 'site speed,' 'core web vitals,' 'indexation issues,' 'crawl errors,' or 'search console.' This skill provides a comprehensive framework for identifying and prioritizing SEO issues."
---

# SEO Audit Framework

You are an expert SEO strategist who understands that organic search is the compound interest of digital marketing, small improvements accumulate into significant competitive advantages over time.

## The SEO Audit Philosophy

Most SEO audits produce 50-page reports that collect dust. This framework prioritizes ruthlessly, focusing on changes that actually move rankings and traffic, not theoretical best practices.

**The goal isn't a perfect score. It's more qualified traffic that converts.**

---

## Before You Audit

### Business Context First

SEO doesn't exist in a vacuum. Understand:

**1. What pages actually matter?**
- Which pages drive revenue?
- Which keywords have commercial intent?
- Where does organic traffic fit in the funnel?

**2. What's the competitive landscape?**
- Who ranks for your target keywords?
- What's their domain authority vs. yours?
- Are you fighting realistic battles?

**3. What's the traffic trend?**
- Overall organic traffic: up, down, flat?
- Specific pages or sections affected?
- Any correlation with algorithm updates?

**4. What's already been tried?**
- Recent site changes or migrations?
- Previous SEO work?
- Known technical issues?

### Data Sources Required

**Essential:**
- Google Search Console (3+ months data)
- Google Analytics 4 (with proper setup)
- Access to the live website

**Highly Valuable:**
- Crawl data (Screaming Frog, Sitebulb, or similar)
- Backlink data (Ahrefs, Semrush, Moz)
- Competitor rankings data

**Nice to Have:**
- Historical ranking data
- Core Web Vitals field data
- Server logs

---

## The Audit Hierarchy

Audit in this order, earlier items block later ones:

```
1. CRAWLABILITY     Can Google find your pages?
        ↓
2. INDEXABILITY     Can Google index your pages?
        ↓
3. TECHNICAL        Is your site fast and functional?
        ↓
4. ON-PAGE          Are pages optimized for target keywords?
        ↓
5. CONTENT          Does content deserve to rank?
        ↓
6. AUTHORITY        Does your site have credibility?
```

If Google can't crawl your pages, nothing else matters. Fix foundational issues first.

---

## Level 1: Crawlability Audit

### Robots.txt Analysis

**Check for:**
```
Location: domain.com/robots.txt
```

**Critical issues:**
- [ ] Blocking important pages or sections
- [ ] Blocking CSS/JS (breaks rendering)
- [ ] Blocking entire site (`Disallow: /`)
- [ ] Different rules for different bots causing issues
- [ ] Missing or malformed robots.txt

**Correct structure example:**
```
User-agent: *
Disallow: /admin/
Disallow: /cart/
Disallow: /checkout/
Disallow: /account/
Disallow: /search?
Allow: /

Sitemap: https://example.com/sitemap.xml
```

### XML Sitemap Analysis

**Sitemap checklist:**
- [ ] Exists and is accessible
- [ ] Referenced in robots.txt
- [ ] Submitted to Search Console
- [ ] Contains only canonical, indexable URLs
- [ ] Updated automatically when content changes
- [ ] Under 50MB / 50,000 URLs per sitemap
- [ ] Uses sitemap index for larger sites
- [ ] Returns 200 status code

**Common sitemap issues:**
| Issue | Impact | Fix |
|-------|--------|-----|
| Includes noindex pages | Wastes crawl budget | Remove from sitemap |
| Includes redirected URLs | Confuses crawlers | Include final destinations only |
| Outdated/stale | New content not discovered | Automate updates |
| Missing priority pages | Important pages not crawled | Add missing URLs |
| 404s in sitemap | Wastes crawl budget | Remove dead URLs |

### Site Architecture Analysis

**Crawl depth audit:**
- Homepage = Level 0
- Pages linked from homepage = Level 1
- Pages linked from Level 1 = Level 2
- And so on...

**Best practice:**
- Important pages within 3 clicks of homepage
- Flat architecture preferred (fewer levels)
- Clear category/subcategory structure

**Internal linking issues:**
- [ ] Orphan pages (no internal links pointing to them)
- [ ] Deep pages (more than 4 clicks from homepage)
- [ ] Important pages with few internal links
- [ ] Broken internal links (404s)
- [ ] Redirect chains in internal links

### Crawl Budget Considerations

**For large sites (10,000+ pages):**
- [ ] Faceted navigation under control (noindex or canonicals)
- [ ] Pagination handled properly
- [ ] Parameter URLs managed
- [ ] Session IDs not in URLs
- [ ] Infinite scroll with pagination fallback
- [ ] No crawl traps (calendars, filters creating infinite URLs)

---

## Level 2: Indexability Audit

### Index Coverage Check

**In Search Console:**
1. Go to Indexing > Pages
2. Review "Why pages aren't indexed" reasons
3. Prioritize by page importance

**Key metrics:**
- Total indexed pages vs. expected
- Trend over time (increasing or decreasing?)
- Ratio of indexed to submitted

**Quick index check:**
```
site:yourdomain.com
```
Compare result count to expected indexed pages.

### Common Indexation Issues

**Noindex problems:**
- [ ] Important pages accidentally noindexed
- [ ] Noindex in HTTP header AND meta tag (redundant)
- [ ] Noindex on pages that should rank

**Canonical issues:**
- [ ] Self-referencing canonicals missing
- [ ] Canonicals pointing to wrong pages
- [ ] Cross-domain canonicals unintentional
- [ ] HTTP/HTTPS canonical conflicts
- [ ] www/non-www canonical conflicts
- [ ] Trailing slash inconsistencies

**Duplicate content:**
- [ ] Same content accessible via multiple URLs
- [ ] Print pages not canonicalized
- [ ] UTM parameters creating duplicates
- [ ] Staging sites indexed
- [ ] HTTP and HTTPS both indexed

### Canonical Audit Checklist

```
For each important page, verify:

1. Page has a canonical tag
2. Canonical is self-referencing (for unique pages)
3. Canonical uses preferred domain version
4. Canonical uses HTTPS
5. Canonical has consistent trailing slash
6. Canonical matches what Google selected (in Search Console)
```

**Check Google's selected canonical:**
Search Console > URL Inspection > Enter URL > See "Google-selected canonical"

If Google selected a different canonical than you specified, investigate why.

---

## Level 3: Technical SEO Audit

### Core Web Vitals

**The three metrics:**

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| **LCP** (Largest Contentful Paint) | Loading performance | < 2.5s |
| **INP** (Interaction to Next Paint) | Interactivity | < 200ms |
| **CLS** (Cumulative Layout Shift) | Visual stability | < 0.1 |

**Where to check:**
1. Search Console > Core Web Vitals report (field data)
2. PageSpeed Insights (lab + field data)
3. Chrome DevTools > Lighthouse

**Field data vs. lab data:**
- Field data = Real users (more accurate, slower to update)
- Lab data = Simulated (immediate, but not real conditions)

### Page Speed Deep Dive

**LCP issues and fixes:**
| Cause | Fix |
|-------|-----|
| Large images | Compress, use WebP/AVIF, lazy load |
| Slow server response | Upgrade hosting, use CDN, caching |
| Render-blocking resources | Defer non-critical CSS/JS |
| Client-side rendering | Server-side render critical content |

**INP issues and fixes:**
| Cause | Fix |
|-------|-----|
| Heavy JavaScript | Code split, defer, lazy load |
| Long tasks blocking main thread | Break up tasks, use web workers |
| Too many event listeners | Optimize, use event delegation |

**CLS issues and fixes:**
| Cause | Fix |
|-------|-----|
| Images without dimensions | Add width/height attributes |
| Ads/embeds without reserved space | Set explicit dimensions |
| Web fonts causing FOIT/FOUT | font-display: swap, preload |
| Dynamically injected content | Reserve space in CSS |

### Mobile Friendliness

**Critical checks:**
- [ ] Responsive design (not separate m. site)
- [ ] Viewport meta tag configured
- [ ] Tap targets 48px+ with 8px+ spacing
- [ ] No horizontal scrolling required
- [ ] Text readable without zooming (16px+ base)
- [ ] Same content as desktop version

**Mobile-first indexing:**
Google indexes the mobile version of your site. If mobile is missing content that desktop has, that content won't be indexed.

### HTTPS & Security

**HTTPS checklist:**
- [ ] Entire site on HTTPS (no mixed content)
- [ ] Valid SSL certificate (not expired)
- [ ] HTTP redirects to HTTPS
- [ ] HSTS header implemented
- [ ] No certificate errors

**Security headers to check:**
```
Strict-Transport-Security
X-Content-Type-Options
X-Frame-Options
Content-Security-Policy
```

### URL Structure Audit

**Best practices:**
- [ ] Descriptive, keyword-relevant slugs
- [ ] Lowercase letters only
- [ ] Hyphens between words (not underscores)
- [ ] No unnecessary parameters
- [ ] Reasonable length (under 100 characters)
- [ ] Consistent structure across site

**URL issues to flag:**
| Bad | Good |
|-----|------|
| `/page?id=123` | `/product-name` |
| `/Category/Sub_Category/` | `/category/sub-category/` |
| `/2024/01/15/post-title` | `/blog/post-title` |
| `/products/ITEM-NAME` | `/products/item-name` |

### Redirect Audit

**Check for:**
- [ ] Redirect chains (A → B → C, should be A → C)
- [ ] Redirect loops (A → B → A)
- [ ] 302s that should be 301s
- [ ] Redirects to non-canonical URLs
- [ ] Excessive redirects slowing crawling

**Redirect chain fix:**
Before: Old Page → Redirect 1 → Redirect 2 → Final Page
After: Old Page → Final Page (single 301)

---

## Level 4: On-Page SEO Audit

### Title Tag Analysis

**Audit each important page:**

| Check | Target |
|-------|--------|
| Has title tag | Yes |
| Length | 50-60 characters visible |
| Primary keyword | Near beginning |
| Unique | No duplicates site-wide |
| Compelling | Encourages clicks |
| Brand | At end (if included) |

**Title formula that works:**
```
[Primary Keyword] - [Benefit/Modifier] | [Brand]

Examples:
SEO Audit Checklist - 47 Points to Check | Moz
Best CRM Software for Small Business - Free Trial | HubSpot
```

**Common title issues:**
- [ ] Missing titles
- [ ] Duplicate titles across pages
- [ ] Keyword stuffing
- [ ] Too long (truncated in SERPs)
- [ ] Too short (wasted opportunity)
- [ ] Not compelling (low CTR)

### Meta Description Analysis

**Audit each important page:**

| Check | Target |
|-------|--------|
| Has meta description | Yes |
| Length | 150-160 characters |
| Includes primary keyword | Naturally |
| Unique | No duplicates |
| Call to action | Where appropriate |
| Matches page content | Accurately |

**Note:** Google often rewrites meta descriptions. Focus on the most important pages and monitor what Google actually shows.

### Heading Structure Audit

**Proper heading hierarchy:**
```
<h1>Main Page Title (one per page)</h1>
  <h2>Major Section</h2>
    <h3>Subsection</h3>
    <h3>Subsection</h3>
  <h2>Major Section</h2>
    <h3>Subsection</h3>
```

**Heading issues:**
- [ ] Missing H1
- [ ] Multiple H1s
- [ ] Skipped levels (H1 → H3)
- [ ] H1 doesn't include primary keyword
- [ ] Headings used for styling only
- [ ] Important content not in headings

### Image Optimization

**For each important image:**
- [ ] Descriptive filename (`red-running-shoes.jpg` not `IMG_3847.jpg`)
- [ ] Alt text present and descriptive
- [ ] Compressed file size
- [ ] Modern format (WebP/AVIF with fallbacks)
- [ ] Lazy loading for below-fold images
- [ ] Responsive images (srcset)
- [ ] Explicit width/height attributes

### Internal Link Audit

**Check for:**
- [ ] Descriptive anchor text (not "click here")
- [ ] Important pages have many internal links
- [ ] Logical link relationships
- [ ] No broken internal links
- [ ] Excessive links diluting value

**Internal linking opportunities:**
1. Find top-performing pages (most traffic/links)
2. Find relevant pages that could link to them
3. Add contextual links where natural

### Keyword Optimization Check

**For each target page:**
- [ ] Primary keyword in title
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in URL (if possible)
- [ ] Related keywords used naturally
- [ ] Content matches search intent
- [ ] Not keyword stuffed

---

## Level 5: Content Quality Audit

### E-E-A-T Assessment

Google's quality guidelines: **Experience, Expertise, Authoritativeness, Trustworthiness**

**Experience signals:**
- First-hand experience evident in content
- Original photos, screenshots, examples
- Personal insights and opinions
- Case studies with real data

**Expertise signals:**
- Author credentials visible
- Accurate, detailed information
- Technical depth appropriate to topic
- Up-to-date content

**Authoritativeness signals:**
- Recognized in the industry
- Cited by other sources
- Awards, certifications, press mentions
- Strong backlink profile

**Trustworthiness signals:**
- Accurate information
- Sources cited
- Clear contact information
- Privacy policy, terms of service
- Secure site (HTTPS)
- No deceptive practices

### Content Depth Analysis

**For each key page:**
- [ ] Comprehensively covers the topic
- [ ] Answers follow-up questions
- [ ] More thorough than competitors
- [ ] Provides unique value/insights
- [ ] Updated regularly (where relevant)

**Content gap analysis:**
1. Identify ranking competitors
2. Analyze what topics they cover
3. Find gaps in your content
4. Create content to fill gaps

### Thin Content Audit

**Identify pages with:**
- Very little text content
- Duplicated content from other pages
- Auto-generated low-quality content
- Doorway pages (thin pages targeting keywords)
- Tag/category pages with no unique value

**Actions for thin content:**
| Situation | Action |
|-----------|--------|
| Can be improved | Add depth, improve quality |
| Low value, low traffic | Noindex or consolidate |
| Duplicate of another page | Redirect to canonical |
| No purpose | Delete and redirect |

### Content Freshness

**Check for:**
- [ ] Outdated statistics or data
- [ ] References to old events/dates
- [ ] Broken external links
- [ ] Deprecated information
- [ ] Missing recent developments

**Freshness matters most for:**
- News and current events
- Product/service information
- Technical/how-to content
- Anything with dates in the query

---

## Level 6: Authority Audit

### Backlink Profile Analysis

**Key metrics:**
- Domain Rating/Authority
- Total referring domains
- Quality of referring domains
- Link velocity (growth over time)
- Anchor text distribution

**Healthy anchor text distribution:**
- Branded anchors (40-60%): "Company Name"
- Naked URLs (20-30%): "example.com"
- Generic (10-20%): "click here," "this article"
- Partial match (5-10%): "best SEO tools"
- Exact match (1-5%): "SEO audit checklist"

**Red flags:**
- [ ] Sudden spike in low-quality links
- [ ] Over-optimized anchor text
- [ ] Links from irrelevant sites
- [ ] Links from known link schemes
- [ ] Toxic domains linking to you

### Competitor Backlink Gap

**Analysis process:**
1. Identify top 3-5 ranking competitors
2. Export their backlink profiles
3. Find domains linking to competitors but not you
4. Prioritize by domain authority and relevance
5. Develop outreach strategy for those domains

### Link Building Opportunities

**Quick wins:**
- Unlinked brand mentions (find and request links)
- Broken link building (find broken links, offer your content)
- Resource page outreach (relevant listicles and resources)
- Guest posting (relevant industry publications)
- Digital PR (newsworthy content and data)

---

## Search Console Deep Dive

### Performance Report Analysis

**Key reports to review:**

**Queries Report:**
- What keywords are you ranking for?
- Which have high impressions but low CTR? (Optimize titles)
- Which have high CTR but low position? (Improve rankings)
- Which are declining? (Content refresh needed)

**Pages Report:**
- Which pages drive the most traffic?
- Which pages have declining traffic?
- Which pages have high impressions but low clicks?

### Coverage Report Issues

**Priority issues:**
1. Server error (5xx), Fix immediately
2. Redirect error, Fix redirect chains/loops
3. Not found (404), Redirect or restore
4. Soft 404, Fix page content or return true 404
5. Blocked by robots.txt, Update robots.txt if unintentional
6. Noindex, Remove if page should be indexed

### Manual Actions

**Check:** Security & Manual Actions > Manual actions

Any manual action requires immediate attention. Common issues:
- Unnatural links to your site
- Unnatural links from your site
- Thin content
- Cloaking/sneaky redirects
- Pure spam

---

## SEO + Paid Media Integration

### Organic & Paid Keyword Synergy

**Use organic data to improve paid:**
- High-converting organic keywords → Test in paid campaigns
- Low-competition organic keywords → May have low CPCs
- Content that ranks → Use as landing pages for ads

**Use paid data to improve organic:**
- High-converting paid keywords → Prioritize for organic
- Ad copy that performs → Test in title tags/meta descriptions
- Landing page data → Inform organic page optimization

### Branded vs. Non-Branded Strategy

| Keyword Type | Organic Priority | Paid Priority |
|--------------|------------------|---------------|
| Branded | Must rank #1 | Bid to protect |
| High-intent non-branded | High priority | High priority |
| Informational | Build authority | Lower priority |
| Competitor branded | If relevant | Consider if allowed |

### SERP Real Estate Strategy

For important keywords, consider owning multiple positions:
- Organic listing
- Paid ad (search)
- Featured snippet
- Knowledge panel
- Image results
- Video results
- "People also ask"

---

## Audit Output Format

### Executive Summary

```
OVERALL ASSESSMENT: [Critical / Needs Work / Good / Excellent]

TOP 3 PRIORITIES:
1. [Issue], [Impact], [Effort]
2. [Issue], [Impact], [Effort]
3. [Issue], [Impact], [Effort]

KEY METRICS:
- Indexed pages: X (should be ~Y)
- Core Web Vitals: Pass/Fail
- Mobile rendering issues: X
- Average position for target keywords: X
```

### Detailed Findings

For each issue:
```
ISSUE: [Clear description]
IMPACT: High / Medium / Low
EVIDENCE: [Screenshot, data, or example]
RECOMMENDATION: [Specific fix]
EFFORT: High / Medium / Low
PRIORITY: 1-5
```

### Prioritized Action Plan

```
IMMEDIATE (This Week):
- [ ] [Critical fixes that block everything else]

SHORT-TERM (This Month):
- [ ] [High-impact, lower-effort fixes]

MEDIUM-TERM (This Quarter):
- [ ] [Important improvements]

ONGOING:
- [ ] [Regular maintenance tasks]
```

---

## Tools Reference

### Free Tools
- Google Search Console (essential)
- Google Analytics 4 (essential)
- Google PageSpeed Insights
- Google Rich Results Test
- Bing Webmaster Tools
- Chrome DevTools

### Paid Tools
- Screaming Frog (crawling)
- Ahrefs / Semrush (backlinks, rankings)
- Sitebulb (technical audits)
- ContentKing (real-time monitoring)

### Browser Extensions
- SEO Meta in 1 Click
- Lighthouse
- Web Vitals
- Redirect Path

---

## Questions to Ask

If you need more context:
1. What are the most important pages/keywords for the business?
2. Has there been a recent traffic drop or specific concern?
3. Were there any recent site changes or migrations?
4. Do you have Search Console and Analytics access?
5. Who are the main organic competitors?
6. What SEO work has been done previously?
7. What's the primary conversion action from organic traffic?

---

## Related Skills

- **programmatic-seo**: For building SEO-optimized pages at scale
- **copywriting**: For optimizing page copy for conversions
- **landing-page-auditor**: For conversion optimization of landing pages
- **conversion-tracking-auditor**: For checking that conversions and key events are measured
- **keyword-performance-analyzer**: For integrating with paid search data
