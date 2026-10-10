---
name: onboarding-cro
description: Maps the new-user journey from first visit to signup, onboarding, activation and the first return, on live GA4 data pulled through the InsightfulPipe MCP, finds the step that loses the most people, and designs the onboarding fix (activation metric, first-run patterns, onboarding emails, personalisation). Use when someone asks to improve onboarding, activation, time to value, the first-run or new-user experience, the "aha moment", or to design or map a user journey. Reads Klaviyo onboarding flows when connected, and offers a key event and stage audiences that it creates only after the user confirms.
---

# Onboarding CRO

Signing up is not the win. A new user is only worth something once they reach the moment the product proves itself and they come back for more. This skill finds where new users stall on the way there, using the product's own analytics, and then designs the onboarding that moves them past that point.

It reads the data itself. Every number in the report comes from a call below, and every call shows what it returned.

## Before you start

You need the InsightfulPipe MCP connected to the GA4 property that records the product (the app or the site where people sign up and use it). A Klaviyo account is optional.

1. Call `query_contexts` with `request="accounts"` and `platform="google-analytics"`. Note `workspace_id`, `brand_id` and the `property_id`. If there are several properties, ask which one records the product.
2. Call `query_contexts` with `request="actions_details"` and `platform="google-analytics"` for `events`, `get_report`, `list_key_events`, `list_audiences`, `create_key_event` and `create_audience`, and follow the body shapes it returns. If Klaviyo is connected, do the same for `get_flows` and `get_flow_report` with `platform="klaviyo"`.
3. Ask the user these things, and use the defaults when they don't know:
   - **What the product is and who it's for** (one line). This decides which onboarding model fits (see "Design the fix").
   - **The signup event.** Default: `sign_up`, the name GA4 recommends.
   - **The onboarding step events**, in order. Default: `tutorial_begin` then `tutorial_complete`, plus any event whose name contains `onboard`, `setup`, `connect`, `create`, `invite` or `import`.
   - **The activation event:** the action that shows the user got real value (a first project, a first report, a first message sent and answered). Default: the first key event that fires and isn't the signup event. If none fires, activation is **unknown**; never pick one at random.
   - **What onboarding looks like today:** the screens after signup, whether they change by role, goal or plan, and any human touch (a setup call, a named contact). This tells you which patterns are already in place. When the user doesn't say, recommend patterns without assuming any exist, and say so.
   - **Where signup happens,** and the paths of the signup, onboarding and help pages. Default for the pages: paths containing `pricing`, `signup`, `sign-up`, `demo` or `onboarding`, plus paths starting with `/docs` (call 8). Add `register`, `get-started`, `welcome` or `/help` when the site uses them.

**Window.** Use the last 12 complete weeks, Monday to Sunday, ending on the last Sunday that is at least 2 days before today (GA4 is still processing the most recent days). Call the first day `START` and the last day `END`, and print both at the top of the report.

## How to run the calls

Every GA4 call goes through `query_data` with `platform="google-analytics"`. Add `workspace_id` and `brand_id` from step 1 to each body. Rules the API enforces, all seen on live runs:

- **Request keys are camelCase where GA4 defines them.** Filters go in `dimensionFilter`; `dimension_filter` is ignored without an error and quietly returns every row. The cohort spec goes in `cohortSpec`. After any filtered call, check that the rows that come back match the filter.
- **Only add up users where each user can sit in one row.** Each user has one `firstSessionDate` and one `firstUserDefaultChannelGroup`, so users in those rows can be summed. Users across devices, pages or days can't, because one person can be in several rows. Never add the `(not set)` first-session rows to the dated ones.
- **New users in the window** are the users of rows whose `firstSessionDate` falls between `START` and `END`. Rows with an earlier first-session date are people who first came before the window; leave them out of the journey.
- **GA4 doesn't know the order of steps.** A user who signed up in the window and did the activation event in the window counts for both, whatever the order. When a later step has more users than the step before it, say so: the earlier step is under-tracked, or users skip it.
- **Missing cohort cells are zeros.** The cohort report leaves out weeks in which nobody came back. A missing cell whose week ends on or before `END` is 0. A cell whose week ends after `END` is blank, even if GA4 returns a number for it, because that week isn't over.
- **Dates** come back as `YYYY-MM-DD` or `YYYYMMDD`. Read both.
- **Rate limits.** When a call is refused with "Retry in N seconds", tell the user how long that is, then wait or stop. Don't retry in a loop.

If a call fails, keep going. Mark the area it feeds **unknown**, say which call failed and why, and never fill the gap with a guess.

## The calls

**1. Key events configured.**
```json
{"action": "list_key_events", "property_id": "properties/<id>"}
```

**2. Existing audiences.** So the skill never offers an audience that already exists.
```json
{"action": "list_audiences", "property_id": "properties/<id>"}
```

**3. Event inventory.** Every event that fired in the window, with users.
```json
{"action": "events", "property_id": "properties/<id>",
 "dimensions": ["eventName"], "metrics": ["eventCount", "totalUsers"],
 "start_date": "START", "end_date": "END"}
```

**4. What the property can see.** If only the marketing site's host shows up, the product itself isn't tracked here, and everything after the signup click is invisible to this property.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["hostName"], "metrics": ["sessions", "totalUsers"],
 "start_date": "START", "end_date": "END"}
```

**5. The new-user journey, by first channel.** Users per event, per first-session date, per the channel that first brought them. Summed over the dated rows in the window, this is the journey funnel; per channel, it's the segment view.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["firstSessionDate", "firstUserDefaultChannelGroup", "eventName"],
 "metrics": ["totalUsers"], "start_date": "START", "end_date": "END", "limit": 100000}
```

**6. Journey events by device.** Only the signup, onboarding, activation and return events, so the rows stay few. Device rows can't be summed into a total (one person can use two devices); read each device's rate within its own rows, against that device's `first_visit` users.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["firstSessionDate", "deviceCategory", "eventName"],
 "metrics": ["totalUsers"], "start_date": "START", "end_date": "END", "limit": 100000,
 "dimensionFilter": {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["first_visit", "sign_up", "tutorial_begin", "tutorial_complete", "login"]}}}}
```
Put the user's own signup, step and activation events in `values`, and keep `first_visit` as the base.

**7. Time to value.** The same events by the day they happened. The gap between `date` and `firstSessionDate` is how many days after their first visit people got there.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["firstSessionDate", "date", "eventName"],
 "metrics": ["totalUsers"], "start_date": "START", "end_date": "END", "limit": 100000,
 "dimensionFilter": {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["sign_up", "tutorial_begin", "tutorial_complete", "login"]}}}}
```
Put the user's own signup, step and activation events in `values`. A user who does the event on 3 different days is counted on each of those days, so this gives the spread of "user-days", not of people. Report the share on day 0, days 1–2, days 3–7, days 8–14 and day 15 or later, and say it counts user-days.

**8. Journey pages: evaluation, signup and help.** New users who reached the pricing, signup, onboarding or help pages.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["firstSessionDate", "pagePath"],
 "metrics": ["totalUsers"], "start_date": "START", "end_date": "END", "limit": 100000,
 "dimensionFilter": {"orGroup": {"expressions": [
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "pricing"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "signup"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "sign-up"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "demo"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "CONTAINS", "value": "onboarding"}}},
   {"filter": {"fieldName": "pagePath", "stringFilter": {"matchType": "BEGINS_WITH", "value": "/docs"}}}]}}}
```
Swap in the user's own paths. Drop pages that only mention the word, such as a blog post or a guide about signup forms. Leave out paths GA4 returns cut short (ending in `...`), and say how many. For one page, users can be summed over the dated first-session rows. Across pages they can't (one person can read three help pages), so a stage made of several pages is reported as "at least" its biggest page. Help pages read by new users are an early sign of where setup gets hard: name the most-read ones by what they cover (troubleshooting, a connection guide, account setup). Give every group an explicit rule; never let a catch-all group collect what's left. When one guide shows up at two paths, count the topics (platforms, features) as well as the pages.

**9. Hand-off clicks.** When signup lives on another domain, GA4's outbound-click event shows which links new visitors followed. A link to a subdomain of the same site is often not recorded as outbound; if the signup link never shows up here, the hand-off isn't measured.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["linkDomain", "linkUrl"], "metrics": ["eventCount", "totalUsers"],
 "start_date": "START", "end_date": "END",
 "dimensionFilter": {"filter": {"fieldName": "eventName", "stringFilter": {"value": "click"}}}}
```

**10. Return by weekly cohort.** GA4's own cohort report: 12 weekly cohorts by first-session date, each followed for up to 11 weeks. Cohort calls take no `start_date` or `end_date`; the dates live in each cohort. `W01_START` is `START`, and each cohort is 7 days.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["cohort", "cohortNthWeek"],
 "metrics": ["cohortActiveUsers", "cohortTotalUsers"],
 "cohortSpec": {"cohorts": [
   {"name": "w01", "dimension": "firstSessionDate", "dateRange": {"startDate": "W01_START", "endDate": "W01_END"}},
   {"name": "w02", "dimension": "firstSessionDate", "dateRange": {"startDate": "W02_START", "endDate": "W02_END"}},
   {"name": "w03", "dimension": "firstSessionDate", "dateRange": {"startDate": "W03_START", "endDate": "W03_END"}},
   {"name": "w04", "dimension": "firstSessionDate", "dateRange": {"startDate": "W04_START", "endDate": "W04_END"}},
   {"name": "w05", "dimension": "firstSessionDate", "dateRange": {"startDate": "W05_START", "endDate": "W05_END"}},
   {"name": "w06", "dimension": "firstSessionDate", "dateRange": {"startDate": "W06_START", "endDate": "W06_END"}},
   {"name": "w07", "dimension": "firstSessionDate", "dateRange": {"startDate": "W07_START", "endDate": "W07_END"}},
   {"name": "w08", "dimension": "firstSessionDate", "dateRange": {"startDate": "W08_START", "endDate": "W08_END"}},
   {"name": "w09", "dimension": "firstSessionDate", "dateRange": {"startDate": "W09_START", "endDate": "W09_END"}},
   {"name": "w10", "dimension": "firstSessionDate", "dateRange": {"startDate": "W10_START", "endDate": "W10_END"}},
   {"name": "w11", "dimension": "firstSessionDate", "dateRange": {"startDate": "W11_START", "endDate": "W11_END"}},
   {"name": "w12", "dimension": "firstSessionDate", "dateRange": {"startDate": "W12_START", "endDate": "W12_END"}}],
  "cohortsRange": {"granularity": "WEEKLY", "startOffset": 0, "endOffset": 11}}}
```

**11. Repeat use of the activation event.** The same cohort report with a filter on one event. On a live run the filter shrank each cohort to the users who did that event (week 0 active users equal the cohort size), and each later week counted the cohort's users who did it in that week. Week-N users ÷ week-0 users over weeks 1–4 shows whether the "aha" action turns into a habit.
```json
{"action": "get_report", "property_id": "properties/<id>",
 "dimensions": ["cohort", "cohortNthWeek"],
 "metrics": ["cohortActiveUsers", "cohortTotalUsers"],
 "dimensionFilter": {"filter": {"fieldName": "eventName", "stringFilter": {"value": "ACTIVATION_EVENT"}}},
 "cohortSpec": {"cohorts": [
   {"name": "w01", "dimension": "firstSessionDate", "dateRange": {"startDate": "W01_START", "endDate": "W01_END"}},
   {"name": "w02", "dimension": "firstSessionDate", "dateRange": {"startDate": "W02_START", "endDate": "W02_END"}},
   {"name": "w03", "dimension": "firstSessionDate", "dateRange": {"startDate": "W03_START", "endDate": "W03_END"}},
   {"name": "w04", "dimension": "firstSessionDate", "dateRange": {"startDate": "W04_START", "endDate": "W04_END"}},
   {"name": "w05", "dimension": "firstSessionDate", "dateRange": {"startDate": "W05_START", "endDate": "W05_END"}},
   {"name": "w06", "dimension": "firstSessionDate", "dateRange": {"startDate": "W06_START", "endDate": "W06_END"}},
   {"name": "w07", "dimension": "firstSessionDate", "dateRange": {"startDate": "W07_START", "endDate": "W07_END"}},
   {"name": "w08", "dimension": "firstSessionDate", "dateRange": {"startDate": "W08_START", "endDate": "W08_END"}},
   {"name": "w09", "dimension": "firstSessionDate", "dateRange": {"startDate": "W09_START", "endDate": "W09_END"}},
   {"name": "w10", "dimension": "firstSessionDate", "dateRange": {"startDate": "W10_START", "endDate": "W10_END"}},
   {"name": "w11", "dimension": "firstSessionDate", "dateRange": {"startDate": "W11_START", "endDate": "W11_END"}},
   {"name": "w12", "dimension": "firstSessionDate", "dateRange": {"startDate": "W12_START", "endDate": "W12_END"}}],
  "cohortsRange": {"granularity": "WEEKLY", "startOffset": 0, "endOffset": 11}}}
```
Run it only when the activation event fires in the window. It shows repeat use of one action, not whether the action predicts staying; for that, see "Finding the activation metric".

**12. Onboarding emails (Klaviyo, optional).** Use `platform="klaviyo"`.
```json
{"action": "get_flows", "auto_paginate": true, "filter": "equals(archived,false)"}
```
```json
{"action": "get_flow_report", "body": {"data": {"type": "flow-values-report", "attributes": {
  "timeframe": {"key": "last_90_days"},
  "statistics": ["recipients", "delivered", "opens_unique", "open_rate", "clicks_unique", "click_rate", "conversions", "conversion_rate", "unsubscribes"],
  "group_by": ["flow_id", "flow_message_id", "flow_name", "flow_message_name"]}}}}
```
Rates come back as fractions from 0 to 1. Klaviyo counts conversions against its "Placed Order" metric unless you pass `conversion_metric_id`; for a product without orders, pass the id of the activation or upgrade metric if the product sends one to Klaviyo, and otherwise read clicks, not conversions.

## Map the journey

Sort every event from call 3 and every page from call 8 into one of seven stages. Name an event's stage only from its name and what the user told you; when it's unclear, ask.

| Stage | What counts | Usual signals |
|---|---|---|
| 1. Arrive | first visit | `first_visit` (web) or `first_open` (app) |
| 2. Engage | the visit was more than a bounce | `user_engagement`, `scroll` |
| 3. Evaluate | looked at what it costs or how it works | pricing, demo and docs pages (call 8) |
| 4. Hand-off | started signing up | the signup page view, or a click to the signup domain (call 9) |
| 5. Sign up | account created | `sign_up` |
| 6. Onboard | the setup steps | `tutorial_begin`, `tutorial_complete`, the user's step events |
| 7. Activate and return | first value, then coming back | the activation event; week-1 return from call 10 |

For each stage, give the new users who reached it (call 5, dated rows in the window), the share of the stage before, and the share of all new users. Mark a stage **not tracked** when no event or page stands for it. The stage with the biggest drop from the one before it is the one to fix first, unless an earlier stage is not tracked; then the first fix is to track it, because a drop you can't see can't be ranked.

## The areas

Score each area **pass**, **warn**, **fail** or **unknown**. The thresholds are starting points. When the user has their own history or target, use that instead and say so.

### 1. Measurement: can the journey be seen?

From calls 1, 3 and 4.

| Check | Result |
|---|---|
| The product is tracked | fail when call 4 shows only the marketing site and no app host, and the user says the product lives elsewhere |
| Signup is tracked | fail when the signup event doesn't fire in the window |
| Activation is tracked | fail when no activation event fires; warn when one fires but isn't a key event |
| Onboarding steps are tracked | warn when signup and activation fire but no step event does |
| Key events are real | warn when key events are configured that never fired in the window; list how many |
| Tracking is steady | warn when one week's new users (call 5, summed by week) are 3 or more times the median of the other weeks: a tag change or a burst of automated visits. Read rates within the steady weeks too, and say which weeks those are |
| Test traffic is kept out | warn when `localhost`, a staging host or a preview host shows up in call 4 |

### 2. Hand-off: from visitor to signup

From calls 5, 8 and 9. The share of new users who reach the signup page or click to the signup domain. When neither is tracked, the area is **unknown**, and the evaluation pages (pricing, demo, docs) are reported as information. Show the split by first channel (call 5) for channels with 30 or more new users.

### 3. Onboarding completion

From calls 5 and 6. Users who finished the last onboarding step ÷ users who signed up. Pass at 70% or more, warn from 50% to 70%, fail under 50%. When a step has more users than the step before it, warn and say which step is under-tracked or skipped.

### 4. Activation and time to value

From calls 5 and 7. Activation rate = users who did the activation event ÷ users who signed up, both from dated rows in the window. Pass at 40% or more, warn from 20% to 40%, fail under 20%. These are rough starting points for a self-serve product; a product sold with hands-on setup should beat them, and the product's own trend matters more than any outside number.

Feature adoption, as information: for each other key event that fires, its users ÷ the activation event's users, both from call 5. GA4 doesn't know the order, so it shows how many activated users also use the feature, not when.

Time to value: the share of activation user-days that land on day 0. Warn when under half of them happen on the first day, because the first session is where most of the onboarding effort pays off.

### 5. Early return

From call 10 (and 11 when activation fires). Pool the cohorts whose week 1 is complete: week-1 return = cohort users active in week 1 ÷ cohort size. Do the same for week 4 with the cohorts old enough. Read one cohort on its own only when it has 30 or more users. When signup isn't tracked, these are site visitors, not product users: report them as information and leave the area **unknown**.

### 6. Segments: who gets stuck

From calls 5 and 6. The step rate of the stage to fix, by first channel and by device. When the stage to fix isn't tracked, use the deepest step that is (often first visit to engaged visit), and say so. A gap is worth reporting when both sides have 30 or more users and the rates differ by more than 2 × √(p(1−p)(1/n1 + 1/n2)), with p the pooled rate. Warn when a channel or device that brings 20% or more of new users converts at under half the rate of the rest. Below 30 users a side, say "too few users to compare".

### 7. Onboarding emails

From call 12. Fail when the account has no live flow for new users (a welcome or onboarding flow, or one triggered by signup or by a list join). Warn when the only onboarding flow is purely time-based, with no message triggered by what the user did or didn't do. When Klaviyo isn't connected, mark it **unknown** and ask what emails go out after signup.

## Scoring

- **Grade:** start at 100. Each **fail** costs 12 points, each **warn** 5. An **unknown** costs nothing, but list it.
- **No grade** when 3 or more areas are unknown: a grade over half the journey would mislead. Say "not graded" and why.
- **Rating:** 85 or above is healthy, 65–84 needs work, under 65 is at risk.
- Print each area's result next to its deduction, so the grade can be checked.

## Finding the activation metric

The best activation event is the early action that best separates users who stay from users who leave. Compare, for each candidate action in the first week: week-4 retention of users who did it ÷ week-4 retention of users who didn't. The action with the biggest ratio, that enough users can reach in the first session, is the activation metric.

GA4's reporting API can't split one group of users by what they did and then follow them, so this comparison needs user-level data:
- **BigQuery export (untested until connected).** If the GA4 property is linked to BigQuery and the InsightfulPipe BigQuery connection is set up, run the comparison with `run_query` (`platform="bigquery"`) on the export's `events_*` tables: users by `user_pseudo_id`, first-week events, and whether they came back in week 4. Check the table name with `list_datasets` first. This path has not been run on a live account yet.
- **The product's own data.** Otherwise, ask the user for the same comparison from their product analytics or database, and mark every figure "from your data, not checked".

Typical candidates, to start the list: a first project with a first task in it (project tools), a first contact with a logged activity (CRMs), a first campaign sent (email tools), tracking installed and a first report opened (analytics), a first design made (design tools), a first message that gets a reply (chat tools).

Until it's found, use the user's best candidate and say that it hasn't been tested.

Later outcomes (paid conversion, lifetime value, satisfaction scores) sit in billing or survey data, not GA4. Ask for them when the user wants the onboarding tied to revenue, and mark them "from your data, not checked".

## Design the fix

Tie every recommendation to the stage that loses the most people, and to its numbers. A good onboarding gets each new user to the activation event by the shortest path, and gives them a reason to come back.

**Pick the onboarding model** from the product and its price:
- **Self-serve:** cheap or simple products with many signups. Everything happens in the product and by email, so the first-run screens and help content carry the load.
- **Assisted:** mid-priced products with some setup. Automate the basics, and send a person at the points where call 5 or 7 shows people stall.
- **Hands-on:** complex or expensive products. A named person runs the setup, with an agreed definition of "live" and a planned hand-over to support.

**Match the pattern to the drop:**

| Where people stall | Patterns that help |
|---|---|
| Between signup and the first step | ask one question at signup (role, goal or team size) and open on the matching first task; a screen that starts the first task instead of a tour |
| Inside the setup steps | a short guided setup that shows progress, saves partial work and lets people skip a step and come back; ask only for what the first result needs |
| After setup, before first value | empty screens that show what a full one looks like, with one clear first action and templates or sample data |
| Slow time to value | a checklist of 4 to 7 small, ordered tasks with visible progress; a hands-on walkthrough of the one key task, done in the real product in a few minutes |
| Feature confusion | reveal advanced features when they become relevant; a few dismissible hints, shown one at a time and remembered once closed |
| Week-1 return is low | messages triggered by what the user did or didn't do (below), and a visible next step after every success |

**The emails after signup.** Behaviour beats the calendar. Plan one message per trigger, each with one action:
- started signing up but didn't finish: you're almost done, with a link back to the step they left (needs an event when signup starts, or the email captured on the first step; without one, list it as a gap)
- right after signup: welcome, what to do first, one link that opens that task
- signed up but never came back: the account is ready, here's the one thing to do
- came back but didn't do the key action: why it matters, a direct link, and a short example from a similar user
- did the key action: well done, here's the next most useful thing
- still not active after about a week: ask what's in the way, and offer help or a call
- a deadline is coming (a plan or setup window) and the user isn't active: a summary of what they'd miss and a last offer of help

**Personalise** by role, goal, team size or the channel that brought them. Paid-ad visitors arrive with the ad's promise in mind, so their first screen should deliver that promise; organic visitors often need more explanation. If call 6 shows mobile users stall, the first-run must work on a phone.

**Avoid the usual mistakes:** a tour of every feature before the user has done anything; a pile of pop-ups, hints and emails at once; a finished setup with no obvious next step; the same path for every kind of user; a desktop-only first run; and changes shipped with no step tracked to show whether they worked.

**Ship it as a loop:** measure the biggest drop, write down why people might stop there, change one thing for a share of new users, compare the step rate, keep what wins and move to the next drop. Simplifying the first action, cutting setup steps, fixing empty screens and sending a welcome email with one clear action are usually quick wins; rebuilding the flow, personalising it and adding human touchpoints are bigger bets.

**Connect it to paid media.** Every user who never activates is acquisition spend with no return, so lifting activation from 25% to 40% gets 60% more active users from the same budget. Use the stage audiences below to bring stalled users back with the message for their stage, and check that each ad's promise is what the first screen delivers.

## Report format

1. **Header:** property, `START` to `END`, the activation event used (or "unknown"), and the grade or "not graded".
2. **Journey map:** the seven stages, users at each, the step rate and the share of new users; "not tracked" where it applies. Name the stage to fix first.
3. **Scorecard:** one row per area: result, the key number, one sentence on why.
4. **Top fixes,** up to 5. Tracking fixes for stages that aren't tracked come first, because they decide what can be ranked at all. The rest are ranked by the new users the stage loses each month: users lost over the window × 30 ÷ the days in the window. A fix whose loss can't be counted yet goes after the ones that can, and says why. Each has what to change, the pattern or email it uses, the evidence (call and numbers), the expected impact (the stage it moves and the users a month it goes after; never a promised lift), the effort (low: a setting, tag or filter; medium: a product or flow change; high: rebuilding the flow), and who does it ("I can do this now" or "do this in the product or GA4").
5. **Measurement plan,** when stages aren't tracked: the exact events to add, with GA4's recommended names where one exists (`sign_up`, `tutorial_begin`, `tutorial_complete`, `login`), plus one activation event, and which to mark as key events.
6. **Onboarding emails:** what exists, what each trigger above should send, and the gaps.
7. **Personalisation opportunities:** up to 4 segments (first channel, device, or what users read or say at signup), each with its number and call, and the first screen or email tailored to it. A segment under 30 users gets "too few users to compare", not a tailored path.
8. **Unknowns:** what couldn't be checked, and why.
9. **Go deeper:** the next skill to run for each area.

## Fixes this skill can run

Only after the user says yes to the exact change. Each needs a Read & Write connection, and an owner, admin or operator can switch write actions off. Offer a fix only when the events it uses fired in the window; an audience built on an event that never fires stays empty.

**Mark the activation event as a key event** (`create_key_event`, `platform="google-analytics"`), only when the event fires in the window and isn't a key event yet:
```json
{"action": "create_key_event", "property_id": "properties/<id>",
 "event_name": "ACTIVATION_EVENT", "counting_method": "ONCE_PER_SESSION"}
```

**Create a stage audience** (`create_audience`), for example "signed up, not activated in 14 days", to bring those users back with the message for their stage. Only when no audience in call 2 already does the same job. `membership_duration_days` can't be changed later.
```json
{"action": "create_audience", "property_id": "properties/<id>",
 "display_name": "Signed up, not activated",
 "description": "New signups who have not done the activation event; for onboarding re-engagement",
 "membership_duration_days": 30,
 "filter_clauses": [
   {"clauseType": "INCLUDE", "simpleFilter": {"scope": "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
     "filterExpression": {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [
       {"eventFilter": {"eventName": "SIGNUP_EVENT"}}]}}]}}}},
   {"clauseType": "EXCLUDE", "simpleFilter": {"scope": "AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS",
     "filterExpression": {"andGroup": {"filterExpressions": [{"orGroup": {"filterExpressions": [
       {"eventFilter": {"eventName": "ACTIVATION_EVENT"}}]}}]}}}}]}
```
Other stage audiences follow the same shape: "visited pricing, never signed up" (include a `pageLocation` filter, exclude the signup event) and "activated, not yet paying" (include activation, exclude the purchase or upgrade event).

It never changes the product, the site, tags, emails or flows. Those it writes up as recommendations.

## Without a connection

If GA4 isn't connected, or the product is tracked somewhere else, ask the user for:
- users at each stage over the last 12 weeks: new visitors, signups, each onboarding step, activation, and week-1 and week-4 return
- the days from signup to activation, if they have them
- the emails sent after signup, with what triggers each
- screenshots or a description of the first screens after signup

Run the same journey map, areas and design steps on their numbers, and mark every figure "from your data, not checked".

## Rules

- Every number comes from a call in this skill or from the user, and says which.
- Never guess the activation event, and never present a candidate as proven.
- When the journey isn't tracked, the most valuable output is the measurement plan. Say so plainly instead of padding the report with generic advice.
- Never present a share of user-days as a share of people.
- Name onboarding patterns only where the data points to the stage they fix.
- Don't run a write action without a yes to the exact payload.

## Go deeper

- **cro/signup-flow-cro:** the signup form and the steps before the account exists.
- **marketing/email-sequence-builder:** full copy for the onboarding emails.
- **marketing/funnel-dropoff-diagnostician:** the wider funnel beyond onboarding.
- **measurement/conversion-tracking-auditor:** checking that the events in the measurement plan fire and count as key events.
- **measurement/ga4-audience-retention** (if installed): retention by cohort, channel and device in more depth.
- **marketing/klaviyo-flow-auditor** (if installed): a full audit of the email flows.
