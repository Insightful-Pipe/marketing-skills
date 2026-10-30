# How to Use This Skill

Hey Claude, I just added the "email-platform-setup-migration" skill. We're moving from Mailchimp to Klaviyo next month. Plan the migration so nobody gets emailed twice or after they unsubscribed.

## What you need

- **Nothing connected, at minimum.** Paste or upload your contacts export (with each contact's status and opt-in date), your list of automations or flows, segments, templates and forms, and say which store you run.
- **Better: the InsightfulPipe MCP with Klaviyo, Mailchimp and your store connected** (Shopify, WooCommerce or Magento). The skill then reads both email accounts and the store itself, so the inventory is complete and the event check uses real counts.
- **Your cut-over date,** if you have one. Without it, the plan uses 21 days from today.

## Example requests

**Migration (Mailchimp to Klaviyo)**
Hey Claude, I just added the "email-platform-setup-migration" skill. Plan our Mailchimp to Klaviyo migration. Our store is on Shopify and we want to switch on November 16.

**Migration (Klaviyo to Mailchimp)**
Hey Claude, I just added the "email-platform-setup-migration" skill. We're leaving Klaviyo for Mailchimp. Map our profiles, suppressions and custom properties, and tell me which flows to rebuild.

**Any other platforms, from exports**
Hey Claude, I just added the "email-platform-setup-migration" skill. Here are our exports from our current email platform. Give me an email platform migration checklist for moving to Klaviyo.

**Is the new platform ready?**
Hey Claude, I just added the "email-platform-setup-migration" skill. Check whether Klaviyo is getting our Shopify events and catalog yet, and tell me if we can cut over this week.

**First setup**
Hey Claude, I just added the "email-platform-setup-migration" skill. We're setting up email for the first time on Klaviyo. Tell me what to import, what to build first, and in what order.

**Choosing a platform**
Hey Claude, I just added the "email-platform-setup-migration" skill. Help us decide between two email platforms for our store, then plan the switch.

## What you get

1. **An inventory** of lists, segments, flows, templates, forms, custom fields, contacts by status and scheduled campaigns, with where each number came from.
2. **Keep, rebuild or retire** for every flow, segment, template, field and form, with the reason.
3. **A consent and suppression plan:** who is suppressed first, who is imported as subscribed, who is left out, and the contacts your store still marks subscribed after they opted out.
4. **A field map** from every old field to the new platform, with the transforms (phone formats, birthdays, interest groups, tags).
5. **An event check:** whether placed order, started checkout and viewed product events and the product catalog are arriving on the new platform, against your store's own counts.
6. **Go or no-go gates** and a **dated cut-over plan,** including which flows switch in the same hour and which old flows drain first.

## What it can change for you

With your yes on the exact change, it can create the main list, rebuilt templates or mapped fields on the new platform, and suppress people who opted out on the old platform after the export. It never imports subscribed contacts, sends, schedules or turns flows on.

## Tips

- Run it again on the go or no-go date, nine days before cut-over, to recheck the events.
- If your Mailchimp account uses Customer Journeys, list them for the skill; the API doesn't return them.
- For the sending domain and the warm-up schedule, use the Email Deliverability Auditor skill alongside this one.
