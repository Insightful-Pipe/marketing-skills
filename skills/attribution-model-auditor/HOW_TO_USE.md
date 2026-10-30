# How to Use This Skill

Hey Claude, I just added the "attribution-model-auditor" skill. Audit how my conversions are attributed and tell me whether I can trust the numbers my campaigns bid on.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your ad accounts added:** Google Ads, Meta, LinkedIn Ads, Microsoft Ads or TikTok Ads, whichever you run. The skill reads the settings and numbers itself; you don't export anything.
- **GA4 for the same website,** if you have it. It adds the first-touch and last-touch view of your channels.
- **Your real count** of leads, sign-ups or orders for the period, from your CRM or store, if you have it. Without it, the over-count check is marked unknown.
- **How long your customers take to buy,** if you know. Without it, the skill measures it from Google Ads.

If a platform isn't connected, tell the skill its attribution setting and reported conversions, and it grades that platform from what you give, labelled as yours.

## Example requests

**Full audit**
Hey Claude, I just added the "attribution-model-auditor" skill. Audit attribution across my Google Ads, Meta and GA4 for the last 90 days. Our CRM had 410 new leads in that time.

**Numbers that don't match**
Hey Claude, I just added the "attribution-model-auditor" skill. Google Ads and Meta together claim more conversions than we had. Show me where the double counting comes from.

**Windows**
Hey Claude, I just added the "attribution-model-auditor" skill. Are my attribution windows right for how long people take to buy from us?

**Which channels open and close**
Hey Claude, I just added the "attribution-model-auditor" skill. In GA4, which channels bring people in first and which ones get the last click before they convert?

**Explain a model**
Hey Claude, I just added the "attribution-model-auditor" skill. What's the difference between data-driven and last click, and which should we use?

## What you get

1. **A health rating** (GOOD, NEEDS WORK or CRITICAL) with the counts behind it.
2. **A scorecard for six areas:** tracking coverage, what counts as a conversion, windows against time to convert, attribution models, click against view credit, and cross-platform agreement.
3. **A rules table:** every counted conversion on every platform, with its windows, model and counting.
4. **Time to convert:** how many conversions arrive the same day, within 7 and within 30 days, per action, and whether each window is too short (it cuts conversions off) or longer than needed (it credits late touches).
5. **GA4's three views** of the same key events, showing which channels open journeys and which close them.
6. **The over-count:** how far the platforms' sum sits from your real count, and where overlap comes from.
7. **A model, window and source-of-truth recommendation,** where your measurement stands and its next step, an action plan in three time frames, and what to monitor.
8. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can update a Google Ads conversion action's click or view window, or make an overlapping action secondary. It never changes counting, models or settings on other platforms; it tells you what to change there.

## Tips

- Use 90 days or more. Short periods hide slow conversions.
- Give your real count. It turns "the platforms disagree" into "the platforms claim this much more than happened".
- Rerun after any change to windows, counted actions or tags, and once a quarter.
