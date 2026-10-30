# How to Use This Skill

Hey Claude, I just added the "meta-bid-strategy-advisor" skill. Look at every Meta campaign and tell me which bid strategy each should use and where to set the caps.

## What you need

- **Your Meta Ads data, one of two ways.** Connect Meta Ads through the InsightfulPipe MCP and the skill reads campaigns, ad sets, caps, daily results and change history itself. Or paste an Ads Manager export at ad set level for the last 30 days, broken down by day, with the bid strategy, bid, budget, results and amount spent columns.
- **Your target,** if you have one: the most you can pay per lead, sign-up or purchase, or the lowest ROAS you accept. Without it, caps come from your own history alone.
- **Two answers the API can't give:** whether any campaign already has a ROAS goal, and whether you use value rules.
- **What a result is worth by segment** (optional): for example, how often sign-ups from each country become paying customers. The skill plans value rules only from numbers you give.

## Example requests

**Every campaign at once**
Hey Claude, I just added the "meta-bid-strategy-advisor" skill. Look at every Meta campaign and tell me which bid strategy each should use. We can pay up to $40 per lead.

**Cost cap vs bid cap**
Hey Claude, I just added the "meta-bid-strategy-advisor" skill. Should my sales campaign use a cost per result goal or a bid cap, and at what amount? My break-even cost per purchase is $55.

**A capped campaign stopped spending**
Hey Claude, I just added the "meta-bid-strategy-advisor" skill. My campaign on a cost per result goal only spends half its budget. Is the cap too low, and what should it be?

**From an export**
Hey Claude, I just added the "meta-bid-strategy-advisor" skill. Here's my Ads Manager ad set export for the last 30 days, by day. Which ad sets have enough results for a ROAS goal of 2.5?

## What you get

1. **A strategy table:** each campaign and ad set, its strategy now, weekly results, whether that volume can carry a cap, and what to change.
2. **A cap table:** your own daily cost per result percentiles, the current and proposed cap, and on how many of the last 30 days each cap would have sat below what results really cost.
3. **Findings:** caps that choke spend, caps on ad sets with too few results, and changes on hold because of a recent edit.
4. **A value rule plan** for segments worth more or less to you, with the math.
5. **A change plan** in order: the exact payloads it can run after your yes, and the Ads Manager steps for the rest.

## What it can change for you

With your yes on the exact change, it can:
- raise, lower or set the cap amount on an ad set
- change the bid strategy of a campaign that holds the budget, for example removing a cap

It never changes an ad set's own strategy, a ROAS goal or value rules: the connection can't, so you get the Ads Manager steps. It won't change anything edited in the last 7 days.

## Tips

- Run it after any big change in cost per result, and 7 days after you change a cap to see whether spend came back.
- If an ad set is under 50 results a week, merging it with a similar one often does more than any cap.
- Treat percentiles from a campaign that was already choked as a floor: the real cost of more volume is higher.
