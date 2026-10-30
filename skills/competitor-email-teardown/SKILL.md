---
name: competitor-email-teardown
description: Email marketing competitor analysis from real inboxes. Measures the emails each rival sends after someone signs up (minutes to the first email, emails in the first 14 days, regular sends a week, signup offer, discount depth and whether it climbs, subject line patterns, the promotional, product and content mix, and how early a sale is announced), sets them beside the user's own program read live from Klaviyo or Mailchimp through the InsightfulPipe MCP or from the user's own seed inbox, and returns what to adopt, what to avoid and three tests sized on the account's own volume. Works from dated inbox exports the user pastes or uploads. Use when someone asks to analyze, benchmark, track or tear down competitors' emails, newsletters, welcome series or email promotions. Never signs up for anything and changes nothing.
---

# Competitor Email Teardown

Turns a few weeks of rival emails into numbers you can set beside your own program. Every measure has one fixed definition, so a rival's inbox and yours are counted the same way. Your own side adds what no inbox can show: your click and order rates and your signup volume, which decide which gaps are worth a test and how long each test takes.

## Before you start

### The research inboxes (the user does this, never Claude)

Ask whether the user already has rival emails with dates. If not, give them this setup and stop until they have at least 28 days of mail:

1. Make one address per rival on a domain or mailbox the business owns, for example `research+rivalname@yourbrand.com`. Never use a person's private address, a colleague's name, or anyone else's details.
2. Sign up to every rival on the same day, from their own signup form, and write down the exact time of each signup and the offer the form showed.
3. Sign your own seed address up to your own list the same day, the same way. Your program is then measured exactly like theirs.
4. Leave the inboxes alone. Don't buy anything and don't enter payment details. Starting a cart with the research address is optional; if the user does it, note which rival and when, because that triggers cart emails the comparison would otherwise miss.
5. Wait 56 days if you can, ideally across one sale event (a holiday, a seasonal sale). 28 days is the minimum.
6. When the teardown is done, unsubscribe the research addresses.

Claude never fills in a signup form, never creates an inbox and never subscribes anyone.

### What to ask

1. **The rivals.** Two to five, with their sites.
2. **The window and time zone.** Default: day 0 is the signup date, through day 55, in the user's time zone.
3. **The sale event** inside the window, with its date. Default: none; the sale rows are then "not graded".
4. **The discount ceiling:** the deepest discount the business will ever give. Default: the deepest % off in the user's own emails in the window.
5. **The smallest lift worth detecting** in a test. Default: 20% relative.

### The emails, without a connection

Ask for every email each inbox received in the window, as a paste, a CSV, or a mailbox export (Gmail: put each rival under its own label, then export with Google Takeout as MBOX; Outlook: export the folder). Each email needs:
- received date and time, with the time zone
- sender name
- subject and preview text
- the body text, or the first lines of it

Plus, per program: the signup time and the offer the signup form showed. For the user's own results without a connection, ask for the welcome or onboarding report for the last 90 days (recipients, click rate, orders or conversions per email) and the campaign report for the same 90 days.

## How to run the queries

With the InsightfulPipe MCP connected:
1. Call `query_contexts` with `request="accounts"` for `klaviyo` or `mailchimp`. Note `workspace_id`, `brand_id` and the account. If there are several, ask which one is the user's own.
2. Call `query_contexts` with `request="actions_details"` for the actions below and follow the body shapes it returns.

Every read goes through `query_data`. Rules found on a live account:
- **An empty answer is not an error.** An account with no flows or campaigns answers `success` with an empty list. Say "no history" for that part.
- **Klaviyo rates are fractions** (0.0125 is 1.25%).
- **Never fire calls in parallel.** On a 429, wait the `retry_after` seconds and retry once.
- If a call fails, mark that part **unknown**, name the call, and never fill the gap with a guess.

### Your own program: Klaviyo

Which automations exist:
```json
{"action": "get_flows", "fields[flow]": "name,status,trigger_type", "auto_paginate": true}
```
Welcome and other flow results per email, last 90 days:
```json
{"action": "get_flow_report", "body": {"data": {"type": "flow-values-report", "attributes": {"timeframe": {"key": "last_90_days"}, "filter": "equals(send_channel,\"email\")", "group_by": ["flow_id", "flow_message_id", "flow_name", "flow_message_name"], "statistics": ["recipients", "click_rate", "unsubscribe_rate", "conversions", "conversion_rate"]}}}}
```
Campaigns sent, and their results for the same 90 days:
```json
{"action": "get_campaigns", "filter": "and(equals(messages.channel,'email'),equals(status,'Sent'))", "fields[campaign]": "name,send_time", "sort": "-created_at", "auto_paginate": true}
```
```json
{"action": "get_campaign_report", "body": {"data": {"type": "campaign-values-report", "attributes": {"timeframe": {"key": "last_90_days"}, "group_by": ["campaign_id", "campaign_message_id", "send_channel"], "statistics": ["recipients", "click_rate", "unsubscribe_rate", "conversion_rate"]}}}}
```
- `get_campaigns` fails without the channel filter, and status values are Title Case.
- The report actions count conversions on the account's `Placed Order` metric unless you pass `conversion_metric_id`; `meta.report.conversion_metric` names the one used.
- Flow delays are not in these actions. Your welcome timing comes from the seed inbox.

**No seed inbox export?** Read what your own seed profile received instead:
1. `get_metrics` (`auto_paginate: true`), and keep the id of `Received Email`.
2. `get_profiles` with `"filter": "equals(email,'<SEED_ADDRESS>')"`. Use only the user's own test address, never a customer's.
3. `get_events` with `"filter": "and(equals(metric_id,\"<RECEIVED_EMAIL_ID>\"),equals(profile_id,\"<PROFILE_ID>\"))"`, `"sort": "datetime"`, `"auto_paginate": true`.
- Don't pass `fields[event]` with `profile_id`; the call fails (allowed fields are `datetime`, `event_properties`, `id`, `timestamp`, `uuid`). An unknown profile id returns "does not exist".
- Each event gives the time, and its `event_properties` carry the subject (Klaviyo names it `Subject`; check the first event's keys). Preview text and body are not there, so offers inside the body need the inbox export. Say so in "Not captured".

### Your own program: Mailchimp (untested until a Mailchimp account is connected)

- `list_automations`, then `list_automation_emails` with each `workflow_id`: each email's delay and subject.
- `list_campaigns` with `status` `sent` and `since_send_time` 90 days back: `send_time`, `settings.subject_line`, `settings.preview_text`, `recipients.recipient_count`.
- `list_reports` with the same `since_send_time`: `emails_sent`, `clicks.click_rate`, `unsubscribed`.
- Customer Journeys built in Mailchimp's newer editor may not appear in `list_automations`. Then the seed inbox is the only timing source.

### The rivals' public signals

**Signup offer on the page.** The site crawler's text checkers return nothing on many storefronts (bot walls, popups drawn by scripts), so take a picture instead:
```json
{"platform": "screenshot", "action": "capture", "url": "https://www.rival.example", "include_desktop": false, "include_mobile": true, "modes": ["mobile"]}
```
It returns `data.captures.mobile.public_url`, a full-page image. Read the signup offer from it. The capture can render in another country's currency and may not show a popup; if no offer is visible, use what the user saw when they signed up.

**Signup offer in paid ads (optional).** `ads-libraries`:
- `facebook_search_companies` with `query` (the rival's name) and `country` `US`, to get the `page_id`. Pick the verified page that matches the site.
- `facebook_company_ads` with `page_id`, `country`, `max_ads` 30 and `trim` true. Rows are under `data.results`; `start_date` is in Unix seconds. Catalog ads have empty `body_text`, and the call can return more rows than `max_ads`.
- Count the active ads whose text offers something on the first order. A rival paying to advertise its signup offer is telling you the offer earns its keep.

## The measures

Count every program the same way. Day numbers are calendar days after the signup date in the window's time zone; the signup day is day 0.

| Measure | Definition |
|---|---|
| Minutes to first email | first received time minus the signup time |
| Emails in the first 14 days | every email received on days 0 to 13 |
| Regular emails a week | emails on days 14 to the window's last day that don't name the sale event, divided by the number of weeks in that span |
| Offer | the email offers `N% off`, `$N off`, free shipping, a free sample, a free gift, 2 for 1 or buy one get one, anywhere in the subject, preview or body |
| Type | **promotional** if it has an offer; otherwise **product** if it announces something new, back in stock, a new harvest or now available; otherwise **content** |
| Signup offer | the offer in the first email: a % off, a non-discount offer (such as a free sample), or none |
| Deepest % off | the highest % off in any email in the window |
| Climbing welcome offer | among days 0 to 13, the emails that carry a % off and mention a code or the first order: yes when a later one offers more than an earlier one |
| Subject patterns | median length in characters, and the share of subjects with a number, an offer, an urgency word (end, ends, ending, last chance, tonight, final hours, today only, hours left), a question mark, an emoji |
| Sale timing | for emails naming the sale event: how many days before the event the first one arrived, how many there were, the most in one day, the deepest offer, and whether one said "extended" after an earlier sale subject used an urgency word |
| Usual send | the most common weekday and the most common send time, sale emails left out |

The rival median is the median across rivals; the user's own program is never part of it.

## Decisions

### Adopt

Adopt only a change that costs no margin, adds no regular sends, and that at least 2 rivals share:
- **Welcome speed.** Your first email takes more than 60 minutes and at least 2 rivals send theirs within 10: send email 1 on signup.
- **Sale lead time.** Your first sale email arrives less than 2 days before the event and at least 2 rivals start 2 or more days ahead: announce the next sale to subscribers at least 2 days before.

### Avoid

List a rival pattern under "avoid" when the inbox shows:
- **A deceptive subject:** starts with `Re:` or `Fwd:` with no earlier thread, or claims an order or account action that never happened. US CAN-SPAM forbids deceptive subject lines.
- **A deadline that moves:** a sale said it was ending, then came back as extended.
- **A discount above the user's ceiling,** with the climbing welcome offer named when there is one.

### Test candidates

| Gap | Becomes a candidate when | Metric | Unit and volume |
|---|---|---|---|
| Subject style | your median subject length is 10 or more characters away from the rival median | campaign click rate | one campaign recipient; half the average campaign recipients per arm per send |
| Welcome length | you send at least 2 fewer emails in the first 14 days than the rival median | welcome orders per new subscriber (welcome flow conversions ÷ welcome email 1 recipients) | one new subscriber; half the weekly new subscribers per arm |
| Signup offer depth | your signup % off is 5 or more points away from the rival median (a rival with no discount counts as 0) | welcome email 1 placed-order rate, then margin per new subscriber | one new subscriber; half the weekly new subscribers per arm |

New subscribers a week = welcome email 1 recipients over the last 90 days ÷ (90 ÷ 7), rounded. Use click rate, not open rate: Apple Mail Privacy Protection opens almost every email it receives.

**Frequency is not a test here.** When your regular emails a week are 0.5 or more away from the rival median, list it as a handoff: a frequency change plays out per person over weeks, and it needs your own unsubscribe and complaint history.

**Size each test:** n per arm = ⌈(1.959964 + 0.841621)² × (p1(1 − p1) + p2(1 − p2)) ÷ (p2 − p1)²⌉, with p1 the baseline from your own data and p2 = p1 × (1 + the smallest lift). That is 5% significance, two-sided, at 80% power. Time to read = n ÷ your volume per arm, rounded up to whole sends or weeks. A test that needs more than 12 weeks is marked **slow**; say what lift it could read in 12 weeks instead.

**Pick three.** Rank candidates by how many rivals sit on the other side of your value, then by the units affected each week. The top three are the tests; the rest are "later".

## The report

1. **Summary:** the window, the emails read per program, and the two biggest gaps.
2. **Side by side:** one row per measure, a column per program, and the rival median.
3. **Rival profiles:** per rival, its signup offer, what the signup page said, how many active ads push the signup offer, its usual send, its sale timing, and a two-line read of its program.
4. **Your results:** live and draft flows, new subscribers a week, welcome and campaign click and order rates.
5. **Adopt, avoid, three tests and handoffs,** each with the numbers behind it.
6. **Not captured:** what the inboxes couldn't see, such as cart flows that were never triggered and every rival's own results.

Rival patterns show what rivals do, not that it works for them. Say so once, and let the tests decide.

## What this skill changes

Nothing. It reads, measures and recommends. It never edits a flow, a campaign or a signup form, and never sends or schedules an email.

## Rules

- Never sign up, subscribe or create an inbox for the user, and never use a real person's details for research.
- Quote rival subject lines as evidence; never republish a rival's email body or images.
- Count every program with the same definitions and the same window.
- Every number in the report comes from the inboxes or from a call this skill made.
- No em or en dashes in the report.

## Go deeper

- **klaviyo-flow-auditor**, if installed: audit your own flows end to end.
- **email-sequence-builder**, if installed: write the extra welcome emails a test calls for.
- **email-campaign-calendar**, if installed: set a send frequency from your own fatigue history.
- **competitor-swot-analyzer** and **competitor-ad-research**, if installed: the rest of each rival's marketing.
