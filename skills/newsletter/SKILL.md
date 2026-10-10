---
name: newsletter
description: Writes email newsletters from what you actually published and what your readers actually clicked. Pulls the month's posts, their traffic (GA4, Search Console or public search estimates) and past issue results (Klaviyo or Mailchimp) through the InsightfulPipe MCP, picks the lead story and supporting items by a stated rule, and drafts the issue in one of nine formats with subject lines, preview text, tagged links and checks. Also generates issue ideas, reviews a sent issue, plans cross-promotion and turns a cluster of posts into an email course. Use when someone asks for a newsletter, a monthly or weekly roundup, newsletter ideas, a newsletter review, newsletter growth or swaps, or an email course. Can save the issue as a draft campaign only after the user confirms; it never sends.
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
4. Pick the mode from the request: **issue** (default), **ideas**, **review**, **cross-promotion** or **email course**. One request can combine them.

## How to run the calls

Every read goes through `query_data` with the `platform` named in the step. Rules the APIs enforce:
- **Rate limits are shared.** On `rate_limit_exceeded`, wait `retry_after` seconds and retry. Don't fire calls in parallel.
- **An empty answer is not an error.** A Klaviyo account with no sends returns `success` with an empty list. Say "no history" and move on.
- **GA4 needs `properties/` before the id**, and filters use `dimensionFilter`. Drop rows whose title says "Not Found" or "404" and paths with stray characters: in testing, broken links to posts showed up as their own rows.
- **Search Console pages are full URLs**; GA4 paths are not. Join on the path.
- **Klaviyo campaigns need a channel filter** (`equals(messages.channel,'email')`), and status values are Title Case (`'Sent'`). Klaviyo reports carry `campaign_message_name`, not the subject line; ask the user for subjects if you need them.
- **Mailchimp calls in this skill are untested until a Mailchimp account is connected.** Their shapes come from the helper. Run `actions_details` first and adjust if a field name differs.
- **The crawler can fail.** On 2026-10-06 it returned `Error fetching URL` for every page during testing. When it does, read the pages with DataForSEO `onpage_content_parsing`, or read them directly, and say which you used.
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
| Curator | a month of posts, busy readers | short intro, 3–7 picks each with a one-line "why it matters", sign-off |
| Teacher | one skill worth learning | promise, why now, the steps with an example each, one thing to do today |
| Storyteller | one strong story | open mid-scene, the problem, the turn, the lesson, a light bridge to the link |
| Roundup | a recurring, easy-to-make issue | fixed sections (news, tool, stat, tip, read), same order every time |
| Analyst | a data-minded audience | the finding first, how you know, what it means, the limits |
| Behind the scenes | building trust | something normally hidden, why you're sharing it, the details, the lesson |
| Interview or Q&A | outside expertise | who and why, 3–5 sharp questions, a takeaway, where to find them |
| Contrarian | cutting through noise | the common belief, where it breaks, the alternative, the evidence, an invitation to disagree |
| Product update | adoption of something new | what changed, the problem it solves, how to try it in one step |

Default, first match wins: **Product update** when the lead is a launch; **Teacher** when the issue covers one topic (only one on-audience topic has a score, or the user asks for a single-topic issue); otherwise **Curator** for a monthly or weekly digest, even when one topic holds most of the score, because the lead slot and the email course carry that topic.

**Write these parts:**
1. **Three subject lines,** one each of: *specific* (numbers or names from the posts), *curiosity* (a question or an odd detail), *direct value* (what the reader gets). A *personal* one ("quick question") suits reply goals. Each 50 characters or fewer.
2. **Preview text** of 40–110 characters that adds something the subject doesn't say.
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
| Preview | 40–110 characters and doesn't repeat the subject |
| Facts | every factual line traces to a post read in this run (keep a fact ledger: line, post, the sentence it came from) |
| No invented numbers | no stats, results or promises that aren't in the posts or the data |
| Links | 7 or fewer in the body, every one tagged, one primary call to action |
| Length | Curator, Roundup, Product update: 150–450 words. Teacher, Storyteller, Analyst, Behind the scenes, Interview, Contrarian: 300–800 |
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

**Email course.** From a topic with 3 or more posts: 3–7 lessons, one a day, ordered from the overview post to the specific ones. Each lesson: a subject of 50 characters or fewer, one idea in 200 words or fewer drawn from its post, one small practice task, one tagged link (`utm_campaign=<course-slug>`). Lesson 1 says what the course covers; the last lesson points to the next step (the newsletter, a product, a reply). Build it as an automation in the email platform; this skill writes it, it doesn't build the automation.

## Report format

1. **Header:** newsletter, issue, window, mode, format and why, goal, which sources scored the posts.
2. **What was published:** the ranking table from Step 4, including the posts left out and why.
3. **What the history says:** Step 3's findings, or "not graded" with the reason.
4. **The issue:** subjects, preview, body, links, what's needed, send timing, the A/B test.
5. **Checks:** the Step 6 table.
6. **Extras the request asked for:** course outline, ideas, review grades or the cross-promotion plan.
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
- Never send, schedule or send a test. Drafts only, after a yes on the exact payload.
- If a call fails or a source isn't connected, say so in the report and keep going.

## Go deeper

- **email-campaign-analyst** (if installed) for a full campaign performance report.
- **email-sequence-builder** for welcome and nurture sequences.
- **content-repurposer** (if installed) to turn the lead post into social posts that point to the issue.
- **brand-voice** to pin down the voice before the first issue.
