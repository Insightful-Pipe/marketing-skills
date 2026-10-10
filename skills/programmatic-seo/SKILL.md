---
name: programmatic-seo
description: Plans programmatic SEO pages (one template filled from data, one page per variable such as a city, trade, integration or competitor) on live data through the InsightfulPipe MCP. Finds the search pattern, measures demand for every permutation, reads the SERPs, tears down the sites already ranking with the same kind of page, checks your own Search Console, then gives a build or don't-build verdict and a page template with the data field behind every section. Use when someone mentions programmatic SEO, pSEO, template pages, location pages, comparison or alternatives pages at scale, integration pages, "[x] for [y]" pages, keyword permutations or building hundreds of pages, or asks why existing template pages don't rank or index.
---

# Programmatic SEO

Programmatic SEO is one page template filled from a dataset, one page per value of a variable: "{trade} invoice template", "coworking in {city}", "{tool} alternatives". It works when three things are true: people search the pattern, each page carries data the others don't, and the site can beat what already ranks. This skill measures all three on live data before anyone builds a page, then writes the template.

Most programmatic projects fail in one of two ways: pages for searches nobody makes, or pages that differ only by the swapped word. Google's spam policies call the second one scaled content abuse, and many near-identical pages aimed at slightly different queries count as doorway pages. Every check below exists to catch one of these two.

## Before you start

You need the InsightfulPipe MCP with DataForSEO connected. Search Console is optional and adds step 5.

1. Call `query_contexts` with `request="accounts"` for `platform="dataforseo"` and, if the user has a site, `platform="google-search-console"`. Note `workspace_id`, `brand_id` and the Search Console `site_url`. If several properties are listed, ask which site the pages will live on.
2. Call `query_contexts` with `request="actions_details"` for the actions below and follow the body shapes it returns:
   - dataforseo: `labs_keyword_suggestions`, `kw_google_ads_search_volume`, `serp_google_organic`, `labs_ranked_keywords`, `onpage_instant_pages`, `onpage_content_parsing`
   - google-search-console: `search_analytics`, `batch_url_inspection`
3. Ask the user, and use the defaults when they don't know:
   - **The head term** (what every page is about, e.g. "invoice template") and **the variable list** (every trade, city or tool they could make a page for). Default: no list; step 1 finds the variables people search.
   - **The data they own per variable.** This decides whether the pages can be different (see "The data ladder"). There is no default: ask until you have an answer.
   - **The business goal:** what a visitor should do on the page, and the conversion rate for that goal if they know it (for the success metrics). Default: no rate; the conversion target is left to them.
   - **Country and language.** Default `location_code` 2840 (United States), `language_code` "en".

DataForSEO bills per call. One run is about 11 calls (1 + 1 + 3 + 2 + 4). Tell the user before going past 15.

## How to run the calls

Every call goes through `query_data` with the `platform` and `action` named in the step. Rules the API enforces:
- Send `location_code` or `location_name`, never both; the same for `language_code` and `language_name`.
- `labs_keyword_suggestions` takes one `keyword` string. `kw_google_ads_search_volume` takes a `keywords` array of up to 700.
- `filters` are arrays like `[["keyword_info.search_volume", ">", 0]]`. The `like` operator takes `%` wildcards.
- `serp_google_organic` returns a flat list of SERP items. Read the `organic` items for rankings, and `people_also_ask` and `related_searches` for questions and sub-modifiers.
- Search Console `ctr` comes back as a percentage (1.56 means 1.56%).

If a call fails, keep going: mark that check **unknown**, say which call failed, and never fill the gap with a guess.

## The steps

### 1. Find the pattern

```json
{"platform": "dataforseo", "action": "labs_keyword_suggestions", "keyword": "invoice template",
 "location_code": 2840, "language_code": "en", "limit": 1000,
 "filters": [["keyword_info.search_volume", ">", 0]], "order_by": ["keyword_info.search_volume,desc"]}
```

- **Count each search once.** Google groups close variants ("template for invoice", "invoice template", "invoice billing template") under one volume, and the rows repeat it. Group rows by `keyword_properties.core_keyword` and keep one volume per group. Never add up rows that share a core keyword.
- **Sort the modifiers into classes:** remove the head term and filler words (for, a, of, free, sample, template) and look at what is left. Typical classes: a format (word, excel, pdf), a segment (a trade, an industry, a city), a brand (a competitor or a tool), a document type. Each class is a possible pattern. For each class give the number of values found and the volume of its biggest value.
- **Keep the limit at 1000.** The list is sorted by volume, so segment modifiers sit lower down. In testing, the first 200 rows of a broad head term held almost only format modifiers; the industry modifiers began further down.
- Pick the class that matches what the business can fill with real data. Mention a bigger class you're not building, so the user can decide.

### 2. Test every permutation

Build one keyword per variable in the main word order, plus the other order when people use both. Run them in one call:

```json
{"platform": "dataforseo", "action": "kw_google_ads_search_volume",
 "keywords": ["plumbing invoice template", "invoice template for plumbing", "tutoring invoice template"],
 "location_code": 2840, "language_code": "en"}
```

- **Two word orders are one page.** The other order usually comes back with the same volume (grouped) or with none: in testing, 20 of 40 came back the same, 19 empty and 1 lower. Use the higher of the two per variable, never the sum.
- **Demand:** the total monthly volume across variables, and the share of variables with any measured volume.
- **Spread:** the share of total demand held by the top 10 variables. A head-heavy pattern needs only a few pages.
- **Phases:** phase 1 is the smallest set of variables, highest volume first, that reaches 80% of the total. Phase 2 is the rest with at least 50 searches a month. Below 50, don't build a standalone page: fold the variable into a parent page, or wait until your own Search Console shows impressions for it.
- **Commercial value:** report the CPC range across variables. A high CPC means advertisers pay for these visitors, which is evidence the traffic converts.

### 3. Read the SERPs

Run `serp_google_organic` for 3 variables you would build: the biggest, one from the lower half of phase 1, and one from phase 2. Don't sample the hold list: those variables get no page, so their SERPs can't change what you build.

```json
{"platform": "dataforseo", "action": "serp_google_organic", "keyword": "plumbing invoice template",
 "location_code": 2840, "language_code": "en", "depth": 10}
```

Sort each organic result into one type:
- **Template page:** a page about this one variable, with the variable in its URL slug (`/invoice-templates/plumbing`, `/plumbing-invoice-template`). These are your direct rivals.
- **Platform or user content:** social, video, document-sharing and marketplace sites (Pinterest, YouTube, Scribd, Reddit, marketplaces). These rank on weak SERPs and are the easiest to pass.
- **Article:** a blog post, guide or resource page (a `/blog/`, `/resources/`, `/resource/`, `/stories/` or `/guides/` path), even when the variable is in its slug.
- **General page:** a page about the head term with no variable (a generic template gallery).

Then report:
- **Openness:** whether one rival domain (a template page or an article, not a platform) sits in the top 3 of several sampled SERPs. If one sits in all of them, the pattern is held: you need better data than theirs, not just more pages. A platform result in the top 3 is a weak result, so it makes a SERP more open, not less.
- **Weak results:** the number of platform or user-content results in each top 10. More of them on the phase 2 SERP means the smaller pages are easier.
- **Intent drift:** results whose titles answer a different need than the user's pages ("independent contractor" for a page about building contractors). Say which variables have it.
- **Sub-modifiers:** the `related_searches` items show what people add to each variable (formats, "free", "example"). These belong on the one page as sections or downloads, not as extra pages.
- **Questions:** the `people_also_ask` items are candidate FAQ entries and show which data a page needs (for example rate questions on a tutoring page call for rate data).

Do not use `labs_bulk_keyword_difficulty` to judge these patterns: on 40 long-tail permutations it returned 0 for 34 and nothing for 1, while the SERPs for the same keywords were full of established sites, so it says little here. Read the SERPs instead.

### 4. Tear down the incumbent

Pick the best-ranked template page on each of the first two SERPs. Their domains are the incumbents. For each, see how big its template folder is:

```json
{"platform": "dataforseo", "action": "labs_ranked_keywords", "target": "invoicefly.com",
 "location_code": 2840, "language_code": "en", "limit": 300,
 "filters": [["ranked_serp_element.serp_item.relative_url", "like", "/free-resources/free-templates/free-invoice-templates/%"]],
 "order_by": ["ranked_serp_element.serp_item.etv,desc"]}
```

- Report `total_count` (keywords the folder ranks for), the number of distinct URLs in the rows, and the estimated monthly traffic (`etv`) per page type: the hub, segment pages and any other class (format pages, for example). Say that `etv` is an estimate and that it covers only the rows returned.
- This sets expectations: if the incumbent's segment pages earn a few visits each while another page type earns hundreds, say so plainly.

Then open two sibling pages from the main incumbent's folder, for different variables:

```json
{"platform": "dataforseo", "action": "onpage_instant_pages",
 "url": "https://invoicefly.com/free-resources/free-templates/free-invoice-templates/plumbing-invoice-template/"}
```
```json
{"platform": "dataforseo", "action": "onpage_content_parsing",
 "url": "https://invoicefly.com/free-resources/free-templates/free-invoice-templates/plumbing-invoice-template/"}
```

- From `onpage_instant_pages` (`meta`): the title and description formulas, the H1 and H2 list (`htags`), word count (`content.plain_text_word_count`, navigation included), internal links, canonical, and whether there is any structured data (`checks.has_micromarkup`).
- From `onpage_content_parsing` (`page_content.main_topic` and `secondary_topic`, headings plus `primary_content` text): the shared text between the two pages. Lowercase both, replace the variable and its obvious forms ("plumbing", "plumber", "plumbers") with one placeholder, split into words, and compare 5-word sequences. **Shared text** is the share of the shorter page's sequences that also appear on the other page.
- A shared H2 skeleton is normal for a template. Shared body text is what makes pages thin. The incumbent's shared-text figure is the bar your pages have to meet.

### 5. Your site (if Search Console is connected)

Check whether the site already has pages or demand for the pattern. Use the last 28 complete days.

```json
{"platform": "google-search-console", "action": "search_analytics", "site_url": "https://example.com/",
 "dimensions": ["page"], "start_date": "2026-09-06", "end_date": "2026-10-03", "row_limit": 1000,
 "dimension_filter_groups": [{"filters": [{"dimension": "page", "operator": "contains", "expression": "/invoice-templates/"}]}]}
```
```json
{"platform": "google-search-console", "action": "search_analytics", "site_url": "https://example.com/",
 "dimensions": ["query", "page"], "start_date": "2026-09-06", "end_date": "2026-10-03", "row_limit": 1000,
 "dimension_filter_groups": [{"filters": [{"dimension": "query", "operator": "includingRegex", "expression": "invoice template"}]}]}
```

- Existing pages in the folder: impressions, clicks and position per page. A variable that already earns impressions moves into phase 1 whatever its volume.
- Queries for the pattern that land on a non-template page: the new page must take over that query, so link the old page to it.
- **Indexing of pages that already exist:** inspect up to 50 of them in one call.

```json
{"platform": "google-search-console", "action": "batch_url_inspection", "site_url": "https://example.com/",
 "urls": ["https://example.com/invoice-templates/plumbing", "https://example.com/invoice-templates/roofing"],
 "language_code": "en"}
```

  Count `coverage_state` = "Submitted and indexed" against the total. Don't read the indexed count from `sitemaps_list`: in testing it returned `indexed: 0` for a sitemap whose pages were indexed. The daily quota is 2,000 inspections per property.

Without Search Console, mark step 5 **not run** and say what it would have added.

## The verdict

Score each check **pass**, **warn**, **fail** or **unknown**. The thresholds are starting points; say so when the business makes one wrong.

| Check | Pass | Warn | Fail |
|---|---|---|---|
| Demand (step 2) | 60% or more of variables have measured volume, and the total is 1,000 a month or more | 30–60% have volume, or the total is under 1,000 | under 30% have volume: the demand is imagined |
| SERP openness (step 3) | no rival domain in the top 3 of 2 or more sampled SERPs | one rival domain in the top 3 of 2 of the 3 | one rival domain in the top 3 of all 3 |
| Data per page (user input) | a proprietary, product or user-generated field changes per page | only licensed or combined public data | only the variable's name and public facts change |
| Template uniqueness (step 4, then your draft) | shared text 30% or less | 30–50% | over 50%: a name swap |
| Business fit (steps 2 and 3, user input) | the visitor's need matches what the business sells, and the CPC shows paid demand | the need is near the offer | the page would attract people who can't buy |

Apply the decisions in this order; the first that matches wins:
- **Don't build** when Demand, Data per page or Business fit fails. No template change fixes missing searches, missing data or the wrong audience.
- **Fix first** when SERP openness or Template uniqueness fails (find data the incumbent can't match, or rewrite the template until the shared text is under the bar), or when two or more checks warn.
- **Build** when nothing fails and at most one check warns.
- An **unknown** check doesn't change the decision. Name it as a condition of the build (for example, Template uniqueness before any draft exists).
- Template uniqueness is checked twice: the bar from the incumbent, then your own draft once two pages exist (run `onpage_content_parsing` on both, or compare the drafts directly).
- Kill the idea outright when the pages could only swap the name, when the demand comes from guesses, when it takes thousands of pages to reach meaningful traffic, or when no person would be helped by landing on the page.

## The page template

Write the template as a spec the user's developer or CMS can fill:

1. **URL:** a subfolder, `/{folder}/{variable-slug}/`, lowercase with hyphens, no parameters, no IDs. Use a subfolder by default so the pages sit inside the site's existing structure.
2. **Title, meta description and H1 formulas,** each with the variable slot and the modifiers the SERP showed (formats, "free", "example"). Each must read naturally for the lowest-volume variable too.
3. **Sections, in order, each naming the data field that fills it.** At least 3 sections must come from fields that change per page. Add a condition to any section whose field can be empty (show the licence block only for trades that need a licence; show averages only when the sample behind them is big enough to be meaningful and to protect individual customers).
4. **Sub-modifiers on the page, not as pages.** Formats and variants from `related_searches` become download buttons or sections. A {variable} × {format} grid of pages is near-duplicate content.
5. **FAQ:** from `people_also_ask`, answered with the page's own data where possible.
6. **Internal links:** a hub page that links to every page; each page links to the hub and to 4–6 siblings in the same group; breadcrumbs. No orphan pages.
7. **Structured data:** BreadcrumbList on every page, plus the type that fits the playbook (see the table). FAQPage markup is valid, but Google now shows FAQ rich results only for a few authoritative government and health sites, so don't promise one.
8. **Indexing plan:** publish phase 1 only, in its own sitemap. After 4 weeks, inspect the phase 1 URLs (step 5). Publish phase 2 when 80% or more of phase 1 pages are indexed and earning impressions. Never publish a page you would have to noindex for being thin; don't build it.
9. **Uniqueness target:** shared text at or under 30% between any two pages, measured as in step 4, next to the incumbent's figure.
10. **Data refresh plan:** for each data field, where it comes from and how often it changes, and how the pages pick up the change (regenerate on that schedule and show a "data updated" date on the page). Pages built once and never refreshed drift out of date while their rivals update; this is the set-and-forget mistake.

## Before you publish

Check the first drafted pages on their final URLs, before they go into the sitemap or get linked. Run `onpage_instant_pages` on each (the same body as step 4; each call is billed) and compare:
- **Titles and meta descriptions are unique:** `meta.title` and `meta.description` differ on every page and read naturally for the smallest variable.
- **One H1:** `meta.htags.h1` holds exactly one heading, with the variable in it.
- **The canonical points to the page itself:** `meta.canonical` equals the page's own URL. A canonical to the hub or a sibling asks Google to index that page instead.
- **Structured data is present:** `checks.has_micromarkup` is true.
- **No empty sections:** no blank blocks, placeholders or "{field}" text where a data field was empty. The section's condition should have hidden it.
- **Shared text** is under the uniqueness target (`onpage_content_parsing` on two pages, as in step 4).
- **Robots.txt** doesn't disallow the folder: open `/robots.txt` and read its Disallow lines.
- **The phase sitemap** lists every phase 1 URL.

Once Google has crawled the pages, `batch_url_inspection` (step 5) confirms the rest per URL: `robots_txt_state` is "ALLOWED", `indexing_state` is "INDEXING_ALLOWED" (a noindex tag shows as "BLOCKED_BY_META_TAG"), `page_fetch_state` is "SUCCESSFUL", and `google_canonical` matches `user_canonical`.

## The 15 playbooks

Pick the one that fits the pattern from step 1. Each needs the data in its row, or it becomes a name swap.

| Playbook | Pattern | Each page needs | Schema |
|---|---|---|---|
| Location | {service} in {city} | local providers, local prices or rules, reviews, a map | LocalBusiness, Place |
| Comparison | {A} vs {B} | a real feature-by-feature table, pros and cons, who each fits | Product, Review |
| Alternatives | {competitor} alternatives | real alternatives including yours, why people switch, who each fits | ItemList |
| Integration | {your product} + {tool} | the integration must exist; setup steps and use cases | SoftwareApplication |
| Template | {type} template | a usable download in several formats, variations | CreativeWork |
| Calculator | {type} calculator | a working tool, the method explained | WebApplication |
| Statistics | {topic} statistics | sourced or original data, dated and updated | Dataset |
| How-to | how to {task} with {tool} | current steps, screenshots, common errors | HowTo is no longer shown as a rich result; use Article |
| Glossary | what is {term} | a clear definition, an example, related terms linked | DefinedTerm |
| Use case | {product} for {segment} | features and examples specific to that segment | Article |
| Pricing | {product} pricing | every tier, hidden costs, the date checked | Product, Offer |
| Roundup | best {category} | stated criteria, real testing, a visible date | ItemList, Review |
| Job and salary | {job} salary | sourced pay data by region and level | Occupation |
| Product feed | one page per product | unique descriptions, images, stock and price | Product, Offer |
| API reference | {endpoint} reference | tested examples, parameters, errors, version | TechArticle |

## The data ladder

What makes each page different, from hardest to copy to easiest:
1. **Proprietary data** you create (your own research, benchmarks).
2. **Product data** from your users, aggregated ("median days to get paid, by trade").
3. **User content** (reviews, questions, submissions).
4. **Licensed data** others can't easily get.
5. **Public data combined** and analysed in a new way.
6. **Raw public data** anyone can copy: the easiest to compete against and the hardest to rank with.

Pages built only on level 6 fail the "Data per page" check.

## After launch

- **Weekly:** the step 5 `search_analytics` call filtered on the folder: impressions, clicks and position per page, and the share of pages with any impressions.
- **Weekly crawl errors:** `batch_url_inspection` on up to 50 URLs per template, rotating through the folder. Any `page_fetch_state` other than "SUCCESSFUL" (not found, server error, soft 404) or a `robots_txt_state` of "DISALLOWED" is a crawl error to fix.
- **Weekly Core Web Vitals by template:** pages built from one template share their speed problems, so check one or two URLs per template rather than every page. The Search Console API doesn't return the Core Web Vitals report: read it in Search Console, where it groups similar URLs, or use the **core-web-vitals-fixer** skill, if installed.
- **At 4 weeks and after every phase:** `batch_url_inspection` on the new URLs; report the indexed share and the most common `coverage_state` for the rest ("Crawled - currently not indexed" on many pages is the classic thin-content signal).
- **Refresh:** regenerate each field on the schedule in the data refresh plan, and re-run step 3 on the sampled SERPs every few months for new questions and sub-modifiers.
- **Prune:** a page with no impressions after 3 months gets better data, gets merged into a sibling, or is removed with a redirect.

## Programmatic pages and paid search

- The CPCs from step 2 show which variables advertisers pay for. Pages for high-CPC variables are good landing pages for search ads too; match the ad headline to the page H1.
- Before sending ad traffic, make sure the page's call to action records a conversion (**conversion-tracking-auditor**, if installed, checks this). Then A/B test where the call to action sits: paid visitors arrive with one intent, so test a version with the call to action above the fold.
- Paid keywords that convert are good candidates for new variables. Organic pages ranking 4–10 for a valuable variable are worth supporting with ads while they climb.

## Report format

1. **Header:** the head term, the pattern, the country, the date and the number of paid calls.
2. **Verdict:** build, fix first or don't build, with the five checks in a table (result, key number, one sentence).
3. **Demand:** total, share of variables with volume, top-10 share, CPC range, and the phase list (variable, keyword, volume, CPC).
4. **The SERPs:** per sampled keyword, the result types, openness, weak results, intent drift, sub-modifiers and questions.
5. **The incumbent:** folder size, traffic by page type, the page skeleton, and the shared-text bar.
6. **Your site:** step 5 results, or "not run" and why.
7. **The template:** the spec from "The page template", with its data refresh plan and the "Before you publish" checks.
8. **Success metrics:**
   - **Indexed pages:** 80% or more of each published phase indexed 4 weeks after it goes live. This is also the gate for the next phase.
   - **Traffic at 6 months:** the main incumbent's estimated traffic per page of the same type (step 4), times the pages you plan to have live by month 6. Call it a benchmark built on an estimate, not a forecast.
   - **Conversions:** the traffic benchmark times the user's own conversion rate for the page's goal. If the user has no rate, leave this target for them to set; never assume one.
9. **Risks and how the plan handles them:** thin content (the uniqueness target and when it's measured), quality control (the "Before you publish" checks), intent drift from step 3, data too thin for small variables (the section conditions), stale data (the refresh plan), and the monitoring plan from "After launch".
10. **What's not known,** and why.

## Fixes this skill can run

Only after the user confirms the exact change:
- **Save the page matrix to Google Sheets** (one row per variable: keyword, volume, CPC, phase, URL, title, H1). Create a tab with `create_sheet` (`spreadsheet_id`, `title`), then write the rows with `update_cells` (`spreadsheet_id`, `sheet_id` from the first call, `range`, `values` as a list of rows). Both need a Read & Write connection, and an owner, admin or operator can switch them off.

It never publishes pages and never changes the site.

## If a platform isn't connected

- **No DataForSEO:** ask the user to export, from any keyword tool, the volume for every permutation and the top 10 results for 3 of them. Run steps 2 to 4 on the export, and mark the incumbent teardown as manual.
- **No Search Console:** skip step 5 and say so.

## Go deeper

If installed: **keyword-research-clustering** for the wider topic around the pattern, **content-brief-writer** for the hub page, **internal-linking-planner** for the link map, **schema-markup-generator** for the markup, and **seo-audit** to audit the pages after launch.

## Rules

- Every number in the report comes from a call in this run. Name the call next to it.
- Count a close-variant group once. Never add up volumes of word-order variants.
- Never call a pattern viable because a keyword tool scored it easy; read the SERPs.
- Never build a page for a {variable} × {sub-modifier} grid; put sub-modifiers on the page.
- Never write a section whose only difference between pages is the variable's name.
- Name businesses in SERP findings, never private individuals.
- Say where the data is thin, and mark checks you couldn't run as unknown.
