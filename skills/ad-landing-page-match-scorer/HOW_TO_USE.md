# How to Use This Skill

Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Check every active ad in my Google Ads account against the page it sends people to, and tell me which routes lose the most.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your ad account added** (Google Ads, and Meta Ads if you run it). The skill pulls the ads, keywords, sitelinks, Google's landing page rating and conversion rate by page itself.
- **Nothing extra for the pages.** It captures each landing page on desktop and mobile, reads its headings and title, and runs a PageSpeed check through the same MCP.
- **Optional:** your GA4 property, for engagement by landing page from paid traffic.
- **No ad account connected?** Paste the ad copy, the final URL and the keywords, and it scores that one ad the same way.

## Example requests

**Every active ad**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Score every active Google Ads route against its landing page for the last 30 days and rank the fixes by spend.

**Screenshots only**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Take desktop and mobile screenshots of the landing page behind every active ad, grouped by the ads that use each page.

**Clicks but no conversions**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. My Drain Cleaning campaign gets clicks but few leads. Check whether the ads and the page say the same thing, and what happens after the click.

**Quality Score**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Google rates my landing page experience below average on some keywords. Find which pages and why.

**Many keywords, one page**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Twenty keywords go to one page. Which keyword themes does the page not cover?

**Meta ads**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Check my active Meta ads: does each image and headline carry through to the page it links to?

**Then fix**
Hey Claude, I just added the "ad-landing-page-match-scorer" skill. Score my routes, then point any non-brand ad that lands on my home page to its service page. Show me the change first.

## What you get

1. **A match score out of 100 for each route** (an ad group and its page) on five dimensions: headline, offer, keyword, visual and audience match, shown as "x of y checked" when a page can't be read.
2. **Route flags that need only the ad account:** generic destinations, off-topic ad lines, Google's landing page rating (and whether keywords that name a city or state score worse), conversion rate against your own baseline, and sitelinks that land on the wrong page.
3. **Post-click checks for each page:** mobile speed, the first screen, mobile use, trust and the steps to convert.
4. **Side-by-side tables** of ad versus page for the weakest routes.
5. **Desktop and mobile screenshots** of every page checked.
6. **Fixes ranked by the spend that flows through each route,** with rewrite suggestions and effort.

## What it can change for you

With your yes on the exact change, in Google Ads it can:
- point an ad to a better page, or change its display path
- rewrite an ad's headlines and descriptions to match the page
- add sitelinks that go to the right pages

It never edits your website; page changes come as exact instructions.

## Tips

- Some sites block automated page checks. The report marks those checks unknown instead of failing them; send a phone and a desktop screenshot of the page to finish them.
- The page reads (screenshots, headings, speed) had not yet returned data on a live run when the skill was built; if they fail, the report says so, keeps the ad-side checks and asks for screenshots.
- Run it after any new landing page or campaign launch, and whenever Google's landing page rating drops.
- On LinkedIn Ads, give the landing page URL and ad copy: the API only shares a reference to the sponsored post.
