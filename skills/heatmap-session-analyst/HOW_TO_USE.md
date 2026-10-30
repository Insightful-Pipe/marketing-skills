# How to Use This Skill

Hey Claude, I just added the "heatmap-session-analyst" skill. Read our Clarity data and GA4 for the last 30 days, tell me which rage clicks, dead clicks and other problems cost us the most conversions, and which recordings to watch for each.

## What you need

- **Behaviour data, any one of these:**
  - Microsoft Clarity connected through the InsightfulPipe MCP. Clarity's data API serves only the last 1 to 3 days, so for a longer view keep a Google Sheet history (the skill can set one up).
  - A pasted Clarity dashboard filtered by page, or Clarity's click and scroll heatmap exports.
  - A Hotjar recordings export (CSV or XLSX).
- **Conversion data:** GA4 connected through the InsightfulPipe MCP, or a pasted GA4 landing page report with sessions and key event rate. Without it you still get the problems, ranked by flagged sessions instead of conversions.
- **Optional:** where your main call to action sits on key pages, and notes from any recordings you've already watched.

## Example requests

**Ranked fix list**
Hey Claude, I just added the "heatmap-session-analyst" skill. Use our Clarity history sheet and GA4, and give me the five behaviour problems that cost the most sign-ups.

**Rage clicks and dead clicks on one page**
Hey Claude, I just added the "heatmap-session-analyst" skill. Our pricing page gets lots of rage clicks and dead clicks on mobile. Is it worth fixing, and which recordings should I watch?

**From a Hotjar export**
Hey Claude, I just added the "heatmap-session-analyst" skill. Here's our Hotjar recordings export and last month's GA4 landing page report. Which pages have the most rage clicks and u-turns, and which ones matter?

**Start a history**
Hey Claude, I just added the "heatmap-session-analyst" skill. Set up a Google Sheet that keeps our daily Clarity numbers, so next month you can analyse 30 days instead of 3.

**After watching recordings**
Hey Claude, I just added the "heatmap-session-analyst" skill. I watched the recordings you suggested for the signup page. Here are my notes; what should we change?

## What you get

1. **A header** with the Clarity window, GA4 dates, your site conversion rate and the site baseline for each signal.
2. **The top 5 problems,** each a page and a signal (rage clicks, dead clicks, quick backs, excessive scrolling or JavaScript errors), ranked by the conversions it probably costs, with the math shown.
3. **For each one:** the device and channel where it happens, the likely cause or "watch first", the exact Clarity recording filter, the heatmap view, and how to check the fix worked.
4. **Other findings:** scroll depth against your call to action, site-wide errors and slow pages.
5. **What couldn't be graded,** and why.

## What it can change for you

With your yes on the exact change, it can create a history tab in your Google Sheet and append each Clarity pull to it. It never changes your site, your Clarity settings or GA4.

## Tips

- Clarity allows 10 API requests per project a day. A daily scheduled pull uses 9, so don't run other Clarity tools on the same project that day.
- Watch 5 to 10 recordings per problem before changing anything, then share your notes. The skill turns them into the fix.
- Run it again two weeks after a fix to see the share drop.
