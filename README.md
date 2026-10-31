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

Claude Code keeps its list of skill descriptions within a size limit, so with every skill installed Claude sees the names of all of them but the full description of only some. A skill may then not start by itself from a plain request: call it by name (for example `/google-ads-account-audit`), or install just the skills you need, below.

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
| [Agency Pricing Calculator](skills/agency-pricing-calculator/) | Works out what an agency or freelancer should charge for marketing services (PPC, paid social, social media management, SEO, content, email). |  |
| [Client Onboarding Kit](skills/client-onboarding-kit/) | Builds a marketing agency's client onboarding kit for week one of a new account. |  |
| [Client Update and Hard Conversation Writer](skills/client-conversation-writer/) | Writes the client messages agencies and freelance marketers dread, built on the account's own numbers. |  |
| [Marketing Agency Performance Review](skills/agency-performance-review/) | Helps a business judge its marketing agency or freelancer, or pick a new one. |  |
| [Marketing Proposal Writer](skills/marketing-proposal-writer/) | Writes a client-ready marketing proposal from discovery notes, a call transcript, a prospect audit or an RFP. |  |
| [Prospect Marketing Audit](skills/prospect-marketing-audit/) | Audits a prospect's digital marketing from public data alone, before any account access, so an agency can open a pitch with proof. |  |

### App Marketing

App store optimization, store listing tests, install campaigns, attribution and ratings.

| Skill | What it does | |
|---|---|---|
| [App Install (User Acquisition) Campaign Planner](skills/app-install-ua-planner/) | Plans paid user acquisition for a live mobile app across Apple Ads, Google App campaigns, Meta, TikTok, Snapchat and AppLovin. |  |
| [App Install Attribution Auditor](skills/app-attribution-auditor/) | Audits mobile app install attribution before anyone moves app budget. |  |
| [App Marketing Plan](skills/app-marketing-plan/) | Writes a marketing plan for a mobile app from pre-launch to scale. |  |
| [App Rating Prompt Planner](skills/app-rating-prompt-planner/) | Plans when an iOS or Android app should show the store's own rating prompt (the App Store review request and the Google Play in-app review card), from the app's real… |  |
| [App Store Conversion Analyst](skills/app-store-conversion-analyst/) | Reads App Store Connect App Analytics and Google Play Console store listing reports (impressions, page views or visitors, downloads, by source, country and device) and… |  |
| [App Store Listing Localizer](skills/app-store-localization/) | App Store and Google Play listing localization (ASO localization). |  |
| [App Store Screenshot and Preview Video Brief](skills/app-screenshot-video-brief/) | Plans the App Store and Google Play screenshot set, captions, frame order, app preview video, icon notes and Google Play feature graphic for one app, and writes a… |  |
| [Apple Search Ads Manager](skills/apple-ads-manager/) | Audits and builds Apple Ads (formerly Apple Search Ads) search results campaigns for an iOS app. |  |
| [AppLovin Ads Analyzer](skills/applovin-ads-analyzer/) | Analyzes AppLovin Ads (Axon Ads Manager) campaigns for app installs and for web and e-commerce sales, on live data through the InsightfulPipe MCP or from an AppLovin… |  |
| [In-App Events and Featuring Planner](skills/in-app-events-featuring-planner/) | Plans App Store in-app events, Google Play promotional content and seasonal listing refreshes for the months ahead, and drafts the App Store featuring nominations worth… |  |
| [Store Listing Experiments and Custom Product Pages](skills/store-listing-experiments/) | Plans, sizes and reads App Store product page optimization tests and Google Play store listing experiments (icon, screenshots, preview video, feature graphic… |  |
| [Web-to-App Funnel Planner](skills/web-to-app-funnel/) | Plans a web-to-app (web2app) funnel that sells a mobile app subscription on the web before the install, then hands the buyer into the app. |  |

### Audience

Audience overlap and cannibalization analysis across campaigns.

| Skill | What it does | |
|---|---|---|
| [Audience Overlap Analyzer](skills/audience-overlap-analyzer/) | Finds where your own Meta and Google Ads targeting reaches the same people, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/audience/audience-overlap-analyzer) |

### B2B Sales

Outbound, prospecting, ABM, lead scoring, handoff and sales enablement.

| Skill | What it does | |
|---|---|---|
| [Abm Program Planner](skills/abm-program-planner/) | Plans an account-based marketing (ABM) program across channels from the user's own evidence. | [Page](https://insightfulpipe.com/marketing-claude-skills/sales/abm-program-planner) |
| [B2B Cold Email Writer](skills/cold-email-writer/) | Writes B2B cold email for one offer and one segment, from a pasted brief and lead list or a CSV. |  |
| [B2B Demand Generation Planner](skills/b2b-demand-gen-planner/) | Plans a B2B demand generation and lead generation program backwards from a revenue target, on the business's own numbers. |  |
| [B2B Prospect List Builder](skills/prospect-list-builder/) | Builds a B2B prospect list of real target companies from public sources (business listings, Meta, LinkedIn and Google ad libraries, Google search results, App Store and… |  |
| [Closed Lost Deal Re-engagement Planner](skills/lost-deal-reengagement/) | Turns a closed lost deals export into a ranked list of deals worth another try, with a date for each retry and a play for each group. |  |
| [Cold Email Campaign Analyzer](skills/outbound-campaign-analyzer/) | Analyzes cold email and outbound sequence results from any sending tool's export or pasted step numbers. |  |
| [Cold Email Deliverability Setup Planner](skills/cold-email-infrastructure-planner/) | Plans the cold email sending setup before the first email goes out, from the user's own weekly target. |  |
| [Customer Advocacy Program Planner](skills/customer-advocacy-program/) | Plans a B2B customer advocacy and reference program from the user's customer export. |  |
| [Lead Scoring Model from Deal History](skills/lead-scoring-model-builder/) | Builds a lead scoring model from your own won and lost leads. |  |
| [LinkedIn Prospecting Message Writer](skills/linkedin-outreach-writer/) | Writes LinkedIn prospecting messages for a prospect list, from pasted posts and news or a CSV. |  |
| [MQL to SQL Handoff Designer](skills/lead-handoff-designer/) | Designs the marketing to sales lead handoff from the team's own CRM lead export. |  |
| [Objection Handling Guide](skills/objection-handling-guide/) | Builds a sales objection handling guide from the team's own evidence instead of a stock list. | [Page](https://insightfulpipe.com/marketing-claude-skills/sales/objection-handling-guide) |
| [ROI Business Case Builder](skills/roi-business-case-builder/) | Builds the ROI business case for one buyer in one deal. |  |
| [Sales Call Script Writer](skills/sales-call-script-writer/) | Writes reusable sales call guides from the team's own evidence, a cold calling script with openers, a voicemail and a gatekeeper line, a discovery call guide whose… |  |
| [Sales Deck Writer](skills/sales-deck-builder/) | Writes a B2B sales deck slide by slide, with a headline, body, source line and speaker notes on every slide. |  |
| [Sales Follow-Up Email Writer](skills/sales-follow-up-writer/) | Writes the one-to-one sales follow-up emails that keep an open deal moving, from the rep's own call notes or transcript. |  |
| [Sales One-Pager Writer](skills/sales-one-pager-writer/) | Writes one-page sales sheets, namely a product or solution one pager per persona or industry with three to five benefit blocks, a why-us-versus-the-alternative sheet… |  |
| [Sales Playbook Builder](skills/sales-playbook-builder/) | Builds the sales playbook a new sales hire, an SDR or a founder handing off sales can run from, using the team's own CRM opportunity export, outbound sequence report… |  |
| [Sales Proposal and RFP Response Writer](skills/sales-proposal-writer/) | Writes B2B sales proposals and RFP responses where every claim traces to a source. |  |

### ChatGPT Ads

Performance analysis and campaign building for ads in ChatGPT through the OpenAI Ads API.

| Skill | What it does | |
|---|---|---|
| [Chatgpt Ads Analyzer](skills/chatgpt-ads-analyzer/) | Analyzes a ChatGPT Ads (OpenAI Ads) account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/chatgpt-ads/chatgpt-ads-analyzer) |
| [Chatgpt Ads Campaign Builder](skills/chatgpt-ads-campaign-builder/) | Builds a ChatGPT Ads (OpenAI Ads) campaign from a brief on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/chatgpt-ads/chatgpt-ads-campaign-builder) |

### Content Marketing

Content distribution, editorial workflow, podcasts, ebooks, original research and pre-publish QA.

| Skill | What it does | |
|---|---|---|
| [Blog Charts and Visuals Planner](skills/blog-visuals-planner/) | Plans every visual a blog post or report needs (featured image, charts, diagrams, screenshots, tables, an infographic) and writes the spec for each one, with chart data… |  |
| [Blog Lead Conversion Planner](skills/blog-lead-conversion-planner/) | Plans how to turn blog readers into leads. |  |
| [Content Distribution Planner](skills/content-distribution-planner/) | Plans how one finished piece (blog post, guide, report, case study, episode) reaches its readers in its first 30 days. |  |
| [Content Strategy Builder](skills/content-marketing-strategy/) | Builds a content marketing strategy a team can run for a year, plus a dated 90-day editorial calendar across every format (articles, guides, templates, comparisons… |  |
| [Editorial QA and Fact Check](skills/content-pre-publish-qa/) | Editorial QA and fact check for a finished article, guide or report before it goes live. |  |
| [Editorial Workflow Builder](skills/editorial-workflow-builder/) | Designs a content team's editorial workflow from idea to published, with stages, one owner per stage, approvers only where there is real risk, turnaround targets, a… |  |
| [Original Research and Industry Report Builder](skills/original-research-report/) | Plans and writes an original research report, industry report or benchmark report from a company's own data. |  |
| [Podcast Episode Prep and Show Notes](skills/podcast-episode-kit/) | Preps and packages one podcast episode. |  |
| [Podcast Marketing Strategy Planner](skills/podcast-strategy-planner/) | Builds a podcast marketing strategy and a dated 12-episode plan for a brand podcast, or reviews a running one. |  |
| [Whitepaper and Ebook Writer](skills/ebook-whitepaper-writer/) | Writes a whitepaper or an ebook, guide or playbook in full, from a brief, notes and drafts, or by compiling and updating the brand's strongest articles. |  |

### Copywriting

Advertorials, transcreation, UX microcopy, print and audio ads, and marketing claims checks.

| Skill | What it does | |
|---|---|---|
| [Advertorial and Presell Page Writer](skills/advertorial-presell-writer/) | Writes an advertorial or presell page, the editorial-style page between an ad and a product page, as a story, a numbered listicle or a short reasons-why presell, with… |  |
| [Brand and Product Naming](skills/brand-product-naming/) | Runs a naming project for a company, product, feature or plan. |  |
| [Content Localization and Transcreation](skills/copy-transcreation/) | Localizes and transcreates marketing copy and content for another market and language, rewriting, not translating. |  |
| [Marketing Claims Compliance Checker](skills/marketing-claims-checker/) | Checks marketing claims for compliance before they go out. |  |
| [Radio, Podcast, Print and Direct Mail Ad Writer](skills/offline-audio-print-ad-writer/) | Writes ad copy for the channels outside the ad platforms, with a way to respond built into every piece. |  |
| [UX Microcopy Writer](skills/ux-microcopy-writer/) | Writes and audits UX microcopy (buttons, links and nav labels, form labels and hints, error and validation messages, empty states, success, confirmation and thank-you… |  |

### Creative

Creative briefs, video ad scripts, testing roadmaps and fatigue detection.

| Skill | What it does | |
|---|---|---|
| [Ad Creative Brief Generator](skills/ad-creative-brief-generator/) | Writes ad creative briefs from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/ad-creative-brief-generator) |
| [Ad Creative Fatigue Detector](skills/ad-creative-fatigue-detector/) | Finds ad creatives that are wearing out on Meta, Google Ads, TikTok, LinkedIn, Snapchat and X by pulling ad-level history itself through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/ad-creative-fatigue-detector) |
| [Ad Creative Scorer](skills/ad-creative-scorer/) | Grades one draft ad (a video, image, storyboard, script or set of frames, plus its copy) before it goes live, for one platform and placement. |  |
| [Ad Specs and Asset Matrix](skills/ad-specs-asset-matrix/) | Builds the ad specs and asset matrix for one campaign across Meta, TikTok, LinkedIn, Pinterest, Snapchat, X and Google Ads, then checks the files you supply against it. |  |
| [Creative Testing Roadmap](skills/creative-testing-roadmap/) | Builds a creative testing roadmap from live ad data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/creative-testing-roadmap) |
| [Video Ad Script Writer](skills/video-ad-script-writer/) | Writes ready-to-shoot video ad scripts for TikTok, Reels, Meta feed, YouTube and LinkedIn, plus video sales letters and product demos, from live data pulled through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/creative/video-ad-script-writer) |

### CRO

Conversion rate optimization for forms, signup flows and onboarding.

| Skill | What it does | |
|---|---|---|
| [Checkout Optimization Auditor](skills/checkout-cro-auditor/) | Audits an online store's checkout to find why shoppers leave between the cart and payment, and ranks the fixes by the revenue at stake. |  |
| [Form CRO](skills/form-cro/) | Audits lead, contact, demo, quote and checkout forms on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/form-cro) |
| [Heatmap and Session Recording Analyst](skills/heatmap-session-analyst/) | Turns Microsoft Clarity or Hotjar behaviour data into a short, ranked list of page fixes. |  |
| [Onboarding CRO](skills/onboarding-cro/) | Maps the new-user journey from first visit to signup, onboarding, activation and the first return, on live GA4 data pulled through the InsightfulPipe MCP, finds the… | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/onboarding-cro) |
| [Signup Flow CRO](skills/signup-flow-cro/) | Audits a signup or registration flow on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/cro/signup-flow-cro) |
| [Website Conversion Rate Benchmark](skills/conversion-rate-benchmark/) | Answers "is my conversion rate good?" for a website or online store. |  |
| [Website Personalization Planner](skills/website-personalization-planner/) | Plans website and landing page personalization from measured data, on live data through the InsightfulPipe MCP or from a pasted segment report. |  |

### Cross-Platform

Budget allocation across Google, Meta, TikTok, LinkedIn and Microsoft Ads.

| Skill | What it does | |
|---|---|---|
| [Ad Platform vs GA4 vs Store Reconciliation](skills/conversion-reconciliation/) | Reconciles what each ad platform claims against GA4 and the store, through the InsightfulPipe MCP or from exports. |  |
| [Agency Client Health Monitor](skills/agency-client-health/) | Monitors the health of every client an agency manages, live through the InsightfulPipe MCP. |  |
| [Blended ROAS and CAC Report](skills/blended-roas-report/) | Works out blended ROAS, customer acquisition cost and full-cost marketing ROI across every connected ad platform through the InsightfulPipe MCP, or from numbers the… |  |
| [Campaign Launch Preflight](skills/campaign-launch-preflight/) | Runs a go/no-go preflight on a Google Ads, Meta or LinkedIn Ads campaign through the InsightfulPipe MCP, before it launches or before its budget goes up. |  |
| [Cross Platform Budget Allocator](skills/cross-platform-budget-allocator/) | Splits an ad budget across Google, Meta, Microsoft, LinkedIn, TikTok, Pinterest, Snapchat, X and OpenAI Ads on live data through the InsightfulPipe MCP, and plans the… | [Page](https://insightfulpipe.com/marketing-claude-skills/cross-platform/cross-platform-budget-allocator) |
| [KPI Alerts and Daily Digest](skills/kpi-alerts-digest/) | Runs a daily marketing health check and a week-over-week anomaly scan across every connected ad, analytics and search source through the InsightfulPipe MCP, then drafts… |  |
| [Marketing Dashboard Builder](skills/marketing-dashboard-builder/) | Builds a live marketing dashboard in Google Sheets or Looker Studio, a weekly report page in Notion, a weekly summary in Slack or a campaign tracker in Airtable, from… |  |
| [Marketing Performance Report](skills/marketing-performance-report/) | Builds a marketing performance report from every connected source through the InsightfulPipe MCP, or from pasted exports. | [Page](https://insightfulpipe.com/marketing-claude-skills/cross-platform/marketing-performance-report) |
| [Paid vs Organic Search Overlap](skills/paid-organic-overlap/) | Compares what you pay for in Google Ads with where you already rank organically, on live data through the InsightfulPipe MCP. |  |
| [Performance Drop Investigator](skills/performance-drop-investigator/) | Investigates why a marketing number moved, on live data through the InsightfulPipe MCP or from pasted exports. |  |

### E-commerce

Store reports, merchandising, promotions, AOV, bundles, inventory, returns and profit on ad spend.

| Skill | What it does | |
|---|---|---|
| [Average Order Value Optimizer](skills/aov-optimizer/) | Finds out how to increase average order value for an online store from its own orders. |  |
| [Competitor Price Tracker](skills/competitor-price-tracker/) | Tracks an online store's prices against named competitors and marketplace sellers, product by product. |  |
| [Cross-Border Store Setup Planner](skills/cross-border-store-expansion/) | Sets up an online store to sell into countries it has already chosen. |  |
| [Discount and Promotion Analyst](skills/discount-promo-analyst/) | Measures discount code performance and every sale an online store ran, from its own orders. |  |
| [Ecommerce Store Report](skills/ecommerce-store-report/) | Builds the weekly or monthly sales report for an online store from its own orders, not from ad-platform claims. |  |
| [Online Store Launch Checklist](skills/store-launch-checklist/) | Checks a new online store before it launches and gives every item a pass, fail, unknown or not-applicable result with its evidence and the fix. |  |
| [Product Bundle and Cross-Sell Builder](skills/bundle-cross-sell-builder/) | Finds which products a store's customers buy together and turns the strong pairs into product bundles, "pairs well with" placements, post-purchase offers and cross-sell… |  |
| [Product Merchandising Analyst](skills/product-merchandising-analyst/) | Ranks every product and collection in an online store on item views, add-to-cart rate, purchase rate, revenue and margin, then says what to feature on the home page… |  |
| [Profit on Ad Spend (POAS) Report](skills/poas-profit-report/) | Profit on ad spend (POAS) calculator and report for online stores. |  |
| [Repeat Purchase and Subscribe-and-Save Planner](skills/repeat-purchase-planner/) | Plans how an online store turns first-time buyers into repeat buyers, from its own order history. |  |
| [Returns and Refunds Analyst](skills/returns-refunds-analyst/) | Analyses an online store's returns and refunds from its own orders and refunds, pulled live from Shopify, WooCommerce or Magento through the InsightfulPipe MCP or read… |  |
| [Stock-Out and Excess Inventory Planner](skills/inventory-planner/) | Plans an online store's marketing around its stock. |  |
| [Store Site Search Analyst](skills/store-site-search-analyst/) | Analyses an online store's site search. |  |

### Email Marketing

Lifecycle strategy, deliverability, segmentation, list health, retention and SMS planning.

| Skill | What it does | |
|---|---|---|
| [Churn Risk and Win-back Planner](skills/churn-risk-winback-planner/) | Customer churn analysis and win-back planning from the business's own buying rhythm. |  |
| [Competitor Email Teardown](skills/competitor-email-teardown/) | Email marketing competitor analysis from real inboxes. |  |
| [Customer Retention Cohort Analyst](skills/retention-cohort-analyst/) | Builds a customer retention cohort analysis from orders, subscriptions or an app retention export. |  |
| [Email and Lifecycle Marketing Strategy](skills/email-lifecycle-strategy/) | Writes the email and lifecycle marketing strategy for a business, from the first sign-up or purchase onward. |  |
| [Email Deliverability Auditor](skills/email-deliverability-auditor/) | Audits why marketing email lands in spam or bounces and what to repair first. |  |
| [Email List Cleaner](skills/email-list-cleaner/) | Cleans an email contact file before it is imported or mailed. |  |
| [Email List Growth Optimizer](skills/email-list-growth-optimizer/) | Shows how to grow your email and SMS list from the numbers you already have. |  |
| [Email Marketing Calendar and Send Frequency Planner](skills/email-campaign-calendar/) | Plans the broadcast side of email marketing for the next quarter and answers how often to send marketing emails. |  |
| [Email Platform Setup and Migration Planner](skills/email-platform-setup-migration/) | Plans an email platform migration (ESP migration) or a first setup, such as Mailchimp to Klaviyo, Klaviyo to Mailchimp, or any platform from exports. |  |
| [Email Send Check](skills/email-send-check/) | Proofs a built campaign or flow email just before it goes out and returns Go, Go after fixes or Hold with a numbered fix list. |  |
| [HTML Email Template Builder](skills/html-email-template-builder/) | Builds a responsive HTML email template that holds up in Gmail, Outlook, Apple Mail and Yahoo, from pasted copy, a screenshot or design, an existing email, or a brand's… |  |
| [Loyalty and VIP Program Designer](skills/loyalty-vip-program-designer/) | Designs a customer loyalty program, or reviews and redesigns one that already runs (points, spend tiers, a VIP tier, an optional paid membership), from the store's own… |  |
| [Push Notification and In-App Message Planner](skills/push-inapp-message-planner/) | Plans an app's or website's push notifications and in-app messages, the push notification strategy end to end. |  |
| [RFM Analysis and Segmentation](skills/customer-segmentation-rfm/) | Runs an RFM analysis on a store's order history and turns it into email list segmentation. |  |
| [SMS and WhatsApp Marketing Planner](skills/sms-whatsapp-planner/) | Plans and writes an SMS marketing program, with WhatsApp where it fits. |  |
| [Subscription Cancel Flow and Dunning Planner](skills/cancel-flow-dunning-planner/) | Subscription churn plan for SaaS and subscription businesses: splits lost revenue into customers who chose to leave and customers lost to failed payments, measuring the… |  |

### Facebook Ads

Account audits, audiences, structure, creative tests, budgets and reports for Meta Ads.

| Skill | What it does | |
|---|---|---|
| [Facebook Ads Account Auditor](skills/facebook-ads-account-auditor/) | Audits a Meta (Facebook and Instagram) Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-account-auditor) |
| [Facebook Ads Audience Builder](skills/facebook-ads-audience-builder/) | Builds a Meta (Facebook and Instagram) Ads audience plan from the live ad account through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-audience-builder) |
| [Facebook Ads Budget Allocator](skills/facebook-ads-budget-allocator/) | Reallocates Meta (Facebook and Instagram) ad budgets on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-budget-allocator) |
| [Facebook Ads Campaign Structure](skills/facebook-ads-campaign-structure/) | Designs or restructures a Meta (Facebook and Instagram) Ads account on live data through the InsightfulPipe MCP, plans how much a new campaign needs to spend, and… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-campaign-structure) |
| [Facebook Ads Creative Tester](skills/facebook-ads-creative-tester/) | Plans, sizes, launches and reads Meta (Facebook and Instagram) creative tests on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-creative-tester) |
| [Facebook Ads Launch Checklist](skills/facebook-ads-launch-checklist/) | Checks a Meta (Facebook and Instagram) Ads campaign before it goes live, and finds why a live one is not spending or not delivering, on live data through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-launch-checklist) |
| [Facebook Ads Monthly Report](skills/facebook-ads-monthly-report/) | Writes a monthly or weekly Meta (Facebook and Instagram) Ads report from live account data through the InsightfulPipe MCP, and a quarterly creative strategy review on… | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-monthly-report) |
| [Facebook Ads Scaling Roadmap](skills/facebook-ads-scaling-roadmap/) | Builds a phased Meta (Facebook and Instagram) Ads scaling roadmap on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/facebook-ads/facebook-ads-scaling-roadmap) |

### Google Ads

Search term, keyword, bidding, budget, PMax and reporting skills for Google Ads.

| Skill | What it does | |
|---|---|---|
| [Ad Copy Performance Ranker](skills/ad-copy-performance-ranker/) | Ranks Google Ads responsive search ads and their individual headlines and descriptions on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/ad-copy-performance-ranker) |
| [AI Max for Search Reviewer](skills/ai-max-search-reviewer/) | Decides whether a Google Ads Search campaign should turn on AI Max for Search, then reviews it once it runs. |  |
| [Bid Strategy Auditor](skills/bid-strategy-auditor/) | Audits Google Ads bid strategies on live data through the InsightfulPipe MCP and sets up value-based bidding, data exclusions and seasonality adjustments. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/bid-strategy-auditor) |
| [Budget Allocation Optimizer](skills/budget-allocation-optimizer/) | Moves Google Ads budget between campaigns to get more conversions from the same total, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/budget-allocation-optimizer) |
| [Competitor Keyword Campaign Planner](skills/competitor-keyword-campaign-planner/) | Plans a Google Ads competitor campaign that bids on rival brand names. |  |
| [Display Video Demand Gen Auditor](skills/display-video-demand-gen-auditor/) | Audits Google Ads Display, YouTube (Video) and Demand Gen campaigns on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/display-video-demand-gen-auditor) |
| [GAQL Query Builder](skills/gaql-report-builder/) | Turns a plain Google Ads reporting question into a working GAQL (Google Ads Query Language) query, or repairs a query that fails, checks it against the rules and… |  |
| [Geo Performance Optimizer](skills/geo-performance-optimizer/) | Finds where, on which device and at what hour a Google Ads account wastes or earns its money, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/geo-performance-optimizer) |
| [Google Ad Grants Manager](skills/google-ad-grants-manager/) | Keeps a nonprofit's Google Ad Grants account compliant and helps it use more of the 10,000 USD monthly grant. |  |
| [Google Ads Account Audit](skills/google-ads-account-audit/) | Runs a full Google Ads account audit on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-account-audit) |
| [Google Ads Account Restructure Planner](skills/google-ads-account-restructure-planner/) | Plans a Google Ads account restructure and writes the step-by-step migration. |  |
| [Google Ads Audience Analyzer](skills/google-ads-audience-analyzer/) | Analyzes Google Ads audiences on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-audience-analyzer) |
| [Google Ads Bulk Ad and URL Updater](skills/google-ads-bulk-updater/) | Changes a price, offer, year, phone number, final URL, tracking template or final URL suffix everywhere it lives in a Google Ads account at once, after a price rise, a… |  |
| [Google Ads Campaign Builder](skills/google-ads-campaign-builder/) | Builds a Google Ads Search campaign from a short brief using live account data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-campaign-builder) |
| [Google Ads Click Fraud Check](skills/google-ads-click-fraud-check/) | Checks whether a Google Ads account is paying for fake or accidental clicks. |  |
| [Google Ads Delivery Troubleshooter](skills/google-ads-delivery-troubleshooter/) | Finds out why Google Ads campaigns, ad groups, keywords or ads aren't showing or can't spend their budget. |  |
| [Google Ads Disapproval and Suspension Fixer](skills/google-ads-disapproval-suspension-fixer/) | Fixes Google Ads disapprovals, limited approvals and account suspensions. |  |
| [Google Ads Extensions and Assets Auditor](skills/google-ads-assets-auditor/) | Audits every Google Ads asset (extension) across the account. |  |
| [Google Ads Hacked Account Check and Recovery](skills/google-ads-hacked-account-recovery/) | Checks a Google Ads account for signs that someone else took control (unknown users or invitations, unknown manager account links, new campaigns, budget raises, edited… |  |
| [Google Ads Recommendations Reviewer](skills/google-ads-recommendations-reviewer/) | Reviews every open Google Ads recommendation and gives each one an accept, adapt or dismiss verdict tested on the account's own numbers, not on Google's estimated uplift. |  |
| [Google Ads Scripts and Automated Rules Writer](skills/google-ads-scripts-rules-writer/) | Writes, explains, fixes and safety-checks Google Ads scripts and automated rules for guard jobs like a monthly budget cap, broken final URL checks, keywords that spend… |  |
| [Google Ads Weekly Brief](skills/google-ads-weekly-brief/) | Writes the weekly Google Ads brief for a client, boss or team from live account data through the InsightfulPipe MCP, and reviews the last 90 days of Google Ads change… | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/google-ads-weekly-brief) |
| [Google App Campaigns Planner and Reviewer](skills/google-app-campaigns-manager/) | Plans and reviews Google App campaigns (formerly UAC) for installs, in-app actions, value or pre-registration. |  |
| [Google Shopping and Retail PMax Review](skills/google-shopping-retail-pmax-review/) | Reviews how Google Shopping and retail Performance Max campaigns are built and where their money goes, product by product. |  |
| [Impression Share Analyst](skills/impression-share-analyst/) | Analyzes Google Ads search impression share on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/impression-share-analyst) |
| [Keyword Performance Analyzer](skills/keyword-performance-analyzer/) | Analyzes Google Ads keywords on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/keyword-performance-analyzer) |
| [Month End Report Generator](skills/month-end-report-generator/) | Writes the month-end Google Ads report from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/month-end-report-generator) |
| [Negative Keyword Implementer](skills/negative-keyword-implementer/) | Finds, checks and adds Google Ads negative keywords on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/negative-keyword-implementer) |
| [PMax Asset Group Analyzer](skills/pmax-asset-group-analyzer/) | Reviews Google Performance Max campaigns on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/pmax-asset-group-analyzer) |
| [Quality Score Fixer](skills/quality-score-fixer/) | Diagnoses and fixes low Google Ads Quality Score on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/quality-score-fixer) |
| [Rsa Ad Copy Writer](skills/rsa-ad-copy-writer/) | Writes Google Ads ad copy from the account's own evidence, live through the InsightfulPipe MCP or from a paste. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/rsa-ad-copy-writer) |
| [Scaling Roadmap Builder](skills/scaling-roadmap-builder/) | Builds a phased plan to scale Google Ads spend on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/scaling-roadmap-builder) |
| [Search Term Gold Miner](skills/search-term-gold-miner/) | Mines Google Ads search terms on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/search-term-gold-miner) |
| [Shopping Feed Optimizer](skills/shopping-feed-optimizer/) | Audits and optimizes product feeds for Google Shopping, Meta Catalog, and other platforms. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/shopping-feed-optimizer) |
| [Spend Pacing Monitor](skills/spend-pacing-monitor/) | Checks Google Ads spend pacing on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/google-ads/spend-pacing-monitor) |
| [YouTube, Demand Gen and Display Campaign Builder](skills/youtube-demand-gen-campaign-builder/) | Builds a Google Ads YouTube (Video), Demand Gen or Display campaign for a stated goal. |  |

### Growth

Product-led growth: growth loops, North Star metric, trial-to-paid, paywalls, lead magnets and experiment backlogs.

| Skill | What it does | |
|---|---|---|
| [Developer Tool Growth Plan](skills/developer-oss-growth/) | Builds a developer marketing strategy and a 90-day growth plan for a developer tool, API or open-source project, with monthly targets. |  |
| [Feature Adoption Planner](skills/feature-adoption-planner/) | Plans feature adoption campaigns for existing users of a software product. |  |
| [Growth Experiment Backlog](skills/growth-experiment-backlog/) | Builds and keeps a growth experiment backlog. |  |
| [Growth Loop Designer](skills/growth-loop-designer/) | Designs the growth loops a product can run and picks the one to build first, with the math shown. |  |
| [Interactive Calculator Builder](skills/interactive-calculator-builder/) | Builds a working calculator a website can give away (ROI, savings, cost, payback, sizing or price estimate) as one embeddable HTML file with no backend. |  |
| [Lead Magnet Writer](skills/lead-magnet-writer/) | Writes a finished lead magnet, ready to hand out, plus its opt-in page copy and delivery email. |  |
| [Net Revenue Retention and Expansion Planner](skills/expansion-revenue-planner/) | Plans SaaS expansion revenue from the business's own billing and usage data. |  |
| [North Star Metric Builder](skills/north-star-metric-builder/) | Chooses a North Star metric that counts the value customers get from the product, tests every candidate against the business's own month-by-month retention and revenue… | [Page](https://insightfulpipe.com/marketing-claude-skills/growth/north-star-metric-builder) |
| [Paywall Screen Optimizer](skills/paywall-screen-optimizer/) | Reviews and improves the paywall screen of a subscription app or SaaS product, the screen where a free user is asked to pay. |  |
| [PLG and SaaS Growth Audit](skills/plg-saas-growth-audit/) | Audits a self-serve SaaS business from first visit to paying, growing and leaving (visit to signup, activation, trial or free plan to paid, expansion, cancellations… |  |
| [Plugin and Integration Marketplace Optimizer](skills/integration-marketplace-listing/) | Audits and rewrites a software product's listings in the marketplaces people install it from (WordPress.org plugin directory, Shopify App Store, Chrome Web Store… |  |
| [Quiz Funnel Builder](skills/quiz-funnel-builder/) | Designs a quiz funnel for a product recommendation quiz, a lead generation quiz or a self-assessment scorecard. |  |
| [Trial-to-Paid Conversion Optimizer](skills/trial-to-paid-optimizer/) | Works out why free trial users don't pay and plans the fix for the whole trial. |  |

### LinkedIn Ads

B2B targeting, lead quality and CPL audits for LinkedIn Ads.

| Skill | What it does | |
|---|---|---|
| [LinkedIn Abm Reporting](skills/linkedin-abm-reporting/) | Builds a LinkedIn Ads ABM and pipeline report from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-abm-reporting) |
| [LinkedIn Ad Copy Writer](skills/linkedin-ad-copy-writer/) | Writes LinkedIn ad copy for every format LinkedIn sells (single image and video intro text and headlines, document ad teasers, carousel card lines, Message Ads… |  |
| [LinkedIn Ads Auditor](skills/linkedin-ads-auditor/) | Audits a LinkedIn Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-auditor) |
| [LinkedIn Ads B2B Optimizer](skills/linkedin-ads-b2b-optimizer/) | Optimizes LinkedIn Ads for B2B lead generation and account-based marketing on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-b2b-optimizer) |
| [LinkedIn Ads Campaign Builder](skills/linkedin-ads-campaign-builder/) | Builds a LinkedIn Ads campaign from a brief on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-ads-campaign-builder) |
| [LinkedIn Lead Gen Optimizer](skills/linkedin-lead-gen-optimizer/) | Reviews and improves LinkedIn Lead Gen Form campaigns on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/linkedin-ads/linkedin-lead-gen-optimizer) |
| [LinkedIn Thought Leader Ads Planner](skills/linkedin-thought-leader-ads-planner/) | Plans LinkedIn Thought Leader Ads. |  |

### Local Marketing

Google Business Profile, reviews and local search performance for local businesses.

| Skill | What it does | |
|---|---|---|
| [Fake Review Removal Handler](skills/review-removal-handler/) | Decides which negative or suspicious reviews can be reported and removed, and which will stay. |  |
| [Google Business Profile Manager](skills/google-business-profile-manager/) | Manages Google Business Profile locations on live data through the InsightfulPipe MCP. |  |
| [Local Business Marketing Report](skills/local-business-marketing-report/) | Builds a local business marketing report on live data through the InsightfulPipe MCP, or a 90-day marketing plan for one location. |  |
| [Local Citation and NAP Audit](skills/local-citation-nap-audit/) | Runs a local citation and NAP consistency audit. |  |
| [Local Competitor Gap Analysis](skills/local-competitor-gap/) | Local SEO competitor analysis for a business that loses the Google map pack. |  |
| [Local Lead Ads Planner](skills/local-lead-ads-planner/) | Plans and grades a service business's spend on local lead platforms (Yelp Ads, Angi, Thumbtack and Nextdoor Ads) by booked jobs instead of lead counts. |  |
| [Local Rank Tracker by Area](skills/local-rank-grid-tracker/) | Local rank tracker by area. |  |
| [Local Services Ads Manager](skills/local-services-ads-manager/) | Reviews Google Local Services Ads for a service business (plumbers, HVAC, electricians, roofers, lawyers and other pay-per-lead categories). |  |
| [Multi-Location and Franchise Marketing Plan](skills/multi-location-marketing-plan/) | Builds a franchise marketing plan or multi-location marketing strategy for a brand with many locations. |  |
| [Review Generation Planner](skills/review-generation-planner/) | Plans how a local business or an online store earns more reviews, the right way. |  |
| [Review Insights Analyzer](skills/review-insights-analyzer/) | Analyzes customer reviews for a local business or an online store and turns them into numbers to act on. |  |
| [Reviews and Comments Responder](skills/reviews-and-comments-responder/) | Finds every review, comment and mention that still needs an answer and drafts short replies in your brand voice. |  |

### Marketing

Copywriting, brand voice, SEO, landing pages, email and competitor research.

| Skill | What it does | |
|---|---|---|
| [Ad Landing Page Match Scorer](skills/ad-landing-page-match-scorer/) | Scores how well every active ad matches the page it sends people to, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/ad-landing-page-match-scorer) |
| [B2B Lead Enrichment and Scoring](skills/b2b-lead-enrichment/) | Cleans, enriches and scores a B2B lead list through the InsightfulPipe MCP, watches target accounts for buying signals every week, and writes a pre-call account… |  |
| [Brand Voice](skills/brand-voice/) | Builds a brand voice and tone guide, a messaging house and a copy check from the brand's own live copy through the InsightfulPipe MCP, and audits a website's messaging… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/brand-voice) |
| [Buyer Persona Builder](skills/buyer-persona-builder/) | Builds buyer personas and an ideal customer profile from customer evidence pulled live through the InsightfulPipe MCP (Search Console queries, GA4 key events, LinkedIn… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/buyer-persona-builder) |
| [Case Study Writer](skills/case-study-writer/) | Writes a case study from real, measured results through the InsightfulPipe MCP. |  |
| [Competitor Ad Research](skills/competitor-ad-research/) | Researches competitors' live ads in the public Meta, Google, Microsoft and LinkedIn ad libraries through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-ad-research) |
| [Competitor SWOT Analyzer](skills/competitor-swot-analyzer/) | Builds a competitor SWOT, positioning read and sales battlecard from live public data through the InsightfulPipe MCP, and monitors competitors. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-swot-analyzer) |
| [Competitor Website Teardown](skills/competitor-website-teardown/) | Tears down up to four competitor websites against yours on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/competitor-website-teardown) |
| [Content Calendar Scheduler](skills/content-calendar-scheduler/) | Builds a social media content calendar from live data through the InsightfulPipe MCP and schedules it. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/content-calendar-scheduler) |
| [Content Performance Analyst](skills/content-performance-analyst/) | Analyses content performance across the blog, social pages and email, and what that content earns, on live data through the InsightfulPipe MCP or from pasted exports. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/content-performance-analyst) |
| [Copywriting](skills/copywriting/) | Writes, reviews and rewrites conversion copy from live evidence through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/copywriting) |
| [Cross Channel Attribution Analyst](skills/cross-channel-attribution-analyst/) | Works out which marketing channels really bring customers in and which only collect the credit at the end, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/cross-channel-attribution-analyst) |
| [Email Campaign Analyst](skills/email-campaign-analyst/) | Analyses email campaigns on live Klaviyo or Mailchimp data through the InsightfulPipe MCP. |  |
| [Email Sequence Builder](skills/email-sequence-builder/) | Plans and writes email sequences and flows (welcome, lead nurture, onboarding, cart and browse abandonment, post-purchase, winback, launch, event and transactional… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/email-sequence-builder) |
| [Funnel Dropoff Diagnostician](skills/funnel-dropoff-diagnostician/) | Finds where a conversion funnel loses people, on live data pulled through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/funnel-dropoff-diagnostician) |
| [Klaviyo Flow Auditor](skills/klaviyo-flow-auditor/) | Audits email automation on live data through the InsightfulPipe MCP, or from pasted exports. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/klaviyo-flow-auditor) |
| [Landing Page Auditor](skills/landing-page-auditor/) | Audits a landing page, homepage, sales page or any key page for conversion on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/landing-page-auditor) |
| [Marketing Psychology](skills/marketing-psychology/) | Applies behavioural science to marketing on live evidence through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/marketing-psychology) |
| [Newsletter](skills/newsletter/) | Writes email newsletters from what you actually published and what your readers actually clicked. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/newsletter) |
| [Pricing Page Auditor](skills/pricing-page-auditor/) | Audits a pricing page on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/pricing-page-auditor) |
| [Programmatic SEO](skills/programmatic-seo/) | Plans programmatic SEO pages (one template filled from data, one page per variable such as a city, trade, integration or competitor) on live data through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/programmatic-seo) |
| [Retargeting Sequence Designer](skills/retargeting-sequence-designer/) | Designs retargeting ad sequences from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/retargeting-sequence-designer) |
| [SEO Audit](skills/seo-audit/) | Runs a full SEO audit of a site on live data through the InsightfulPipe MCP, or an E-E-A-T and helpful content review of its key pages. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/seo-audit) |
| [Social Content](skills/social-content/) | Plans, writes and checks organic social media content from the brand's own post history through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/social-content) |
| [USP Extractor](skills/usp-extractor/) | Finds a business's unique selling proposition from live evidence through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/marketing/usp-extractor) |

### Marketing Ops

Campaign briefs, SOPs, capacity, team planning, hiring and the martech stack.

| Skill | What it does | |
|---|---|---|
| [AI Marketing Workflow Planner](skills/ai-marketing-workflow-planner/) | Plans how a marketing team uses AI and automation. |  |
| [Marketing Campaign Brief Writer](skills/campaign-brief-writer/) | Writes a one-page marketing campaign brief that a team, agency or freelancer can work from, starting from a pasted request, email or meeting notes. |  |
| [Marketing Capacity Planner](skills/marketing-capacity-planner/) | Plans whether a marketing team or agency can deliver the work, and which clients make money. |  |
| [Marketing Hiring Kit](skills/marketing-hiring-kit/) | Builds a complete kit to hire one marketer (PPC, paid social, SEO, content, email, marketing ops, head of marketing or a freelancer) at a given level. |  |
| [Marketing Ops and Martech Stack Audit](skills/marketing-ops-stack-audit/) | Audits a marketing technology stack and the marketing ops process around it. |  |
| [Marketing SOP Builder](skills/marketing-sop-builder/) | Writes a marketing SOP (standard operating procedure) for a recurring process such as monthly reporting, campaign launch, tracking QA, client onboarding or content… |  |
| [Marketing Team Structure Planner](skills/marketing-team-planner/) | Designs the marketing team for a company's stage, goal and people budget. |  |

### Marketplaces

Amazon Ads, retail media, TikTok Shop and marketplace expansion.

| Skill | What it does | |
|---|---|---|
| [Amazon Ads Audit](skills/amazon-ads-audit/) | Audits an Amazon Ads account (Sponsored Products, Sponsored Brands, Sponsored Display and Amazon DSP) from the seller's own exports. |  |
| [Amazon PPC Bid Optimizer](skills/amazon-ppc-bid-optimizer/) | Sets Amazon Sponsored Products keyword and product-target bids to hit a target ACOS or TACOS, from the seller's own targeting and placement reports. |  |
| [Amazon PPC Campaign Builder](skills/amazon-ppc-campaign-builder/) | Builds the Amazon PPC campaign structure for a new or relaunched product, or Amazon ads for a book. |  |
| [Amazon Search Term Harvester](skills/amazon-search-term-harvester/) | Runs the weekly Amazon PPC search term harvest from a Sponsored Products or Sponsored Brands search term report and a bulk file download. |  |
| [Etsy SEO and Shop Audit](skills/etsy-shop-optimizer/) | Audits a whole Etsy shop for Etsy SEO and sales from the shop's own listings CSV and Stats. |  |
| [Marketplace Expansion Planner](skills/marketplace-expansion-planner/) | Plans which online marketplaces a brand should sell on next (Amazon, Walmart, eBay, Etsy, TikTok Shop or a regional marketplace) and in what order. |  |
| [Retail Media Planner (Walmart, Instacart, Target)](skills/retail-media-planner/) | Plans and reviews retail media ads beyond Amazon (Walmart Connect, Instacart Ads, Target's Roundel, and any other retail network the brand runs) from each network's own… |  |
| [TikTok Shop GMV Max Planner](skills/tiktok-shop-gmv-max-planner/) | Plans and reviews TikTok Shop ads run as GMV Max (Product GMV Max and LIVE GMV Max). |  |
| [TikTok Shop Launch and Growth Planner](skills/tiktok-shop-planner/) | Plans how to sell on TikTok Shop, for a launch or for growth. |  |

### Measurement

GA4 tracking, attribution audits, A/B tests, incrementality and LTV:CAC.

| Skill | What it does | |
|---|---|---|
| [A/B Test Designer](skills/ab-test-designer/) | Designs A/B tests and reads out finished ones on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ab-test-designer) |
| [Attribution Model Auditor](skills/attribution-model-auditor/) | Audits how conversions are attributed across Google Ads, Meta, LinkedIn, Microsoft Ads, TikTok and GA4 on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/attribution-model-auditor) |
| [B2B Pipeline and Revenue Attribution](skills/pipeline-revenue-attribution/) | Credits CRM pipeline and closed revenue to the sources that produced them, paid and unpaid (each ad campaign, organic search, email, referrals, partners, events), from… |  |
| [Bulk UTM Link Builder](skills/bulk-utm-links/) | Bulk UTM builder and campaign naming sheet. |  |
| [Call Tracking Analyst](skills/call-tracking-analyst/) | Builds a call tracking report from a CallRail account through the InsightfulPipe MCP or from any pasted call log CSV. |  |
| [Consent Mode Auditor](skills/consent-mode-auditor/) | Audits Google Consent Mode v2 and the cookie banner on a live site. |  |
| [Conversion Tracking Auditor](skills/conversion-tracking-auditor/) | Audits conversion tracking end to end on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/conversion-tracking-auditor) |
| [GA4 Audience Retention](skills/ga4-audience-retention/) | Analyses who a GA4 property's users are and whether they come back, from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-audience-retention) |
| [GA4 BigQuery Query Writer](skills/ga4-bigquery-query-writer/) | Writes, explains, fixes and runs BigQuery SQL on the GA4 export and the Google Ads transfer tables, for questions the GA4 interface can't answer well. |  |
| [GA4 Channel Performance](skills/ga4-channel-performance/) | Reports GA4 channel and source/medium performance on live data through the InsightfulPipe MCP, adds ad spend from Google Ads, Meta, LinkedIn, Microsoft Ads and TikTok… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-channel-performance) |
| [GA4 Ecommerce Funnel](skills/ga4-ecommerce-funnel/) | Analyses a store's GA4 ecommerce on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-ecommerce-funnel) |
| [GA4 Landing Page Analyst](skills/ga4-landing-page-analyst/) | Analyses every landing page in a GA4 property on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-landing-page-analyst) |
| [GA4 Property Audit](skills/ga4-property-audit/) | Audits a GA4 property's setup and data quality on live data through the InsightfulPipe MCP, or sets up a new or empty property step by step. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-property-audit) |
| [GA4 Weekly Report](skills/ga4-weekly-report/) | Builds a weekly (or monthly) Google Analytics 4 report from live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ga4-weekly-report) |
| [Gtm Container Auditor](skills/gtm-container-auditor/) | Audits a Google Tag Manager container on live data through the InsightfulPipe MCP or from a pasted export, and builds the event tracking it is missing. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/gtm-container-auditor) |
| [How Did You Hear About Us Survey Analyst](skills/self-reported-attribution/) | Runs self-reported attribution end to end. |  |
| [Incrementality Test Designer](skills/incrementality-test-designer/) | Designs an incrementality test (geo holdout, audience holdout or platform conversion lift) from live ad data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/incrementality-test-designer) |
| [Junk Lead and Form Spam Investigator](skills/junk-lead-investigator/) | Finds where spam, fake and poor-fit leads come from and how to stop them. |  |
| [LTV CAC Ratio Optimizer](skills/ltv-cac-ratio-optimizer/) | Analyzes customer lifetime value (LTV) and customer acquisition cost (CAC) to optimize advertising profitability. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/ltv-cac-ratio-optimizer) |
| [Marketing Data Warehouse and SQL Builder](skills/marketing-data-warehouse/) | Sets up and checks a marketing data warehouse. |  |
| [Marketing Forecast](skills/marketing-forecast/) | Forecasts leads, spend and revenue from the account's own monthly history in two modes, the next two months or a 12-month annual forecast by month and by channel for… |  |
| [Marketing Mix Model Builder](skills/marketing-mix-model-builder/) | Builds a marketing mix model (MMM) from weekly spend by channel and weekly total sales or leads, with carryover and diminishing returns, then reports each channel's… |  |
| [Measurement Plan Builder](skills/measurement-plan-builder/) | Builds a measurement plan on live data through the InsightfulPipe MCP, with a North Star metric and its inputs and guardrails, a KPI tree with a baseline on every node… | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/measurement-plan-builder) |
| [Offline Conversion Setup](skills/offline-conversion-setup/) | Sets up offline conversion tracking so Google Ads, Microsoft Ads, Meta, LinkedIn and ChatGPT Ads bid on the leads that become customers, not on form fills. |  |
| [Server-Side Tracking Planner](skills/server-side-tracking-planner/) | Decides whether a website needs server-side tracking and, if it does, writes the build plan. |  |
| [TV, Offline Media and Geo Lift Analyst](skills/offline-media-lift-analyst/) | Measures the lift from media that gets no clicks (TV, connected TV, radio, billboards and transit, events and sponsorships) and reads out geo holdout tests after they… |  |
| [Utm Auditor](skills/utm-auditor/) | Audits UTM and campaign tagging on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/measurement/utm-auditor) |

### Meta Ads

Placement, creative and audience performance analysis for Meta Ads.

| Skill | What it does | |
|---|---|---|
| [Click-to-WhatsApp and Messenger Ads Planner](skills/meta-click-to-message-ads/) | Plans, builds and reviews Meta click-to-message ads, the Facebook and Instagram ads whose button opens a WhatsApp, Messenger or Instagram Direct chat instead of a… |  |
| [Facebook and Instagram Boost Post Picker](skills/meta-boost-post-picker/) | Picks which organic Facebook and Instagram posts and Reels are worth paying to promote, and how. |  |
| [Facebook Lead Ads Optimizer](skills/meta-lead-ads-optimizer/) | Reviews Facebook and Instagram lead ads and every Meta instant form behind them, then ranks forms, ad sets and ads by cost per qualified lead instead of cost per lead. |  |
| [Meta Ad Copy Writer](skills/meta-ad-copy-writer/) | Writes new Meta (Facebook and Instagram) ad copy from the ads that already win. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-ad-copy-writer) |
| [Meta Ad Rejection and Account Restriction Fixer](skills/meta-ad-rejection-fixer/) | Fixes rejected Facebook and Instagram ads and restricted Meta ad accounts. |  |
| [Meta Ad Specs and Safe Zone Checker](skills/meta-ad-specs-checker/) | Checks every Facebook and Instagram image and video ad against the placements it will run in (Facebook Feed, Instagram Feed, Facebook and Instagram Stories, Instagram… |  |
| [Meta Ads Automated Rules Builder](skills/meta-automated-rules-builder/) | Designs the automated rules a Meta (Facebook and Instagram) ad account should run, tests them on the account's own history, and writes them ready to enter in Ads Manager. |  |
| [Meta Ads Bid Strategy and Cost Cap Advisor](skills/meta-bid-strategy-advisor/) | Chooses the bid strategy for every Meta (Facebook and Instagram) campaign and ad set (highest volume, cost per result goal, bid cap, highest value or ROAS goal), sets… |  |
| [Meta Ads Performance Analyzer](skills/meta-ads-performance-analyzer/) | Analyzes Meta Ads (Facebook and Instagram) performance on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-ads-performance-analyzer) |
| [Meta Advantage Plus Auditor](skills/meta-advantage-plus-auditor/) | Audits Meta Advantage+ campaigns, Advantage+ creative enhancements and catalog (dynamic product) ads on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta-ads/meta-advantage-plus-auditor) |
| [Meta Business Portfolio Audit](skills/meta-business-portfolio-audit/) | Audits a Meta Business portfolio (formerly Facebook Business Manager) for setup, access and security. |  |
| [Meta Catalog Ads and Product Set Planner](skills/meta-catalog-product-set-planner/) | Plans Meta catalog ads (Advantage+ catalog ads, formerly dynamic product ads) from profit and stock instead of guesswork. |  |
| [Meta Opportunity Score and Recommendations Reviewer](skills/meta-recommendations-reviewer/) | Reviews the recommendations Meta shows in Ads Manager (the opportunity score list) and gives each one a verdict of apply, test first, skip or your call, decided by the… |  |
| [Meta Reach and Frequency Planner](skills/meta-reach-frequency-planner/) | Plans and reads out awareness and reach flights on Facebook and Instagram. |  |

### Microsoft Ads

Account audits and optimization for Microsoft Advertising (Bing) search, shopping and audience campaigns.

| Skill | What it does | |
|---|---|---|
| [Microsoft Ads Account Audit](skills/microsoft-ads-account-audit/) | Runs a full Microsoft Advertising (Bing Ads) account audit on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/microsoft-ads/microsoft-ads-account-audit) |
| [Microsoft Ads Optimizer](skills/microsoft-ads-optimizer/) | Finds and drafts the changes a Microsoft Advertising (Bing Ads) search account needs, on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/microsoft-ads/microsoft-ads-optimizer) |

### Paid Media

Media plans, benchmarks, stop-loss rules and channels beyond the big ad platforms.

| Skill | What it does | |
|---|---|---|
| [Ad Delivery Troubleshooter](skills/ad-delivery-troubleshooter/) | Finds why a campaign on LinkedIn Ads, TikTok Ads, Microsoft Ads, Pinterest Ads, Snapchat Ads, X Ads, OpenAI Ads or Reddit Ads is not delivering, gets no impressions, or… |  |
| [Ad Placement and Brand Safety Auditor](skills/placement-brand-safety-auditor/) | Audits where ads ran outside the main feeds (TikTok Ad Network, formerly Pangle; Microsoft Audience Network; LinkedIn Audience Network; and any DSP's domain and app… |  |
| [Ad Rejection Fixer](skills/ad-policy-fixer/) | Fixes rejected, disapproved and stuck ads, and restricted ad accounts, on LinkedIn, TikTok, Microsoft Ads (Bing), Pinterest, Snapchat, X, ChatGPT (OpenAI) Ads and Reddit. |  |
| [Ad Smoke Test Planner](skills/ad-demand-test-planner/) | Plans and reads a small paid smoke test that checks demand for an offer, or which message sells it, before anyone builds or repositions. |  |
| [Ad Stop-Loss Rules Designer](skills/ad-stop-loss-rules/) | Designs stop-loss rules for new ads before money is spent, on TikTok, LinkedIn, Microsoft Ads, Snapchat, Pinterest, X or several at once. |  |
| [Billboard and Out-of-Home Advertising Planner](skills/ooh-dooh-planner/) | Plans a billboard, transit and digital out-of-home (DOOH) buy from the business's own demand. |  |
| [Break-Even ROAS and Target CPA Calculator](skills/paid-media-math/) | Break-even ROAS and target CPA calculator for paid media. |  |
| [CTV and Streaming TV Ads Planner](skills/ctv-streaming-ads-planner/) | Plans connected TV (CTV) and streaming TV ad buys and sets up how to measure them. |  |
| [International PPC Expansion Planner](skills/international-paid-expansion-planner/) | Plans an international PPC and paid social expansion. |  |
| [Multi-Platform Paid Media Audit](skills/multi-platform-paid-audit/) | Audits every ad platform a business runs in one pass and returns one paid media scorecard. |  |
| [Native Ads Manager (Taboola, Outbrain)](skills/native-ads-manager/) | Plans and reviews native ads on Taboola, Outbrain and similar content-recommendation networks from the network's own exports. |  |
| [Newsletter and Podcast Ads Planner](skills/newsletter-podcast-ads-planner/) | Plans and judges paid ads in other people's newsletters and podcasts. |  |
| [Paid Ads Benchmark Check](skills/paid-ads-benchmark-check/) | Answers "are my ad numbers good?" for Google Ads, Meta (Facebook and Instagram), LinkedIn, TikTok, Microsoft Ads, Pinterest, Snapchat and X. |  |
| [Paid Media Plan Builder](skills/media-plan-builder/) | Builds a paid media plan from a brief for a launch, a new budget or a campaign flight. |  |
| [Programmatic Display and Video Planner](skills/programmatic-display-planner/) | Plans a programmatic display and video campaign bought through a DSP, then reviews it once it runs. |  |
| [Software Directory Ads Planner](skills/software-marketplace-ads-planner/) | Plans and reviews paid placements on software review sites and app marketplaces, including Capterra PPC (and its sister site GetApp), G2 sponsored listings and G2… |  |
| [Spotify and Streaming Audio Ads Planner](skills/streaming-audio-ads-planner/) | Plans and reads out Spotify and streaming audio ad buys (Spotify Ads Manager music and podcast ad sets, streaming radio sellers, programmatic audio through a DSP). |  |

### Playbooks

Full-funnel advertising playbooks for e-commerce brands.

| Skill | What it does | |
|---|---|---|
| [App Growth Audit](skills/app-growth-audit/) | Audits a mobile app's growth on live public data through the InsightfulPipe MCP, and writes its store listing. |  |
| [B2B Lead Generation Audit](skills/b2b-lead-gen-audit/) | Audits a lead generation business end to end on live data through the InsightfulPipe MCP, for B2B companies, real estate agents and law firms. |  |
| [Ecommerce Ads Playbook](skills/ecommerce-ads-playbook/) | E-commerce growth skill with two modes. | [Page](https://insightfulpipe.com/marketing-claude-skills/playbooks/ecommerce-ads-playbook) |
| [Vertical Growth Audit](skills/vertical-growth-audit/) | Runs a growth audit for one business in one vertical (travel and booking, events and tickets, education and courses, two-sided marketplaces, mobile games, nonprofits… |  |

### PR & Partnerships

Press releases, media pitches, press kits, coverage reports, events, sponsorships and crisis communications.

| Skill | What it does | |
|---|---|---|
| [Analyst Relations Planner](skills/analyst-relations-planner/) | Plans industry analyst relations for a B2B tech company. |  |
| [Award Entry Writer](skills/award-entry-writer/) | Picks the marketing, industry and business awards worth entering and writes the award submission. |  |
| [Brand Impersonation Response](skills/brand-impersonation-response/) | Finds and responds to brand impersonation (scam ads, lookalike domains, fake sites in brand search and fake social profiles using a brand's name or logo). |  |
| [Conference Speaker Proposal Writer](skills/speaker-proposal-writer/) | Gets a founder or expert booked to speak at conferences. |  |
| [Crisis Communications Plan](skills/crisis-comms-plan/) | Writes a crisis communications plan before anything goes wrong, sized to the business. |  |
| [Crisis Response Kit](skills/crisis-response-kit/) | Handles a PR crisis that is happening now. |  |
| [Event and Sponsorship ROI Calculator](skills/event-sponsorship-roi/) | Event ROI calculator and sponsorship planner. |  |
| [Event and Trade Show Marketing Plan](skills/event-marketing-plan/) | Builds a dated marketing plan for one in-person event (a trade show stand, a customer day the business hosts, or a dinner or roundtable for target accounts). |  |
| [Gift Guide and Product Seeding Planner](skills/gift-guide-seeding-planner/) | Plans product seeding and gift guide PR for an online store. |  |
| [Media Interview Prep](skills/spokesperson-interview-prep/) | Prepares a spokesperson for one specific media interview, podcast, panel or broadcast. |  |
| [Media List Builder](skills/media-list-builder/) | Builds a media list for one story from what writers actually published. |  |
| [Media Monitoring and PR Report](skills/pr-coverage-report/) | Media monitoring and PR measurement in one skill. |  |
| [Media Pitch Writer](skills/media-pitch-writer/) | Writes a personal media pitch for each journalist, editor or producer on a list, for one story, with two subject lines each. |  |
| [Newsjacking and Reactive PR Finder](skills/newsjacking-angle-finder/) | Finds news stories and trends a brand can credibly comment on within hours (reactive PR, newsjacking) and drafts the response. |  |
| [Podcast Guesting Planner](skills/podcast-guest-pitching/) | Gets a founder or expert booked as a guest on other people's podcasts. |  |
| [PR Strategy Plan Builder](skills/pr-strategy-plan/) | Builds a 6 or 12 month public relations strategy and PR plan from the company's own evidence. |  |
| [Press Kit Builder](skills/press-kit-builder/) | Builds a company press kit and newsroom page, or audits the press page a company already has. |  |
| [Press Release Writer](skills/press-release-writer/) | Writes a press release for one piece of news (a product launch, funding round, partnership, hire, milestone, award or data story) or a media advisory for an event, from… |  |
| [Sponsorship Proposal Writer](skills/sponsorship-proposal-writer/) | Writes a sponsorship proposal, sponsorship deck and sponsor outreach for an event, nonprofit, club, conference or show, priced from the audience the user can prove. |  |

### SEO

Keyword research, content decay, cannibalization, briefs, schema, internal links and AI search visibility on live Search Console and SEO data.

| Skill | What it does | |
|---|---|---|
| [AI Answer Source Placement Planner](skills/ai-answer-source-placement/) | Plans LLM seeding from evidence. |  |
| [Ai Search Visibility](skills/ai-search-visibility/) | Tracks how visible a website is in AI search on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/ai-search-visibility) |
| [AI Shopping Visibility Audit (ChatGPT Shopping SEO)](skills/ai-shopping-visibility/) | Checks whether a store's own products are named when shoppers ask ChatGPT, Google AI Overviews, Perplexity and other assistants what to buy, and finds the data reason… |  |
| [Backlink Auditor and Outreach Planner](skills/backlink-auditor/) | Audits a site's backlink profile on live data through the InsightfulPipe MCP. |  |
| [Bing Webmaster SEO Analyst](skills/bing-seo-analyst/) | Analyses a site's Bing search performance on live Bing Webmaster Tools data through the InsightfulPipe MCP. |  |
| [Brand SERP and Knowledge Panel Optimizer](skills/brand-serp-knowledge-panel/) | Audits and improves the brand SERP, the page people see when they search a company or founder name. |  |
| [Competitor Keyword and Content Gap](skills/competitor-keyword-gap/) | Finds the keywords and topics your competitors rank for and you don't, on live data through the InsightfulPipe MCP. |  |
| [Content Brief Writer](skills/content-brief-writer/) | Writes an SEO content brief for one target keyword from the live Google top 10, through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/content-brief-writer) |
| [Content Decay Refresh](skills/content-decay-refresh/) | Finds the pages losing Google clicks on live Search Console data through the InsightfulPipe MCP, works out why each one is falling (lost rank, lower click-through… | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/content-decay-refresh) |
| [Core Web Vitals Fixer](skills/core-web-vitals-fixer/) | Finds and fixes Core Web Vitals problems on live data through the InsightfulPipe MCP. |  |
| [Digital PR Link Campaign Planner](skills/digital-pr-link-campaign/) | Plans a digital PR campaign that earns links from news sites. |  |
| [Ecommerce SEO Auditor](skills/ecommerce-seo-auditor/) | Runs an ecommerce SEO audit of an online store on Shopify, WooCommerce, Magento or a custom cart. |  |
| [GitHub README Optimizer](skills/repo-readme-optimizer/) | Writes or audits the README and repo details (About line, website field, topics, social preview) of a product, open-source tool, SDK, plugin or MCP server so the repo… |  |
| [Google Discover and News SEO Optimizer](skills/news-discover-seo/) | Google Discover and Google News SEO optimizer for publishers, media sites and large blogs. |  |
| [Google Penalty Recovery Planner](skills/penalty-recovery/) | Works out why a site lost Google visibility and plans the way back. |  |
| [Image SEO and Alt Text Generator](skills/image-seo-alt-text/) | Image SEO audit and alt text generator. |  |
| [Indexing and Sitemap Monitor](skills/indexing-monitor/) | Checks which pages Google and Bing have indexed, on live Search Console and Bing Webmaster data through the InsightfulPipe MCP. |  |
| [Internal Linking Planner](skills/internal-linking-planner/) | Plans internal links on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/internal-linking-planner) |
| [International SEO and Hreflang Planner](skills/international-seo-planner/) | Plans and audits international SEO for a multi-country or multi-language site. |  |
| [JavaScript SEO Rendering Check](skills/javascript-seo-rendering-check/) | Checks what search engines and AI crawlers can read on a JavaScript site. |  |
| [Keyword Cannibalization Fixer](skills/keyword-cannibalization-fixer/) | Finds keyword cannibalization on live Google Search Console data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/keyword-cannibalization-fixer) |
| [Keyword Research Clustering](skills/keyword-research-clustering/) | Researches keywords for a topic on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/keyword-research-clustering) |
| [On-Page SEO Optimizer](skills/on-page-seo-optimizer/) | Optimizes one existing page, or a finished draft before it goes live, for one target query. |  |
| [Rank and SERP Feature Tracker](skills/rank-tracker/) | Tracks where a site ranks on Google for its target keywords, on live data through the InsightfulPipe MCP. |  |
| [Schema Markup Generator](skills/schema-markup-generator/) | Audits and writes schema markup on live data through the InsightfulPipe MCP, or from pasted page source. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/schema-markup-generator) |
| [SEO Blog Writer](skills/seo-blog-writer/) | Writes an SEO blog post draft, or reworks an existing page so AI answers can quote it, from live data through the InsightfulPipe MCP. |  |
| [SEO Content Planner](skills/seo-content-planner/) | Builds a site's SEO content plan on live data through the InsightfulPipe MCP, runs a content audit, and turns customer questions into decision-stage content. |  |
| [SEO Forecast and ROI Calculator](skills/seo-forecast/) | Forecasts what an SEO plan will deliver and when it pays back. |  |
| [SEO Performance Report](skills/seo-performance-report/) | Builds an organic search performance report from live Google Search Console data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/seo-performance-report) |
| [SEO Roadmap Planner](skills/seo-roadmap-planner/) | Builds a 3, 6 and 12-month SEO strategy and roadmap from the site's own numbers. |  |
| [SEO Split Test Designer](skills/seo-split-test/) | Designs and reads SEO split tests (SEO A/B tests) on groups of similar pages, on live Google Search Console data through the InsightfulPipe MCP or on a pasted page list… |  |
| [Server Log and Crawl Budget Analyzer](skills/log-file-crawl-analyzer/) | Analyzes server and CDN access logs for SEO and crawl budget. |  |
| [Site Migration SEO Monitor](skills/site-migration-monitor/) | Protects organic traffic through a site migration or launch, on live data through the InsightfulPipe MCP or from pasted crawl exports and URL lists. |  |
| [Site Structure Planner](skills/site-structure-planner/) | Plans a website's structure for SEO from real search demand. |  |
| [Striking Distance Optimizer](skills/striking-distance-optimizer/) | Finds the Google searches a site almost wins and fixes the titles and meta descriptions that lose clicks. | [Page](https://insightfulpipe.com/marketing-claude-skills/seo/striking-distance-optimizer) |
| [XML Sitemap, Robots.txt and llms.txt Generator](skills/robots-llms-txt-builder/) | Writes and tests a site's robots.txt, XML sitemap (or sitemap index) and llms.txt. |  |

### Skill Orchestration

A routing skill that picks and sequences the other marketing skills.

| Skill | What it does | |
|---|---|---|
| [Orchestrator](skills/orchestrator/) | The router for the InsightfulPipe marketing skills. | [Page](https://insightfulpipe.com/marketing-claude-skills/meta/orchestrator) |

### Social Media

Organic social: page and channel analysis, posting plans, repurposing and influencer campaigns on live account data.

| Skill | What it does | |
|---|---|---|
| [Community Strategy Builder](skills/community-strategy-builder/) | Plans and scores a brand community on Slack, Discord, Circle, Telegram or a forum. |  |
| [Content Repurposer](skills/content-repurposer/) | Turns one blog post into a pack of ready-to-edit drafts, and turns a webinar, podcast, video or interview transcript into a blog article, through the InsightfulPipe MCP. |  |
| [Creator Program Builder](skills/creator-program-builder/) | Builds an always-on creator program from the creators a brand has already paid. |  |
| [Customer UGC Strategy Planner](skills/customer-ugc-program/) | Builds a user-generated content strategy for earned, unpaid customer photos and videos. |  |
| [Employee Advocacy Program Planner](skills/employee-advocacy-program/) | Plans, launches and runs an employee advocacy program on LinkedIn and X. |  |
| [Engagement Rate Calculator](skills/engagement-rate-calculator/) | Calculates social media engagement rate for an account, a single post or a creator in every common way (by reach, by views, by impressions, by followers, per post and… |  |
| [Facebook Page Analyst](skills/facebook-page-analyst/) | Analyses an organic Facebook Page on live data through the InsightfulPipe MCP. |  |
| [Influencer Campaign Manager](skills/influencer-campaign-manager/) | Plans and measures influencer campaigns, on live data through the InsightfulPipe MCP or from what you paste. |  |
| [Influencer Rate Calculator and Contract Terms](skills/influencer-rates-and-contract/) | Sets a fair fee for an influencer or creator deal and writes the deal terms. |  |
| [Influencer Vetting and Fake Follower Checker](skills/influencer-vetting/) | Vets Instagram, TikTok and YouTube creators before a deal and works as a fake follower checker. |  |
| [Instagram DM Automation Designer](skills/dm-automation-flow-designer/) | Designs comment-to-DM automation flows for Instagram, Facebook Messenger and X. |  |
| [Instagram Growth Analyst](skills/instagram-growth-analyst/) | Builds a monthly Instagram analytics report for a business or creator account from live insights through the InsightfulPipe MCP, or from a Meta Business Suite export… |  |
| [LinkedIn Newsletter Planner](skills/linkedin-newsletter/) | Plans and writes a LinkedIn newsletter for a company Page or a founder's profile. |  |
| [LinkedIn Page Analyst](skills/linkedin-page-analyst/) | Analyses a LinkedIn company page on live data through the InsightfulPipe MCP, or from the page's analytics exports. |  |
| [Live Stream Marketing Planner](skills/social-live-stream-planner/) | Plans a brand live stream or live audio session on YouTube Live, TikTok LIVE, Instagram Live, Facebook Live, LinkedIn Live or X Spaces from topic to replay. |  |
| [Long Video to Shorts Clip Finder](skills/video-to-shorts-clip-finder/) | Turns a long video, webinar, podcast recording or livestream into 5 to 10 short clips for YouTube Shorts, Instagram Reels, TikTok, LinkedIn, Facebook Reels and X. |  |
| [Pinterest Organic Manager](skills/pinterest-organic-manager/) | Manages an organic Pinterest business account on live data through the InsightfulPipe MCP. |  |
| [Reddit and Forum Marketing Planner](skills/reddit-marketing-planner/) | Plans organic Reddit marketing for a brand, plus Quora, Hacker News and niche forums. |  |
| [Social Listening and Share of Voice Report](skills/social-listening-monitor/) | Runs a weekly social listening report for a brand. |  |
| [Social Media Audit](skills/social-media-audit/) | Runs a social media audit across every profile a brand runs, in one pass. |  |
| [Social Media Competitor Benchmark](skills/social-competitor-benchmark/) | Runs a social media competitor analysis that compares your accounts with up to five named rivals on each network (Instagram, Facebook, LinkedIn, YouTube, X, TikTok… |  |
| [Social Media Giveaway Planner](skills/social-giveaway-planner/) | Plans, draws and measures a brand-run social media giveaway or contest on Instagram, Facebook, TikTok or X. |  |
| [Social Media Policy Writer](skills/social-media-policy/) | Writes a complete social media policy pack for a business: employee social media guidelines, public community guidelines with the moderation rules behind them, a post… |  |
| [Social Media ROI Analyst](skills/social-media-roi/) | Works out the ROI of organic social media in money, per network. |  |
| [Social Media Trend Finder](skills/social-trend-scout/) | Finds this week's social media trends in a brand's niche and says which ones to act on. |  |
| [Social Reach Drop Diagnostic](skills/social-reach-drop-diagnostic/) | Explains a sudden fall in reach, views or followers on Instagram, TikTok, Facebook, LinkedIn, X or YouTube. |  |
| [TikTok and Instagram SEO Optimizer](skills/social-search-optimizer/) | TikTok SEO and Instagram SEO for short videos and profiles. |  |
| [TikTok Organic Analyst](skills/tiktok-organic-analyst/) | Analyses an organic TikTok account on live data through the InsightfulPipe MCP. |  |
| [Video Content Program Planner](skills/video-marketing-strategy/) | Plans an organic video marketing strategy across YouTube (long-form and Shorts), Instagram Reels, TikTok, Facebook and LinkedIn from the account's own results. |  |
| [X (Twitter) Organic Analyst](skills/x-organic-analyst/) | Analyses an X (Twitter) account's own organic posts, replies and audience, from the X analytics CSV export or pasted posts, or live through the InsightfulPipe X Organic… |  |
| [YouTube Channel Analyst](skills/youtube-channel-analyst/) | Runs a monthly YouTube channel review on live data through the InsightfulPipe MCP, covering views, watch time, retention curves, Shorts versus long-form, which videos… |  |
| [YouTube SEO Optimizer](skills/youtube-seo-optimizer/) | Audits and rewrites YouTube video titles, descriptions, chapters and tags on live data through the InsightfulPipe MCP. |  |
| [YouTube Video Idea Finder](skills/youtube-topic-finder/) | Finds YouTube video ideas with proven demand and beatable competition, and plans a channel's next quarter from them. |  |
| [YouTube Video Script Writer](skills/youtube-script-writer/) | Writes long-form YouTube video scripts and their Shorts cut-downs around the points where your own channel's viewers leave. |  |

### Social Media Ads

Paid social creative ranking and UGC creator briefs.

| Skill | What it does | |
|---|---|---|
| [Meta Ads Creative Ranker](skills/meta-ads-creative-ranker/) | Ranks Meta (Facebook and Instagram) ads by what they actually deliver, on live data through the InsightfulPipe MCP or from a pasted Ads Manager export. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/meta-ads-creative-ranker) |
| [Pinterest Ads Manager](skills/pinterest-ads-manager/) | Reviews and manages a Pinterest Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/pinterest-ads-manager) |
| [Reddit Ads Manager](skills/reddit-ads-manager/) | Sets up and reviews Reddit Ads from Reddit Ads Manager exports. |  |
| [Snapchat Ads Manager](skills/snapchat-ads-manager/) | Reviews and manages a Snapchat Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/snapchat-ads-manager) |
| [UGC Brief Generator](skills/ugc-brief-generator/) | Writes UGC creator briefs and timed video ad scripts from the hooks and ads that actually worked in your Meta (and TikTok) account, pulled live through the… | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/ugc-brief-generator) |
| [X Ads Manager](skills/x-ads-manager/) | Reviews and manages an X (Twitter) Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/social-media-ads/x-ads-manager) |

### Strategy

Launches, pricing, referral programs, free tools and privacy-first targeting.

| Skill | What it does | |
|---|---|---|
| [Brand Architecture Planner](skills/brand-architecture/) | Plans brand architecture from measured brand equity. |  |
| [Brand Health and Share of Search Tracker](skills/brand-health-tracker/) | Tracks brand health month by month and runs a one-off brand audit. |  |
| [Brand Positioning Builder](skills/brand-positioning-builder/) | Builds brand positioning from live evidence through the InsightfulPipe MCP. |  |
| [Customer Journey Map](skills/customer-journey-map/) | Builds a customer journey map from how customers really behave, from first hearing of the business to buying, coming back and recommending it. |  |
| [Customer Survey Builder and Analyzer](skills/survey-design-analysis/) | Designs a customer survey around one decision and analyses the answers with real statistics. |  |
| [First 100 Customers Plan](skills/first-customers-plan/) | Plans how a product that has not sold yet wins its first paying customers, and the road to the first 100. |  |
| [Five Forces, PESTLE and Ansoff Analysis](skills/strategy-frameworks/) | Runs Porter's Five Forces, a PESTLE analysis and an Ansoff growth matrix on one real market for a business, and ends each framework with what it changes in the… |  |
| [Free Tool Strategy](skills/free-tool-strategy/) | Plans a free marketing tool or lead magnet (calculator, generator, checker, quiz, template, checklist) on live data through the InsightfulPipe MCP, and audits the ones… | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/free-tool-strategy) |
| [Holiday Campaign Planner](skills/holiday-campaign-planner/) | Plans a holiday or seasonal campaign (Black Friday, Cyber Monday, December, the Christmas lull, or any season named) from last year's history, pulled through the… |  |
| [Integrated Campaign Planner](skills/integrated-campaign-planner/) | Plans one integrated marketing campaign across every channel a business uses (ads, its own site, email and social accounts, press and creators), sized from the… |  |
| [Launch Strategy](skills/launch-strategy/) | Plans a product, feature, book, webinar or promotion launch from the business's own live data through the InsightfulPipe MCP, or from numbers the user gives. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/launch-strategy) |
| [Market and Trend Research](skills/market-research/) | Researches a market, an industry or a product category on live public data through the InsightfulPipe MCP (search demand, five-year and weekly trends, rising and early… |  |
| [Market Entry Strategy Planner](skills/market-entry-plan/) | Builds a market entry strategy for one country or region that has already been chosen, for software, service and B2B businesses. |  |
| [Market Sizing (TAM, SAM, SOM)](skills/market-sizing/) | Calculates market size as TAM, SAM and SOM three ways and shows the math. |  |
| [Marketing Audit and Scorecard](skills/marketing-audit/) | Runs a full marketing audit of a business in one pass and returns a scorecard for ten areas (positioning and customer, offer and pricing, measurement, channel mix… |  |
| [Marketing Ideas Generator](skills/marketing-ideas-generator/) | Generates a long list of marketing ideas for one specific business (channels, campaigns, partnerships, content, offers and low-budget tactics), drops the ones that… |  |
| [Marketing Plan Builder](skills/marketing-plan-builder/) | Builds a marketing plan from the channels you actually run, reading GA4, Search Console, Google Ads, Meta, LinkedIn Ads, Klaviyo and YouTube through the InsightfulPipe… | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/marketing-plan-builder) |
| [Pricing Research and Price Elasticity Analyzer](skills/pricing-research-survey/) | Designs and analyses willingness-to-pay research and calculates price elasticity from real sales. |  |
| [Pricing Strategy](skills/pricing-strategy/) | Builds a pricing strategy on live market data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/pricing-strategy) |
| [Privacy First Targeting Strategist](skills/privacy-first-targeting-strategist/) | Builds an advertising plan for a world with less tracking from your live accounts through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/privacy-first-targeting-strategist) |
| [Product Idea Validation Plan](skills/idea-validation-plan/) | Tests whether a new product, offer or feature has demand before anyone builds it. |  |
| [Product-Market Fit Assessment](skills/product-market-fit-assessment/) | Measures how close a product is to product-market fit by combining the Sean Ellis survey with behaviour. |  |
| [Rebrand Planner: Rebranding Strategy and Checklist](skills/rebrand-planner/) | Plans a rebrand from the decision to the weeks after launch. |  |
| [Referral Program](skills/referral-program/) | Designs, grows and audits customer referral, affiliate and partner programs from the business's own data through the InsightfulPipe MCP or from pasted data. | [Page](https://insightfulpipe.com/marketing-claude-skills/strategy/referral-program) |
| [Win-Loss Analysis](skills/win-loss-analysis/) | Runs a win-loss analysis. |  |

### TikTok Ads

Creative, hook and audience analysis for TikTok Ads.

| Skill | What it does | |
|---|---|---|
| [TikTok Ads Analyzer](skills/tiktok-ads-analyzer/) | Analyzes a TikTok Ads account on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/tiktok-ads/tiktok-ads-analyzer) |
| [TikTok Ads Campaign Builder](skills/tiktok-ads-campaign-builder/) | Builds and runs TikTok Ads campaigns on live data through the InsightfulPipe MCP. | [Page](https://insightfulpipe.com/marketing-claude-skills/tiktok-ads/tiktok-ads-campaign-builder) |
| [TikTok Competitor Ads Research](skills/tiktok-competitor-ads-research/) | Researches competitors' TikTok ads in the TikTok Ad Library and the top ads in a category in TikTok Creative Center Top Ads, through the InsightfulPipe MCP or from… |  |
| [TikTok Spark Ads Planner](skills/tiktok-spark-ads-planner/) | Plans TikTok Spark Ads from posts that already earned attention. |  |

<!-- SKILLS:END -->

Every reviewed skill is added here as soon as it passes review, and its page on insightfulpipe.com follows. This repository syncs with the site twice a day.

## License

[MIT](LICENSE). Running the skills on live data needs an InsightfulPipe account.
