# How to Use This Skill

Hey Claude, I just added the "meta-click-to-message-ads" skill. Review our WhatsApp, Messenger and Instagram chat ads for the last 30 days against our chat outcomes, and tell me which ads bring sales, not just chats.

## What you need

- **For a review:** your ad results by ad (the Meta MCP server connected through InsightfulPipe, or an Ads Manager export with amount spent and "Messaging conversations started"), plus a chat export from your inbox, CRM or sheet: one row per chat with the ad it came from, start and first-reply times, and whether it qualified, booked and bought.
- **Your target cost per sale,** or your average sale value and margin so the skill can work out break-even.
- **Who answers chats, and when:** staffed days and hours, languages, and whether a bot answers first.
- **For a new ad:** your business type, the offer, which chat app your customers use, and an image or video.

No connection? Paste or upload the exports and describe the business. The skill does the same math.

## Example requests

**Review chat ads against sales**
Hey Claude, I just added the "meta-click-to-message-ads" skill. Here's our Ads Manager export and our CRM export of every chat. A sale is a paid order and our target is $40 per sale. Which ads should we pause?

**Plan a click-to-WhatsApp ad**
Hey Claude, I just added the "meta-click-to-message-ads" skill. We're a home cleaning company in Mexico City and customers prefer WhatsApp. Plan a click-to-WhatsApp ad with the greeting, the prefilled message and the starters. We answer Monday to Saturday, 8 to 6.

**Messenger ads with cheap chats and no sales**
Hey Claude, I just added the "meta-click-to-message-ads" skill. Our Facebook Messenger ads get conversations for a few dollars each but almost nobody buys. Find out where the chats break.

**Build it paused**
Hey Claude, I just added the "meta-click-to-message-ads" skill. Plan an Instagram Direct message ad for our salon and build it in my Meta account, paused. Show me the payloads first.

## What you get

1. **A per-ad table:** spend, conversations started, cost per conversation, chats matched, qualified rate, cost per qualified chat, sales, cost per sale, return and a verdict (scale, keep, fix, pause or too early) against your own target.
2. **Up to 5 findings** ranked by the spend they touch, each with the numbers behind it and who does the fix.
3. **Reply speed against sales,** and how many chats arrive when nobody is answering.
4. **A message kit** for every ad to fix or build: ad text, greeting, WhatsApp prefilled message, three starters, the first human reply and the qualification questions.
5. **Paused payloads** for any new ad, each marked "not run" until you say yes.

## What it can change for you

With your yes on the exact payload, and a Read & Write connection, it can:
- create a campaign, an ad set with a WhatsApp, Messenger or Instagram Direct destination, a creative with your greeting and starters, and the ad, all paused
- pause a losing chat ad

It never turns ads on, never changes the budget of a campaign or ad set that already exists, and never sends messages to your customers.

## Tips

- Ask your team to keep the ad id or ad name on every chat. Without it, the skill can only grade by app.
- On WhatsApp, a different prefilled message per ad tells your team which ad started the chat, even without an inbox tool.
- Chats from the last week of the window may still turn into sales. Rerun the review a week later before pausing a close call.
- Don't judge a chat ad on cost per conversation. In the example on this page, the ad with the cheapest chats made no sale at all.
