# How to Use This Skill

Hey Claude, I just added the "prospect-marketing-audit" skill. Audit tarrowcreekhvac.example before my pitch call and tell me the findings worth opening with.

## What you need

- **The prospect's website,** and the city if it's a local business.
- **Your agency's name and the services you sell,** so the pitch only leads with problems you can fix.
- **Optional: the InsightfulPipe MCP connected to Claude,** with the Ads Libraries, PageSpeed Insights, Crawler and DataForSEO sources. With it, the skill pulls everything itself. Without it, paste what you have (an ad library count, a PageSpeed report, an SEO tool export, Google Maps review counts) and the skill marks the rest as not checked.

## Example requests

**Full pre-pitch audit**
Hey Claude, I just added the "prospect-marketing-audit" skill. Audit tarrowcreekhvac.example, a heating and cooling company in Tarrow Creek, CO. We sell paid social, local SEO and website speed work.

**Ads only**
Hey Claude, I just added the "prospect-marketing-audit" skill. Which ad libraries is this company in, how old are their Meta ads, and do they have the matching pixels on the site?

**From pasted data, no connection**
Hey Claude, I just added the "prospect-marketing-audit" skill. Here's the PageSpeed report and the Meta Ad Library count for a prospect. Grade what you can and write the email.

**Email and talk track**
Hey Claude, I just added the "prospect-marketing-audit" skill. Use the audit to write a short cold email and a talk track for a 15-minute call.

**The deep version after they sign**
Hey Claude, I just added the "prospect-marketing-audit" skill. The client just gave us access. Rerun the audit on their Search Console and Google Business Profile and show what changed from the outside view.

## What you get

1. **A scorecard for six areas:** ads in the public libraries, tags, speed, site basics, search footprint and local reputation, each graded pass, warn, fail or not checked.
2. **Three to five pitch findings,** each with what was seen (a library link and date, a URL and status code, a keyword and position, a PageSpeed run), what is assumed, and a size in searches, ads, days, seconds or reviews.
3. **A short outreach email** that leads with the finding the prospect can check for themselves.
4. **A call talk track** with one question per finding and the access you'd ask for.
5. **A list of what couldn't be checked,** and why.

## Good to know

- It reads public data only and changes nothing.
- It never estimates a prospect's ad spend, leads or revenue. The ad libraries don't show spend, so it doesn't guess.
- It uses real-user speed data when Google has it and says when a number is a lab run instead.
- A tag missing from one page load is reported as "not seen", because a consent banner can hold a pixel back.
- Search numbers are DataForSEO estimates, not the prospect's analytics.

## Tips

- Run it the day before the call: libraries and pages change daily, and the audit is dated.
- Tell it what you sell. A finding you can't fix doesn't belong in your pitch.
- After you win the account, run the deep version to replace every estimate with the client's own numbers.
