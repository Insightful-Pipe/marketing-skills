# How to Use This Skill

Hey Claude, I just added the "growth-experiment-backlog" skill. Build a growth experiment backlog from my GA4 and ad data, score it with ICE, and plan the next six weeks of tests.

## What you need

- **Nothing connected is fine.** Paste your funnel counts for the last 28 days and the 28 days before (visitors, then each step up to the goal), your idea list, and any finished tests with visitors and conversions per version.
- **With the InsightfulPipe MCP connected,** the skill reads GA4 for the funnel, Google Ads, Meta Ads and Search Console for acquisition ideas, and Google Sheets for an existing results log.
- **Your goal event,** such as purchases, paid plans, booked demos or leads.
- **Build hours per week** for experiments, if you know them. Without them, it plans for 10.

## Example requests

**Build the backlog**
Hey Claude, I just added the "growth-experiment-backlog" skill. Find the weakest step in our funnel from GA4 and build a ranked experiment backlog around it. Our goal is paid plans.

**ICE scoring for your own ideas**
Hey Claude, I just added the "growth-experiment-backlog" skill. Here are 12 test ideas from our team. Score them with ICE against our real traffic and tell me which ones we can actually test.

**RICE framework instead**
Hey Claude, I just added the "growth-experiment-backlog" skill. Prioritise these growth ideas with the RICE framework. Some touch the homepage, some touch Google Ads, and one is a new channel.

**Six-week sprint**
Hey Claude, I just added the "growth-experiment-backlog" skill. We have 8 build hours a week. Plan a six-week experiment sprint from our backlog, with readout dates and stop rules.

**Log finished tests**
Hey Claude, I just added the "growth-experiment-backlog" skill. Our pricing test ended: control 2,140 visitors and 96 sign-ups, variant 2,155 visitors and 121 sign-ups. Did it win? Add it to the results log and re-score the backlog.

**Growth hacking ideas for your funnel**
Hey Claude, I just added the "growth-experiment-backlog" skill. Give me growth hacking ideas we can test this month, based on where our funnel loses the most people.

## What you get

1. **The funnel,** step by step, with what changed for real since the prior 28 days and the weakest step named.
2. **A results log** of finished tests: lift, interval, p-value, split check, verdict, lesson and next step.
3. **A ranked backlog:** one hypothesis card per idea, ICE or RICE scores with the numbers behind each part, and the sample size and run weeks each test needs.
4. **A "not testable at this traffic" list,** with the smallest lift each one could detect and what would make it testable.
5. **A six-week sprint:** builds, live tests and readouts week by week, plus what waits for the next sprint and why.

## What it can change for you

With your yes on the exact change, it can:
- add a new tab with the backlog to a Google Sheet
- add finished tests to the empty rows of your results log in Google Sheets

It never launches, pauses or edits a test, an ad or a page.

## Tips

- Run it at the start of each sprint, and log every finished test, even the losses. The log raises or lowers Confidence on related ideas.
- If most ideas land on the "not testable" list, test earlier in the funnel where traffic is bigger, or make each change bolder.
- Give it your real build hours. A sprint planned past them slips.
