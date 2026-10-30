# How to Use This Skill

Hey Claude, I just added the "feature-adoption-planner" skill. Check which of our features keep customers around, and plan campaigns to raise adoption of the ones that do.

## What you need

- **A list of the features to check:** for each one, the event that means someone used it, its release date and the plans that include it.
- **Your product events,** in one of three forms: an export of events by user, a BigQuery table (a GA4 BigQuery export works), or GA4 connected through InsightfulPipe. GA4 alone gives adoption rates but not the retention check.
- **A past feature announcement, if you've done one:** the feature and the date. Your own result becomes the benchmark for the targets.
- **Optional:** Klaviyo or Mailchimp connected through InsightfulPipe, so the plan respects your last feature email and can draft the new one after you approve it.

## Example requests

**Pick the features worth pushing**
Hey Claude, I just added the "feature-adoption-planner" skill. Here's our events export and a list of our six main features. Tell me which ones are worth announcing to existing customers and which aren't.

**From BigQuery**
Hey Claude, I just added the "feature-adoption-planner" skill. Our product events are in BigQuery. Measure the feature adoption rate for recurring bookings, waitlist and deposits, and check whether the people who use them stay longer.

**From GA4 only**
Hey Claude, I just added the "feature-adoption-planner" skill. We only have GA4. Show me the 28-day adoption rate for each feature event and tell me what I'd need to see which features keep users.

**Why isn't anyone using it**
Hey Claude, I just added the "feature-adoption-planner" skill. We announced deposits twice and adoption is still low. Is it an awareness problem or a product problem?

**Plan and draft the campaign**
Hey Claude, I just added the "feature-adoption-planner" skill. Plan the adoption campaign for our top feature, write the in-app prompt and the email, and draft the email in Klaviyo once I approve it.

## What you get

1. **A feature table:** 28-day adoption, how many people who tried each feature used it again, and the retention lift against matched non-users, with a 95% interval.
2. **A status for each feature:** promote, test first, fix first, leave, or not graded, with the reason.
3. **A target for each campaign,** set from your own last feature push, and an estimate of the extra customers kept.
4. **A dated campaign plan:**
   - an in-app prompt tied to the moment the feature becomes useful;
   - an email;
   - a changelog entry and a help article;
   - a holdout group, kept out of every message;
   - two read-out dates.
5. **Finished copy** for the first campaign's in-app prompt, email and changelog line.
6. **Next steps** for the features that shouldn't get a campaign.

## What it can change for you

With your yes on the exact payloads, it can:
- create a Klaviyo list of the messaged group, an email template and a draft campaign;
- or create a Mailchimp segment and a draft campaign.

It never sends a campaign and never runs anything but read-only queries in BigQuery.

## Tips

- Name the moment just before each feature is useful, for example "a fully booked day". That moment is the in-app trigger, and it matters more than the copy.
- Keep the holdout. Without it, you can't tell whether the campaign or the season moved adoption.
- Re-run the check after the retention read-out, and again a month after any fix to a "fix first" feature.
