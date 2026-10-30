# How to Use This Skill

Hey Claude, I just added the "linkedin-thought-leader-ads-planner" skill. Which of our team's LinkedIn posts should we boost as Thought Leader Ads, and how much should each get?

## What you need

- **Each author's last 20 posts:** date, format, impressions, reactions, comments and reposts. Paste them, or attach each person's LinkedIn post analytics export. LinkedIn shows a post's numbers only to its author, so each person sends their own.
- **The campaign brief:** the goal (awareness or engagement), the audience, two to five themes, the total budget and the start date.
- **Optional, the InsightfulPipe MCP:** with LinkedIn Pages connected, the skill reads the connected member's totals and the company Page's posts itself. With LinkedIn Ads connected, it takes the bid from LinkedIn's suggested bids for your audience and can create the campaign group and paused campaigns after you confirm.

## Example requests

**Pick the posts**
Hey Claude, I just added the "linkedin-thought-leader-ads-planner" skill. Here are the last 20 posts from our founder and our head of sales. Which ones are worth paying to boost to US finance directors?

**Plan the budget**
Hey Claude, I just added the "linkedin-thought-leader-ads-planner" skill. We have $5,000 for Thought Leader Ads next month. Rank these posts and split the budget, with a check halfway through.

**Sponsor a creator**
Hey Claude, I just added the "linkedin-thought-leader-ads-planner" skill. A partner creator shared her post stats with us. Should we sponsor any of them, and what do we send her to ask for permission?

**Set it up in the account**
Hey Claude, I just added the "linkedin-thought-leader-ads-planner" skill. Plan our Thought Leader Ads, then create the campaign group and paused campaigns in our LinkedIn ad account. Show me the payloads first.

## What you get

1. **A bar for each author:** the median engagement rate of their last 20 posts, and the 1.5x line a post must clear.
2. **A verdict for every post:** boost, hold, wait, skip or ineligible, with the reason and the numbers.
3. **A ranked boost list** with a budget per post, and a reserve held back for the posts that win.
4. **The campaign plan:** one campaign per ad format, targeting, a manual CPM bid, total and daily budgets, a 14-day run and a day-7 pause rule per post.
5. **The exact payloads,** marked not run, the Campaign Manager steps to attach each post, and a permission request message for each author.

## What it can change for you

With your yes on the exact payloads, it can create:
- a campaign group (LinkedIn creates new groups active, but a group spends nothing without running campaigns)
- one campaign per ad format, created paused

It never sets a campaign active, and it doesn't attach the posts: a member's post needs the author's approval in Campaign Manager, so the skill writes those steps for you.

## Tips

- Run it every month or two. A post that waits today can qualify next week.
- Ask each author for the same 20-post export, so their bars are built the same way.
- After the run, use `linkedin-ads-auditor`, if installed, to compare the thought leader ads with your Page-authored ads.
