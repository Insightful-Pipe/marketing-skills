---
name: newsletter
description: Writes email newsletters from what you actually published and what your readers actually clicked. Pulls the month's posts, their traffic (GA4, Search Console or public search estimates) and past issue results (Klaviyo or Mailchimp) through the InsightfulPipe MCP, picks the lead story and supporting items by a stated rule, and drafts the issue in one of nine formats with subject lines, preview text, tagged links and checks. Also generates issue ideas, reviews a sent issue, plans cross-promotion, turns posts into an email course, and plans a new newsletter's launch (promise, format, cadence, platform, targets) and revenue (sponsor slots priced from its own delivered and unique clicks, a media kit, a paid tier, affiliates). Use for a newsletter, a weekly or monthly roundup, newsletter ideas, a review, growth or swaps, an email course, starting a newsletter, monetizing one, or getting sponsors. Saves a draft campaign only after the user confirms; it never sends.
---

# Newsletter

A newsletter is a promise: something worth opening, on a schedule. This skill keeps the promise with evidence. It reads what you published, what people read and what past issues got clicked, then writes the issue around that. Every item it features has a reason you can see, and every fact in the copy comes from a page it read.

## Before you start

You need the InsightfulPipe MCP. The more of these are connected, the better the picks, but none is required:

| Source | What it adds | Platform |
|---|---|---|
| Google Analytics 4 | which posts people read and stayed on | `google-analytics` |
| Search Console | which posts pull search clicks | `google-search-console` |
| Klaviyo or Mailchimp | what past issues got clicked, and where to save the draft | `klaviyo`, `mailchimp` |
| SEO crawler | reads the blog index and the posts | `crawler` (built in) |
| DataForSEO (added to the MCP; bills per call) | public search estimates for a site you don't own, partner discovery, a backup page reader | `dataforseo` |

1. Call `query_contexts` with `request="accounts"` for each platform above. Note `workspace_id`, `brand_id`, the GA4 `property_id`, the Search Console `site_url`, and which email platform is connected. If there are several properties or sites, ask which one belongs to the blog.
2. Call `query_contexts` with `request="actions_details"` for every action you will use (listed in each step) and follow the body shapes it returns.
3. Ask for what the data can't tell you. Use the defaults when the user doesn't know:
   - **Newsletter name and audience.** Default: the blog's name; audience = people who read the blog.
   - **Goal.** What should a reader do: click to a post, reply, buy, share, or learn something. Default: click to the lead post.
   - **Cadence and window.** Default: monthly, window = the last full calendar month. Weekly: the last 7 complete days.
   - **Blog URL** (the index page that lists posts) and **voice** (two or three past issues or posts they like). Default voice: the blog's own.
   - **Topics that are off-audience** (for example hiring or engineering posts in a customer newsletter). Default: none; Claude flags likely ones and asks.
4. Pick the mode from the request: **issue** (default), **ideas**, **review**, **cross-promotion**, **email course** or **launch and sponsorship** (start a newsletter, or make money from one). One request can combine them.

## How to run the calls

Every read goes through `query_data` with the `platform` named in the step. Rules the APIs enforce:
- **Rate limits are shared.** On `rate_limit_exceeded`, wait `retry_after` seconds and retry. Don't fire calls in parallel.
- **An empty answer is not an error.** A Klaviyo account with no sends returns `success` with an empty list. Say "no history" and move on.
- **GA4 needs `properties/` before the id**, and filters use `dimensionFilter`. Drop rows whose title says "Not Found" or "404" and paths with stray characters: in testing, broken links to posts showed up as their own rows.
- **Search Console pages are full URLs**; GA4 paths are not. Join on the path.
- **Klaviyo campaigns need a channel filter** (`equals(messages.channel,'email')`), and status values are Title Case (`'Sent'`). Klaviyo reports carry `campaign_message_name`, not the subject line; ask the user for subjects if you need them.
- **Mailchimp calls in this skill are untested until a Mailchimp account is connected.** Their shapes come from the helper. Run `actions_details` first and adjust if a field name differs.
- **The crawler can fail.** On 2026-10-06 it returned `Error fetching URL` for every page during testing. When it does, read the pages with DataForSEO `onpage_content_parsing`, or read them directly, and say which you used.
- **More than one DataForSEO connection on the brand?** Add `"account_id"` (from `accounts`) to every DataForSEO body; without it the call is refused. `Payment Required` means that login has no balance: use another connection or mark the signal unknown.
- **DataForSEO costs money.** Use `location_code` 2840 and `language_code` `en` unless the audience is elsewhere. Keep a run to about 12 calls: one or two `labs_ranked_keywords` pages, and content parsing only for the posts you feature or put in a course.

If a call fails, keep going. Mark that signal **unknown**, say which call failed, and never fill the gap with a guess.

## Step 1: what was published in the window

**List the posts.** Run `link-extractor` on the blog index (and page 2 if the index pages):
```json
{"platform": "crawler", "workspace_id": "<WORKSPACE_ID>", "action": "link-extractor", "url": "<BLOG_INDEX_URL>"}
```
Keep internal links whose path looks like a post (not tags, authors, hubs or pagination). The publish date comes from the blog's feed or sitemap when it has one (Claude can read those directly), from the page itself, or from the GA4 rule below. If none works, ask the user which posts are new.

**Titles and outlines.** For each candidate post:
```json
{"platform": "crawler", "workspace_id": "<WORKSPACE_ID>", "action": "meta-tags-checker", "url": "<POST_URL>"}
```
```json
{"platform": "crawler", "workspace_id": "<WORKSPACE_ID>", "action": "headings-checker", "url": "<POST_URL>"}
```
`content-quality-checker` (same body) adds word count and readability when you need a reading-time line.

**Backup page reader** (the crawler is down, or the site blocks it):
```json
{"platform": "dataforseo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "onpage_content_parsing", "url": "<POST_URL>"}
```
The text sits in `page_content.main_topic`: each block has `h_title`, `level` and `primary_content[].text`.

## Step 2: what got attention

Use the first source that applies.

**A. Your own site, GA4 connected.** Posts read in the window:
```json
{"platform": "google-analytics", "action": "get_report", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "property_id": "properties/<PROPERTY_ID>", "dimensions": ["pagePath", "pageTitle"], "metrics": ["screenPageViews", "engagedSessions", "userEngagementDuration"], "start_date": "<START>", "end_date": "<END>", "dimensionFilter": {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "BEGINS_WITH", "value": "<BLOG_PATH_PREFIX>"}}}, "limit": 500}
```
The same body for the 90 days before `<START>`, with `"dimensions": ["pagePath"]` and `"metrics": ["screenPageViews"]`: a post with views in the window and none in those 90 days is **new this window**. Use this when the blog has no dates.

**B. Search Console connected.** Search clicks per post:
```json
{"platform": "google-search-console", "action": "search_analytics", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "site_url": "<SITE_URL>", "dimensions": ["page"], "start_date": "<START>", "end_date": "<END>", "row_limit": 1000, "dimension_filter_groups": [{"filters": [{"dimension": "page", "operator": "contains", "expression": "<BLOG_PATH_PREFIX>"}]}]}
```

**C. A site you don't own or haven't connected.** Public search estimates for the window's posts:
```json
{"platform": "dataforseo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "labs_ranked_keywords", "target": "<BLOG_HOST>", "location_code": 2840, "language_code": "en", "limit": 1000, "filters": [["ranked_serp_element.serp_item.url", "in", ["<POST_URL_1>", "<POST_URL_2>"]]], "order_by": ["ranked_serp_element.serp_item.etv,desc"]}
```
If `total_count` is over 1,000, run it again with `"offset": 1000`. Sum `ranked_serp_element.serp_item.etv` per URL: that is the page's estimated monthly US search visits. It is the current estimate, not traffic inside the window, so say so. Use the blog's own host as `target` (a subdomain blog needs the subdomain); `labs_relevant_pages` returned nothing for a subdomain blog in testing. A post the feed dates to the window can still be an older page that was updated (in testing, one "September" post already ranked for nearly 800 phrases), so call them "dated in the window", not "new".

**Score.** Per post: GA4 engaged sessions (A); if there is no GA4, Search Console clicks (B); if neither, the estimated search visits (C). Posts with no row score 0. Say which source scored the posts.

## Step 3: what past issues taught (email platform)

**Klaviyo.** Sent email campaigns, then their results over the last 12 months:
```json
{"platform": "klaviyo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "get_campaigns", "filter": "and(equals(messages.channel,'email'),any(status,['Sent','Variations Sent']))", "fields[campaign]": "name,status,send_time,audiences", "sort": "-created_at", "auto_paginate": true}
```
```json
{"platform": "klaviyo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "get_campaign_report", "body": {"data": {"type": "campaign-values-report", "attributes": {"timeframe": {"key": "last_12_months"}, "group_by": ["campaign_id", "campaign_message_id", "campaign_message_name", "send_channel"], "statistics": ["recipients", "delivered", "opens_unique", "clicks_unique", "click_rate", "unsubscribe_rate", "spam_complaint_rate", "conversion_value"]}}}}
```
Rates come back as fractions (0.021 = 2.1%).

**Mailchimp** (untested until connected). Sent campaigns with subject lines and results, then the links clicked in each recent issue:
```json
{"platform": "mailchimp", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "list_campaigns", "status": "sent", "since_send_time": "<12_MONTHS_AGO_ISO>", "fields": "id,send_time,archive_url,settings.subject_line,settings.preview_text,recipients.list_id", "auto_paginate": true}
```
```json
{"platform": "mailchimp", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "list_reports", "since_send_time": "<12_MONTHS_AGO_ISO>", "auto_paginate": true}
```
```json
{"platform": "mailchimp", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "get_report_click_details", "campaign_id": "<CAMPAIGN_ID>", "auto_paginate": true}
```

**What to take from the history** (only with at least 3 sent issues and 1,000 delivered in total; below that, say "not graded" and use the defaults):
- **Topics that get clicks.** Share of clicks by the topic of the linked post (Mailchimp click details). Topics that won twice get the lead slot more readily.
- **Subject styles.** Click rate by style (specific, curiosity, direct value, personal; see Step 5). Judge on clicks, not opens: privacy features inflate opens.
- **Fatigue.** An issue with an unsubscribe rate over twice the median, or any spam rate over 0.1%, is a warning. Name what was different about it (length, topic, frequency).
- **Send slot.** The weekday and hour with the best median click rate, only if each slot has 3 or more sends. Otherwise keep the current slot.

## Step 4: rank and pick

Apply these in order and show the result as a table (post, topic, score, role, reason):
1. **Window.** Keep posts dated in the window. A post dated after it waits for the next issue.
2. **Audience.** Drop posts off-audience for this newsletter (hiring, engineering, investor news in a customer newsletter) and list them with the reason. Ask when unsure.
3. **Topics.** Group posts on the same subject into one topic. A topic's score is the sum of its posts.
4. **Lead.** The highest-scoring topic leads. Its best post is the lead link. Past-issue history can move a topic up one place when it won clicks twice; say so when it does.
5. **Supporting.** The next 3 topics by score, one post each (the topic's best).
6. **Fresh pick.** One on-audience post with score 0, newest first, so new work gets a chance before it has data.
7. **Quick links.** Up to 2 more on-audience posts as one-line links. The rest are listed as "also published", not in the issue.
8. **Course check.** A topic with 3 or more posts in the window is an email-course candidate: offer it in the issue and outline it (see Email course).

## Step 5: pick a format and write

**Nine formats.** Pick one per issue and say why. Keep it the same across issues unless the user wants a change; readers learn the shape.

| Format | When it fits | Shape |
|---|---|---|
| Curator | a month of posts, busy readers | short intro, 3 to 7 picks each with a one-line "why it matters", sign-off |
| Teacher | one skill worth learning | promise, why now, the steps with an example each, one thing to do today |
| Storyteller | one strong story | open mid-scene, the problem, the turn, the lesson, a light bridge to the link |
| Roundup | a recurring, easy-to-make issue | fixed sections (news, tool, stat, tip, read), same order every time |
| Analyst | a data-minded audience | the finding first, how you know, what it means, the limits |
| Behind the scenes | building trust | something normally hidden, why you're sharing it, the details, the lesson |
| Interview or Q&A | outside expertise | who and why, 3 to 5 sharp questions, a takeaway, where to find them |
| Contrarian | cutting through noise | the common belief, where it breaks, the alternative, the evidence, an invitation to disagree |
| Product update | adoption of something new | what changed, the problem it solves, how to try it in one step |

Default, first match wins: **Product update** when the lead is a launch; **Teacher** when the issue covers one topic (only one on-audience topic has a score, or the user asks for a single-topic issue); otherwise **Curator** for a monthly or weekly digest, even when one topic holds most of the score, because the lead slot and the email course carry that topic.

**Write these parts:**
1. **Three subject lines,** one each of: *specific* (numbers or names from the posts), *curiosity* (a question or an odd detail), *direct value* (what the reader gets). A *personal* one ("quick question") suits reply goals. Each 50 characters or fewer.
2. **Preview text** of 40 to 110 characters that adds something the subject doesn't say.
3. **The body** in the chosen format: value in the first two sentences, the lead, the supporting items, the fresh pick, quick links, one clear call to action, a sign-off with a reply prompt.
4. **Links** tagged `utm_source=newsletter&utm_medium=email&utm_campaign=<yyyy-mm>-<newsletter-slug>` so GA4 can show what each issue drove. At most 7 links in the body.
5. **What's needed to finish:** images (one per lead and supporting item, with alt text), personalisation fields, the course signup link if there is one.
6. **Send timing** from the history (Step 3), or "keep your current slot" with the reason.
7. **One A/B test,** usually subject A against subject B, judged on click rate.

**Repurposing inside an issue:** a long guide becomes its 3 most useful points plus the link; a list post becomes its best item plus a teaser of the rest; a case study becomes the story with the result as the hook; a social thread becomes the expanded version; a post that did unusually well becomes a Behind the scenes issue on why; poll results become an Analyst issue; common customer questions become a Teacher issue, a customer success story a Storyteller issue, and a common objection a Contrarian issue.

## Step 6: checks before handing it over

| Check | Pass when |
|---|---|
| Subjects | 3 options, each 50 characters or fewer, three different styles |
| Preview | 40 to 110 characters and doesn't repeat the subject |
| Facts | every factual line traces to a post read in this run (keep a fact ledger: line, post, the sentence it came from) |
| No invented numbers | no stats, results or promises that aren't in the posts or the data |
| Links | 7 or fewer in the body, every one tagged, one primary call to action |
| Length | Curator, Roundup, Product update: 150 to 450 words. Teacher, Storyteller, Analyst, Behind the scenes, Interview, Contrarian: 300 to 800 |
| Voice | matches the samples the user gave, or the blog's own tone |
| Mobile | paragraphs of 60 words or fewer, no layout that relies on side-by-side columns |

Report each check as pass or fail. Fix a fail before handing over, and say what you changed.

## Other modes

**Ideas.** Ten (or the number asked) issue ideas, each tied to evidence: a topic whose posts led on engaged sessions or clicks, a search phrase with real demand where the site ranks in the top 20 (GSC query rows, or DataForSEO keyword rows for a public site), a topic that won clicks in past issues, or a question readers asked. Rule: among topics that didn't lead this issue and aren't the course, take each topic's highest-volume search phrase where the site ranks 20 or better, and rank the topics by that volume. Each idea gets a working subject line, a format and the evidence row. Don't invent demand: an idea with no evidence is labelled "editorial".

**Review a sent issue.** Pull the issue and its numbers, then grade it with the Step 6 checks plus results:
- Klaviyo: the campaign row from Step 3, and its template HTML:
```json
{"platform": "klaviyo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "get_email_templates", "fields[template]": "name,editor_type,created,updated", "sort": "-updated", "auto_paginate": true}
```
```json
{"platform": "klaviyo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "get_email_template", "template_id": "<TEMPLATE_ID>", "fields[template]": "name,editor_type,html,text"}
```
- Mailchimp (untested until connected): the `archive_url` from `list_campaigns` is the issue's web version. Run the crawler's `link-extractor`, `headings-checker` and `image-optimization-checker` on it, and `get_report_click_details` for which links earned the clicks.
- Grade: click rate against the newsletter's own median (not an industry figure), unsubscribe and spam against Step 3's fatigue rule, links that got no clicks, images without alt text, a missing plain-text part, more than one competing call to action, and a subject that promised something the body didn't deliver. End with the 3 changes for the next issue.

**Cross-promotion.** Grow the list from what already gets traffic and from partners:
- Own pages: the GA4 landing pages with the most sessions in the last 30 days are where a signup form or a "get this in your inbox" line pays most:
```json
{"platform": "google-analytics", "action": "get_report", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "property_id": "properties/<PROPERTY_ID>", "dimensions": ["landingPage"], "metrics": ["sessions", "engagedSessions"], "start_date": "<START>", "end_date": "<END>", "limit": 50}
```
- The list to grow: Klaviyo `get_lists` (`{"platform": "klaviyo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "get_lists", "auto_paginate": true}`) or Mailchimp `list_lists` (`"fields": "id,name,stats.member_count,stats.avg_sub_rate"`, untested until connected).
- Partners: newsletters in the same niche that rank for "<topic> newsletter" (one call):
```json
{"platform": "dataforseo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "serp_google_organic", "keyword": "<TOPIC> newsletter", "location_code": 2840, "language_code": "en", "depth": 10}
```
  Keep organic results that are a business's newsletter; skip personal pages. For each, propose the swap: a one-line recommendation in each other's issue, a guest section, or a shared resource, with its own UTM campaign so both sides can see what it drove.
- Plus the placements you already own: the social profiles' bio links, a line in every blog post's footer, the email signature, and the thank-you page after a purchase or signup.

**Email course.** From a topic with 3 or more posts: 3 to 7 lessons, one a day, ordered from the overview post to the specific ones. Each lesson: a subject of 50 characters or fewer, one idea in 200 words or fewer drawn from its post, one small practice task, one tagged link (`utm_campaign=<course-slug>`). Lesson 1 says what the course covers; the last lesson points to the next step (the newsletter, a product, a reply). Build it as an automation in the email platform; this skill writes it, it doesn't build the automation.

## Launch and sponsorship

For a newsletter that doesn't exist yet, or one that should start paying for itself. It works from a description alone (topic, audience, the hours a week the user has, the money goal); every connected source replaces an assumption with a number, and each assumption is labelled in the plan.

**Ask first** (defaults in brackets): who it's for and what they should be able to do after reading; hours a week for the newsletter [ask, no default]; the money goal per month [none: plan the launch only]; the smallest sponsor deal worth selling and running [the user's hourly rate times 2 hours]; the platform they send from today [none]; for an existing newsletter on Substack, Beehiiv, Ghost or Kit (not connectors), paste per-issue delivered (or recipients) and unique clicks for the last 3 or more issues from the dashboard or an export.

### Part 1: the launch

1. **Topic angle from demand.** List 3 to 10 candidate angles (the user's, plus topics the blog already covers). If Search Console is connected, pull the queries that contain each angle's main word over the last 90 days:
```json
{"platform": "google-search-console", "action": "search_analytics", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "site_url": "<SITE_URL>", "dimensions": ["query"], "start_date": "<START>", "end_date": "<END>", "row_limit": 25000, "dimension_filter_groups": [{"filters": [{"dimension": "query", "operator": "contains", "expression": "<ANGLE_WORD>"}]}]}
```
   Sum `impressions` per angle. Keep `row_limit` at 25000: in testing, one angle word matched 1,063 queries, and a limit of 1,000 would have cut the sum short.
   With DataForSEO added, check public demand for the angles in one call (the same call also feeds the rate card in Part 2, so put the sponsor keywords in it too):
```json
{"platform": "dataforseo", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "action": "labs_keyword_overview", "account_id": "<DATAFORSEO_ACCOUNT_ID>", "keywords": ["<ANGLE_KEYWORD_1>", "<ANGLE_KEYWORD_2>", "<SPONSOR_KEYWORD_1>", "<SPONSOR_KEYWORD_2>"], "location_code": 2840, "language_code": "en"}
```
   (Body checked with the helper. The live call is untested in this build: one DataForSEO login answered `Payment Required` and the other returned an empty provider answer, `Ok. (status 20000)` with no rows. An empty answer like that means unknown, not zero demand.) Each row has `keyword_info.search_volume`, `keyword_info.cpc`, `keyword_info.low_top_of_page_bid`, `keyword_info.high_top_of_page_bid` and `search_intent_info.main_intent`. Rule: pick the angle with the most Search Console impressions (the site already earns attention there); with no Search Console, the angle with the highest informational search volume. An angle the user insists on wins and is labelled "editorial".
2. **The promise,** one sentence the signup form can carry: who it's for, what they get, how often, and what they'll be able to do. Then 3 subject lines for issue 1 (Step 5 rules).
3. **Format** from the Step 5 table, by what the user can feed it: Curator or Roundup when they publish or collect at least 3 items per issue; Teacher when one subject runs deep; Analyst when they have their own data; Storyteller or Behind the scenes when the value is their experience.
4. **Cadence the user can keep for 12 issues.** Take the most frequent of weekly, every two weeks and monthly where both hold:
   - hours per issue (the user's estimate for the chosen format) times issues a month is no more than 80% of the hours they have a month, leaving room for a bad week;
   - for Curator and Roundup, posts published a month (Step 1's post list, or the user's count) cover at least 3 items per issue.
   Show the arithmetic. If no cadence passes, say which input to change.
5. **Platform by need,** not by ranking:
   - Already emailing this audience from Klaviyo or Mailchimp: start there. One list, one unsubscribe, and through InsightfulPipe this skill reads its results and saves drafts.
   - A paid tier from day one: a platform with paid subscriptions built in, for example Substack, Beehiiv, Ghost or Kit. Fees and features change; tell the user to check each pricing page, and never quote a fee.
   - A sponsor-led newsletter on Mailchimp or Klaviyo works too; sponsors are sold directly, as in Part 2.
   Say plainly that Substack, Beehiiv, Ghost and Kit aren't InsightfulPipe connectors: for them the skill works from pasted stats.
6. **Subscriber targets.** The milestones are the audiences the chosen revenue options need (Part 2), in delivered emails per issue. Monthly signups needed = (target minus current delivered) / months to the target date. Compare it with what signups run at today: Mailchimp `list_lists` with `"fields": "id,name,stats.member_count,stats.avg_sub_rate"` (`avg_sub_rate` is the average number of new subscribers a month, not a percentage; untested until connected), or the user's number. The gap goes to the cross-promotion mode, which names where the signups come from.
7. **First 90 days,** dated from the launch day: authenticate the sending domain (SPF, DKIM and DMARC; Gmail and Yahoo require them for bulk senders), a welcome email that restates the promise, signup placements from cross-promotion, a backlog of 3 issues from the ideas mode before issue 1 goes out, then issues on the cadence. After issue 3 (and 1,000 delivered in total), Step 3's history opens and the rate card can be priced on real numbers.

### Part 2: revenue options and the audience each needs

**Baseline,** from Step 3's history (the same gate: 3 or more sent issues and 1,000 delivered in total; Klaviyo `get_campaign_report`, Mailchimp `list_reports` (the Step 3 body), or the pasted export):
- **D**, median delivered per issue (Klaviyo `delivered`; Mailchimp `emails_sent` minus bounces, or `emails_sent` when bounces aren't pulled, and say so).
- **U**, median unique clickers per issue (Klaviyo `clicks_unique`, Mailchimp `clicks.unique_subscriber_clicks`), and **CR** = U / D.
- Below the gate, nothing is priced: the plan shows the formulas, the audience each option needs at a click rate the user supplies (labelled assumption), and the date the gate should open on the planned cadence.

**Slot share (s),** the part of an issue's unique clickers one placement can expect:
- Mailchimp (untested until connected): for each of the last issues, `get_report_click_details` gives unique clicks per link, and the crawler's `link-extractor` on the issue's `archive_url` gives the link order. Primary slot (top, after the intro) = the median share the first featured link got; secondary (mid-issue) = the median share of the links in places 2 to 4; classified (one line near the end) = the median share of the last two links.
- Pasted link reports: Substack, Beehiiv, Ghost and Kit dashboards usually list clicks for each link in a sent issue. Ask for that list for each of the last issues, top to bottom as the links appear, and apply the same three medians. When the counts are total clicks rather than unique clickers, divide each link by the issue's total link clicks instead of by U, and say which count was used.
- No per-link numbers at all (Klaviyo through the connector, or an export with only issue totals): use 1 / the typical link count per issue for the primary slot (1/7 at this skill's link cap), half of that for secondary and classified, and label it an estimate to replace after the first 3 placements.

**Value per click (V).** What advertisers already pay to reach this audience by search: the median `low_top_of_page_bid` (floor) and median `cpc` (ceiling) across 3 to 10 commercial or transactional keywords the likely sponsors buy, from the same `labs_keyword_overview` call. If a sponsor shares what a click is worth to them, use that. Without DataForSEO, ask the user for a floor and label it.

**Rate card.**

| Placement | Expected clicks | List price | Ceiling | Implied CPM |
|---|---|---|---|---|
| Primary | U × s(primary) | clicks × floor V, rounded down to $5 | clicks × ceiling V | list price / D × 1,000 |
| Secondary | U × s(secondary) | same | same | same |
| Classified | U × s(classified) | same | same | same |
| Dedicated issue (one sponsor, whole issue) | median U of the newsletter's own single-topic issues (Teacher, Product update) when 3 or more exist; otherwise U, labelled an upper bound | same | same | same |

The CPM column is there for buyers who compare that way; it never sets the price. Booking 4 issues gets the same placement each time at the same per-issue price; offer a discount only if the user wants one. Re-price after every 3 placements from what they actually earned.

**The audience each option needs,** in delivered emails per issue, with "met" or the gap:
- **Sponsor slots:** D needed = minimum deal / (CR × s(primary) × floor V).
- **Paid tier:** paid subscribers needed = monthly goal / (monthly price × (1 minus the platform's fee share)). List needed = paid subscribers / the paid conversion rate, measured by a founding-member test (one line in 2 issues linking to a waitlist; waitlist signups / D is the planning rate, an upper bound). No test yet: show the paid subscribers needed and "list needed: unknown until the test runs". Paid content: the topics with the best click rate over 3 or more issues are the candidates for paid extras; the free issue keeps its promise.
- **Affiliate placements:** revenue per issue = U × s × the program's conversion rate × commission per sale (from the program's terms or the user's affiliate dashboard; GA4 can't see the sale on the merchant's site). D needed = minimum deal / (CR × s × conversion × commission).
Recommend the options already met; the next one is the one with the smallest gap.

**Media kit,** written from the numbers above, never rounded up:
- Who reads it: the audience in the user's words, plus where newsletter readers come from when GA4 is connected and links carry this skill's tags (`utm_medium=email`):
```json
{"platform": "google-analytics", "action": "get_report", "workspace_id": "<WORKSPACE_ID>", "brand_id": "<BRAND_ID>", "property_id": "properties/<PROPERTY_ID>", "dimensions": ["country", "deviceCategory"], "metrics": ["sessions", "engagedSessions"], "start_date": "<START>", "end_date": "<END>", "dimensionFilter": {"filter": {"fieldName": "sessionMedium", "stringFilter": {"matchType": "EXACT", "value": "email"}}}, "limit": 50}
```
  This counts clickers who reached the site, not every subscriber; say so.
- Reach and engagement: D, U and CR, with the number of issues and the date range behind them. Opens only if a sponsor asks, with the note that privacy features inflate them.
- What readers click: the topics with the most clicks from Step 3, when the history has them.
- Placements: where each sits, its length (a headline and up to 60 words for primary and secondary, one line for classified), one link each, an image only in primary.
- Rates and terms: the rate card, copy due a set number of working days before the send (the user's choice), the newsletter's right to refuse an off-audience sponsor (the Step 4 audience rule applies to sponsors too), and a report after each send of delivered and unique clicks on the sponsor's link (Mailchimp click details; with Klaviyo, the sponsor reads its own tagged link in its analytics).
- Past sponsors and testimonials only when the user supplies them; never invented.

**Disclosure.** Every paid placement carries a visible "Sponsored" label and every affiliate link a short disclosure, because the FTC expects a material connection to be clear to the reader.

## Report format

1. **Header:** newsletter, issue, window, mode, format and why, goal, which sources scored the posts.
2. **What was published:** the ranking table from Step 4, including the posts left out and why.
3. **What the history says:** Step 3's findings, or "not graded" with the reason.
4. **The issue:** subjects, preview, body, links, what's needed, send timing, the A/B test.
5. **Checks:** the Step 6 table.
6. **Extras the request asked for:** course outline, ideas, review grades, the cross-promotion plan, or the launch and sponsorship plan (angle with its evidence, promise, format, cadence arithmetic, platform, targets, 90-day dates, rate card with its inputs, the audience each revenue option needs, media kit, and every assumption labelled).
7. **What couldn't be checked,** and why.

## Drafts this skill can create

Only after the user approves the final copy and says which list to use. Each is a write through `execute_action` and needs a Read & Write connection; an owner, admin or operator can switch writes off. These create a **draft**. The skill never sends, schedules or sends a test.

| Platform | Steps | Body (key parts) |
|---|---|---|
| Klaviyo | 1. `create_email_template` | `{"data": {"type": "template", "attributes": {"name": "<ISSUE_NAME>", "editor_type": "CODE", "html": "<HTML>"}}}` |
| | 2. `create_campaign` (created as Draft) | `{"data": {"type": "campaign", "attributes": {"name": "<ISSUE_NAME>", "audiences": {"included": ["<LIST_ID>"]}, "campaign-messages": {"data": [{"type": "campaign-message", "attributes": {"definition": {"channel": "email", "label": "Main", "content": {"subject": "<SUBJECT>", "preview_text": "<PREVIEW>", "from_email": "<FROM_EMAIL>", "from_label": "<FROM_NAME>"}}}}]}}}}` |
| | 3. `assign_template_to_campaign_message` | `{"data": {"type": "campaign-message", "id": "<CAMPAIGN_MESSAGE_ID>", "relationships": {"template": {"data": {"type": "template", "id": "<TEMPLATE_ID>"}}}}}` |
| Mailchimp (untested until connected) | 1. `create_campaign` | `{"type": "regular", "recipients": {"list_id": "<LIST_ID>"}, "settings": {"subject_line": "<SUBJECT>", "preview_text": "<PREVIEW>", "title": "<ISSUE_NAME>", "from_name": "<FROM_NAME>", "reply_to": "<REPLY_TO>"}}` |
| | 2. `set_campaign_content` | `campaign_id` from step 1, `{"html": "<HTML>", "plain_text": "<TEXT>"}` |

Show the exact payloads, with the real list id and subject, before asking. After a write, read it back (`get_campaigns` with the Draft status, or `list_campaigns` with `"status": "save"`) and confirm it is a draft.

## Rules

- Pull before asking. Ask only for what no connected source holds.
- Every featured post has a role and a reason from Step 4. Every fact in the copy comes from a post read in this run.
- No invented numbers, results or testimonials. A story or example the user didn't give is labelled as a placeholder for them to fill.
- Opens are not a success measure; clicks, replies and unsubscribes are.
- History needs at least 3 sent issues and 1,000 delivered before it changes a pick, a subject style or the send slot.
- One format per issue, one primary call to action, 7 links or fewer.
- Name businesses, never private people: drop author bylines and personal names from posts unless the user is the author.
- Keep DataForSEO to about 12 calls a run.
- Sponsor prices come from the newsletter's own delivered and unique clicks and a stated value per click, never from an industry CPM. No price until the history gate is met; no media kit number rounded up; no invented sponsors or testimonials.
- Every sponsored placement is labelled "Sponsored" and every affiliate link disclosed.
- Never send, schedule or send a test. Drafts only, after a yes on the exact payload.
- If a call fails or a source isn't connected, say so in the report and keep going.

## Go deeper

- **email-campaign-analyst** (if installed) for a full campaign performance report.
- **email-sequence-builder** for welcome and nurture sequences.
- **content-repurposer** (if installed) to turn the lead post into social posts that point to the issue.
- **brand-voice** to pin down the voice before the first issue.
- **referral-program** to add a subscriber referral scheme once the launch plan is running.
- **pricing-strategy** to set the paid tier's price before the founding-member test.
