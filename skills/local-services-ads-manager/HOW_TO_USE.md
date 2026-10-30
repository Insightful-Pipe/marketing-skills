# How to Use This Skill

Hey Claude, I just added the "local-services-ads-manager" skill. Review my Google Local Services Ads for the last 30 days and tell me where my budget should go.

## What you need

- **Either the lead export or a connection.** Without any connection, download the lead report from the Local Services dashboard (Leads, then download) and paste your budget, bidding mode, bids, job types, hours and service areas. With the InsightfulPipe MCP and Google Ads connected, the skill pulls leads, credits, budget and bids itself; you still paste your Local Services hours, service areas and job types, because the skill's queries don't read those.
- **Job outcomes,** so it can count booked jobs: leads you marked Booked in Local Services, a CallRail tag your office sets on booked calls, or a list of booked jobs.
- **Your target,** if you have one: the most a booked job may cost, or your average job value and the share of it you'll spend on ads. Without it, the skill uses your own cost per booked job.
- **Optional connections:** CallRail (call outcomes and answered calls), Google Business Profile (reviews and hours) and DataForSEO (rating and review count of nearby rivals on Google Maps).

## Example requests

**Monthly review**
Hey Claude, I just added the "local-services-ads-manager" skill. Review my Local Services Ads for the last 30 days. We can spend up to 20% of a job's value on ads, and booked calls are tagged "Booked" in CallRail.

**From an export**
Hey Claude, I just added the "local-services-ads-manager" skill. Here's my Local Services lead export and my settings. Which job types and towns are worth paying for?

**Bad leads**
Hey Claude, I just added the "local-services-ads-manager" skill. I'm getting charged for spam and wrong-number calls. Find the leads worth rating and draft the feedback for each one.

**Budget question**
Hey Claude, I just added the "local-services-ads-manager" skill. Should I raise my Local Services budget? Show me the cost per booked job first.

## What you get

1. **A header** with spend, leads, charged and credited leads, booked jobs, cost per lead and cost per booked job.
2. **A fix plan** ranked by the money at stake this month, each fix with its numbers and who does it.
3. **Job type and area tables** with booking rate, cost per booked job, your target and a verdict.
4. **Responsiveness:** answer rate, missed charged calls, and the hours when calls go unanswered.
5. **Lead feedback drafts** for charged leads with evidence for a credit (spam, sales calls, wrong business, repeat callers), plus the out-of-area leads Google no longer credits.
6. **Reviews against nearby rivals,** budget use and bidding, verification, hours and service areas.

In the example, an invented plumbing and heating company finds that it spends 99% of its budget, AC repair books nothing in the 30 days, a town outside its wanted area takes spend, and six charged calls in 30 days went unanswered after 17:00 because the ad stays open after the office closes.

## What it can change for you

With your yes on the exact change, it can:
- change the Local Services daily budget (Google Ads `update_campaign`)
- tag Local Services calls in CallRail, so the next review joins them exactly (`update_call`)

Lead feedback, job types, hours, service areas and bids per category are changed by you in the Local Services dashboard; the skill tells you exactly what to change.

## Tips

- Run it monthly, and after changing job types, hours or service areas.
- Mark booked leads in Local Services, or tag them in CallRail, every day. The review is only as good as the booked count.
- Rate bad leads soon. Google decides every credit, so treat the money as possible, not promised.
