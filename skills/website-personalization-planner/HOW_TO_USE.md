# How to Use This Skill

Hey Claude, I just added the "website-personalization-planner" skill. Find the visitor groups on my homepage that convert far below everyone else, and plan what each one should see.

## What you need

- **The InsightfulPipe MCP connected to Claude, with Google Analytics 4 added.** Google Ads, Microsoft Ads, Search Console, LinkedIn Ads and Meta Ads add each group's own search words and the B2B industry split. The skill pulls the data itself.
- **The page and the goal** (sign up, demo request, purchase). Without them, the skill picks your busiest landing page and its main key event.
- **How you can show a variant:** a personalization tool, your page builder's URL or country rules, or your developers.
- **What you can stand behind for each audience:** case studies, review counts, local prices, setup offers. Variants use only these.

No connections? Paste a GA4 export of the page's sessions and conversions by channel, campaign, country, device and new or returning, plus your search terms and the hero copy.

## Example requests

**Full plan for one page**
Hey Claude, I just added the "website-personalization-planner" skill. Plan personalization for example.com/ for the last 90 days. The goal is sign_up, and our page builder can swap the hero by URL parameter or country.

**Personalized landing pages for ad campaigns**
Hey Claude, I just added the "website-personalization-planner" skill. Our Google Ads campaigns all land on the same page. Which campaigns need their own headline, and what should it say?

**Dynamic text replacement**
Hey Claude, I just added the "website-personalization-planner" skill. I want dynamic text replacement on my landing page from the search keyword. Plan it safely and tell me which keyword themes are worth it.

**B2B by industry**
Hey Claude, I just added the "website-personalization-planner" skill. Our LinkedIn ads target five industries and all go to /demo. Which industries convert worst, and is any big enough to test its own version?

**From a paste**
Hey Claude, I just added the "website-personalization-planner" skill. Here's my GA4 export by channel, country and device for /pricing, and the page copy. Which groups should see something different?

## What you get

1. **A table of every visitor group** with its conversion rate against the rest of the page, the gap, a significance check and the conversions it loses a month.
2. **Up to three variants,** each with headline, subhead, offer, proof and CTA, and the search term behind every headline.
3. **The targeting rule for each,** the order the rules apply in, and an allowlist for dynamic text.
4. **A holdout sized from each group's own traffic,** with the weeks the test takes and the rule for keeping or dropping the variant.
5. **The groups left out and why:** no real gap, too small to test, a tracking problem, or the default page's job.

## What it can change for you

With your yes on the exact change, it can:
- register the `pz_variant` custom dimension in GA4 so you can read the test
- add the variant parameter to a Google Ads campaign's final URL suffix, keeping the suffix you already have

It never edits your website, your ads' text or your audiences.

## Tips

- Use 90 days of data. Shorter windows leave most groups too small to judge.
- Fix the default page first if most of your visitors convert poorly. Personalization helps a minority, not the majority.
- Rerun after each test ends: a winning variant changes the numbers for every other group.
