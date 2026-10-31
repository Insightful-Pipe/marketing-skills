# Free Claude Marketing Skills by InsightfulPipe

Free, MIT-licensed Claude skills for the whole marketing job: Google, Meta, LinkedIn, TikTok and other ads, GA4 and conversion tracking, SEO and AI search, content and copywriting, email, social media, PR, sales, local, e-commerce and app growth. Download any of the 410+ skills from this repository, or install them all in Claude Code as one plugin. Skills that need numbers pull them through [InsightfulPipe](https://insightfulpipe.com) MCP servers, so there is nothing to export, and you can also paste an export or describe the situation instead. Each one runs the analysis or writes the deliverable and comes back with the findings, the fixes and a plan.

Browse the skills with their worked sample runs at **[insightfulpipe.com/marketing-claude-skills](https://insightfulpipe.com/marketing-claude-skills)**.

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

Claude Code keeps its list of skill descriptions within a size limit, so with every skill installed Claude sees the names of all of them but the full description of only some. A skill may then not start by itself from a plain request: call it by name (for example `/google-ads-account-audit`), or install one area's plugin or just the skills you need, below.

### Claude Code: one area, as a plugin (recommended)

Each area of the library is also its own plugin. A plugin holds a few dozen skills at most, so Claude sees far more of each skill's description than with the whole library installed. Install the areas you work in:

| Plugin | Install in Claude Code |
|---|---|
| [Agency and Reporting](https://github.com/Insightful-Pipe/agency-reporting-skills) | `/plugin marketplace add Insightful-Pipe/agency-reporting-skills` then `/plugin install insightfulpipe-agency-reporting@insightfulpipe-agency-reporting` |
| [Analytics & CRO](https://github.com/Insightful-Pipe/analytics-cro-skills) | `/plugin marketplace add Insightful-Pipe/analytics-cro-skills` then `/plugin install insightfulpipe-analytics-cro@insightfulpipe-analytics-cro` |
| [B2B Sales](https://github.com/Insightful-Pipe/b2b-sales-skills) | `/plugin marketplace add Insightful-Pipe/b2b-sales-skills` then `/plugin install insightfulpipe-b2b-sales@insightfulpipe-b2b-sales` |
| [Content, Copywriting & Ad Creative](https://github.com/Insightful-Pipe/content-creative-skills) | `/plugin marketplace add Insightful-Pipe/content-creative-skills` then `/plugin install insightfulpipe-content-creative@insightfulpipe-content-creative` |
| [E-commerce](https://github.com/Insightful-Pipe/ecommerce-skills) | `/plugin marketplace add Insightful-Pipe/ecommerce-skills` then `/plugin install insightfulpipe-ecommerce@insightfulpipe-ecommerce` |
| [Email Marketing](https://github.com/Insightful-Pipe/email-marketing-skills) | `/plugin marketplace add Insightful-Pipe/email-marketing-skills` then `/plugin install insightfulpipe-email-marketing@insightfulpipe-email-marketing` |
| [Google Ads](https://github.com/Insightful-Pipe/google-ads-skills) | `/plugin marketplace add Insightful-Pipe/google-ads-skills` then `/plugin install insightfulpipe-google-ads@insightfulpipe-google-ads` |
| [Growth & App Marketing](https://github.com/Insightful-Pipe/growth-skills) | `/plugin marketplace add Insightful-Pipe/growth-skills` then `/plugin install insightfulpipe-growth@insightfulpipe-growth` |
| [LinkedIn Ads](https://github.com/Insightful-Pipe/linkedin-skills) | `/plugin marketplace add Insightful-Pipe/linkedin-skills` then `/plugin install insightfulpipe-linkedin-ads@insightfulpipe-linkedin-ads` |
| [Local Marketing](https://github.com/Insightful-Pipe/local-skills) | `/plugin marketplace add Insightful-Pipe/local-skills` then `/plugin install insightfulpipe-local@insightfulpipe-local` |
| [Marketing Strategy](https://github.com/Insightful-Pipe/marketing-strategy-skills) | `/plugin marketplace add Insightful-Pipe/marketing-strategy-skills` then `/plugin install insightfulpipe-marketing-strategy@insightfulpipe-marketing-strategy` |
| [Meta Ads](https://github.com/Insightful-Pipe/meta-ads-skills) | `/plugin marketplace add Insightful-Pipe/meta-ads-skills` then `/plugin install insightfulpipe-meta-ads@insightfulpipe-meta-ads` |
| [Paid Media](https://github.com/Insightful-Pipe/paid-media-skills) | `/plugin marketplace add Insightful-Pipe/paid-media-skills` then `/plugin install insightfulpipe-paid-media@insightfulpipe-paid-media` |
| [PR & Communications](https://github.com/Insightful-Pipe/pr-skills) | `/plugin marketplace add Insightful-Pipe/pr-skills` then `/plugin install insightfulpipe-pr@insightfulpipe-pr` |
| [SEO](https://github.com/Insightful-Pipe/seo-skills) | `/plugin marketplace add Insightful-Pipe/seo-skills` then `/plugin install insightfulpipe-seo@insightfulpipe-seo` |
| [Social Media](https://github.com/Insightful-Pipe/social-media-skills) | `/plugin marketplace add Insightful-Pipe/social-media-skills` then `/plugin install insightfulpipe-social-media@insightfulpipe-social-media` |

Any agent that reads Agent Skills (Claude Code, Codex, Cursor and others) can also install a plugin's skills with `npx skills add Insightful-Pipe/<repo>`, or one skill with `--skill <name>`.

### Claude Code: the skills you need

Copy the folders you want from [`skills/`](skills/) to `~/.claude/skills/` to use them in every project, or to `.claude/skills/` inside one project. With fewer skills installed, Claude sees each one's full description and picks the right one from a plain request.

### Claude.ai and Claude Desktop

Download the skill's ZIP from its page on insightfulpipe.com (the **Page** link in the list below), or, for a skill without a Page link yet, zip its folder from [`skills/`](skills/). In Claude, open **Customize > Skills**, choose **+ Create skill > Upload a skill** and pick the ZIP. Skills need code execution turned on.

### Other agents

Any agent that reads Agent Skills (a folder with a `SKILL.md`) can load a folder from [`skills/`](skills/).

## Connect your data

The skills read live data through InsightfulPipe MCP servers. Connect your ad, analytics, SEO, email, social and store accounts to InsightfulPipe, then add the [InsightfulPipe MCP server](https://insightfulpipe.com/mcp-servers/insightfulpipe) to your assistant. Its page has setup steps for Claude, Claude Code, ChatGPT, Cursor, Gemini CLI and Codex. You can also paste exported data instead.

Then start with a request from the skill's `HOW_TO_USE.md`, for example:

> Hey Claude, I just added the "google-ads-account-audit" skill. Audit my Google Ads account and tell me the five fixes worth the most money.

Most skills only read data and make recommendations. Skills that write, such as adding negative keywords, ask you to confirm first. Accounts connect as Read-only or Read & Write, and owners, admins and operators switch each action on or off per account. Delete-type actions start switched off until an admin turns them on.

## Skills

<!-- SKILLS:START -->
**414 skills in 32 categories.** The skill name opens its folder here; **Page** opens it on insightfulpipe.com with the full sample run and a ZIP download. Skills without a Page link are new here; their page on the site follows soon.

### Agency

Proposals, pricing, prospect audits, client onboarding, performance reviews and client messages.

| Skill | What it does | |
|---|---|---|
| [Agency Pricing Calculator](skills/agency-pricing-calculator/) | Prices PPC, paid social, social media and SEO work for an agency or freelancer from team costs and account size, comparing retainer, hourly and percent of ad spend… |  |
| [Client Onboarding Kit](skills/client-onboarding-kit/) | Builds an agency's client onboarding kit with intake questionnaire, least-privilege access requests for Google Ads, GA4, Meta, Shopify and Klaviyo, kickoff agenda… |  |
| [Client Update and Hard Conversation Writer](skills/client-conversation-writer/) | Writes hard client emails, Slack notes and call agendas from Google Ads, Meta and GA4 numbers, for missed targets, budget asks, pushback, out-of-scope fees, renewals… |  |
| [Marketing Agency Performance Review](skills/agency-performance-review/) | Grades the agency or freelancer a business pays against the contract, from Google Ads, Meta, GA4 and agency reports, then writes the review agenda and a fix or exit… |  |
| [Marketing Proposal Writer](skills/marketing-proposal-writer/) | Writes a marketing proposal, statement of work or RFP response from discovery notes or an audit, with baselines, hours sized from Google Ads and Meta counts, options… |  |
| [Prospect Marketing Audit](skills/prospect-marketing-audit/) | Audits a prospect's marketing from public data alone, checking Meta and Google ad libraries, page speed, tags, search footprint and Google reviews, then writes a cold… |  |

### App Marketing

App store optimization, store listing tests, install campaigns, attribution and ratings.

| Skill | What it does | |
|---|---|---|
| [App Install (User Acquisition) Campaign Planner](skills/app-install-ua-planner/) | Plans paid user acquisition for a live mobile app across Apple Ads, Google App campaigns, Meta, TikTok, Snapchat and AppLovin, setting max CPI, day 7 ROAS targets and a… |  |
| [App Install Attribution Auditor](skills/app-attribution-auditor/) | Audits mobile app install attribution across AppsFlyer, Adjust, Branch or Singular, SKAdNetwork conversion values, Google Ads, Meta, TikTok and GA4. |  |
| [App Marketing Plan](skills/app-marketing-plan/) | Writes a mobile app marketing plan from pre-launch to scale, covering ASO, Google Play pre-registration, App Store pre-order, soft launch, paid UA, creators and… |  |
| [App Rating Prompt Planner](skills/app-rating-prompt-planner/) | Plans when an iOS or Android app should show the App Store review request or Google Play in-app review card, checks the prompt against store rules and compares reviews… |  |
| [App Store Conversion Analyst](skills/app-store-conversion-analyst/) | Analyzes App Store Connect and Google Play Console store listing exports to find why visitors do not install, splitting conversion by source, mix shift from real drops… |  |
| [App Store Listing Localizer](skills/app-store-localization/) | Localizes App Store and Google Play listings, picking which countries to localize next and finding the keywords each locale searches instead of translating, then writes… |  |
| [App Store Screenshot and Preview Video Brief](skills/app-screenshot-video-brief/) | Writes a designer brief for App Store and Google Play screenshots, captions, app preview video and feature graphic, choosing the first three frames from reviews and… |  |
| [Apple Search Ads Manager](skills/apple-ads-manager/) | Audits and builds Apple Ads (Apple Search Ads) campaigns for an iOS app, covering brand, category, competitor and discovery structure, keyword bids, negatives, search… |  |
| [AppLovin Ads Analyzer](skills/applovin-ads-analyzer/) | Analyzes AppLovin Ads (Axon Ads Manager) campaigns for app installs or web sales, grading CPI, cost per purchase and ROAS by campaign, country and creative set, and… |  |
| [In-App Events and Featuring Planner](skills/in-app-events-featuring-planner/) | Plans App Store in-app events, Google Play promotional content and featuring nominations on a dated calendar timed to seasonal demand, with event cards in store limits. |  |
| [Store Listing Experiments and Custom Product Pages](skills/store-listing-experiments/) | Plans, sizes and reads App Store product page optimization tests and Google Play store listing experiments, and plans custom product pages and custom store listings for… |  |
| [Web-to-App Funnel Planner](skills/web-to-app-funnel/) | Plans a web2app funnel that sells app subscriptions on the web before install, weighing the store fee saved against drop-off, checking App Store and Google Play rules… |  |

### Audience

Audience overlap and cannibalization analysis across campaigns.

| Skill | What it does | |
|---|---|---|
| [Audience Overlap Analyzer](skills/audience-overlap-analyzer/) | Finds where your Meta and Google Ads targeting reaches the same people, scores overlapping ad sets, lookalikes and campaigns, and plans exclusions and merges. | [Page](https://insightfulpipe.com/marketing-claude-skills/audience/audience-overlap-analyzer) |

### B2B Sales

Outbound, prospecting, ABM, lead scoring, handoff and sales enablement.

| Skill | What it does | |
|---|---|---|
| [Abm Program Planner](skills/abm-program-planner/) | Plans an account-based marketing (ABM) program from your target account list and closed deals. | [Page](https://insightfulpipe.com/marketing-claude-skills/sales/abm-program-planner) |
| [B2B Cold Email Writer](skills/cold-email-writer/) | Writes B2B cold email sequences for a lead list, with subject lines, follow-ups and a personal first line per prospect built on one dated public fact, and sorts replies. |  |
| [B2B Demand Generation Planner](skills/b2b-demand-gen-planner/) | Plans B2B demand generation backwards from a revenue target, working out deals, SQLs, MQLs and leads from your own CRM rates, then splits channels and outbound into a… |  |
| [B2B Prospect List Builder](skills/prospect-list-builder/) | Builds a B2B prospect list of real companies from business listings, ad libraries, search results and app stores, each with dated evidence and a reason to reach out… |  |
| [Closed Lost Deal Re-engagement Planner](skills/lost-deal-reengagement/) | Ranks closed lost deals worth another try, codes each loss cause, dates the retry from it and checks accounts for signs of change, then drafts owner notes, a nurture… |  |
| [Cold Email Campaign Analyzer](skills/outbound-campaign-analyzer/) | Analyzes cold email campaign results from a sending tool export by step, variant, segment and mailbox, with confidence ranges, to find delivery, list, message or offer… |  |
| [Cold Email Deliverability Setup Planner](skills/cold-email-infrastructure-planner/) | Plans the cold email sending setup before launch. |  |
| [Customer Advocacy Program Planner](skills/customer-advocacy-program/) | Plans a B2B customer advocacy and reference program from your customer export. |  |
| [Lead Scoring Model from Deal History](skills/lead-scoring-model-builder/) | Builds a lead scoring model from your own won and lost leads, turning traits and actions into points, fitting decay and picking the MQL threshold from a backtest. |  |
| [LinkedIn Prospecting Message Writer](skills/linkedin-outreach-writer/) | Writes LinkedIn prospecting messages per prospect, including connection notes, first messages, follow-ups and InMails, each opening from a dated post or news and… |  |
| [MQL to SQL Handoff Designer](skills/lead-handoff-designer/) | Designs the marketing to sales lead handoff from your CRM lead export, setting MQL vs SQL rules, lead routing, a response time SLA, rejected lead recycling and no-show… |  |
| [Objection Handling Guide](skills/objection-handling-guide/) | Builds a sales objection handling guide from your own call notes, lost reasons, comments and reviews, ranking objections by pipeline touched and writing a sourced reply… | [Page](https://insightfulpipe.com/marketing-claude-skills/sales/objection-handling-guide) |
| [ROI Business Case Builder](skills/roi-business-case-builder/) | Builds the ROI business case for one buyer in one deal from their own numbers, with low, expected and high results, payback, NPV, sensitivity and a one-page case for… |  |
| [Sales Call Script Writer](skills/sales-call-script-writer/) | Writes sales call guides from your own call notes, including a cold calling script with voicemail and gatekeeper lines, a discovery guide tied to BANT or MEDDICC fields… |  |
| [Sales Deck Writer](skills/sales-deck-builder/) | Writes a B2B sales deck slide by slide from the buyer's goal, with headlines, speaker notes and a checked source for every claim, plus an optional .pptx. |  |
| [Sales Follow-Up Email Writer](skills/sales-follow-up-writer/) | Writes one-to-one sales follow-up emails for open deals from call notes, like the demo recap, proposal chasers and a polite last email, with when each is due. |  |
| [Sales One-Pager Writer](skills/sales-one-pager-writer/) | Writes a one-page sales sheet for one persona or industry, a solution brief, why-us comparison or customer result sheet, with sourced proof, benefits ranked by buyer… |  |
| [Sales Playbook Builder](skills/sales-playbook-builder/) | Builds a sales playbook from a CRM export, sequence report and call notes, with who to target, deal stages, weekly activity targets worked back from quota and a… |  |
| [Sales Proposal and RFP Response Writer](skills/sales-proposal-writer/) | Writes B2B sales proposals with priced options from discovery notes, and RFP responses with a compliance matrix and a bid or no-bid score before any answer, every claim… |  |

### ChatGPT Ads

Performance analysis and campaign building for ads in ChatGPT through the OpenAI Ads API.

| Skill | What it does | |
|---|---|---|
| [Chatgpt Ads Analyzer](skills/chatgpt-ads-analyzer/) | Audits a ChatGPT Ads (OpenAI Ads) account, grading campaigns, ads, conversions, pixel health, audiences, lead forms and budget pacing, then ranks fixes. | [Page](https://insightfulpipe.com/marketing-claude-skills/chatgpt-ads/chatgpt-ads-analyzer) |
| [Chatgpt Ads Campaign Builder](skills/chatgpt-ads-campaign-builder/) | Builds a ChatGPT Ads (OpenAI Ads) campaign from a brief, with ad groups, context hints, chat card ad copy, pixel, customer list audience and lead form as exact… | [Page](https://insightfulpipe.com/marketing-claude-skills/chatgpt-ads/chatgpt-ads-campaign-builder) |

### Content Marketing

Content distribution, editorial workflow, podcasts, ebooks, original research and pre-publish QA.

| Skill | What it does | |
|---|---|---|
| [Blog Charts and Visuals Planner](skills/blog-visuals-planner/) | Plans the charts, diagrams, screenshots and featured image a blog post needs, with chart specs, alt text and captions built only from sourced numbers, and ranks old… |  |
| [Blog Lead Conversion Planner](skills/blog-lead-conversion-planner/) | Plans blog calls to action and content upgrades from GA4 and Search Console, ranking articles by the leads they miss and matching each to an offer you already have. |  |
| [Content Distribution Planner](skills/content-distribution-planner/) | Plans how to promote one finished blog post, guide or report over its first 30 days, ranking your channels by what past pieces earned in GA4 and sizing any paid boost. |  |
| [Content Strategy Builder](skills/content-marketing-strategy/) | Builds a yearly content marketing strategy and a dated 90-day editorial calendar from what already converts in GA4 and Search Console, with themes, formats, gaps by… |  |
| [Editorial QA and Fact Check](skills/content-pre-publish-qa/) | Fact-checks and QAs a finished article, guide or report before publishing, checking claims against sources, quotes, links, stale years and prices, byline and… |  |
| [Editorial Workflow Builder](skills/editorial-workflow-builder/) | Designs a content team's editorial workflow from idea to published, with stage owners, approvals, turnaround targets and a capacity plan measured from WordPress output… |  |
| [Original Research and Industry Report Builder](skills/original-research-report/) | Plans and writes an original research, benchmark or industry report from your own product or survey data, with a 95% range on every figure, findings gated for precision… |  |
| [Podcast Episode Prep and Show Notes](skills/podcast-episode-kit/) | Preps and packages one podcast episode, with the guest brief, timed outline and interview questions before recording, then titles, descriptions, show notes with… |  |
| [Podcast Marketing Strategy Planner](skills/podcast-strategy-planner/) | Builds a podcast marketing strategy and a dated 12-episode plan, or reviews a running show, judging themes and guests against its own download and YouTube Analytics… |  |
| [Whitepaper and Ebook Writer](skills/ebook-whitepaper-writer/) | Writes a whitepaper, ebook, guide or playbook in full, from a brief or by compiling your best blog posts picked by Search Console clicks and GA4 key events, with an… |  |

### Copywriting

Advertorials, transcreation, UX microcopy, print and audio ads, and marketing claims checks.

| Skill | What it does | |
|---|---|---|
| [Advertorial and Presell Page Writer](skills/advertorial-presell-writer/) | Writes advertorial and presell pages, the story, listicle or reasons-why page between a Meta, TikTok or native ad and the product page, plus the lead-in ads and an FTC… |  |
| [Brand and Product Naming](skills/brand-product-naming/) | Names or renames a company, product, app, feature or pricing plan, scoring 30 ideas and checking the shortlist against Google results, App Store, Google Play, domains… |  |
| [Content Localization and Transcreation](skills/copy-transcreation/) | Localizes and transcreates landing pages, Google Ads and Microsoft Ads, emails, taglines, UI strings and blog posts for another country in the words that market… |  |
| [Marketing Claims Compliance Checker](skills/marketing-claims-checker/) | Checks claims in ads, landing pages, emails and product listings against FTC, UK CAP Code, EU and Google Ads or Meta policy rules, with a keep, fix or remove verdict… |  |
| [Radio, Podcast, Print and Direct Mail Ad Writer](skills/offline-audio-print-ad-writer/) | Writes radio and TV spots, podcast host reads, newsletter sponsorships, print ads, billboards, flyers and direct mail postcards, word counted per format, each with a… |  |
| [UX Microcopy Writer](skills/ux-microcopy-writer/) | Writes and audits UX microcopy for buttons, form labels, error messages, empty states, tooltips and 404 pages, with every state, a character limit and one UI glossary. |  |

### Creative

Creative briefs, video ad scripts, testing roadmaps and fatigue detection.

| Skill | What it does | |
|---|---|---|
| [Ad Creative Brief Generator](skills/ad-creative-brief-generator/) | Writes ad creative briefs for static, video, UGC and agency work from winning Google Ads or Meta lines, search terms, landing page and competitor ads, with scored… | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/ad-creative-brief-generator) |
| [Ad Creative Fatigue Detector](skills/ad-creative-fatigue-detector/) | Finds worn-out ads on Meta, Google Ads, TikTok, LinkedIn, Snapchat and X by comparing each live ad's peak and recent CTR, frequency and CPM, then scores fatigue and… | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/ad-creative-fatigue-detector) |
| [Ad Creative Scorer](skills/ad-creative-scorer/) | Grades one draft video or image ad out of 100 before launch for a Meta, TikTok, LinkedIn or Snapchat placement, with a policy check and the three edits worth the most… |  |
| [Ad Specs and Asset Matrix](skills/ad-specs-asset-matrix/) | Builds the ad specs and sizes matrix for one campaign across Meta, TikTok, LinkedIn, Pinterest, Snapchat, X and Google Ads, then checks your files and copy against it. |  |
| [Creative Testing Roadmap](skills/creative-testing-roadmap/) | Plans a quarter of creative tests from your Google Ads, Meta, TikTok or LinkedIn ads, finding winning angles and hooks and sizing the tests your traffic can decide… | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/creative-testing-roadmap) |
| [Video Ad Script Writer](skills/video-ad-script-writer/) | Writes timed video ad scripts for TikTok, Reels, YouTube, Meta and LinkedIn, plus VSLs and demos, built on Meta and TikTok hook and hold rates and Google Ads search… | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/video-ad-script-writer) |

### CRO

Conversion rate optimization for forms, signup flows and onboarding.

| Skill | What it does | |
|---|---|---|
| [Checkout Optimization Auditor](skills/checkout-cro-auditor/) | Audits an online store checkout step by step in GA4, checks Shopify, WooCommerce or Magento orders and checkout screenshots, and ranks fixes by revenue at stake. |  |
| [Form CRO](skills/form-cro/) | Audits lead, contact, demo and quote forms field by field and checks the GA4 form_start to form_submit funnel, giving keep, cut or make optional verdicts. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/form-cro) |
| [Heatmap and Session Recording Analyst](skills/heatmap-session-analyst/) | Ranks Microsoft Clarity or Hotjar rage clicks, dead clicks, quick backs and scroll depth by the GA4 conversions each costs, and names the Clarity recording filters to… |  |
| [Onboarding CRO](skills/onboarding-cro/) | Maps the new user journey in GA4 from first visit to activation and return, finds the biggest drop and designs the onboarding fix and emails, reading Klaviyo flows. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/onboarding-cro) |
| [Signup Flow CRO](skills/signup-flow-cro/) | Audits a signup or registration flow, checks GA4 sees sign_up, measures the funnel and tears down the signup page fields, SSO and password rules. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/signup-flow-cro) |
| [Website Conversion Rate Benchmark](skills/conversion-rate-benchmark/) | Benchmarks a website or store conversion rate against dated, sourced industry figures by channel, device and landing page type, from GA4 or pasted numbers, and prices… |  |
| [Website Personalization Planner](skills/website-personalization-planner/) | Plans website and landing page personalization from GA4, Google Ads and LinkedIn data, picking visitor groups that convert below the rest, writing their headline and… |  |

### Cross-Platform

Budget allocation across Google, Meta, TikTok, LinkedIn and Microsoft Ads.

| Skill | What it does | |
|---|---|---|
| [Ad Platform vs GA4 vs Store Reconciliation](skills/conversion-reconciliation/) | Reconciles conversions and revenue between Google Ads, Meta, LinkedIn, TikTok, GA4 and Shopify, WooCommerce or Magento orders, explaining each gap and finding missing… |  |
| [Agency Client Health Monitor](skills/agency-client-health/) | Scores the health of every agency client across Google Ads, Meta, GA4 and Search Console, flags churn risk, paces budgets across clients and audits account access. |  |
| [Blended ROAS and CAC Report](skills/blended-roas-report/) | Calculates blended ROAS, CAC and full-cost marketing ROI across Google Ads, Meta, LinkedIn, TikTok and other ad platforms against GA4 or store revenue. |  |
| [Campaign Launch Preflight](skills/campaign-launch-preflight/) | Runs a go or no-go preflight on a Google Ads, Meta or LinkedIn Ads campaign, checking tracking, GA4, the landing page and budget before launch or a budget raise. |  |
| [Cross Platform Budget Allocator](skills/cross-platform-budget-allocator/) | Splits ad budget across Google Ads, Meta, Microsoft, LinkedIn, TikTok and other platforms by what the next dollar buys, and plans the yearly marketing budget. | [Page](https://insightfulpipe.com/marketing-claude-skills/cross-platform/cross-platform-budget-allocator) |
| [KPI Alerts and Daily Digest](skills/kpi-alerts-digest/) | Runs a daily marketing health check and week-over-week anomaly scan across ad accounts, GA4 and Search Console, then drafts a short KPI digest or alert for Slack… |  |
| [Marketing Dashboard Builder](skills/marketing-dashboard-builder/) | Builds marketing dashboards in Google Sheets or Looker Studio, weekly report pages in Notion, Slack summaries and Airtable trackers, plus budget vs actual and the… |  |
| [Marketing Performance Report](skills/marketing-performance-report/) | Writes marketing reports across ad platforms, GA4, Search Console and Klaviyo, from weekly updates and monthly client reports to QBR or board decks, campaign wrap-ups… | [Page](https://insightfulpipe.com/marketing-claude-skills/cross-platform/marketing-performance-report) |
| [Paid vs Organic Search Overlap](skills/paid-organic-overlap/) | Compares Google Ads search terms with Search Console rankings to find keywords you pay for but already rank first for, pricing each by incremental CPA. |  |
| [Performance Drop Investigator](skills/performance-drop-investigator/) | Investigates why a marketing number dropped across Search Console, GA4, Google Ads, Meta and LinkedIn, ruling out broken tracking first and grading each cause. |  |

### E-commerce

Store reports, merchandising, promotions, AOV, bundles, inventory, returns and profit on ad spend.

| Skill | What it does | |
|---|---|---|
| [Average Order Value Optimizer](skills/aov-optimizer/) | Finds how to raise average order value from Shopify, WooCommerce or Magento orders, pricing shipping thresholds, gift with purchase, tiers, add-ons and code minimums in… |  |
| [Competitor Price Tracker](skills/competitor-price-tracker/) | Tracks a store's prices against named competitors and Amazon sellers by matched GTIN, compares landed prices and promotions, and sets match, beat, premium or hold… |  |
| [Cross-Border Store Setup Planner](skills/cross-border-store-expansion/) | Sets up a store to sell in countries already chosen, pricing each market on landed cost with duty, VAT and currency fees, plus shipping rates, local payments… |  |
| [Discount and Promotion Analyst](skills/discount-promo-analyst/) | Measures discount codes and sitewide sales from a store's own orders, showing margin given away, who used each code, codes leaked to coupon sites and whether a sale… |  |
| [Ecommerce Store Report](skills/ecommerce-store-report/) | Builds the weekly or monthly sales report from a store's orders (Shopify, WooCommerce, Magento), with net sales, AOV, new and returning buyers, channels, countries and… |  |
| [Online Store Launch Checklist](skills/store-launch-checklist/) | Checks a new store before launch, marking each item pass, fail or unknown with evidence across domain, policies, payments, taxes, shipping, products, GA4, speed, email… |  |
| [Product Bundle and Cross-Sell Builder](skills/bundle-cross-sell-builder/) | Runs market basket analysis on a store's orders to find products bought together, then prices bundles against margin and plans pairs well with picks, post-purchase… |  |
| [Product Merchandising Analyst](skills/product-merchandising-analyst/) | Ranks a store's products and collections on GA4 item views, add-to-cart rate, purchase rate and margin, then picks home page products, sorts each collection and flags… |  |
| [Profit on Ad Spend (POAS) Report](skills/poas-profit-report/) | Calculates profit on ad spend (POAS) next to ROAS per campaign, product group and product for Google Ads, Meta, TikTok and Pinterest, from a store's own costs, fees and… |  |
| [Repeat Purchase and Subscribe-and-Save Planner](skills/repeat-purchase-planner/) | Plans how a store turns first-time buyers into repeat buyers from its own orders, finding gateway products, reorder intervals, subscribe and save candidates and refill… |  |
| [Returns and Refunds Analyst](skills/returns-refunds-analyst/) | Analyses a store's returns and refunds from Shopify, WooCommerce or Magento orders, finding which products, sizes, campaigns and discount codes return most and why, and… |  |
| [Stock-Out and Excess Inventory Planner](skills/inventory-planner/) | Plans marketing around stock, with days of cover and reorder-by dates per variant, holding low stock out of Shopping, Performance Max, Meta catalog ads and emails, and… |  |
| [Store Site Search Analyst](skills/store-site-search-analyst/) | Analyses a store's GA4 or Shopify site search terms against its catalogue, classing failed searches as misspellings, synonyms, sold out or not carried, and ranks fixes… |  |

### Email Marketing

Lifecycle strategy, deliverability, segmentation, list health, retention and SMS planning.

| Skill | What it does | |
|---|---|---|
| [Churn Risk and Win-back Planner](skills/churn-risk-winback-planner/) | Finds lapsed and at-risk customers from Shopify, WooCommerce, Magento or BigQuery orders by each product line's repurchase gap, then plans margin-capped win-back… |  |
| [Competitor Email Teardown](skills/competitor-email-teardown/) | Benchmarks rival email programs from inbox exports, measuring welcome speed, frequency, signup offers, discounts, subject lines and sale timing against your Klaviyo or… |  |
| [Customer Retention Cohort Analyst](skills/retention-cohort-analyst/) | Builds customer retention cohorts from Shopify, WooCommerce, Magento or subscription orders, with repeat rate, days to second order and refill reminder delays. |  |
| [Email and Lifecycle Marketing Strategy](skills/email-lifecycle-strategy/) | Writes an email and lifecycle marketing strategy, setting customer stages from Shopify or WooCommerce reorder gaps, mapping Klaviyo or Mailchimp flows, SMS, push and… |  |
| [Email Deliverability Auditor](skills/email-deliverability-auditor/) | Audits email deliverability, checking SPF, DKIM and DMARC alignment, Gmail, Yahoo and Microsoft bulk-sender rules, and bounces and complaints by mailbox provider, then… |  |
| [Email List Cleaner](skills/email-list-cleaner/) | Cleans an email contact CSV, Excel file or Google Sheet before import, flagging bad syntax, duplicates, typo and throwaway domains, dead mail servers, role addresses… |  |
| [Email List Growth Optimizer](skills/email-list-growth-optimizer/) | Grades every popup, flyout, embedded form and checkout opt-in on sign-ups per 1,000 sessions from Klaviyo or Mailchimp, GA4 and Shopify data, then writes paste-ready… |  |
| [Email Marketing Calendar and Send Frequency Planner](skills/email-campaign-calendar/) | Plans a quarter of Klaviyo or Mailchimp email broadcasts, setting send frequency per engagement tier from the list's own unsubscribes, complaints and revenue, then… |  |
| [Email Platform Setup and Migration Planner](skills/email-platform-setup-migration/) | Plans an email platform migration such as Mailchimp to Klaviyo, or a first setup, with inventory, field and consent mapping, suppressions imported first, store event… |  |
| [Email Send Check](skills/email-send-check/) | Proofs a finished Klaviyo or Mailchimp campaign or flow email before it sends, checking links, UTM tags against GA4, merge tag fallbacks, alt text, Gmail clipping… |  |
| [HTML Email Template Builder](skills/html-email-template-builder/) | Codes responsive HTML email templates for Gmail, Outlook, Apple Mail and dark mode from copy, a design or a broken email, with plain text and a 15-point check, saved to… |  |
| [Loyalty and VIP Program Designer](skills/loyalty-vip-program-designer/) | Designs or reviews a points and VIP tier loyalty program from Shopify, WooCommerce or Magento orders, placing tiers on real spend, sizing rewards to gross margin and… |  |
| [Push Notification and In-App Message Planner](skills/push-inapp-message-planner/) | Plans push notifications and in-app messages for iOS, Android and web, setting the permission ask, caps from the app's opt-outs, quiet hours and copy, using GA4 and App… |  |
| [RFM Analysis and Segmentation](skills/customer-segmentation-rfm/) | Scores every buyer by RFM from Shopify, WooCommerce, Magento, BigQuery or CSV orders, names segments with revenue shares, and sets each segment's offer and email… |  |
| [SMS and WhatsApp Marketing Planner](skills/sms-whatsapp-planner/) | Plans SMS and WhatsApp marketing for Klaviyo or any SMS platform, picks text or email per moment, writes opt-ins and every text with segment counts and cost per send… |  |
| [Subscription Cancel Flow and Dunning Planner](skills/cancel-flow-dunning-planner/) | Plans subscription cancel flows and dunning from Stripe, Chargebee, Paddle or Recharge exports, splitting churn into cancellations and failed payments, and writes save… |  |

### Facebook Ads

Account audits, audiences, structure, creative tests, budgets and reports for Meta Ads.

| Skill | What it does | |
|---|---|---|
| [Facebook Ads Account Auditor](skills/facebook-ads-account-auditor/) | Audits a whole Meta Ads account for Facebook and Instagram across billing, policy, pixel tracking, structure, audiences, budget, creative fatigue and naming, with fixes… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-account-auditor) |
| [Facebook Ads Audience Builder](skills/facebook-ads-audience-builder/) | Builds a Meta Ads audience plan for Facebook and Instagram with cold, warm and hot tiers, exclusions, and specs for retargeting and lookalike audiences. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-audience-builder) |
| [Facebook Ads Budget Allocator](skills/facebook-ads-budget-allocator/) | Reallocates Facebook and Meta Ads budget between campaigns and ad sets in 20% steps, graded on cost per result, saturation and marginal cost. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-budget-allocator) |
| [Facebook Ads Campaign Structure](skills/facebook-ads-campaign-structure/) | Designs or restructures a Facebook and Meta Ads account into campaigns and ad sets that can exit learning, picks CBO or ABO and naming, plans a starting budget, and… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-campaign-structure) |
| [Facebook Ads Creative Tester](skills/facebook-ads-creative-tester/) | Plans, sizes and reads Facebook and Instagram creative A/B tests on Meta with sample size, budget and significance, compares ad formats, and ranks assets inside… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-creative-tester) |
| [Facebook Ads Launch Checklist](skills/facebook-ads-launch-checklist/) | Checks one Meta Ads campaign before launch with a pre-flight checklist and a READY or NOT READY verdict, and diagnoses Facebook ads that are not spending, not… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-launch-checklist) |
| [Facebook Ads Monthly Report](skills/facebook-ads-monthly-report/) | Writes monthly or weekly Facebook and Meta Ads reports with goal tracking, what drove cost per result, campaign, audience, placement and creative breakdowns, and next… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-monthly-report) |
| [Facebook Ads Scaling Roadmap](skills/facebook-ads-scaling-roadmap/) | Builds a phased Facebook and Meta Ads scaling roadmap with a readiness check, winning ads to scale, a week-by-week budget path to a target spend, expected cost per… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-scaling-roadmap) |

### Google Ads

Search term, keyword, bidding, budget, PMax and reporting skills for Google Ads.

| Skill | What it does | |
|---|---|---|
| [Ad Copy Performance Ranker](skills/ad-copy-performance-ranker/) | Ranks Google Ads responsive search ads and each headline and description by clicks and conversions, with head-to-heads per ad group and an ad strength reality check. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/ad-copy-performance-ranker) |
| [AI Max for Search Reviewer](skills/ai-max-search-reviewer/) | Decides whether a Google Ads Search campaign should turn on AI Max, then reviews it by match source, added search terms, landing pages and generated headlines, and… |  |
| [Bid Strategy Auditor](skills/bid-strategy-auditor/) | Audits Google Ads Smart Bidding per campaign and sets target CPA or ROAS, value-based and profit bidding, data exclusions and seasonality adjustments. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/bid-strategy-auditor) |
| [Budget Allocation Optimizer](skills/budget-allocation-optimizer/) | Moves Google Ads budget between campaigns for more conversions from the same total, using marginal CPA, budget simulations and impression share lost to budget. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/budget-allocation-optimizer) |
| [Competitor Keyword Campaign Planner](skills/competitor-keyword-campaign-planner/) | Plans a Google Ads competitor campaign on rival brand names, rating each rival go, test or skip and drafting paused ad groups, negatives, comparison ads without rival… |  |
| [Display Video Demand Gen Auditor](skills/display-video-demand-gen-auditor/) | Audits running Google Ads Display, YouTube and Demand Gen campaigns, builds a paste-ready placement exclusion list from spend and clicks, reports video view rates and… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/display-video-demand-gen-auditor) |
| [GAQL Query Builder](skills/gaql-report-builder/) | Writes and fixes GAQL (Google Ads Query Language) queries from a plain reporting question, runs them read-only when Google Ads is connected, and adds API, Google Ads… |  |
| [Geo Performance Optimizer](skills/geo-performance-optimizer/) | Finds which Google Ads locations, devices and hours waste or earn money, grades each slice against its own campaign CPA and picks the lever the bid strategy actually… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/geo-performance-optimizer) |
| [Google Ad Grants Manager](skills/google-ad-grants-manager/) | Checks a nonprofit's Google Ad Grants account against every compliance rule, plans keyword pauses to get back over the 5% CTR line and builds a plan to spend more of… |  |
| [Google Ads Account Audit](skills/google-ads-account-audit/) | Runs a full Google Ads account audit across tracking, wasted spend, structure, Quality Score, ads, assets, bidding, settings and change history, scores eight areas and… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-account-audit) |
| [Google Ads Account Restructure Planner](skills/google-ads-account-restructure-planner/) | Plans a Google Ads restructure that merges or splits Search campaigns so each clears its bid strategy volume, keeps brand apart and writes a week-by-week migration with… |  |
| [Google Ads Audience Analyzer](skills/google-ads-audience-analyzer/) | Analyzes Google Ads audience segments, remarketing lists, Customer Match and age, gender, income and parental status against each campaign, after a personalized ads… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-audience-analyzer) |
| [Google Ads Bulk Ad and URL Updater](skills/google-ads-bulk-updater/) | Finds and replaces a price, offer, year, phone number, final URL or tracking template everywhere in a Google Ads account, paused items included, checks lengths, policy… |  |
| [Google Ads Campaign Builder](skills/google-ads-campaign-builder/) | Builds a Google Ads Search campaign from a short brief with a launch checklist, keywords, negatives, ads and paused payloads, plus keyword budget forecasts and Smart… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-campaign-builder) |
| [Google Ads Click Fraud Check](skills/google-ads-click-fraud-check/) | Checks a Google Ads account for click fraud, reading invalid clicks first, then testing search partner, placement, off-area, night and device clicks against GA4… |  |
| [Google Ads Delivery Troubleshooter](skills/google-ads-delivery-troubleshooter/) | Finds why Google Ads campaigns, keywords or ads are not showing or not spending, reading status reasons, billing, policy, blocking negatives, settings and lost share… |  |
| [Google Ads Disapproval and Suspension Fixer](skills/google-ads-disapproval-suspension-fixer/) | Fixes Google Ads disapproved and limited ads, keywords and assets with plain policy reasons and compliant rewrites, and drafts proof lists and appeals for suspensions… |  |
| [Google Ads Extensions and Assets Auditor](skills/google-ads-assets-auditor/) | Audits every Google Ads asset or extension by campaign, from sitelinks, callouts and snippets to call, price and image assets, flags gaps, override traps, disapproved… |  |
| [Google Ads Hacked Account Check and Recovery](skills/google-ads-hacked-account-recovery/) | Checks a Google Ads account for takeover signs such as unknown users, manager links, new campaigns, edited URLs, spend spikes and billing changes, then sets out the… |  |
| [Google Ads Recommendations Reviewer](skills/google-ads-recommendations-reviewer/) | Reviews open Google Ads recommendations with an accept, adapt or dismiss verdict tested on the account's own numbers, plus auto-apply and asset automation settings. |  |
| [Google Ads Scripts and Automated Rules Writer](skills/google-ads-scripts-rules-writer/) | Writes, explains and fixes Google Ads scripts and automated rules for budget caps, broken URL checks, zero-conversion keywords, search terms to Sheets and spend jump… |  |
| [Google Ads Weekly Brief](skills/google-ads-weekly-brief/) | Writes the weekly Google Ads brief for a client, boss or team as an email, Slack post or slides, and reviews 90 days of change history for edits that helped or hurt. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-weekly-brief) |
| [Google App Campaigns Planner and Reviewer](skills/google-app-campaigns-manager/) | Plans and reviews Google App campaigns (UAC) for installs, in-app actions, value or pre-registration, checking budget and event volume, writing assets from the store… |  |
| [Google Shopping and Retail PMax Review](skills/google-shopping-retail-pmax-review/) | Reviews Google Shopping and retail Performance Max structure product by product against target, splits unserved products into not eligible, not targeted or outbid, and… |  |
| [Impression Share Analyst](skills/impression-share-analyst/) | Analyzes Google Ads search impression share lost to budget or rank, with a 12-week trend, top of page detail, Auction Insights exports and a weekly brand defense… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/impression-share-analyst) |
| [Keyword Performance Analyzer](skills/keyword-performance-analyzer/) | Analyzes Google Ads keywords into stars, bleeders and Quality Score victims, checking CPA or ROAS, match types, Migrate to Exact, duplicates, cannibalisation, low… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/keyword-performance-analyzer) |
| [Month End Report Generator](skills/month-end-report-generator/) | Writes the month-end Google Ads report against last month, last year and goals, with a graded scorecard, campaign tiers, changes that worked and next month's plan, plus… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/month-end-report-generator) |
| [Negative Keyword Implementer](skills/negative-keyword-implementer/) | Adds Google Ads negative keywords safely, checking existing negatives for conflicts with live keywords, building new ones from search terms, rolling lists to campaigns… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/negative-keyword-implementer) |
| [PMax Asset Group Analyzer](skills/pmax-asset-group-analyzer/) | Reviews Google Ads Performance Max campaigns by asset group, asset, audience signal, search term and channel split, and drafts a first PMax campaign when none exists. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/pmax-asset-group-analyzer) |
| [Quality Score Fixer](skills/quality-score-fixer/) | Diagnoses low Google Ads Quality Score by expected CTR, ad relevance and landing page experience, then ranks fixes across keyword to ad match, ad strength, pinned… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/quality-score-fixer) |
| [Rsa Ad Copy Writer](skills/rsa-ad-copy-writer/) | Writes Google Ads responsive search ad headlines and descriptions from converting keywords and the landing page, plus sitelinks, callouts, keyword insertion… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/rsa-ad-copy-writer) |
| [Scaling Roadmap Builder](skills/scaling-roadmap-builder/) | Plans how to scale Google Ads spend in phases, checking readiness, marginal CPA headroom and new keywords, with daily budgets and pause triggers. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/scaling-roadmap-builder) |
| [Search Term Gold Miner](skills/search-term-gold-miner/) | Mines Google Ads search terms into gold, garbage and grey zone with n-grams and returns safe negatives, exact keywords to promote and keyword ideas. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/search-term-gold-miner) |
| [Shopping Feed Optimizer](skills/shopping-feed-optimizer/) | Audits product feeds for Google Shopping, Merchant Center and Meta Catalog from an export, scoring attributes, GTINs, titles, images, prices and custom labels. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/shopping-feed-optimizer) |
| [Spend Pacing Monitor](skills/spend-pacing-monitor/) | Checks Google Ads month-to-date spend pacing, projects where the month will land against a target or budget ceiling, flags capped or stopped campaigns and drafts… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/spend-pacing-monitor) |
| [YouTube, Demand Gen and Display Campaign Builder](skills/youtube-demand-gen-campaign-builder/) | Plans a Google Ads YouTube, Demand Gen or Display campaign from a goal and budget, choosing bidding, audiences, videos by retention and exclusions, and checking asset… |  |

### Growth

Product-led growth: growth loops, North Star metric, trial-to-paid, paywalls, lead magnets and experiment backlogs.

| Skill | What it does | |
|---|---|---|
| [Developer Tool Growth Plan](skills/developer-oss-growth/) | Plans developer marketing and a 90-day growth plan for a dev tool, API or open-source project, tracing docs traffic, GitHub stars and signup cohorts through to paid… |  |
| [Feature Adoption Planner](skills/feature-adoption-planner/) | Plans feature adoption campaigns for existing software users. |  |
| [Growth Experiment Backlog](skills/growth-experiment-backlog/) | Builds a growth experiment backlog from the weakest funnel step in GA4 or pasted numbers, scores ideas with ICE or RICE, drops tests the traffic cannot power, plans a… |  |
| [Growth Loop Designer](skills/growth-loop-designer/) | Designs growth loops (invites, shared outputs, public pages, content, paid reinvestment), measures each loop's output and cycle time from product numbers or GA4, and… |  |
| [Interactive Calculator Builder](skills/interactive-calculator-builder/) | Builds a working ROI, savings, cost or quote calculator as one embeddable HTML file, with the formula checked against worked examples, GA4 events, optional email… |  |
| [Lead Magnet Writer](skills/lead-magnet-writer/) | Writes a finished lead magnet (checklist, fill-in template, one-page guide or email course) with opt-in copy and a delivery email, picking the angle from Search Console… |  |
| [Net Revenue Retention and Expansion Planner](skills/expansion-revenue-planner/) | Calculates SaaS net revenue retention (NRR) and GRR from Stripe or billing exports, scores which paying accounts are ready to upgrade, add seats or buy add-ons, and… |  |
| [North Star Metric Builder](skills/north-star-metric-builder/) | Chooses a North Star metric by testing candidates against your retention and revenue history from GA4, BigQuery or pasted data, then builds 3 to 5 input metrics with… | [Page](https://insightfulpipe.com/marketing-claude-skills/growth/north-star-metric-builder) |
| [Paywall Screen Optimizer](skills/paywall-screen-optimizer/) | Reviews subscription app and SaaS paywall screens by placement, ranks where starts are lost from GA4 or pasted counts, checks App Store and Google Play disclosure… |  |
| [PLG and SaaS Growth Audit](skills/plg-saas-growth-audit/) | Audits a self-serve SaaS funnel from visit to signup, activation, paid, expansion, churn and failed payments, puts an MRR figure on each leak from GA4, Stripe or… |  |
| [Plugin and Integration Marketplace Optimizer](skills/integration-marketplace-listing/) | Audits and rewrites app and plugin listings on the Shopify App Store, Chrome Web Store, WordPress.org and Atlassian Marketplace against field limits and rivals, and… |  |
| [Quiz Funnel Builder](skills/quiz-funnel-builder/) | Builds a quiz funnel (product recommendation quiz, lead gen quiz or scorecard) from real customer groups in Shopify, WooCommerce, Klaviyo or GA4, with every answer path… |  |
| [Trial-to-Paid Conversion Optimizer](skills/trial-to-paid-optimizer/) | Finds why free trial users don't pay from Stripe, Paddle or Chargebee exports, splits trials by activation and source, checks trial emails, length and card rule, and… |  |

### LinkedIn Ads

B2B targeting, lead quality and CPL audits for LinkedIn Ads.

| Skill | What it does | |
|---|---|---|
| [LinkedIn Abm Reporting](skills/linkedin-abm-reporting/) | Builds a LinkedIn Ads ABM report showing target account coverage, buying committee reach by seniority, matched audience and retargeting results, and a monthly funnel to… | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-abm-reporting) |
| [LinkedIn Ad Copy Writer](skills/linkedin-ad-copy-writer/) | Writes LinkedIn ad copy from the account's lowest cost per lead ads, with character counts, for intro text, headlines, document, carousel, event, Message Ads and… |  |
| [LinkedIn Ads Auditor](skills/linkedin-ads-auditor/) | Audits a LinkedIn Ads account across tracking, structure, Audience Network, targeting, frequency, bidding, formats and lead quality, ranking fixes by spend at stake. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-auditor) |
| [LinkedIn Ads B2B Optimizer](skills/linkedin-ads-b2b-optimizer/) | Optimizes LinkedIn Ads for B2B by finding which seniorities, job titles, company sizes and industries earn qualified leads, then fixes bids, budgets, weak ads and… | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-b2b-optimizer) |
| [LinkedIn Ads Campaign Builder](skills/linkedin-ads-campaign-builder/) | Builds a new LinkedIn Ads campaign or three-stage funnel from a brief, with objective, targeting, suggested bid pricing, intro text and headlines, a pre-flight check… | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-campaign-builder) |
| [LinkedIn Lead Gen Optimizer](skills/linkedin-lead-gen-optimizer/) | Reviews LinkedIn Lead Gen Forms for form design, open to completion drop-off, cost per lead by campaign and audience, and lead quality from work email share or CRM… | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-lead-gen-optimizer) |
| [LinkedIn Thought Leader Ads Planner](skills/linkedin-thought-leader-ads-planner/) | Plans LinkedIn Thought Leader Ads by ranking founder, employee and creator posts against each author's usual engagement rate, then drafts the bid, budget per post and a… |  |

### Local Marketing

Google Business Profile, reviews and local search performance for local businesses.

| Skill | What it does | |
|---|---|---|
| [Fake Review Removal Handler](skills/review-removal-handler/) | Tests negative or fake Google, Yelp and Amazon reviews against each site's content policy, spots review bombing, drafts report notes and calm replies, and tracks appeals. |  |
| [Google Business Profile Manager](skills/google-business-profile-manager/) | Audits Google Business Profile locations on Google Maps, grading completeness, hours, photos, posts, reviews and calls, ranks the locations, and drafts posts and review… |  |
| [Local Business Marketing Report](skills/local-business-marketing-report/) | Builds a local business marketing report from Google Business Profile and Search Console with a 30/60/90-day local SEO plan, or a 90-day marketing plan for one location. |  |
| [Local Citation and NAP Audit](skills/local-citation-nap-audit/) | Audits local citations and NAP consistency, comparing name, address, phone, website and hours on each listing with the Google Business Profile, and flags duplicate Maps… |  |
| [Local Competitor Gap Analysis](skills/local-competitor-gap/) | Compares a local business with the Google Maps listings that outrank it in the map pack on categories, reviews, photos, hours and website, and ranks the gaps by impact. |  |
| [Local Lead Ads Planner](skills/local-lead-ads-planner/) | Grades Yelp Ads, Angi, Thumbtack and Nextdoor Ads spend by booked jobs, not leads, sets the most a lead can cost, picks services and ZIP codes to keep, and drafts lead… |  |
| [Local Rank Tracker by Area](skills/local-rank-grid-tracker/) | Tracks local map pack rankings by area, checking each service keyword from every town, neighborhood or ZIP code served, and maps strong and gap areas and who holds them. |  |
| [Local Services Ads Manager](skills/local-services-ads-manager/) | Reviews Google Local Services Ads by cost per booked job, with leads by job type and area, missed charged calls, budget use, bids and lead feedback drafts for credits. |  |
| [Multi-Location and Franchise Marketing Plan](skills/multi-location-marketing-plan/) | Builds a franchise or multi-location marketing plan, tiering locations by Google Business Profile views and actions, splitting the brand fund and co-op, and setting… |  |
| [Review Generation Planner](skills/review-generation-planner/) | Plans how to get more Google reviews and product reviews, setting a target and monthly pace against local rivals, checking asks against Google review policy and the FTC… |  |
| [Review Insights Analyzer](skills/review-insights-analyzer/) | Analyzes Google, Amazon, Yelp or WooCommerce reviews, coding them into themes that drive 1-star and 5-star ratings, with trends by location or product and what each fix… |  |
| [Reviews and Comments Responder](skills/reviews-and-comments-responder/) | Drafts replies to unanswered Google reviews, Facebook, Instagram, YouTube, LinkedIn and Meta ad comments, X mentions and App Store and Google Play reviews, ranked by… |  |

### Marketing

Copywriting, brand voice, SEO, landing pages, email and competitor research.

| Skill | What it does | |
|---|---|---|
| [Ad Landing Page Match Scorer](skills/ad-landing-page-match-scorer/) | Scores each active Google Ads or Meta ad against its landing page for headline, offer, keyword and audience match plus mobile speed, ranked by spend. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/ad-landing-page-match-scorer) |
| [B2B Lead Enrichment and Scoring](skills/b2b-lead-enrichment/) | Cleans, enriches and scores B2B lead lists from Google Sheets, Airtable or a paste for ICP fit, maps decision makers, drafts cold emails and watches target accounts for… |  |
| [Brand Voice](skills/brand-voice/) | Builds a brand voice and tone guide and a messaging house from your Google Ads, Meta ads, social posts and site copy, then checks live copy against it. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/brand-voice) |
| [Buyer Persona Builder](skills/buyer-persona-builder/) | Builds buyer personas and an ICP from GA4, Search Console, LinkedIn Ads, Meta and Klaviyo evidence, plus interview plans, voice of customer analysis and best-fit… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/buyer-persona-builder) |
| [Case Study Writer](skills/case-study-writer/) | Writes case studies and customer success stories from measured before and after results in Search Console, GA4 or Google Ads, or from a customer interview kit, with… |  |
| [Competitor Ad Research](skills/competitor-ad-research/) | Researches competitors' live ads in the public Meta, Google, Microsoft and LinkedIn ad libraries, mapping longest-running ads, offers, landing pages and hooks. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-ad-research) |
| [Competitor SWOT Analyzer](skills/competitor-swot-analyzer/) | Builds a competitor SWOT, positioning read and sales battlecard from public search, pricing and company data for you and up to three rivals, and runs a weekly or… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-swot-analyzer) |
| [Competitor Website Teardown](skills/competitor-website-teardown/) | Tears down up to four competitor websites against yours on search traffic, ranking page types, home and pricing pages, mobile speed and YouTube output, then ranks five… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-website-teardown) |
| [Content Calendar Scheduler](skills/content-calendar-scheduler/) | Builds a social media content calendar and schedules posts to Facebook, Instagram, TikTok and LinkedIn from each account's own history, with best times and a holidays… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/content-calendar-scheduler) |
| [Content Performance Analyst](skills/content-performance-analyst/) | Analyses blog, social and email content performance from GA4, Facebook, Instagram, LinkedIn, YouTube, TikTok and Klaviyo, with a monthly social media report and a… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/content-performance-analyst) |
| [Copywriting](skills/copywriting/) | Writes and rewrites conversion copy, headlines, taglines, hooks, CTAs, ads and emails from Google Ads search terms, Search Console and winning ad lines, and humanizes… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/copywriting) |
| [Cross Channel Attribution Analyst](skills/cross-channel-attribution-analyst/) | Compares first-touch, last-click and GA4 model credit per channel against spend and claims from Google Ads, Meta, LinkedIn, Microsoft Ads and TikTok, with CPA and ROAS… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/cross-channel-attribution-analyst) |
| [Email Campaign Analyst](skills/email-campaign-analyst/) | Analyses Klaviyo or Mailchimp email campaigns for clicks, revenue, deliverability, subject lines, send times and list growth, with a monthly report. |  |
| [Email Sequence Builder](skills/email-sequence-builder/) | Plans and writes Klaviyo or Mailchimp email sequences and flows, from welcome, onboarding and nurture to abandoned cart, winback, back in stock and replenishment, plus… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/email-sequence-builder) |
| [Funnel Dropoff Diagnostician](skills/funnel-dropoff-diagnostician/) | Finds where a signup, checkout or lead funnel loses people, from GA4 events plus Google Ads, Meta, LinkedIn and Search Console steps, and ranks leaks by conversions lost. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/funnel-dropoff-diagnostician) |
| [Klaviyo Flow Auditor](skills/klaviyo-flow-auditor/) | Audits Klaviyo and Mailchimp flows for missing or weak automations, unengaged profiles and abandoned cart recovery measured from Shopify orders. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/klaviyo-flow-auditor) |
| [Landing Page Auditor](skills/landing-page-auditor/) | Audits a landing page, homepage or sales page for conversion using GA4, Search Console, Google Ads and desktop and mobile renders, scoring seven pillars and ranking… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/landing-page-auditor) |
| [Marketing Psychology](skills/marketing-psychology/) | Tests persuasion levers such as social proof, loss framing and urgency on your Google Ads and Meta ad lines, maps where they sit on landing pages and flags dark patterns. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/marketing-psychology) |
| [Newsletter](skills/newsletter/) | Writes email newsletter issues from your published posts, GA4 or Search Console traffic and past Klaviyo or Mailchimp clicks, with subject lines and preview text. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/newsletter) |
| [Pricing Page Auditor](skills/pricing-page-auditor/) | Audits a pricing page from GA4 behaviour (reach, scroll, next pages, plan clicks) and eight pillars like tier architecture, anchoring and CTA clarity, with rewrites and… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/pricing-page-auditor) |
| [Programmatic SEO](skills/programmatic-seo/) | Plans programmatic SEO pages, one template per city, trade, integration or competitor, by sizing demand per permutation and reading SERPs and incumbents, then gives a… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/programmatic-seo) |
| [Retargeting Sequence Designer](skills/retargeting-sequence-designer/) | Designs retargeting ad sequences sized from GA4, checking the Meta pixel, Google Ads lists and Klaviyo overlap, then sets tiers, windows, messages, frequency… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/retargeting-sequence-designer) |
| [SEO Audit](skills/seo-audit/) | Audits a site's SEO from Search Console, Bing, PageSpeed and GA4, covering indexation, broken links, redirects, titles, H1s, thin pages and speed, ranked by… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/seo-audit) |
| [Social Content](skills/social-content/) | Plans and writes organic social posts from your Facebook, Instagram, TikTok, LinkedIn, Threads and X history, with captions, Reel scripts, threads and hashtags. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/social-content) |
| [USP Extractor](skills/usp-extractor/) | Finds your unique selling proposition by scoring Google Ads response, search terms, reviews and competitor pages, then writes the USP, ad and page messaging and claims… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/usp-extractor) |

### Marketing Ops

Campaign briefs, SOPs, capacity, team planning, hiring and the martech stack.

| Skill | What it does | |
|---|---|---|
| [AI Marketing Workflow Planner](skills/ai-marketing-workflow-planner/) | Plans which marketing tasks to automate with AI, which Claude drafts for approval and which stay human, scored from your task list and time log, with build specs, hours… |  |
| [Marketing Campaign Brief Writer](skills/campaign-brief-writer/) | Writes a one-page marketing campaign brief from a request or meeting notes, with one objective, KPIs baselined on past Google Ads, Meta, LinkedIn Ads and Klaviyo… |  |
| [Marketing Capacity Planner](skills/marketing-capacity-planner/) | Plans team capacity from a timesheet export, with billable utilization per person, retainer hours burned, scope creep and each client's margin, then next month's… |  |
| [Marketing Hiring Kit](skills/marketing-hiring-kit/) | Builds a kit to hire one marketer (PPC, paid social, SEO, content, email, ops or head of marketing) with a first-year scorecard, a job description bias check, interview… |  |
| [Marketing Ops and Martech Stack Audit](skills/marketing-ops-stack-audit/) | Audits a martech stack against what really loads on the site and in Google Tag Manager, finding unused or cancelled tools, duplicate pixels, broken data links and… |  |
| [Marketing SOP Builder](skills/marketing-sop-builder/) | Writes a marketing SOP and one-page checklist for a recurring process like campaign launch, monthly reporting or tracking QA, checking each step against connected… |  |
| [Marketing Team Structure Planner](skills/marketing-team-planner/) | Designs a marketing team structure from where results come from in GA4, Search Console and ad accounts, pricing each role in-house, freelance or agency with your rates… |  |

### Marketplaces

Amazon Ads, retail media, TikTok Shop and marketplace expansion.

| Skill | What it does | |
|---|---|---|
| [Amazon Ads Audit](skills/amazon-ads-audit/) | Audits an Amazon Ads account (Sponsored Products, Brands, Display, DSP) from your exports against each product's break-even ACOS, with TACOS, brand split, wasted search… |  |
| [Amazon PPC Bid Optimizer](skills/amazon-ppc-bid-optimizer/) | Sets Amazon Sponsored Products keyword, product target and placement bids to hit a target ACOS or TACOS, in capped weekly steps with a bulk file to upload. |  |
| [Amazon PPC Campaign Builder](skills/amazon-ppc-campaign-builder/) | Builds the Amazon PPC structure for a new product or book, with exact, phrase, broad, auto, competitor ASIN and brand defense campaigns, bids from break-even ACOS and a… |  |
| [Amazon Search Term Harvester](skills/amazon-search-term-harvester/) | Runs the weekly Amazon search term harvest, moving converting terms into exact match, adding negative and cross-campaign negative keywords and spotting competitor… |  |
| [Etsy SEO and Shop Audit](skills/etsy-shop-optimizer/) | Audits an Etsy shop from its listings CSV and Stats, ranking the listings that lose the most orders and checking tags, titles, photos, price, shipping and shop pages. |  |
| [Marketplace Expansion Planner](skills/marketplace-expansion-planner/) | Plans which marketplaces to sell on next (Amazon, Walmart, eBay, Etsy, TikTok Shop) from each product's margin after fees, channel rules, demand and MAP conflicts, with… |  |
| [Retail Media Planner (Walmart, Instacart, Target)](skills/retail-media-planner/) | Compares retail media beyond Amazon (Walmart Connect, Instacart Ads, Target Roundel) by rebuilding every network's ROAS on one attribution scale against break-even… |  |
| [TikTok Shop GMV Max Planner](skills/tiktok-shop-gmv-max-planner/) | Plans and reviews TikTok Shop GMV Max ads, setting ROI targets from product margins, grouping products into campaigns, ramping budgets and giving weekly scale, fix or… |  |
| [TikTok Shop Launch and Growth Planner](skills/tiktok-shop-planner/) | Plans a TikTok Shop launch or growth push, picking hero products and setting launch prices, affiliate commission, creator samples and a LIVE schedule from each… |  |

### Measurement

GA4 tracking, attribution audits, A/B tests, incrementality and LTV:CAC.

| Skill | What it does | |
|---|---|---|
| [A/B Test Designer](skills/ab-test-designer/) | Designs and reads out A/B tests on Google Ads, GA4 pages and email, with sample size, duration, significance and a winner verdict. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ab-test-designer) |
| [Attribution Model Auditor](skills/attribution-model-auditor/) | Audits attribution windows, models and click vs view credit across Google Ads, Meta, LinkedIn, Microsoft Ads, TikTok and GA4, then recommends a model and source of truth. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/attribution-model-auditor) |
| [B2B Pipeline and Revenue Attribution](skills/pipeline-revenue-attribution/) | Credits CRM pipeline and closed revenue to every source and campaign from a CRM export plus ad spend, with cost per opportunity and won deal, first vs last touch… |  |
| [Bulk UTM Link Builder](skills/bulk-utm-links/) | Builds UTM links in bulk for launches, newsletters, creators, partners and QR codes, reusing GA4 spellings and showing each link's channel, plus matching campaign names… |  |
| [Call Tracking Analyst](skills/call-tracking-analyst/) | Analyses phone calls from CallRail or any call log CSV, grading real leads by source, campaign and keyword, pricing missed calls by hour, and checking Google Ads call… |  |
| [Consent Mode Auditor](skills/consent-mode-auditor/) | Audits Google Consent Mode v2 and the cookie banner from HAR files or Tag Assistant, checks what fires before consent, and estimates the GA4 sessions and Google Ads… |  |
| [Conversion Tracking Auditor](skills/conversion-tracking-auditor/) | Audits conversion tracking across Google Ads, GTM, GA4, Meta and LinkedIn, checking what counts, broken tags, double counting, lag and offline imports, plus tracking QA… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/conversion-tracking-auditor) |
| [GA4 Audience Retention](skills/ga4-audience-retention/) | Analyses GA4 users with new vs returning trends, weekly retention cohorts, user value by first channel, device, browser, country and city splits, the mobile gap and… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-audience-retention) |
| [GA4 BigQuery Query Writer](skills/ga4-bigquery-query-writer/) | Writes, explains, fixes and runs BigQuery SQL on the GA4 export for sessions, page paths, ordered funnels, multi-touch attribution, cohort LTV and Google Ads cost per… |  |
| [GA4 Channel Performance](skills/ga4-channel-performance/) | Reports GA4 channel and source/medium performance with spend from Google Ads, Meta, LinkedIn, Microsoft Ads and TikTok for cost and ROAS, and checks referral quality… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-channel-performance) |
| [GA4 Ecommerce Funnel](skills/ga4-ecommerce-funnel/) | Analyses a store's GA4 ecommerce, with the purchase funnel, checkout drop-off by device, cart abandonment, product and channel revenue and the AOV trend, after checking… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-ecommerce-funnel) |
| [GA4 Landing Page Analyst](skills/ga4-landing-page-analyst/) | Analyses GA4 landing pages for engagement, key events and leaks, paid vs organic fit with Google Ads cost and Search Console clicks, scroll depth, 404 pages and site… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-landing-page-analyst) |
| [GA4 Property Audit](skills/ga4-property-audit/) | Audits a GA4 property's setup and data quality, from streams, key events, retention and links to Unassigned traffic, bots and coverage against Search Console, or walks… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-property-audit) |
| [GA4 Weekly Report](skills/ga4-weekly-report/) | Builds a GA4 weekly or monthly report with week over week and year over year change, real vs noise verdicts, channel and page drivers, daily anomalies and key events. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-weekly-report) |
| [Gtm Container Auditor](skills/gtm-container-auditor/) | Audits a Google Tag Manager container for dead tags, trigger logic, consent settings, naming, versions and workspace conflicts, and builds missing GA4 event tracking… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/gtm-container-auditor) |
| [How Did You Hear About Us Survey Analyst](skills/self-reported-attribution/) | Writes or fixes a how did you hear about us question, codes every answer into channels with margins of error, and matches answers to GA4 orders to show what tracking… |  |
| [Incrementality Test Designer](skills/incrementality-test-designer/) | Designs incrementality tests before launch, geo holdout, audience holdout or platform lift, from Google Ads, GA4 and Meta data, sized from your own volume, with a dated… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/incrementality-test-designer) |
| [Junk Lead and Form Spam Investigator](skills/junk-lead-investigator/) | Finds where spam, bot and poor-fit leads come from, grading each lead in a CRM or form export and tracing junk to campaign, placement, page and form, then ranks form… |  |
| [LTV CAC Ratio Optimizer](skills/ltv-cac-ratio-optimizer/) | Calculates LTV, CAC, the LTV to CAC ratio and payback period from your customer and spend data, by channel, cohort and first product, then sets max CPA and ROAS targets… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ltv-cac-ratio-optimizer) |
| [Marketing Data Warehouse and SQL Builder](skills/marketing-data-warehouse/) | Designs and checks a cross-channel marketing data warehouse, writes staging, union and MERGE SQL, finds missing days and duplicates and reconciles spend with ad… |  |
| [Marketing Forecast](skills/marketing-forecast/) | Forecasts leads, spend and revenue for the next two months or a 12-month plan year by channel, from Google Ads, Meta, LinkedIn, Microsoft Ads, GA4 or pasted history… |  |
| [Marketing Mix Model Builder](skills/marketing-mix-model-builder/) | Builds a marketing mix model from weekly channel spend and total sales or leads, with carryover, diminishing returns and lift test calibration, giving ROI ranges… |  |
| [Measurement Plan Builder](skills/measurement-plan-builder/) | Builds a measurement plan from what GA4, Search Console, Google Ads, Meta, LinkedIn and Tag Manager track today, with a North Star metric, a KPI tree with baselines and… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/measurement-plan-builder) |
| [Offline Conversion Setup](skills/offline-conversion-setup/) | Sets up offline conversion imports so Google Ads, Microsoft Ads, Meta, LinkedIn and ChatGPT Ads bid on CRM stages, valuing each stage and writing a GCLID hidden field… |  |
| [Server-Side Tracking Planner](skills/server-side-tracking-planner/) | Decides if a site needs server-side tracking by weighing orders GA4 and ad platforms miss against hosting cost, then plans the server GTM container, Conversions API… |  |
| [TV, Offline Media and Geo Lift Analyst](skills/offline-media-lift-analyst/) | Measures lift from TV, CTV, radio, billboards, events and sponsorships, and reads out finished geo holdout tests, with a 95% interval, a placebo check and cost per… |  |
| [Utm Auditor](skills/utm-auditor/) | Audits UTM tagging in GA4 and tracking templates, URL suffixes and URL tags in Google Ads, Meta and LinkedIn, finds case splits and untagged ads, and writes one naming… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/utm-auditor) |

### Meta Ads

Placement, creative and audience performance analysis for Meta Ads.

| Skill | What it does | |
|---|---|---|
| [Click-to-WhatsApp and Messenger Ads Planner](skills/meta-click-to-message-ads/) | Plans and reviews Meta click-to-message ads that open WhatsApp, Messenger or Instagram Direct, writing greetings and starters and grading each ad on cost per qualified… |  |
| [Facebook and Instagram Boost Post Picker](skills/meta-boost-post-picker/) | Picks which organic Facebook and Instagram posts and Reels are worth boosting, ranked on shares, saves and clicks against your usual post, then sets goal, audience… |  |
| [Facebook Lead Ads Optimizer](skills/meta-lead-ads-optimizer/) | Optimizes Facebook and Instagram lead ads and Meta instant forms, ranking forms, ad sets and ads on cost per qualified lead from your CRM stages, and rewrites weak forms. |  |
| [Meta Ad Copy Writer](skills/meta-ad-copy-writer/) | Writes Facebook and Instagram ad copy, primary text, headlines and carousel or collection cards, from the angles behind your winning Meta ads or competitors' Ad Library… | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-ad-copy-writer) |
| [Meta Ad Rejection and Account Restriction Fixer](skills/meta-ad-rejection-fixer/) | Fixes rejected Facebook and Instagram ads and disabled or restricted Meta ad accounts. |  |
| [Meta Ad Specs and Safe Zone Checker](skills/meta-ad-specs-checker/) | Checks Facebook and Instagram image and video ads against Meta ad specs for Feed, Stories and Reels, grading size, aspect ratio, video length, text cut-off and safe… |  |
| [Meta Ads Automated Rules Builder](skills/meta-automated-rules-builder/) | Builds Meta Ads automated rules (stop losing ads, raise budgets, frequency and CPM alarms, overspend guard) set from your target cost per result and replayed on 13… |  |
| [Meta Ads Bid Strategy and Cost Cap Advisor](skills/meta-bid-strategy-advisor/) | Chooses the Meta Ads bid strategy for each Facebook and Instagram campaign and sets cost cap, bid cap or ROAS goal amounts from your own daily cost per result. |  |
| [Meta Ads Performance Analyzer](skills/meta-ads-performance-analyzer/) | Analyzes Meta Ads performance across Facebook and Instagram campaigns, ad sets, ads and breakdowns, with a health score, campaign tiers, creative fatigue, cost spikes… | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-ads-performance-analyzer) |
| [Meta Advantage Plus Auditor](skills/meta-advantage-plus-auditor/) | Audits Meta Advantage+ sales campaigns, Advantage+ creative enhancements and catalog ad health, checking which campaigns truly run as Advantage+ and how they compare… | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-advantage-plus-auditor) |
| [Meta Business Portfolio Audit](skills/meta-business-portfolio-audit/) | Audits a Meta Business portfolio (Facebook Business Manager) for ad account ownership, Pages, Instagram, pixels, catalogs, user and partner access, and changes nobody… |  |
| [Meta Catalog Ads and Product Set Planner](skills/meta-catalog-product-set-planner/) | Plans Meta Advantage+ catalog ads (dynamic product ads) from margin and stock, keeps losing or low-stock products out of spend, and builds product sets for prospecting… |  |
| [Meta Opportunity Score and Recommendations Reviewer](skills/meta-recommendations-reviewer/) | Reviews Meta Ads Manager recommendations and the opportunity score, giving each card an apply, test first, skip or your call verdict from the account's own numbers, not… |  |
| [Meta Reach and Frequency Planner](skills/meta-reach-frequency-planner/) | Plans Facebook and Instagram reach and awareness flights, choosing the Reach, ThruPlay or ad recall goal, auction or reservation, and a frequency cap set where your own… |  |

### Microsoft Ads

Account audits and optimization for Microsoft Advertising (Bing) search, shopping and audience campaigns.

| Skill | What it does | |
|---|---|---|
| [Microsoft Ads Account Audit](skills/microsoft-ads-account-audit/) | Audits a Microsoft Ads (Bing Ads) account and grades eight areas, from UET tracking and wasted spend to Quality Score, extensions and impression share, with ranked fixes. | [Page](https://insightfulpipe.com/marketing-claude-skills/microsoft-ads/microsoft-ads-account-audit) |
| [Microsoft Ads Optimizer](skills/microsoft-ads-optimizer/) | Drafts Microsoft Ads (Bing Ads) search changes as exact payloads, such as negatives from search terms, keywords to pause, budgets and RSAs, run only on a yes. | [Page](https://insightfulpipe.com/marketing-claude-skills/microsoft-ads/microsoft-ads-optimizer) |

### Paid Media

Media plans, benchmarks, stop-loss rules and channels beyond the big ad platforms.

| Skill | What it does | |
|---|---|---|
| [Ad Delivery Troubleshooter](skills/ad-delivery-troubleshooter/) | Finds why LinkedIn, TikTok, Microsoft Ads, Pinterest, Snapchat, X, OpenAI or Reddit ads are not delivering, checking billing, status, review, budget, bid, audience and… |  |
| [Ad Placement and Brand Safety Auditor](skills/placement-brand-safety-auditor/) | Audits ads served outside the main feed on TikTok Ad Network (Pangle), Microsoft Audience Network, LinkedIn Audience Network and DSPs, flagging junk apps, accidental… |  |
| [Ad Rejection Fixer](skills/ad-policy-fixer/) | Fixes rejected, disapproved or stuck ads and restricted ad accounts on LinkedIn, TikTok, Microsoft Ads (Bing), Pinterest, Snapchat, X, ChatGPT ads and Reddit, rewriting… |  |
| [Ad Smoke Test Planner](skills/ad-demand-test-planner/) | Plans and reads a paid smoke test on Google Search, Meta, LinkedIn or Reddit that checks demand, a message or a price before you build, with pass and kill lines, budget… |  |
| [Ad Stop-Loss Rules Designer](skills/ad-stop-loss-rules/) | Sets stop-loss kill rules for new ads on TikTok, LinkedIn, Microsoft Ads, Snapchat, Pinterest and X from your target CPA, back-tests them on 90 days of history and… |  |
| [Billboard and Out-of-Home Advertising Planner](skills/ooh-dooh-planner/) | Plans billboard, transit and digital out-of-home (DOOH) buys from your own demand by city, pricing quotes by all-in CPM and GRPs, funding only measurable markets… |  |
| [Break-Even ROAS and Target CPA Calculator](skills/paid-media-math/) | Calculates break-even ROAS, ACOS, target CPA, payback CPA, MER and blended CAC from your margins and repeat orders, plus the budget a revenue goal needs, whether a ROAS… |  |
| [CTV and Streaming TV Ads Planner](skills/ctv-streaming-ads-planner/) | Plans connected TV and streaming TV ad buys across YouTube on TV screens, streaming services and programmatic CTV, pricing quotes after fees, splitting budget by… |  |
| [International PPC Expansion Planner](skills/international-paid-expansion-planner/) | Ranks which countries to open next in Google Ads and Meta from each market's existing demand, search volume, CPC and audience size, then plans each market test, budget… |  |
| [Multi-Platform Paid Media Audit](skills/multi-platform-paid-audit/) | Audits all your ad platforms (Google, Meta, Microsoft, LinkedIn, TikTok, Pinterest, Snapchat, X, OpenAI Ads) in one spend-weighted scorecard judged on your GA4 or store… |  |
| [Native Ads Manager (Taboola, Outbrain)](skills/native-ads-manager/) | Reviews and plans Taboola and Outbrain native ads from their exports, grading each publisher site to block, bid down or boost, checking tracking and GA4 accidental… |  |
| [Newsletter and Podcast Ads Planner](skills/newsletter-podcast-ads-planner/) | Plans and judges sponsor slots in newsletters and podcasts, checking media kits, pricing quotes on matched audience, setting a counter price and rebook rule, and… |  |
| [Paid Ads Benchmark Check](skills/paid-ads-benchmark-check/) | Checks whether CTR, CPC, CPM, conversion rate, cost per lead, CPA and ROAS are good on Google Ads, Meta, LinkedIn, TikTok and Microsoft Ads, against your own 6-month… |  |
| [Paid Media Plan Builder](skills/media-plan-builder/) | Builds a paid media plan for a launch, new budget or flight across Google, Meta, LinkedIn and TikTok, with target CPA, platform picks, monthly budget split, flighting… |  |
| [Programmatic Display and Video Planner](skills/programmatic-display-planner/) | Plans programmatic display and video buys through a DSP, sets viewability and supply rules, then grades running lines on GA4. |  |
| [Software Directory Ads Planner](skills/software-marketplace-ads-planner/) | Plans and reviews paid placements on software directories like Capterra, G2 and the Shopify App Store, setting max bids from target cost per signup and grading… |  |
| [Spotify and Streaming Audio Ads Planner](skills/streaming-audio-ads-planner/) | Plans Spotify and programmatic audio ad buys with effective CPMs, a 30-second spot, offer codes and control regions, then reads lift. |  |

### Playbooks

Full-funnel advertising playbooks for e-commerce brands.

| Skill | What it does | |
|---|---|---|
| [App Growth Audit](skills/app-growth-audit/) | Audits a mobile app on the App Store and Google Play against up to three rivals, grading ratings, review themes, release impact and keyword rank, then writes ASO… |  |
| [B2B Lead Generation Audit](skills/b2b-lead-gen-audit/) | Audits lead generation for B2B companies, real estate agents and law firms across GA4, Search Console, LinkedIn Ads, Google Ads and Meta, from tracking to cost per lead. |  |
| [Ecommerce Ads Playbook](skills/ecommerce-ads-playbook/) | Plans ecommerce ads across Google Shopping, Performance Max, Meta catalog and TikTok with budgets and margin-checked ROAS, and audits a Shopify, WooCommerce or Magento… | [Page](https://insightfulpipe.com/marketing-claude-skills/playbooks/ecommerce-ads-playbook) |
| [Vertical Growth Audit](skills/vertical-growth-audit/) | Audits growth for travel, events, education, marketplace, mobile game, nonprofit or creator businesses from search demand, page speed, ad libraries and GA4. |  |

### PR & Partnerships

Press releases, media pitches, press kits, coverage reports, events, sponsorships and crisis communications.

| Skill | What it does | |
|---|---|---|
| [Analyst Relations Planner](skills/analyst-relations-planner/) | Plans B2B analyst relations, scoring the analyst firms and evaluations that cover your category and timing a year of briefings, inquiry calls, a briefing deck and… |  |
| [Award Entry Writer](skills/award-entry-writer/) | Picks the marketing and business awards worth entering and writes the award submission to each award's criteria and word limits, with results checked in GA4, Klaviyo… |  |
| [Brand Impersonation Response](skills/brand-impersonation-response/) | Finds scam ads, lookalike domains, fake sites and fake profiles using your brand in the Meta, Google, TikTok, LinkedIn and Microsoft ad libraries, ranks them by risk… |  |
| [Conference Speaker Proposal Writer](skills/speaker-proposal-writer/) | Finds conferences with open calls for speakers, ranks them by buyers in the room, and writes the talk title, abstract and speaker bio to each event's limits. |  |
| [Crisis Communications Plan](skills/crisis-comms-plan/) | Writes a crisis communications plan before anything goes wrong, with a risk register, numeric response levels, sign-off chain, holding statements and a pause list of… |  |
| [Crisis Response Kit](skills/crisis-response-kit/) | Handles a PR crisis happening now. |  |
| [Event and Sponsorship ROI Calculator](skills/event-sponsorship-roi/) | Prices a sponsorship or exhibitor package from your CRM conversion rates with break-even, a walk-away fee and a buy, negotiate or pass verdict, then measures event ROI… |  |
| [Event and Trade Show Marketing Plan](skills/event-marketing-plan/) | Builds a dated marketing plan for one trade show stand, hosted customer day or target-account dinner, with targets from your past events, a budget verdict, outreach… |  |
| [Gift Guide and Product Seeding Planner](skills/gift-guide-seeding-planner/) | Plans gift guide PR and product seeding for an online store, picking products by margin and stock from Shopify or WooCommerce, timing pitches to each outlet's lead time… |  |
| [Media Interview Prep](skills/spokesperson-interview-prep/) | Prepares a spokesperson for one media interview, podcast, panel or TV or radio slot. |  |
| [Media List Builder](skills/media-list-builder/) | Builds a media list for one story from journalists, trade outlets, bloggers and YouTube shows that covered your topic or competitors in the last year, with recent… |  |
| [Media Monitoring and PR Report](skills/pr-coverage-report/) | Monitors press coverage of your brand and builds the monthly or campaign PR report with outlet tiers, sentiment, message pull-through, share of voice, GA4 referrals… |  |
| [Media Pitch Writer](skills/media-pitch-writer/) | Writes a personal media pitch per journalist, editor or producer for one story, each tied to a recent article, with subject lines, exclusive or embargo terms, two… |  |
| [Newsjacking and Reactive PR Finder](skills/newsjacking-angle-finder/) | Finds news stories and X trends a brand can comment on within hours, screens out tragedy, politics and legal cases, scores fit and timing, and drafts an expert comment… |  |
| [Podcast Guesting Planner](skills/podcast-guest-pitching/) | Gets a founder or expert booked as a guest on other podcasts, vetting active shows on YouTube, writing the one-sheet, a pitch per host with follow-ups and a booking… |  |
| [PR Strategy Plan Builder](skills/pr-strategy-plan/) | Builds a 6 or 12 month PR strategy from your own evidence, scoring story angles for newsworthiness, tiering outlets that cover your category and laying out a monthly… |  |
| [Press Kit Builder](skills/press-kit-builder/) | Builds a company press kit or newsroom page, or audits the press page you have. |  |
| [Press Release Writer](skills/press-release-writer/) | Writes a press release or media advisory for one piece of news, such as a launch, funding round, hire or data story, checking each number in GA4, Shopify or Google… |  |
| [Sponsorship Proposal Writer](skills/sponsorship-proposal-writer/) | Writes a sponsorship deck, priced package tiers and sponsor pitch emails for an event, nonprofit or club, using audience proof from GA4, Klaviyo, Mailchimp and social. |  |

### SEO

Keyword research, content decay, cannibalization, briefs, schema, internal links and AI search visibility on live Search Console and SEO data.

| Skill | What it does | |
|---|---|---|
| [AI Answer Source Placement Planner](skills/ai-answer-source-placement/) | Finds the third-party pages ChatGPT and Google AI Overviews cite for your category, like best-of lists, Reddit threads and YouTube videos, that name rivals but not you… |  |
| [Ai Search Visibility](skills/ai-search-visibility/) | Scores AI search visibility from GA4 AI referrals, Search Console questions, AI Overview and ChatGPT mentions and llms.txt, checks if assistants get brand facts right… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/ai-search-visibility) |
| [AI Shopping Visibility Audit (ChatGPT Shopping SEO)](skills/ai-shopping-visibility/) | Checks which of a store's products ChatGPT shopping cards and Google AI Overviews name for buying questions, then traces each miss to feed, Merchant Center, markup… |  |
| [Backlink Auditor and Outreach Planner](skills/backlink-auditor/) | Audits backlinks for spam, lost and broken links, decides on disavow, and turns domains linking to competitors but not you into an outreach plan. |  |
| [Bing Webmaster SEO Analyst](skills/bing-seo-analyst/) | Analyses Bing search performance from Bing Webmaster Tools, splits brand and non-brand queries, compares Bing with Google Search Console, finds pages Google ranks that… |  |
| [Brand SERP and Knowledge Panel Optimizer](skills/brand-serp-knowledge-panel/) | Audits what Google shows for a brand or founder name, labels every page-one result, checks sitelinks, the knowledge panel, People Also Ask and negative results, and… |  |
| [Competitor Keyword and Content Gap](skills/competitor-keyword-gap/) | Finds the keywords and topics competitors rank for on Google and you don't, checks each gap against your Search Console, compares domain rank and referring domains, and… |  |
| [Content Brief Writer](skills/content-brief-writer/) | Writes an SEO content brief for one keyword from the live Google top 10, People Also Ask, competitor headings and your Search Console, and says new page or refresh. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/content-brief-writer) |
| [Content Decay Refresh](skills/content-decay-refresh/) | Finds pages losing Google clicks in Search Console, works out why (lost rank, lower CTR, cannibalisation, redirect or demand), checks update timing and AI Overview… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/content-decay-refresh) |
| [Core Web Vitals Fixer](skills/core-web-vitals-fixer/) | Diagnoses Core Web Vitals by page template with PageSpeed Insights and Lighthouse on your top Search Console pages, and writes ranked LCP, INP and CLS fix plans plus… |  |
| [Digital PR Link Campaign Planner](skills/digital-pr-link-campaign/) | Plans a data-led digital PR campaign for news links, testing the story in your survey, Shopify or GA4 data, building a media list from outlets that ran similar stories… |  |
| [Ecommerce SEO Auditor](skills/ecommerce-seo-auditor/) | Audits ecommerce SEO for Shopify, WooCommerce or Magento, covering duplicate product URLs, faceted navigation and filter URLs, out-of-stock and discontinued products… |  |
| [GitHub README Optimizer](skills/repo-readme-optimizer/) | Writes or audits a GitHub README and repo card (About line, topics, social preview) for an open-source tool, SDK, plugin or MCP server so it ranks in Google and gets… |  |
| [Google Discover and News SEO Optimizer](skills/news-discover-seo/) | Reviews Google Discover and Google News traffic from Search Console for publishers, checks articles for large image previews, Article markup, bylines and the news… |  |
| [Google Penalty Recovery Planner](skills/penalty-recovery/) | Diagnoses a Google penalty or sudden traffic drop, telling manual actions, hacked sites, core or spam updates and non-Google causes apart, then plans the cleanup and… |  |
| [Image SEO and Alt Text Generator](skills/image-seo-alt-text/) | Writes alt text by looking at each image and audits image SEO, flagging missing or stuffed alt, camera file names, heavy files and lazy-loaded hero images, ranked by… |  |
| [Indexing and Sitemap Monitor](skills/indexing-monitor/) | Checks which pages Google and Bing have indexed using Search Console URL inspection, sitemaps and Bing Webmaster data, groups not-indexed pages by reason, tracks new… |  |
| [Internal Linking Planner](skills/internal-linking-planner/) | Plans internal links from Google Search Console data, matching pages ranking 4 to 20 with on-topic donor pages, anchors from real queries, anchor text fixes and click… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/internal-linking-planner) |
| [International SEO and Hreflang Planner](skills/international-seo-planner/) | Plans international SEO and checks hreflang across country and language versions, sizes new markets with local keyword volume, picks subfolders vs ccTLDs and writes… |  |
| [JavaScript SEO Rendering Check](skills/javascript-seo-rendering-check/) | Checks what Google and AI crawlers can read on a JavaScript site by comparing raw and rendered HTML per template, then names the rendering fix for Next.js, Nuxt, React… |  |
| [Keyword Cannibalization Fixer](skills/keyword-cannibalization-fixer/) | Finds keyword cannibalization in Google Search Console, where two of your pages split one query, picks the owner page and writes a merge, differentiate or relink fix… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/keyword-cannibalization-fixer) |
| [Keyword Research Clustering](skills/keyword-research-clustering/) | Researches keywords for a topic with volume, difficulty, CPC and intent, clusters them by SERP overlap and Search Console data, and ranks a page plan. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/keyword-research-clustering) |
| [On-Page SEO Optimizer](skills/on-page-seo-optimizer/) | Optimizes one page or draft for one keyword against the Google top 10 and its Search Console queries, writing each edit as before and after text. |  |
| [Rank and SERP Feature Tracker](skills/rank-tracker/) | Tracks Google rankings for up to 5 keywords a run with a live SERP snapshot set against Search Console averages, shows which SERP features you hold and could win, and… |  |
| [Schema Markup Generator](skills/schema-markup-generator/) | Audits structured data against the rich results Google Search Console reports and writes missing or broken JSON-LD for Organization, Breadcrumb, Article, Product… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/schema-markup-generator) |
| [SEO Blog Writer](skills/seo-blog-writer/) | Writes SEO blog posts, roundups, X vs Y comparisons and alternatives pages from Search Console gaps and the live Google top 10, or reworks an existing page so AI… |  |
| [SEO Content Planner](skills/seo-content-planner/) | Plans a 12-week SEO content calendar from Search Console, GA4 and competitor gaps, with pillars, glossary pages, a content audit and ideas from sales calls or tickets. |  |
| [SEO Forecast and ROI Calculator](skills/seo-forecast/) | Forecasts SEO traffic, leads, revenue and the break-even month for a target keyword plan, using the site's own Search Console click curve and GA4 conversion rate, in… |  |
| [SEO Performance Report](skills/seo-performance-report/) | Reports Google Search Console results month over month and year over year, splitting clicks by brand vs non-brand, device, country, folder, page and query, plus… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/seo-performance-report) |
| [SEO Roadmap Planner](skills/seo-roadmap-planner/) | Builds a 3, 6 and 12-month SEO roadmap from Search Console, GA4 and Bing, diagnoses whether the site is new, growing, plateaued or declining, and fits the work into the… |  |
| [SEO Split Test Designer](skills/seo-split-test/) | Designs and reads SEO split tests on similar pages from Search Console, with matched test and control groups, a run length from the site's own noise and a controlled… |  |
| [Server Log and Crawl Budget Analyzer](skills/log-file-crawl-analyzer/) | Analyzes server and CDN access logs for crawl budget, verifying Googlebot, Bingbot and AI crawlers like GPTBot and ClaudeBot against published IP lists, then ranks… |  |
| [Site Migration SEO Monitor](skills/site-migration-monitor/) | Protects organic traffic in a site migration, redesign or replatform with a Search Console baseline, a launch check, a 301 redirect map and day 1 to 90 checks of… |  |
| [Site Structure Planner](skills/site-structure-planner/) | Plans a website's SEO architecture from keyword demand, with sections, hubs, URL and slug rules, menus, breadcrumbs, click depth and orphans, keeping ranking URLs in… |  |
| [Striking Distance Optimizer](skills/striking-distance-optimizer/) | Finds Google Search Console keywords at positions 8 to 20 and low-CTR pages, then rewrites the titles and meta descriptions losing clicks, with a sitewide title tag… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/striking-distance-optimizer) |
| [XML Sitemap, Robots.txt and llms.txt Generator](skills/robots-llms-txt-builder/) | Writes and tests robots.txt, XML sitemaps and llms.txt, checking every URL for Googlebot, Bingbot and AI crawlers so no page with clicks gets blocked, and sets AI bot… |  |

### Skill Orchestration

A routing skill that picks and sequences the other marketing skills.

| Skill | What it does | |
|---|---|---|
| [Orchestrator](skills/orchestrator/) | Diagnoses the real marketing bottleneck from connected GA4, Search Console, Google Ads, Meta and LinkedIn Ads data, then returns an ordered plan of skills to run. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta/orchestrator) |

### Social Media

Organic social: page and channel analysis, posting plans, repurposing and influencer campaigns on live account data.

| Skill | What it does | |
|---|---|---|
| [Community Strategy Builder](skills/community-strategy-builder/) | Plans and scores a brand community on Slack, Discord, Circle, Telegram or a forum, with channels, welcome path, rules, reply rota, 90-day events and a monthly health… |  |
| [Content Repurposer](skills/content-repurposer/) | Repurposes one blog post into an X thread, hooks, tweets, hot takes, LinkedIn, Facebook and Threads posts, email and ad copy, or turns a podcast, webinar or video… |  |
| [Creator Program Builder](skills/creator-program-builder/) | Builds an always-on creator or ambassador program from creators already paid, scoring each on YouTube views, GA4 sign-ups and Meta or TikTok ad results to renew, raise… |  |
| [Customer UGC Strategy Planner](skills/customer-ugc-program/) | Plans an earned, unpaid customer UGC program for Instagram and Facebook, timing the photo ask from Shopify and Klaviyo, writing permission requests and a consent log… |  |
| [Employee Advocacy Program Planner](skills/employee-advocacy-program/) | Plans and runs an employee advocacy program on LinkedIn and X, with topics from the company page's best posts, a volunteer cohort, guidelines, weekly prompt kits, a… |  |
| [Engagement Rate Calculator](skills/engagement-rate-calculator/) | Calculates engagement rate for Instagram, TikTok, Facebook, LinkedIn, X, YouTube or Pinterest by reach, views, impressions, followers and per day, side by side, against… |  |
| [Facebook Page Analyst](skills/facebook-page-analyst/) | Analyses an organic Facebook Page from its connected insights, posts and comments, with a monthly report, reach trend, top posts, post types, best time to post… |  |
| [Influencer Campaign Manager](skills/influencer-campaign-manager/) | Plans and measures influencer campaigns, finding and scoring YouTube creators who rank for your topics, writing briefs, outreach, disclosed captions and UTMs, plus… |  |
| [Influencer Rate Calculator and Contract Terms](skills/influencer-rates-and-contract/) | Prices an influencer or creator deal from the creator's real recent views, with an opening offer, target and walk-away, prices usage rights, whitelisting and… |  |
| [Influencer Vetting and Fake Follower Checker](skills/influencer-vetting/) | Vets Instagram, TikTok and YouTube creators as a fake follower checker, testing engagement by tier, reach, comment quality, follower jumps, audience fit, brand safety… |  |
| [Instagram DM Automation Designer](skills/dm-automation-flow-designer/) | Designs comment-to-DM automation flows for Instagram, Facebook Messenger and X, picking the trigger post and keyword from real comments and keeping DMs inside Meta's… |  |
| [Instagram Growth Analyst](skills/instagram-growth-analyst/) | Builds a monthly Instagram report from account insights or a Meta Business Suite export, scoring Reels, carousels, images and Stories per 1,000 reached against its own… |  |
| [LinkedIn Newsletter Planner](skills/linkedin-newsletter/) | Plans and writes a LinkedIn newsletter for a company Page or founder profile, picking themes from top posts and search questions, with a name, cadence, 12-edition plan… |  |
| [LinkedIn Page Analyst](skills/linkedin-page-analyst/) | Analyses a LinkedIn company page from connected data or exports, covering follower growth, whether followers fit the target buyer, page views, top posts, formats and… |  |
| [Live Stream Marketing Planner](skills/social-live-stream-planner/) | Plans a brand live stream on YouTube Live, TikTok LIVE, Instagram Live, Facebook Live, LinkedIn Live or X Spaces. |  |
| [Long Video to Shorts Clip Finder](skills/video-to-shorts-clip-finder/) | Finds 5 to 10 short clips in a long video, podcast, webinar or livestream transcript and writes hooks, captions and vertical crop notes for YouTube Shorts, Reels… |  |
| [Pinterest Organic Manager](skills/pinterest-organic-manager/) | Audits an organic Pinterest account, ranks pins and boards by saves and outbound clicks, finds Pinterest Trends keywords, plans seasonal pins and writes pin copy. |  |
| [Reddit and Forum Marketing Planner](skills/reddit-marketing-planner/) | Plans Reddit marketing plus Quora, Hacker News and forums. |  |
| [Social Listening and Share of Voice Report](skills/social-listening-monitor/) | Runs a weekly social listening report on X, YouTube, Reddit and your own Facebook and Instagram comments, with brand mentions, share of voice, sentiment, spikes and… |  |
| [Social Media Audit](skills/social-media-audit/) | Audits every social profile a brand runs on Facebook, Instagram, LinkedIn, TikTok, X, Pinterest and YouTube plus GA4 social traffic. |  |
| [Social Media Competitor Benchmark](skills/social-competitor-benchmark/) | Benchmarks your social accounts against up to five rivals on Instagram, Facebook, LinkedIn, YouTube, X, TikTok and Pinterest, comparing followers, posting rhythm… |  |
| [Social Media Giveaway Planner](skills/social-giveaway-planner/) | Plans, draws and measures a social media giveaway or contest on Instagram, Facebook, TikTok or X. |  |
| [Social Media Policy Writer](skills/social-media-policy/) | Writes a social media policy pack with employee guidelines, community guidelines, moderation rules, post approvals, reply times and disclosure rules, plus regulated… |  |
| [Social Media ROI Analyst](skills/social-media-roi/) | Calculates organic social media ROI in money per network from GA4, store orders, discount codes and team costs, giving a floor to ceiling range, a decision per network… |  |
| [Social Media Trend Finder](skills/social-trend-scout/) | Finds this week's social media trends in a brand's niche from X, Pinterest Trends, YouTube, Google Trends and pasted TikTok lists, skips peaked trends and writes post… |  |
| [Social Reach Drop Diagnostic](skills/social-reach-drop-diagnostic/) | Diagnoses a sudden drop in reach, views or followers on Instagram, TikTok, Facebook, LinkedIn, X or YouTube against the account's own baseline, tests eight causes and… |  |
| [TikTok and Instagram SEO Optimizer](skills/social-search-optimizer/) | Optimizes TikTok and Instagram videos and profiles for in-app search. |  |
| [TikTok Organic Analyst](skills/tiktok-organic-analyst/) | Analyses an organic TikTok account against its own median video, finds the hooks, topics, lengths and hashtags that win, then writes a monthly report, strategy, video… |  |
| [Video Content Program Planner](skills/video-marketing-strategy/) | Plans an organic video program across YouTube, Shorts, Instagram Reels, TikTok, Facebook and LinkedIn from past results, with network roles, series, a cadence sized to… |  |
| [X (Twitter) Organic Analyst](skills/x-organic-analyst/) | Analyses an X (Twitter) account's organic posts from live data, the analytics CSV or pasted posts, compares formats, topics and hours with its own median, and drafts… |  |
| [YouTube Channel Analyst](skills/youtube-channel-analyst/) | Reviews a YouTube channel month over month from YouTube Analytics, covering views, watch time, retention drop-offs, Shorts versus long-form, subscribers and RPM, and… |  |
| [YouTube SEO Optimizer](skills/youtube-seo-optimizer/) | Audits and rewrites YouTube titles, descriptions, chapters and tags from search demand and top-ranking videos, applying the update after you confirm. |  |
| [YouTube Video Idea Finder](skills/youtube-topic-finder/) | Finds YouTube video ideas from rival channels' outlier videos, viewer comment questions and search demand, scores each one and plans a 13-week slate of long videos and… |  |
| [YouTube Video Script Writer](skills/youtube-script-writer/) | Writes timed YouTube video scripts with hooks, re-hooks, chapters, sponsor read placement and Shorts cut-downs, built around where your viewers left past videos, and… |  |

### Social Media Ads

Paid social creative ranking and UGC creator briefs.

| Skill | What it does | |
|---|---|---|
| [Meta Ads Creative Ranker](skills/meta-ads-creative-ranker/) | Ranks Meta Ads creatives (Facebook, Instagram) by cost per result or ROAS into tiers, a leaderboard and a kill list, and checks Andromeda variety and partnership ads. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/meta-ads-creative-ranker) |
| [Pinterest Ads Manager](skills/pinterest-ads-manager/) | Audits and manages Pinterest Ads, scoring tag health, pacing, cost per outbound click, pin formats, keyword vs interest targeting and audiences, plans launches from… | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/pinterest-ads-manager) |
| [Reddit Ads Manager](skills/reddit-ads-manager/) | Reviews Reddit Ads from Ads Manager exports, ranking subreddits by cost per result, checking targeting, bids, the Reddit Pixel and Conversions API, reading ad comments… |  |
| [Snapchat Ads Manager](skills/snapchat-ads-manager/) | Audits and manages Snapchat Ads, scoring delivery, the Snap Pixel, swipe-up rate, video completion, placements, audiences and Dynamic Product Ads, writes client reports… | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/snapchat-ads-manager) |
| [UGC Brief Generator](skills/ugc-brief-generator/) | Writes UGC creator briefs and timed video ad scripts from the top hooks and converters in Meta Ads (and TikTok), with Meta Ad Library references. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/ugc-brief-generator) |
| [X Ads Manager](skills/x-ads-manager/) | Audits and manages X Ads (Twitter Ads), grading promoted post engagement, keyword, lookalike and conversation targeting, video completion, X Pixel conversions and cost… | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/x-ads-manager) |

### Strategy

Launches, pricing, referral programs, free tools and privacy-first targeting.

| Skill | What it does | |
|---|---|---|
| [Brand Architecture Planner](skills/brand-architecture/) | Plans brand architecture from name search demand, GA4 and Google Ads data. |  |
| [Brand Health and Share of Search Tracker](skills/brand-health-tracker/) | Tracks brand health monthly, led by share of search against named competitors, plus branded search, direct users, reviews and followers from Search Console, GA4, Google… |  |
| [Brand Positioning Builder](skills/brand-positioning-builder/) | Builds brand positioning from your site, up to four competitor home pages and the words buyers search in Search Console. |  |
| [Customer Journey Map](skills/customer-journey-map/) | Maps the customer journey from GA4, Search Console, Klaviyo or Mailchimp, call logs and Google reviews, tags every cell measured or assumed, and ranks the five… |  |
| [Customer Survey Builder and Analyzer](skills/survey-design-analysis/) | Designs customer surveys around one decision with a bias check and sample size, then analyses answers with margins of error, NPS ranges, significance tests, MaxDiff and… |  |
| [First 100 Customers Plan](skills/first-customers-plan/) | Plans how a product with no sales yet wins its first 10 to 100 paying customers, scoring segments on search demand, communities and rival ads, then building a 30-day… |  |
| [Five Forces, PESTLE and Ansoff Analysis](skills/strategy-frameworks/) | Runs Porter's Five Forces, PESTLE and an Ansoff matrix on one real market, scoring each force from search and ad evidence and ending with marketing plan changes. |  |
| [Free Tool Strategy](skills/free-tool-strategy/) | Plans a lead magnet or marketing tool such as a calculator, generator, checker, quiz or template from search demand and who ranks, and audits existing magnets by the… | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/free-tool-strategy) |
| [Holiday Campaign Planner](skills/holiday-campaign-planner/) | Plans Black Friday, Cyber Monday and holiday campaigns from last season's GA4, Search Console, Klaviyo and Google Ads history, plus a year-round retail promotion… |  |
| [Integrated Campaign Planner](skills/integrated-campaign-planner/) | Plans one campaign across ads, email, social, press and creators, sizing each channel budget from your Google Ads, Meta, LinkedIn, TikTok, Klaviyo and GA4 numbers. |  |
| [Launch Strategy](skills/launch-strategy/) | Plans a product, feature, book or webinar launch from your GA4 baseline and past traffic spikes, with a readiness check and dated phases. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/launch-strategy) |
| [Market and Trend Research](skills/market-research/) | Researches a market, industry or product category from public search data, covering demand, trends, rising keywords, who owns results, channels and countries, plus a… |  |
| [Market Entry Strategy Planner](skills/market-entry-plan/) | Plans entry into one chosen country, using demand by country from Search Console, GA4 and ads, local search costs and rival ads to set the route, local prices and a… |  |
| [Market Sizing (TAM, SAM, SOM)](skills/market-sizing/) | Calculates TAM, SAM and SOM three ways (bottom-up, top-down, search demand by country) with every input labelled, then sizes the three-year share you can win from GA4… |  |
| [Marketing Audit and Scorecard](skills/marketing-audit/) | Audits marketing across ten areas from GA4, Search Console, ad platforms, Klaviyo, social and reviews, scores it out of 100 and ranks the top ten fixes. |  |
| [Marketing Ideas Generator](skills/marketing-ideas-generator/) | Generates marketing ideas for one business, cuts what its budget, hours and model can't carry, and ranks the rest by ICE score with a test plan. |  |
| [Marketing Plan Builder](skills/marketing-plan-builder/) | Builds a marketing plan from GA4, Search Console, Google Ads, Meta and Klaviyo numbers, checks tracking first and fits ICE-scored work to your hours. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/marketing-plan-builder) |
| [Pricing Research and Price Elasticity Analyzer](skills/pricing-research-survey/) | Writes and analyses Van Westendorp and Gabor-Granger price surveys, and measures price elasticity from Shopify or WooCommerce orders. |  |
| [Pricing Strategy](skills/pricing-strategy/) | Recommends what to charge from rival pricing pages and price searches, setting value metric, tiers, price points and annual discount. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/pricing-strategy) |
| [Privacy First Targeting Strategist](skills/privacy-first-targeting-strategist/) | Scores how exposed Google Ads, Meta, LinkedIn and TikTok are to tracking loss and writes a first-party data roadmap. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/privacy-first-targeting-strategist) |
| [Product Idea Validation Plan](skills/idea-validation-plan/) | Tests demand for a new product, offer or feature before it is built, using search volume, CPC and rival ads, then sizes a fake door, smoke test or pre-sale with pass… |  |
| [Product-Market Fit Assessment](skills/product-market-fit-assessment/) | Measures product-market fit with the Sean Ellis survey against the 40% bar and its margin of error, finds the segment that has fit, then checks retention cohorts and… |  |
| [Rebrand Planner: Rebranding Strategy and Checklist](skills/rebrand-planner/) | Plans a rebrand or rename, from testing whether to rename at all to a checklist of every profile and listing scheduled back from launch day, then tracks how brand… |  |
| [Referral Program](skills/referral-program/) | Designs referral, affiliate and partner programs from your GA4 and email data, with rewards, commission, tracking and fraud rules. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/referral-program) |
| [Win-Loss Analysis](skills/win-loss-analysis/) | Runs a win-loss analysis on a CRM deal export and call notes, with win rates by competitor, segment, deal size and lead source, ranked loss reasons and a fix per team. |  |

### TikTok Ads

Creative, hook and audience analysis for TikTok Ads.

| Skill | What it does | |
|---|---|---|
| [TikTok Ads Analyzer](skills/tiktok-ads-analyzer/) | Analyzes TikTok Ads results, grading hook rate, 6-second hold, CTR, cost per result and ROAS by creative, audience, placement and Pangle, and explains cost spikes. | [Page](https://insightfulpipe.com/marketing-claude-skills/tiktok-ads/tiktok-ads-analyzer) |
| [TikTok Ads Campaign Builder](skills/tiktok-ads-campaign-builder/) | Builds TikTok Ads campaigns from a brief, with targeting, captions, CTAs, video hooks and exact payloads created switched off once you confirm, and flags fatigued ads… | [Page](https://insightfulpipe.com/marketing-claude-skills/tiktok-ads/tiktok-ads-campaign-builder) |
| [TikTok Competitor Ads Research](skills/tiktok-competitor-ads-research/) | Researches competitor TikTok ads in the TikTok Ad Library and Creative Center Top Ads, with run length, hooks, angles, formats, landing pages and targeting beside your… |  |
| [TikTok Spark Ads Planner](skills/tiktok-spark-ads-planner/) | Plans TikTok Spark Ads by ranking your own and creator posts on shares, comments, likes and watched-full rate against your usual, logging creator Spark codes and… |  |

<!-- SKILLS:END -->

Every reviewed skill is added here as soon as it passes review, and its page on insightfulpipe.com follows. This repository syncs with the site twice a day.

## License

[MIT](LICENSE). Running the skills on live data needs an InsightfulPipe account.
