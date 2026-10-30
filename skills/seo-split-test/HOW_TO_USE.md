# How to Use This Skill

Hey Claude, I just added the "seo-split-test" skill. Design an SEO split test for the title change I want to make on our product pages, and tell me how long it needs to run.

## What you need

- **A set of similar pages,** built on one template: product pages, location pages, recipe pages, or blog posts of one kind. About 20 pages or more works best; with fewer than 10 per group the skill says a split test won't work and offers another way.
- **One change to test:** titles, meta descriptions, headings, structured data, a content block, or internal links.
- **The data,** either way:
  - **Connected:** the InsightfulPipe MCP with your Google Search Console property. The skill pulls daily clicks per page and inspects the test pages itself. GA4 adds organic sessions and key events, and WordPress lets it apply, roll out or revert the change after you confirm.
  - **Not connected:** paste or upload weekly clicks, impressions and position for each page (12 weeks) to design a test, and a daily clicks export for each group to read one. The skill writes the Search Console regex filters you need for those exports.

## Example requests

**Design a test**
Hey Claude, I just added the "seo-split-test" skill. We have 60 city pages under /locations/. Split them into test and control, check the groups are balanced, and tell me how many weeks the test needs to see a 5% lift.

**Read a test**
Hey Claude, I just added the "seo-split-test" skill. Our title test on the recipe pages launched on September 8 and the planned 5 weeks are over. Here are the two page lists. Did the new titles win?

**Judge a change already made**
Hey Claude, I just added the "seo-split-test" skill. We rewrote every blog title in August without a test. Tell me whether it helped, compared with pages we didn't touch.

**Test structured data**
Hey Claude, I just added the "seo-split-test" skill. I want to add Product markup with price and availability to half of our product pages. Design the test and check that Google sees the markup before the test starts.

## What you get

1. **Design:** the pages left out and why, the test and control lists with the seed that built them, a balance check on clicks, impressions, position and trend, the smallest lift the test can see for each run length from 4 to 8 weeks, and a launch plan with the exact before and after text.
2. **Read-out:** recrawl, canonical, contamination and placebo checks, then the effect on clicks with a 95% interval, split into impressions and CTR, plus position. It also shows what a before and after on the test pages alone would have said, so you can see what the control corrected.
3. **A verdict:** win, loss, no clear effect, or unreliable, with the next step.

## What it can change for you

With WordPress connected and your yes on the exact pages and text, it can apply the change to the test pages, roll it out to the control pages after a win, or revert it after a loss. It never changes URLs or slugs. On other sites it gives you the text to paste.

## Tips

- Decide the run length before launch and don't read the result early. An early look is labelled as one.
- Leave the control pages alone during the test. If someone edits one, tell the skill: it drops that pair.
- Run the recrawl check a week after launch. The test only starts counting once Google has seen the change.
