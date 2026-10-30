# How to Use This Skill

Hey Claude, I just added the "impression-share-analyst" skill. Show me where my Google Ads campaigns lose impression share, whether to fix budget or rank first, and who competes on my brand.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Ads account added.** The skill pulls impression share, the trend, device and keyword detail, and your search terms itself.
- **Your target CPA or ROAS,** if you have one. Without it, the skill uses your own 30-day average. A campaign that has its own target CPA in its bid strategy is judged against that one.
- **Your brand terms and main competitors,** if they aren't obvious. The skill finds likely rivals on its own.
- **Your main target city or region,** so the search results check looks where your customers are.
- **Optional: an Auction Insights export** from Google Ads. Google withholds auction insights from our API access, so the overlap table needs the export. Everything else runs without it.
- **For the weekly brand defense monitor, no connection is needed.** Paste the brand campaign's weekly report, two Auction Insights exports of the brand campaign (the last 4 weeks and the 4 before), the rival ads you saw on a search for your brand, and your search terms report. For a trademark complaint draft, add your marks and their registration numbers.

## Example requests

**Budget or rank?**
Hey Claude, I just added the "impression-share-analyst" skill. Which of my campaigns are losing impression share to budget and which to rank, and which ones are worth more budget at a $40 CPA?

**Share dropped**
Hey Claude, I just added the "impression-share-analyst" skill. Our impressions fell over the last month. Show me the 12-week impression share trend by campaign and what changed.

**Top of page**
Hey Claude, I just added the "impression-share-analyst" skill. How often do my ads show at the top and in the first position, on mobile and desktop, and which keywords hold that back?

**Competitors and brand**
Hey Claude, I just added the "impression-share-analyst" skill. Is anyone bidding on our brand name, and are we showing up for competitors' names? Here's our Auction Insights export.

**Brand defense monitor and trademark complaint**
Hey Claude, I just added the "impression-share-analyst" skill. A competitor is bidding on my brand name and one of their ads says our name in the headline. Here are 8 weeks of my brand campaign, two Auction Insights exports and the ads I saw. Is it allowed, and can you draft a Google Ads trademark complaint?

## What you get

1. **Account impression share,** weighted properly, with the lost share split between budget and rank.
2. **A campaign table** that sorts each search campaign into budget-limited, rank-limited, both, healthy or too thin to judge.
3. **Up to five actions,** ranked by conversions at stake, with the estimate and its assumption shown.
4. **The 12-week trend,** naming the loss bucket behind every move, including the moves a flat share hides.
5. **Top-of-page and first-position detail,** device gaps, and the keywords holding a campaign back.
6. **A competition section:** brand defense, a search results spot check, rivals confirmed as Google advertisers, rivals' names your ads matched, and the overlap table if you pasted the export.
7. **In the weekly brand defense monitor:** brand CPC and share week by week, each rival in your brand auction labelled (arrived, left, more or less aggressive), every rival ad sorted into "name in ad text", "domain only" or "bids on the name only", with Google's reseller and review-site exceptions, brand searches leaking into your other campaigns with what they cost extra, and a trademark complaint draft for you to file.

## What it can change for you

With your yes on the exact change, it can:
- raise the daily budget of a campaign that's capped by budget and hitting its target CPA, or by one small step when it's a little over
- raise the CPC ceiling of a Target impression share campaign held back by it
- add rivals' names as negative keywords, if you don't mean to bid on them
- add your brand terms as phrase negatives in non-brand campaigns, when your brand campaign can take those searches

It never switches bid strategies or changes CPA and ROAS targets, and it never files a trademark complaint: you or your authorised agent file the draft with Google.

## Tips

- Run it monthly, and a week after any budget change, to see whether the extra share came at an acceptable CPA.
- Pull the Auction Insights export per campaign as well as for the whole account. A rival who shows up only on your brand campaign is bidding on your name.
- 100% impression share is rarely worth paying for. Let the CPA decide.
- A rival bidding on your brand name is allowed. Only their use of your name in the ad text can be restricted, so the monitor drafts complaints for those ads alone.
