# How to Use This Skill

Hey Claude, I just added the "lead-handoff-designer" skill. Here is our CRM lead export for the last 13 weeks. Design our MQL to SQL handoff, with the routing rules and the response-time agreement between marketing and sales.

## What you need

- **A lead export from your CRM** (HubSpot, Salesforce, Pipedrive or any other), with one row per lead: created time, source, company size, owner, first touch, and the dates each lead was qualified, rejected (with the reason), booked a meeting, met and turned into an opportunity. Upload it, paste it, or point to the Google Sheet it lives in.
- **Your staffed hours and time zone,** and who works the leads.
- **Your win rate from opportunity to closed won,** if you want a value on each GA4 lead event.
- **Optional, through the InsightfulPipe MCP:** Google Sheets to read the export, GA4 to see which lead events your site sends, and CallRail to add inbound calls as leads.

## Example requests

**Design the whole handoff**
Hey Claude, I just added the "lead-handoff-designer" skill. Here's our lead export. Define MQL vs SQL for us, write the routing rules and the SLA between marketing and sales, and tell me where leads leak.

**Set a response-time target**
Hey Claude, I just added the "lead-handoff-designer" skill. How fast do our reps need to call new leads? Work it out from our own export, not from industry studies.

**Fix rejected and stalled leads**
Hey Claude, I just added the "lead-handoff-designer" skill. Sales rejects half our MQLs and some sit open for weeks. Design what happens to rejected and stalled leads.

**Cut no-shows**
Hey Claude, I just added the "lead-handoff-designer" skill. Too many booked demos don't show up. Look at how far ahead we book and set a booking window and a no-show step.

**Send qualified stages to GA4**
Hey Claude, I just added the "lead-handoff-designer" skill. Map our lead stages to GA4 lead events with a value for each, so our ad platforms can bid on qualified leads. Our win rate is 25%.

## What you get

1. **Lifecycle stages** (lead, MQL, sales accepted, SQL, opportunity), each with entry and exit rules, an owner and a time limit.
2. **The MQL rule,** set from which sources and company sizes actually became SQLs.
3. **Routing rules:** rotation, a fallback owner at the response target, after-hours handling, and any owner who needs help.
4. **The SLA,** with a response target taken from your own conversion by time to first touch.
5. **Rejected and stalled leads:** each of your reject reasons routed to nurture, close or reassign, and stall limits per stage.
6. **Meetings:** show rate by how far ahead they were booked, a booking window, and a no-show rebook step (a labelled starting default, since exports rarely log a rebook date).
7. **The leaks between MQL and opportunity** (untouched, late, stalled and no-show leads), in leads and pipeline value, split into lost and at risk.
8. **A GA4 lead event map** with a value per stage.
9. **A weekly table** both teams review.

## What it can change for you

With your yes on the exact change, and a Read & Write connection, it can:
- add the weekly table to a new tab in your Google Sheet
- make `qualify_lead` and `close_convert_lead` key events in GA4

It never changes your CRM. It writes the rules; you set them up.

## Tips

- Export at least 13 weeks of leads. Fewer leads mean fewer targets the skill can set from data.
- Keep the reject reason, the meeting booked time and the meeting status in the export; they drive the recycling and show-rate steps.
- Rerun it each quarter with a fresh export and compare the targets.
