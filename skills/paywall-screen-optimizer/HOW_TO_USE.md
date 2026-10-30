# How to Use This Skill

Hey Claude, I just added the "paywall-screen-optimizer" skill. Here are our paywall screenshots. Find the placements losing the most starts, check the screens against the App Store and Google Play rules, and write tests we can actually run.

## What you need

- **Views and starts for each placement** over the last 28 days. With GA4 connected through the InsightfulPipe MCP, the skill pulls them itself, as long as your paywall events carry the placement as a parameter. Without GA4, paste the counts from your paywall tool or product analytics: viewers and starts per placement.
- **A screenshot of each paywall design,** or a description: headline, plans, which plan is preselected, every price and its size, the trial line, the button, when the close control appears, and the links.
- **Your plans and prices,** with the billing period and any trial.
- **Where it runs:** iOS, Android, web, or several.

## Example requests

**Find the weakest placement**
Hey Claude, I just added the "paywall-screen-optimizer" skill. Our paywall shows after onboarding, at the daily limit and on locked features. Pull the last 28 days from GA4 and tell me which placement is losing the most starts.

**Check a screen before review**
Hey Claude, I just added the "paywall-screen-optimizer" skill. Here's our new annual-plan paywall. Check it against the App Store and Google Play subscription rules before we submit the update.

**Write paywall A/B tests**
Hey Claude, I just added the "paywall-screen-optimizer" skill. Write test variants for our two weakest paywall placements and tell me how many weeks each test needs at our volume.

**From pasted numbers**
Hey Claude, I just added the "paywall-screen-optimizer" skill. Here are viewers and purchases per placement from our paywall tool, plus the screenshots. We don't use GA4. Run the review on these.

**Web upgrade screen**
Hey Claude, I just added the "paywall-screen-optimizer" skill. Our web app shows an upgrade modal when a free user hits the project limit. Review it and check Clarity for dead clicks on the upgrade page.

## What you get

1. **A placement inventory:** every moment the paywall shows, its screen and its viewers.
2. **A measurement check:** whether your start events carry the placement, and what can't be graded.
3. **The start rate for each placement,** with plan mix and list value per 1,000 views, ranked by the starts each one loses against your own median.
4. **Store and disclosure checks for each screen design:** billed amount, plan terms, trial terms, restore, terms links, cancel, and whether each "save X%" badge matches your prices, each fail with the rule it breaks.
5. **Choices worth testing:** why-now headline, default plan, button wording, and the close control.
6. **One variant each for the two weakest placements,** compliant before it ships.
7. **A test plan** sized to each placement's weekly views, saying which tests run as A/B tests and which are too slow at your volume.

## What it changes

Nothing, unless you ask it to register your placement or plan parameter as a GA4 custom dimension. It shows the exact request first and runs it only after you say yes.

## Tips

- Send the same placement parameter on the purchase or trial start event as on the paywall view. Without it, per-placement rates can't be measured.
- Ship the store-rule fixes before any test, so both arms are ones the stores accept.
- Rerun it 28 days after the changes ship to see each placement move.
