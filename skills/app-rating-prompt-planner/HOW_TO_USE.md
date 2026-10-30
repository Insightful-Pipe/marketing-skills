# How to Use This Skill

Hey Claude, I just added the "app-rating-prompt-planner" skill. Check our app's rating prompt against the App Store and Google Play rules and plan when we should ask for ratings.

## What you need

- **Your app's store ids:** the Apple numeric id or bundle id, and the Google Play package name. One store is enough.
- **How your rating prompt works today:** what triggers it, any dialog or question before it, any Rate us button, any reward.
- **Your event list:** the events your app logs and what each one means, with the last 28 days of counts and users per platform.
- **Reviews with star, text and app version,** pasted or uploaded from App Store Connect or Play Console, if nothing is connected.
- **Your last few release notes,** so a drop can be lined up with what changed.
- **Optional, with the InsightfulPipe MCP:** the Apple App Store, Google Play and Google Analytics servers connected. The skill then reads ratings, reviews by version and your GA4 app events itself.

## Example requests

**Prompt plan**
Hey Claude, I just added the "app-rating-prompt-planner" skill. Plan when our app should show the in-app review prompt on iOS and Android. Here are our events and how the prompt works today.

**Rules check**
Hey Claude, I just added the "app-rating-prompt-planner" skill. We show "Enjoying the app?" before the rating card and send No answers to support. Is that allowed on the App Store and Google Play, and what should we do instead?

**Ratings dropped after an update**
Hey Claude, I just added the "app-rating-prompt-planner" skill. Our ratings dipped after the last release. Compare the reviews by version and tell me what changed.

**Release check**
Hey Claude, I just added the "app-rating-prompt-planner" skill. Version 6.5 has been live for two weeks. Run the release check against 6.4.

## What you get

1. **A baseline per store:** summary rating, ratings count and the reviews read.
2. **Reviews by version,** with average stars, low-star share, the top complaint themes and a better, worse or no clear change verdict for each version.
3. **A rules check of your current prompt,** each check marked pass, breaks a rule or risk, with the rule it comes from.
4. **The prompt plan:** the trigger moments picked from your own events, who is eligible, app-side limits, a store link for Settings, the event to log and a code-level spec for iOS and Android.
5. **A feedback route** that is always available and never stands in front of the store prompt, plus a reply list for reviews about issues you have fixed.
6. **A rating target per store,** set from your own best version.
7. **A release check** to run after every version.

## What it can change for you

Nothing. It reads store and analytics data and writes the plan; your developers ship the change.

## Tips

- Log a `rating_prompt_requested` event when the app calls the review API, so the release check can see the trigger firing.
- Run the release check after every version, not once.
- If your current prompt asks a question first, expect the average to settle once every user can reach the card. The skill measures the next version without the question as the new baseline.
