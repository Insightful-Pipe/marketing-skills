# How to Use This Skill

Hey Claude, I just added the "email-campaign-analyst" skill. How are my email campaigns doing over the last 90 days, and what should I change?

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Klaviyo or Mailchimp account added.** The skill pulls campaigns, reports, events and audience data itself; you don't need to export anything.
- **The window,** if not the last 90 days. For a monthly report it uses the last full calendar month and compares it with the month before.
- **On Klaviyo, your subject lines,** only if your campaign names aren't your subject lines. The Klaviyo data this skill reads doesn't include the subject field.

## Example requests

**Campaign report**
Hey Claude, I just added the "email-campaign-analyst" skill. Rank my Klaviyo campaigns from the last 90 days by revenue per recipient, with opens, clicks and unsubscribes.

**Monthly email report**
Hey Claude, I just added the "email-campaign-analyst" skill. Give me last month's email report compared with the month before, with the top and bottom three campaigns.

**Deliverability**
Hey Claude, I just added the "email-campaign-analyst" skill. Check my bounce, spam complaint and unsubscribe rates and tell me which campaigns caused problems.

**Subject lines and send time**
Hey Claude, I just added the "email-campaign-analyst" skill. Which subject line styles and which send days and times get the most clicks for us?

**List growth**
Hey Claude, I just added the "email-campaign-analyst" skill. Show my audience growth and unsubscribes month by month.

**Mailchimp clean-up**
Hey Claude, I just added the "email-campaign-analyst" skill. Find my inactive Mailchimp subscribers, tag them, and show me the list before archiving anyone.

## What you get

1. **A grade out of 100** with the math shown, or "not graded" with the reason when there isn't enough volume (at least 3 sent campaigns and 1,000 delivered emails for campaign performance and deliverability; at least 100 subscribe plus unsubscribe events for audience growth).
2. **A scorecard:** campaign performance and revenue, deliverability, and audience growth are graded; subject lines, send time and email versus SMS are insights.
3. **A campaign table** ranked by revenue per recipient, or by click rate when no revenue is tracked.
4. **Subject line patterns, the best send slot and email versus SMS,** each with its sample size, so you know how much to trust it.
5. **On Mailchimp:** A/B test winners, top links, ecommerce revenue by campaign, automation performance, segments and tags, and inactive subscribers.
6. **The top actions,** each tied to the numbers behind it.

## What it can change for you

On Mailchimp, with your yes on the exact members, it can:
- tag members by engagement (for example engaged, at risk, inactive)
- archive inactive members (archived members can be re-added later)

It never sends, schedules or edits campaigns, and never permanently deletes anyone. On Klaviyo it changes nothing; list clean-up there belongs to the Klaviyo Flow Auditor skill.

## Tips

- Open rates are inflated by mail privacy features, so the skill grades on clicks, revenue, bounces, complaints and unsubscribes.
- Send-time results are patterns, not proof. Use an A/B send-time test to confirm a new slot.
- The Mailchimp path was written from the Mailchimp schemas and hasn't yet been run on a live Mailchimp account.
