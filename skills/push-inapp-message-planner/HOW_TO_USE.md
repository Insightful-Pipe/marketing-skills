# How to Use This Skill

Hey Claude, I just added the "push-inapp-message-planner" skill. Plan our push notifications and in-app messages: when to ask for permission, which moments get a push, how many a week, and the copy.

## What you need

- **Nothing connected, at the least.** Describe your app (iOS, Android, web), the moments your users want to hear about, and the pushes and in-app messages you send today.
- **Your push provider's export,** if you have one: opted-in devices, pushes delivered, opt-outs and uninstalls per day, direct opens per message, and permission prompt results. The caps come from it. No push provider has a connector, so this is always an export.
- **Better: the InsightfulPipe MCP connected to Claude,** with GA4 and Klaviyo. The skill then reads your active users by platform and hour, your onboarding events and your email flows itself, and pulls your public App Store and Google Play reviews.

## Example requests

**Full push notification strategy**
Hey Claude, I just added the "push-inapp-message-planner" skill. Here is our push provider export for the last 12 weeks. Build our push notification strategy, with caps and the copy for each message.

**People keep turning notifications off**
Hey Claude, I just added the "push-inapp-message-planner" skill. Our opt-outs went up after we started weekly promo pushes. How many pushes can we send, and which ones should go?

**When to ask for permission**
Hey Claude, I just added the "push-inapp-message-planner" skill. We ask for notification permission on first launch and only 40% of iPhone users say yes. Where in onboarding should we ask instead?

**Push notification examples for our app**
Hey Claude, I just added the "push-inapp-message-planner" skill. We run a food delivery app. Write the push and in-app messages for order updates, a first-order nudge and a lapsed customer, within the length limits.

## What you get

1. **Reach per platform:** how many devices can get a push on iOS, Android 13 and later, older Android and the web, and why.
2. **What store reviews say** about your notifications, sorted into themes, each turned into a rule.
3. **The permission plan:** which onboarding step to ask after, the soft ask copy, and what to do after a "not now".
4. **Quiet hours and a send window** from your own users' hours.
5. **Daily and weekly caps** from your own opt-outs and uninstalls.
6. **A channel for each moment:** push, in-app or email, checked against your email flows so nothing stacks.
7. **The copy** for each message, checked against length budgets, with a deep link.
8. **What to track,** with today's baselines.

## What it can change for you

Nothing. It reads and plans; it sends no message and changes no setting.

## Tips

- Give it 12 weeks of daily export so each load level has enough days behind it.
- If your web app can be added to the Home Screen, say so: it decides whether iPhone visitors can get web push.
- Run it again 4 weeks after a change to the prompt or the caps, and compare the baselines.
