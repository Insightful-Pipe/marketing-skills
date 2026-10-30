# How to Use This Skill

Hey Claude, I just added the "content-performance-analyst" skill. Show me how our blog, social posts and email performed last month, and which posts we should promote as ads.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the data itself; you don't need to export anything. No connection? Paste or upload your exports (GA4 pages and landing pages, each network's post or monthly export, your email platform's campaign export) and it applies the same rules.
- **Optional: your content sources in the same workspace.** Facebook Pages, Instagram, LinkedIn Pages, YouTube, Pinterest, TikTok, X and Klaviyo. The report covers whatever is connected and says what it couldn't read.
- **For the content ROI report (optional):** your cost per piece (a paste or a Google Sheet with URL, cost, format and topic), your CRM's closed-won export with each contact's first page seen, and the GA4 BigQuery export if you have it switched on.
- **For the monthly social media report (optional):** your goals per network, and a Google Sheet to save each month's numbers in.
- **Your blog path,** if your posts don't live under `/blog/`.
- **Your main conversion,** if it isn't already a key event in GA4.

## Example requests

**Blog post report**
Hey Claude, I just added the "content-performance-analyst" skill. Which blog posts got the most readers in the last 30 days, which ones do people actually read, and which lost traffic since the month before?

**Content groups**
Hey Claude, I just added the "content-performance-analyst" skill. Compare the sections of my site in GA4: blog, docs, product pages. Use my content groups, or the URL folders if I don't have any.

**Outbound clicks and downloads**
Hey Claude, I just added the "content-performance-analyst" skill. Which links send visitors off my site, and which files do people download most?

**Video engagement**
Hey Claude, I just added the "content-performance-analyst" skill. How are the videos embedded on my site being watched, and how are my YouTube videos doing?

**Social media report for all pages**
Hey Claude, I just added the "content-performance-analyst" skill. Give me one report for all my social pages: posts, views, engagement and the visitors each network sends to the site.

**Promote the winners**
Hey Claude, I just added the "content-performance-analyst" skill. Which of my organic posts did well enough to be worth running as ads?

**Monthly social media report**
Hey Claude, I just added the "content-performance-analyst" skill. Build last month's social media report for my boss: followers, views, engagement and site visits per network, month over month and year over year, our top and bottom posts, how we did against our goals, and targets for next month.

**Content ROI report**
Hey Claude, I just added the "content-performance-analyst" skill. Here are our content costs and our closed-won deals from the CRM. Which articles and formats bring leads and customers, which only bring visitors, and did our content pay for itself?

## What you get

1. **A scorecard for seven areas:** tracking health, blog posts, site sections, on-page actions (outbound clicks, downloads, video), social posts, email, and what content earns.
2. **The top 5 actions,** tracking problems first, then ranked by the site visitors at stake.
3. **A blog table** with views, change from the prior period, engaged time per view, scroll rate and a label for each post.
4. **One cross-channel table** comparing the blog, each social network and email, with the visitors each sent to your site.
5. **What content earns:** leads, closed-won deals and revenue per article, cost per lead and payback, each article marked as a buyer piece, a traffic piece, steady or too early to call, and the same by format and topic.
6. **A list of organic posts worth promoting as ads,** with the rule each one passed and where it would run.
7. **The monthly social media report, when you ask for it:** one row per network with month-over-month and year-over-year changes, results against your goals (or next month's targets from your own trend), what moved the numbers, top and bottom posts, a short narrative and next month's plan.
8. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can turn on outbound click, file download or video tracking in GA4's enhanced measurement when one of them is off, and save the monthly report as a new tab in a Google Sheet you name.

It never posts, edits or boosts content, sends email or creates ads.

## Tips

- Facebook, Instagram, TikTok and X post numbers are lifetime totals for the posts published in your date range. GA4, YouTube, Pinterest and account-level numbers cover the date range itself.
- Each network counts views differently (views, impressions, plays), so the monthly report keeps them apart instead of adding them into one total.
- Save the monthly report to Google Sheets: next month the skill reads it back for follower changes on networks that only give today's count.
- GA4 can't show articles read earlier in a buyer's journey. Switch on the BigQuery export for that; it only collects from the day you turn it on.
- Pinterest keeps analytics for 90 days, so pick a recent range if Pinterest matters to you.
- GA4 counts a download from another domain as an outbound click too. The report takes those out so the two numbers don't overlap.
- Run it monthly. If the report says tracking collapsed, fix that before reading anything else.
