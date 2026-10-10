# How to Use This Skill

Hey Claude, I just added the "onboarding-cro" skill. Map our new-user journey from first visit to activation and tell me where onboarding loses people.

## What you need

- **The InsightfulPipe MCP connected to Claude, with the GA4 property that records your product.** The skill pulls the events, pages, channels and weekly cohorts itself; you don't export anything.
- **Klaviyo connected (optional),** so it can check the emails that go out after signup.
- **Your signup event, onboarding step events and activation event,** if you know them. Without them it uses GA4's recommended names (`sign_up`, `tutorial_begin`, `tutorial_complete`) and the first key event that fires.
- **One line on the product and who it's for,** so it can pick the right onboarding model.

## Example requests

**Find the leak**
Hey Claude, I just added the "onboarding-cro" skill. Our signups are fine but few people stick around. Find the onboarding step that loses the most new users over the last 12 weeks.

**Map the journey**
Hey Claude, I just added the "onboarding-cro" skill. Map the journey from first visit to signup, setup and first value for our product, with the numbers at each step and where it goes dark.

**Time to value**
Hey Claude, I just added the "onboarding-cro" skill. How many days after their first visit do new users reach `project_created`, and how many come back the week after?

**Design the onboarding**
Hey Claude, I just added the "onboarding-cro" skill. Find our weakest onboarding step, then design the first-run screens and the emails after signup to fix it.

**Find the activation metric**
Hey Claude, I just added the "onboarding-cro" skill. Help me pick our activation metric. Our candidates are `report_created`, `teammate_invited` and `integration_connected`.

## What you get

1. **A journey map** in seven stages, from arrival to activation and return: new users at each stage, the step rate, and "not tracked" where the data stops.
2. **A scorecard** for seven areas: measurement, hand-off to signup, onboarding completion, activation and time to value, early return, segments, and onboarding emails. A grade out of 100 when enough of the journey is tracked, or "not graded" with the reason.
3. **Up to 5 fixes:** tracking fixes first, then the rest ranked by the new users each stage loses a month, each with the onboarding pattern or email it uses, the numbers behind it, the expected impact and the effort.
4. **A measurement plan** when stages aren't tracked: the exact events to add and which to mark as key events.
5. **An onboarding email plan** built on what the user did or didn't do, and what your current flows already cover.
6. **Personalisation opportunities:** the segments worth a tailored first screen or email, each with its number.
7. **What couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- mark your activation event as a GA4 key event
- create a GA4 audience for a stage, such as "signed up, not activated", for re-engagement campaigns

It offers these only for events that actually fire. It never changes your product, site, tags or email flows; those come as recommendations.

## Good to know

- If your GA4 property only tracks the marketing site, the report shows the journey up to the signup click and gives you the tracking plan for the rest. That is often the most useful first result.
- Finding which early action predicts users staying needs user-level data: a GA4 BigQuery export connected through InsightfulPipe (not yet tested on a live account), or numbers from your own product analytics.
- Run it again a few weeks after a change to see whether the step rate moved.
