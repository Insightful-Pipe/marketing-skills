# How to Use This Skill

Hey Claude, I just added the "blog-lead-conversion-planner" skill. Our blog gets plenty of readers but hardly any sign-ups. Show me which articles to fix first, what each one should offer and what the calls to action should say.

## What you need

- **Your offers:** the sign-up or trial, demo, downloads (templates, checklists) and newsletter you have today, with their URLs and the GA4 event each one fires. The skill only plans offers that exist.
- **A line on what your product does,** so the call to action copy names real features.
- **Either the InsightfulPipe MCP connected to Claude** with Google Analytics (GA4), and ideally Search Console and Google Tag Manager, **or a paste:** a GA4 landing page export (sessions, engaged sessions and key events by landing page and event name), your article list (URL, title, word count, H2 headings, the CTAs already in it) and, if you have it, a Search Console page and query export.
- **WordPress connected** only if you want the calls to action inserted into your posts for you.

## Example requests

**Full plan from live data**
Hey Claude, I just added the "blog-lead-conversion-planner" skill. Use GA4, Search Console and Tag Manager to rank my blog articles by the leads they miss, then plan the offers and calls to action for the top 5.

**From a paste, nothing connected**
Hey Claude, I just added the "blog-lead-conversion-planner" skill. Here's my GA4 landing page export, my article list and my offers. Which posts should convert better, and what should each one offer?

**One article**
Hey Claude, I just added the "blog-lead-conversion-planner" skill. Our no-shows article gets 5,000 visits a quarter and almost no sign-ups. Plan the content upgrade and write the calls to action for it.

**Check tracking first**
Hey Claude, I just added the "blog-lead-conversion-planner" skill. Before we judge our blog CTAs, check whether clicks on them are tracked in GA4 and Tag Manager, and tell me what to set up.

**Plan, then insert into WordPress**
Hey Claude, I just added the "blog-lead-conversion-planner" skill. Plan the calls to action for our top articles, then show me the exact changes and add them to the WordPress posts once I say yes.

## What you get

1. **An article table** with sessions, engagement, leads, blog-to-lead rate and the leads each article falls short of, measured against your blog's own rate or your target.
2. **Why readers came** to each planned article, read from its Search Console queries (compare, template, how-to or other).
3. **An offer map** that matches each article to one of your existing offers, and names the offer gaps worth building.
4. **Calls to action written for each article:** where each one sits (after which heading), the heading, the line, the button and the link.
5. **A tracking check:** whether CTA clicks are measured, which tag and trigger cover them, and what to add in Tag Manager.
6. **Tracking targets:** the rate to watch per article and when to review it, worked out from its own traffic.

## What it can change for you

With WordPress connected and your yes on the exact change, it can insert the planned call to action blocks into a published post. It shows the before and after around each insert first, and never changes the title, slug, status, date or categories. Tag Manager changes and new offers stay recommendations for you.

## Tips

- Use 90 days or more. Most articles get too few visits in a month to judge.
- Tell it which events count as a lead. A newsletter sign-up can grow the list without counting as a lead, and the skill keeps the two apart.
- Run it again after the review date it gives you to see whether each article's rate moved.
