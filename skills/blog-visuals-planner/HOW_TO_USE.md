# How to Use This Skill

Hey Claude, I just added the "blog-visuals-planner" skill. Plan the charts and images for this blog post, using only the numbers in it and the data I attach.

## What you need

- **The post or report.** Paste the text or upload the file. A draft is fine.
- **The data behind it,** if any: a pasted table, a CSV, or a Google Sheet. Without it, the skill works from the numbers written in the text.
- **Your brand colours and blog column width,** if you have them. Otherwise it uses a neutral grey with one highlight colour and a 760 px column.
- **Optional: the InsightfulPipe MCP** with Google Sheets, GA4, PageSpeed or WordPress connected. Sheets and GA4 supply chart data, GA4 and PageSpeed pick the older posts that need better visuals, and WordPress reads your posts and images.

## Example requests

**Plan a post's visuals**
Hey Claude, I just added the "blog-visuals-planner" skill. Here's my draft. Tell me which charts, diagrams and screenshots it needs, and write the alt text, captions and file names.

**Turn data into charts**
Hey Claude, I just added the "blog-visuals-planner" skill. My post is based on the survey results in this Google Sheet. Pick the right chart for each finding and give me specs my designer can build from.

**Create an infographic**
Hey Claude, I just added the "blog-visuals-planner" skill. Is there enough in this report for an infographic? If so, plan the panels and the social cuts.

**Find posts that need better visuals**
Hey Claude, I just added the "blog-visuals-planner" skill. Use GA4 to find the blog posts where readers drop off early, and tell me which ones need more visuals and which have images that are too heavy.

## What you get

1. **A number check:** every result the text states marked matches, differs, from the text only, or no source, with the corrected sentence where the data disagrees or a number is credited to the wrong group. Settings and step numbers are listed as not results.
2. **A visual plan in reading order:** featured image brief, charts, diagrams, screenshots, tables and stat callouts, each tied to the sentence it supports.
3. **A full spec for each visual:** chart type and the rule that picked it, title that states the finding, data rows, highlight, a Vega-Lite spec you can render, file name, size and format, alt text with its character count, and a caption with the source.
4. **The words between visuals,** before and after the plan.
5. **A needs-data list** for claims that would make good charts but have nothing behind them yet.
6. **An infographic plan,** or the reason it isn't worth making.
7. **The older posts that would gain most,** ranked by how many readers fall short of your blog's median scroll rate, with words per visual and image weight.

## What it can change for you

With your yes on the exact change, it can write the planned alt text and caption to an image already in your WordPress media library. It never generates, uploads or replaces images, never edits the post's text, and never publishes.

## Tips

- Attach the data, not just the post. A chart can only use numbers that have a source.
- Fix any "differs" number in the text before the chart is made, so the post and the chart say the same thing.
- If your GA4 shows no scroll events at all, scroll tracking is switched off in enhanced measurement; the ranking then uses engagement time only.
- Rerun the ranking a month after the new visuals go live to see whether more readers reach the end.
