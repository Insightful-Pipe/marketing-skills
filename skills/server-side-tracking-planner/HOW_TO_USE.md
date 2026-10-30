# How to Use This Skill

Hey Claude, I just added the "server-side-tracking-planner" skill. Do we need server-side tracking? GA4 shows fewer sales than our store. If it's worth it, plan the build.

## What you need

- **Best: the InsightfulPipe MCP connected to Claude** with Google Tag Manager, GA4, your store (Shopify, WooCommerce or Magento) and the ad accounts that spend (Google Ads, Meta, Microsoft Ads, LinkedIn Ads, OpenAI Ads). The skill reads the numbers and your live container itself.
- **Or paste:** your order count, GA4's purchases for the same dates, each ad platform's conversions and spend, and a Tag Manager container export.
- **A few answers:** orders that never touch the website (phone, wholesale, test), your consent banner's accept rate and where it shows, who will own the server and at what rate, and your site stack.

## Example requests

**Decide only**
Hey Claude, I just added the "server-side-tracking-planner" skill. Server-side vs client-side tracking: which do we need? Size what we're missing and give me a yes or no.

**Full build plan**
Hey Claude, I just added the "server-side-tracking-planner" skill. Plan server-side tagging in Google Tag Manager for our store: hosting, subdomain, which tags move, event ids, hashing, consent and the test plan.

**Working from exports**
Hey Claude, I just added the "server-side-tracking-planner" skill. Nothing is connected. Here are our WooCommerce orders, GA4 purchases, ad platform numbers and our GTM container export. Should we go server-side?

**Plan, then draft**
Hey Claude, I just added the "server-side-tracking-planner" skill. Write the server-side tracking setup, then draft the Tag Manager changes in a new workspace. Show me each change first.

## What you get

1. **The sizing:** web orders against what GA4 counted, minus what consent refusals explain, and what each ad platform saw.
2. **The cost:** servers worked out from your busiest hour, hosting, upkeep and the build, as a share of your ad spend.
3. **A verdict:** build, pilot, not now or fix first, with the rule that decided it.
4. **Free fixes first:** click ids that your redirects drop, enhanced conversions, double counting.
5. **The build plan** (for build or pilot): where the server runs and on which address, a tag-by-tag move list, the event map, one event id design, the hashing list, consent per tag, the monthly cost and a test sequence before you switch.

## What it can change for you

With your yes on the exact change, in a new Tag Manager workspace:
- create the event id variable
- point your Google tag at the server
- run a compile check

It can also send one test event to the ChatGPT Ads Conversions API as a dry run that records nothing. It never publishes your container, deletes tags or changes Google Ads conversion actions.

## Tips

- Run decide-only first if you're not sure; it's quick and the free fixes alone often close part of the gap.
- Run it again 30 days after the switch to see how much of the gap closed.
