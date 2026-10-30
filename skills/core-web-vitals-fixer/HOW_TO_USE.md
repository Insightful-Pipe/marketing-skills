# How to Use This Skill

Hey Claude, I just added the "core-web-vitals-fixer" skill. Check my site's Core Web Vitals by template and give me a fix plan for the slowest pages.

## What you need

- **The InsightfulPipe MCP connected to Claude, with PageSpeed Insights added.** The skill runs the speed tests itself; you don't export anything.
- **Search Console for your site,** if you have it. The skill uses it to find the pages people actually land on and group them by template. Without it, give one URL per page type.
- **GA4 or Google Ads,** only if you want speed compared with bounce rate or ad conversions.
- **Claude Code with your site's code open,** if you want the skill to draft the code changes for you.

## Example requests

**Status by template**
Hey Claude, I just added the "core-web-vitals-fixer" skill. Which of my page templates pass Core Web Vitals on mobile, and which fail?

**Fix one metric**
Hey Claude, I just added the "core-web-vitals-fixer" skill. My LCP is poor on blog posts. Find out why and give me a fix plan.

**Scripts and images**
Hey Claude, I just added the "core-web-vitals-fixer" skill. Which third-party scripts and images slow my site down the most?

**Speed and conversions**
Hey Claude, I just added the "core-web-vitals-fixer" skill. Do my slower landing pages have higher bounce rates or lower ad conversion rates?

**Weekly check**
Hey Claude, I just added the "core-web-vitals-fixer" skill. Here is last week's baseline. Did anything get slower this week?

## What you get

1. **Status by template:** the real-user LCP, INP and CLS for each page type. Each number says whether it is the page's own data or the whole site's.
2. **Fix plans for LCP, CLS and INP,** ranked by the traffic they touch. Each fix cites the test result behind it and says whether it is a site-wide or a one-template change.
3. **Image findings** and a **ranked list of heavy scripts,** with the decisions that are yours to make (for example, delaying a chat widget).
4. **Speed against bounce rate and ad conversions,** or a plain "not enough data" with the page counts.
5. **A baseline block** to paste next week, so the skill can flag what got slower.

## What it can change for you

Nothing in your accounts. If your site's code is open in Claude Code, it can draft the changes: image priority hints, image sizes, font settings, deferred scripts. It shows each change as a diff, applies it only after your yes, and never deploys.

## Tips

- Run it after every release that touches the layout, fonts or scripts, and weekly as a monitor.
- Real-user numbers cover the last 28 days, so a fix shows up in them gradually. The lab numbers move at once.
- Low-traffic pages have no real-user data of their own. The report then shows the whole site's numbers and labels them.
- The bounce and ad-conversion check runs 10 minutes after the speed tests start, or as a follow-up request, so a run stays under the API's rate limit.
