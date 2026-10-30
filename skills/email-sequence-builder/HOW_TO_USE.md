# How to Use This Skill

Hey Claude, I just added the "email-sequence-builder" skill. Read my Klaviyo account and build an onboarding sequence for new sign-ups to my Email List.

## What you need

- **The InsightfulPipe MCP connected to Claude, with Klaviyo or Mailchimp added.** The skill reads your account itself: which triggers you track, which flows already run, which emails earned clicks, how your lists collect consent, and which template has your footer. The Mailchimp path is written from the API schema and hasn't been tested on a live account yet.
- **The product pages to read,** or a short description of what you sell.
- **One goal for the sequence,** like a first purchase, a finished setup or a booked call.
- **Your limits,** if you have them: how many emails, whether discounts are allowed, and where your subscribers live.
- **For store flows (back in stock, low stock, price drop, refill reminders):** Shopify, WooCommerce or Magento connected, or an orders and inventory export. The store paths are written from the API schema and haven't been tested on a live store yet. Klaviyo has no low stock or back in stock trigger for WooCommerce stores, and on Mailchimp the skill asks you to check the journey builder for each trigger, since it can't read it there.
- **For subject lines on one email:** the email itself, and your past campaigns' subject lines with their clicks if you have them (Mailchimp gives them through the connection; from Klaviyo, paste the subject lines).

No email platform connected? The skill still writes the sequence from your brief, and marks the account checks as not read.

## Example requests

**Welcome**
Hey Claude, I just added the "email-sequence-builder" skill. Build a welcome sequence for new newsletter subscribers. We sell project management software to agencies, and the goal is a booked demo.

**Abandoned checkout**
Hey Claude, I just added the "email-sequence-builder" skill. Build an abandoned checkout sequence for our coffee store. Check whether Klaviyo tracks checkouts first, and only offer a discount if we have a coupon set up.

**Onboarding**
Hey Claude, I just added the "email-sequence-builder" skill. Write onboarding emails for new sign-ups. Users who create their first project in week one are the ones who stay, so every email should push toward that.

**Lead nurture**
Hey Claude, I just added the "email-sequence-builder" skill. Create a nurture sequence for people who downloaded our SEO guide, moving them toward a consultation call.

**Re-engagement**
Hey Claude, I just added the "email-sequence-builder" skill. Build a winback sequence for subscribers who haven't clicked in 90 days, ending with a last email before we remove them.

**Post-purchase**
Hey Claude, I just added the "email-sequence-builder" skill. Write post-purchase emails for our online course: fewer refunds, more reviews, and a path to our coaching program.

**Launch, from what worked before**
Hey Claude, I just added the "email-sequence-builder" skill. We launch a new feature next month. Look at our best campaigns from the last year, then write the launch emails and save them as a draft campaign for me to review.

**Subject line and preview text for one email**
Hey Claude, I just added the "email-sequence-builder" skill. Here's our Thursday newsletter. Write 10 subject line and preview text pairs, rank them against what our last year of campaigns got clicks on in Mailchimp, and tell me if our list is big enough to test the top two.

**Back in stock and low stock**
Hey Claude, I just added the "email-sequence-builder" skill. Check our Shopify stock and Klaviyo setup, tell me which sold-out items need a back in stock email most, and write the back in stock and low stock flows.

**Replenishment and price drop**
Hey Claude, I just added the "email-sequence-builder" skill. Our coffee and filters get used up. Work out from our Shopify orders how many days people usually take to reorder each one, write refill reminders timed to that, and add a price drop email for viewed items.

**Transactional and compliance**
Hey Claude, I just added the "email-sequence-builder" skill. Rewrite our order confirmation and shipping emails, and check our footer and sign-up list against CAN-SPAM and GDPR.

## What you get

1. **An account readiness table:** sender and address, triggers tracked, existing flows, your sending baseline, entry list and consent, reusable template and coupons, each with what it means for this sequence.
2. **A sequence map and calendar:** every email with its day, purpose, filter and the rule that takes people out of the flow, plus a week-by-week view of when each email lands.
3. **Every email written in full:** three subject lines with different angles, preview text, body with personalisation and fallbacks, one CTA, an optional PS, and the page each product claim came from.
4. **A compliance and sending check:** address, unsubscribe, sender, spam-style wording and image-heavy layouts, ad disclosure, consent by region, opt-outs and bulk-sender rules. Anything to fix is listed at the top of the report.
5. **Build steps** for the flow in Klaviyo or Mailchimp.
6. **What to measure and test first,** judged on clicks and conversions rather than opens, with the rule that decides the winner.

For store flows you also get a product table: sold-out and low-stock items with units sold and weeks of cover, and each refill product's typical reorder gap with the reminder days. In subject line mode you get 8 to 10 subject and preview pairs, each checked for how it shows on a phone, whether the preview adds to the subject, whether the email delivers the promise, tag fallbacks and filter-prone wording, ranked against what your own list clicked on, plus whether your send is big enough to test two of them.

## What it can do for you

With your yes on the exact payload, it can save each email as a Klaviyo template, or create a draft campaign with the template attached (in Mailchimp: a template, or a draft campaign with its content). It never sends or schedules an email, never sets a flow live and never changes your lists or profiles. InsightfulPipe has no action that creates a Klaviyo flow, so you build the flow from the steps it gives you.

## Tips

- Name the one action the sequence is for. A sequence with three goals gets none of them.
- If your app can send events to Klaviyo (like "Created First Project"), the emails can skip people who already did the step. The skill tells you which events would help.
- Tell it where your subscribers live; consent rules differ between the US and the EU, UK and Canada.
- Run it again after the first few weeks of sending, so the next version learns from your own clicks.
