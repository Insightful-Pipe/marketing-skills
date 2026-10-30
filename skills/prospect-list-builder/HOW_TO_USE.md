# How to Use This Skill

Hey Claude, I just added the "prospect-list-builder" skill. Build me a B2B lead list of 20 companies that match our ideal customer, and show me why each one is on it.

## What you need

- **What you sell, in one line,** and who buys it.
- **Your ideal customer:** the type of company, where it is and how big. A pasted list of closed-won customers works too; the skill reads the common traits from it.
- **Two to four must-haves,** such as "physical therapy clinic", "within 15 km of downtown" or "at least 10 Google reviews". If you don't have them, the skill proposes some and asks you to confirm.
- **Optional lists to remove:** current customers, open deals and do-not-contact names, as a CSV, a paste or a Google Sheet.
- **Optional: the InsightfulPipe MCP connected to Claude.** With it, the skill pulls companies itself from Google business listings and search results (through DataForSEO), the Meta, LinkedIn and Google ad libraries, the App Store and Google Play, and checks mobile page speed. Without it, paste or upload any list of companies and the skill cleans, dedupes and grades it the same way.

## Example requests

**Local businesses in one city**
Hey Claude, I just added the "prospect-list-builder" skill. Find 15 independent dental practices within 10 miles of Austin that are running ads right now. Leave out the customers in this CSV.

**Companies advertising on a theme**
Hey Claude, I just added the "prospect-list-builder" skill. We sell field service software. Find US companies advertising on LinkedIn and Meta about technician scheduling, and give me a target account list of 25.

**App publishers**
Hey Claude, I just added the "prospect-list-builder" skill. We sell an in-app subscription analytics tool. List 20 fitness app publishers on Google Play and the App Store with an update in the last 90 days.

**Agency mode: businesses with fixable marketing gaps**
Hey Claude, I just added the "prospect-list-builder" skill. I run a small marketing agency. Find roofing contractors in Phoenix with no ads running, thin reviews or slow mobile pages, and tell me the gap behind each one.

**Clean a list you already have**
Hey Claude, I just added the "prospect-list-builder" skill. Here is a trade show list of 300 companies. Remove our customers and open deals, grade the rest against our must-haves, and give me the top 30.

## What you get

1. **The list,** graded A (passes every must-have and showed a buying signal in the last 90 days) or B (passes every must-have), with the website, area, a one-line reason to reach out and the dated public evidence behind each company.
2. **Near misses:** companies that failed exactly one must-have, and which one.
3. **What was removed and why:** individuals, lead-generation sites, off-topic results, chains, excluded owners, and the customers, open deals and do-not-contact names it matched, each named.
4. **People-search filters** to paste into your own prospecting tool: a job-title Boolean string, the company domains and the location and size.
5. **Sources it could not check,** and why.

## What it can change for you

With your yes on the exact payload, it can save the list to a new tab in your Google Sheet. It never writes into an existing tab. This needs a Read & Write connection, and an owner, admin or operator can switch it off.

It never looks up or guesses personal email addresses or phone numbers, and it never sends anything.

## Tips

- Give it your customer and open-deal lists every time. Dedupe by domain is the reason the list doesn't embarrass your sales team.
- Pass the finished list to the B2B Lead Enrichment skill (if installed) to score each company in depth, then to the Cold Email Writer (if installed) for the first message.
- DataForSEO is paid per call. If the listings or search calls fail with a payment error, the skill says so and carries on with the ad libraries, the app stores or your paste.
