# Marketing Claude Skills by InsightfulPipe

Claude skills for Google Ads, Meta Ads, GA4, SEO, content and reporting that work on your live marketing data. Each skill pulls the numbers itself through [InsightfulPipe](https://insightfulpipe.com) MCP servers, so there is nothing to export. It runs the analysis and comes back with the findings, the fixes and a plan.

Browse every skill with its sample run at **[insightfulpipe.com/marketing-claude-skills](https://insightfulpipe.com/marketing-claude-skills)**.

## What's in a skill

Each folder in [`skills/`](skills/) holds:

- `SKILL.md`: the instructions Claude follows, and a description that tells Claude when to use the skill
- `HOW_TO_USE.md`: what to connect, and example requests to start with
- `sample_input.json` and `expected_output.json`: example data and the result the skill produces from it

## Install

### Claude Code: every skill, as a plugin

```
/plugin marketplace add Insightful-Pipe/marketing-skills
/plugin install marketing-skills@insightfulpipe
```

### Claude Code: one skill

Copy a folder from [`skills/`](skills/) to `~/.claude/skills/` to use it in every project, or to `.claude/skills/` inside one project.

### Claude.ai and Claude Desktop

Download the skill's ZIP from its page on insightfulpipe.com (the **Page** link in the list below). In Claude, open **Customize > Skills**, choose **+ Create skill > Upload a skill** and pick the ZIP. Skills need code execution turned on.

### Other agents

Any agent that reads Agent Skills (a folder with a `SKILL.md`) can load a folder from [`skills/`](skills/).

## Connect your data

The skills read live data through InsightfulPipe MCP servers. Connect your ad, analytics and SEO accounts to InsightfulPipe, then add the [InsightfulPipe MCP server](https://insightfulpipe.com/mcp-servers/insightfulpipe) to your assistant. Its page has setup steps for Claude, Claude Code, ChatGPT, Cursor, Gemini CLI and Codex. You can also paste exported data instead.

Then start with a request from the skill's `HOW_TO_USE.md`, for example:

> Hey Claude, I just added the "google-ads-account-audit" skill. Audit my Google Ads account and tell me the five fixes worth the most money.

Most skills only read data and make recommendations. Skills that write, such as adding negative keywords, ask you to confirm first. Accounts connect as Read-only or Read & Write, owners, admins and operators can turn individual actions off per account, and destructive actions such as deletes are off by default.

## Skills

<!-- SKILLS:START -->
**81 skills in 16 categories.** The skill name opens its folder here; **Page** opens it on insightfulpipe.com with the full sample run and a ZIP download.

### Audience

Audience overlap and cannibalization analysis across campaigns.

| Skill | What it does | |
|---|---|---|
| [Audience Overlap Analyzer](skills/audience-overlap-analyzer/) | Finds where your own Meta and Google Ads targeting reaches the same people, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/audience/audience-overlap-analyzer) |

### Creative

Creative briefs, video ad scripts, testing roadmaps and fatigue detection.

| Skill | What it does | |
|---|---|---|
| [Ad Creative Brief Generator](skills/ad-creative-brief-generator/) | Writes ad creative briefs from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/ad-creative-brief-generator) |
| [Ad Creative Fatigue Detector](skills/ad-creative-fatigue-detector/) | Finds ad creatives that are wearing out on Meta, Google Ads, TikTok, LinkedIn, Snapchat and X by pulling ad-level history itself through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/ad-creative-fatigue-detector) |
| [Creative Testing Roadmap](skills/creative-testing-roadmap/) | Builds a creative testing roadmap from live ad data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/creative-testing-roadmap) |
| [Video Ad Script Writer](skills/video-ad-script-writer/) | Writes ready-to-shoot video ad scripts for TikTok, Reels, Meta feed, YouTube and LinkedIn, plus video sales letters and product demos, from live data pulled through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/video-ad-script-writer) |

### CRO

Conversion rate optimization for forms, signup flows and onboarding.

| Skill | What it does | |
|---|---|---|
| [Form CRO](skills/form-cro/) | Audits lead, contact, demo, quote and checkout forms on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/form-cro) |
| [Onboarding CRO](skills/onboarding-cro/) | Maps the new-user journey from first visit to signup, onboarding, activation and the first return, on live GA4 data pulled through the InsightfulPipe MCP, finds the… | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/onboarding-cro) |
| [Signup Flow CRO](skills/signup-flow-cro/) | Audits a signup or registration flow on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/signup-flow-cro) |

### Cross-Platform

Budget allocation across Google, Meta, TikTok, LinkedIn and Microsoft Ads.

| Skill | What it does | |
|---|---|---|
| [Cross Platform Budget Allocator](skills/cross-platform-budget-allocator/) | Splits an ad budget across Google, Meta, Microsoft, LinkedIn, TikTok, Pinterest, Snapchat, X and OpenAI Ads on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/cross-platform/cross-platform-budget-allocator) |

### Facebook Ads

Account audits, audiences, structure, creative tests, budgets and reports for Meta Ads.

| Skill | What it does | |
|---|---|---|
| [Facebook Ads Account Auditor](skills/facebook-ads-account-auditor/) | Audits a Meta (Facebook and Instagram) Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-account-auditor) |
| [Facebook Ads Audience Builder](skills/facebook-ads-audience-builder/) | Builds a Meta (Facebook and Instagram) Ads audience plan from the live ad account through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-audience-builder) |
| [Facebook Ads Budget Allocator](skills/facebook-ads-budget-allocator/) | Reallocates Meta (Facebook and Instagram) ad budgets on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-budget-allocator) |
| [Facebook Ads Campaign Structure](skills/facebook-ads-campaign-structure/) | Designs or restructures a Meta (Facebook and Instagram) Ads account on live data through the InsightfulPipe MCP, and builds a new campaign, ad set and ads from a brief. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-campaign-structure) |
| [Facebook Ads Creative Tester](skills/facebook-ads-creative-tester/) | Plans, sizes, launches and reads Meta (Facebook and Instagram) creative tests on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-creative-tester) |
| [Facebook Ads Launch Checklist](skills/facebook-ads-launch-checklist/) | Checks a Meta (Facebook and Instagram) Ads campaign before it goes live, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-launch-checklist) |
| [Facebook Ads Monthly Report](skills/facebook-ads-monthly-report/) | Writes a monthly Meta (Facebook and Instagram) Ads report from live account data through the InsightfulPipe MCP, and a quarterly creative strategy review on request. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-monthly-report) |
| [Facebook Ads Scaling Roadmap](skills/facebook-ads-scaling-roadmap/) | Builds a phased Meta (Facebook and Instagram) Ads scaling roadmap on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-scaling-roadmap) |

### Google Ads

Search term, keyword, bidding, budget, PMax and reporting skills for Google Ads.

| Skill | What it does | |
|---|---|---|
| [Ad Copy Performance Ranker](skills/ad-copy-performance-ranker/) | Ranks Google Ads responsive search ads and their individual headlines and descriptions on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/ad-copy-performance-ranker) |
| [Bid Strategy Auditor](skills/bid-strategy-auditor/) | Audits Google Ads bid strategies on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/bid-strategy-auditor) |
| [Budget Allocation Optimizer](skills/budget-allocation-optimizer/) | Moves Google Ads budget between campaigns to get more conversions from the same total, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/budget-allocation-optimizer) |
| [Geo Performance Optimizer](skills/geo-performance-optimizer/) | Finds where, on which device and at what hour a Google Ads account wastes or earns its money, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/geo-performance-optimizer) |
| [Google Ads Account Audit](skills/google-ads-account-audit/) | Runs a full Google Ads account audit on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-account-audit) |
| [Google Ads Weekly Brief](skills/google-ads-weekly-brief/) | Writes the weekly Google Ads brief for a client, boss or team from live account data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-weekly-brief) |
| [Impression Share Analyst](skills/impression-share-analyst/) | Analyzes Google Ads search impression share on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/impression-share-analyst) |
| [Keyword Performance Analyzer](skills/keyword-performance-analyzer/) | Analyzes Google Ads keywords on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/keyword-performance-analyzer) |
| [Month End Report Generator](skills/month-end-report-generator/) | Writes the month-end Google Ads report from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/month-end-report-generator) |
| [Negative Keyword Implementer](skills/negative-keyword-implementer/) | Finds, checks and adds Google Ads negative keywords on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/negative-keyword-implementer) |
| [PMax Asset Group Analyzer](skills/pmax-asset-group-analyzer/) | Reviews Google Performance Max campaigns on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/pmax-asset-group-analyzer) |
| [Quality Score Fixer](skills/quality-score-fixer/) | Diagnoses and fixes low Google Ads Quality Score on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/quality-score-fixer) |
| [Rsa Ad Copy Writer](skills/rsa-ad-copy-writer/) | Writes Google Ads responsive search ad copy from live account data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/rsa-ad-copy-writer) |
| [Scaling Roadmap Builder](skills/scaling-roadmap-builder/) | Builds a phased plan to scale Google Ads spend on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/scaling-roadmap-builder) |
| [Search Term Gold Miner](skills/search-term-gold-miner/) | Mines Google Ads search terms on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/search-term-gold-miner) |
| [Shopping Feed Optimizer](skills/shopping-feed-optimizer/) | Audits and optimizes product feeds for Google Shopping, Meta Catalog, and other platforms. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/shopping-feed-optimizer) |
| [Spend Pacing Monitor](skills/spend-pacing-monitor/) | Checks Google Ads spend pacing on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/spend-pacing-monitor) |

### LinkedIn Ads

B2B targeting, lead quality and CPL audits for LinkedIn Ads.

| Skill | What it does | |
|---|---|---|
| [LinkedIn Ads Auditor](skills/linkedin-ads-auditor/) | Audits a LinkedIn Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-auditor) |
| [LinkedIn Ads B2B Optimizer](skills/linkedin-ads-b2b-optimizer/) | Optimizes LinkedIn Ads for B2B lead generation and account-based marketing on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-b2b-optimizer) |

### Marketing

Copywriting, brand voice, SEO, landing pages, email and competitor research.

| Skill | What it does | |
|---|---|---|
| [Ad Landing Page Match Scorer](skills/ad-landing-page-match-scorer/) | Scores how well every active ad matches the page it sends people to, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/ad-landing-page-match-scorer) |
| [Brand Voice](skills/brand-voice/) | Builds a brand voice and tone guide, a messaging house and a copy check from the brand's own live copy through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/brand-voice) |
| [Competitor SWOT Analyzer](skills/competitor-swot-analyzer/) | Builds a competitor SWOT, positioning read and sales battlecard from live public data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-swot-analyzer) |
| [Copywriting](skills/copywriting/) | Writes, reviews and rewrites conversion copy from live evidence through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/copywriting) |
| [Cross Channel Attribution Analyst](skills/cross-channel-attribution-analyst/) | Works out which marketing channels really bring customers in and which only collect the credit at the end, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/cross-channel-attribution-analyst) |
| [Email Sequence Builder](skills/email-sequence-builder/) | Plans and writes email sequences (welcome, lead nurture, onboarding, cart and browse abandonment, post-purchase, re-engagement, launch, event and transactional emails)… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/email-sequence-builder) |
| [Funnel Dropoff Diagnostician](skills/funnel-dropoff-diagnostician/) | Finds where a conversion funnel loses people, on live data pulled through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/funnel-dropoff-diagnostician) |
| [Landing Page Auditor](skills/landing-page-auditor/) | Audits a landing page, homepage, sales page or any key page for conversion on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/landing-page-auditor) |
| [Marketing Psychology](skills/marketing-psychology/) | Applies behavioural science to marketing on live evidence through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/marketing-psychology) |
| [Newsletter](skills/newsletter/) | Writes email newsletters from what you actually published and what your readers actually clicked. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/newsletter) |
| [Pricing Page Auditor](skills/pricing-page-auditor/) | Audits a pricing page on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/pricing-page-auditor) |
| [Programmatic SEO](skills/programmatic-seo/) | Plans programmatic SEO pages (one template filled from data, one page per variable such as a city, trade, integration or competitor) on live data through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/programmatic-seo) |
| [Retargeting Sequence Designer](skills/retargeting-sequence-designer/) | Designs retargeting ad sequences from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/retargeting-sequence-designer) |
| [SEO Audit](skills/seo-audit/) | Runs a full SEO audit of a website on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/seo-audit) |
| [Social Content](skills/social-content/) | Plans and writes organic social media content from the brand's own post history through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/social-content) |
| [USP Extractor](skills/usp-extractor/) | Finds a business's unique selling proposition from live evidence through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/usp-extractor) |

### Measurement

GA4 tracking, attribution audits, A/B tests, incrementality and LTV:CAC.

| Skill | What it does | |
|---|---|---|
| [A/B Test Designer](skills/ab-test-designer/) | Designs A/B tests and reads out finished ones on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ab-test-designer) |
| [Attribution Model Auditor](skills/attribution-model-auditor/) | Audits how conversions are attributed across Google Ads, Meta, LinkedIn, Microsoft Ads, TikTok and GA4 on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/attribution-model-auditor) |
| [Conversion Tracking Auditor](skills/conversion-tracking-auditor/) | Audits conversion tracking end to end on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/conversion-tracking-auditor) |
| [GA4 Landing Page Analyst](skills/ga4-landing-page-analyst/) | Analyses every landing page in a GA4 property on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-landing-page-analyst) |
| [GA4 Property Audit](skills/ga4-property-audit/) | Audits a GA4 property's setup and data quality on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-property-audit) |
| [GA4 Weekly Report](skills/ga4-weekly-report/) | Builds a weekly (or monthly) Google Analytics 4 report from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-weekly-report) |
| [Incrementality Test Designer](skills/incrementality-test-designer/) | Designs an incrementality test (geo holdout, audience holdout or platform conversion lift) from live ad data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/incrementality-test-designer) |
| [LTV CAC Ratio Optimizer](skills/ltv-cac-ratio-optimizer/) | Analyzes customer lifetime value (LTV) and customer acquisition cost (CAC) to optimize advertising profitability. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ltv-cac-ratio-optimizer) |
| [Utm Auditor](skills/utm-auditor/) | Audits UTM and campaign tagging on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/utm-auditor) |

### Skill Orchestration

A routing skill that picks and sequences the other marketing skills.

| Skill | What it does | |
|---|---|---|
| [Orchestrator](skills/orchestrator/) | The router for the InsightfulPipe marketing skills. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta/orchestrator) |

### Meta Ads

Placement, creative and audience performance analysis for Meta Ads.

| Skill | What it does | |
|---|---|---|
| [Meta Ad Copy Writer](skills/meta-ad-copy-writer/) | Writes new Meta (Facebook and Instagram) ad copy from the ads that already win. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-ad-copy-writer) |
| [Meta Ads Performance Analyzer](skills/meta-ads-performance-analyzer/) | Analyzes Meta Ads (Facebook and Instagram) performance on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-ads-performance-analyzer) |

### Playbooks

Full-funnel advertising playbooks for e-commerce brands.

| Skill | What it does | |
|---|---|---|
| [Ecommerce Ads Playbook](skills/ecommerce-ads-playbook/) | Comprehensive e-commerce advertising strategy covering Google Shopping, Meta catalog ads, Performance Max, and multi-channel funnel optimization. | [Page](https://insightfulpipe.com/marketing-claude-skills/playbooks/ecommerce-ads-playbook) |

### SEO

Keyword research, content decay, cannibalization, briefs, schema, internal links and AI search visibility on live Search Console and SEO data.

| Skill | What it does | |
|---|---|---|
| [Ai Search Visibility](skills/ai-search-visibility/) | Tracks how visible a website is in AI search on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/ai-search-visibility) |
| [Content Brief Writer](skills/content-brief-writer/) | Writes an SEO content brief for one target keyword from the live Google top 10, through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/content-brief-writer) |
| [Content Decay Refresh](skills/content-decay-refresh/) | Finds the pages losing Google clicks on live Search Console data through the InsightfulPipe MCP, works out why each one is falling (lost rank, lower click-through… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/content-decay-refresh) |
| [Internal Linking Planner](skills/internal-linking-planner/) | Plans internal links on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/internal-linking-planner) |
| [Keyword Cannibalization Fixer](skills/keyword-cannibalization-fixer/) | Finds keyword cannibalization on live Google Search Console data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/keyword-cannibalization-fixer) |
| [Keyword Research Clustering](skills/keyword-research-clustering/) | Researches keywords for a topic on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/keyword-research-clustering) |
| [Schema Markup Generator](skills/schema-markup-generator/) | Audits and writes schema markup on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/schema-markup-generator) |
| [Striking Distance Optimizer](skills/striking-distance-optimizer/) | Finds the Google searches a site almost wins, on live Search Console data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/striking-distance-optimizer) |

### Social Media Ads

Paid social creative ranking and UGC creator briefs.

| Skill | What it does | |
|---|---|---|
| [Meta Ads Creative Ranker](skills/meta-ads-creative-ranker/) | Ranks Meta (Facebook and Instagram) ads by what they actually deliver, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/meta-ads-creative-ranker) |
| [UGC Brief Generator](skills/ugc-brief-generator/) | Writes UGC creator briefs and timed video ad scripts from the hooks and ads that actually worked in your Meta (and TikTok) account, pulled live through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/ugc-brief-generator) |

### Strategy

Launches, pricing, referral programs, free tools and privacy-first targeting.

| Skill | What it does | |
|---|---|---|
| [Free Tool Strategy](skills/free-tool-strategy/) | Plans a free marketing tool or lead magnet (calculator, generator, checker, quiz, template, checklist) on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/free-tool-strategy) |
| [Launch Strategy](skills/launch-strategy/) | Plans a product, feature, book, webinar or promotion launch from the business's own live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/launch-strategy) |
| [Pricing Strategy](skills/pricing-strategy/) | Builds a pricing strategy on live market data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/pricing-strategy) |
| [Privacy First Targeting Strategist](skills/privacy-first-targeting-strategist/) | Builds an advertising plan for a world with less tracking, starting from your live accounts through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/privacy-first-targeting-strategist) |
| [Referral Program](skills/referral-program/) | Designs a customer referral, affiliate or partner program from the business's own live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/referral-program) |

### TikTok Ads

Creative, hook and audience analysis for TikTok Ads.

| Skill | What it does | |
|---|---|---|
| [TikTok Ads Analyzer](skills/tiktok-ads-analyzer/) | Analyzes a TikTok Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/tiktok-ads/tiktok-ads-analyzer) |

<!-- SKILLS:END -->

New skills are published on insightfulpipe.com one at a time, and this repository syncs from the site twice a day.

## License

[MIT](LICENSE). Running the skills on live data needs an InsightfulPipe account.
