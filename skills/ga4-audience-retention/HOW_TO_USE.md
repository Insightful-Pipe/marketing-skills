# How to Use This Skill

Hey Claude, I just added the "ga4-audience-retention" skill. Who are my GA4 users, where do they come from, and do they come back?

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the data itself; you don't need to export anything.
- **The countries you sell to,** if you want the skill to point out a market that is missing or small.
- **A window,** if you don't want the default of the last 12 complete weeks.

## Example requests

**New vs returning users**
Hey Claude, I just added the "ga4-audience-retention" skill. Show me new vs returning users by week for the last 12 weeks, and tell me whether returning visitors behave differently.

**Retention cohorts**
Hey Claude, I just added the "ga4-audience-retention" skill. Build a weekly retention cohort table from GA4 and tell me how many people come back one and four weeks after their first visit.

**Value by acquisition channel**
Hey Claude, I just added the "ga4-audience-retention" skill. Which channel brings users who are worth the most over time, not just on their first visit?

**Devices, browsers and the mobile gap**
Hey Claude, I just added the "ga4-audience-retention" skill. Break my GA4 traffic down by device and browser, and tell me whether mobile converts worse than desktop.

**Countries, cities and demographics**
Hey Claude, I just added the "ga4-audience-retention" skill. Which countries and cities send real, engaged visitors, and what do we know about their age, gender and interests? We sell in the US and UK.

## What you get

1. **A three-line headline:** who your users are, whether they come back, and the one thing to act on.
2. **A data quality check first:** cities, browsers or devices that behave like automated traffic, sessions that switch country part-way through, and users with no first-visit record.
3. **New vs returning users by week,** with a verdict on your returning share.
4. **A retention cohort table** from GA4's own cohort report, with week +1 and week +4 return rates, overall and by channel.
5. **Value by acquisition channel,** measured on users who had at least 4 weeks to come back.
6. **Devices and browsers,** including the mobile vs desktop gap, tested so a handful of sessions is never called a trend.
7. **Countries and cities,** shown with and without suspicious traffic.
8. **Age, gender and interests** when GA4 reports them, or the reason it doesn't.

## What it can change for you

With your yes on the exact audience, it can create a GA4 audience for a segment the report found, such as returning users or a strong country. It checks your existing audiences first, and never builds one around suspicious traffic, a segment with fewer than 30 users, or a segment that is nearly your whole audience.

It never changes Google signals, data retention, key events or channel groups.

## Tips

- Run it monthly, or after a campaign that should bring people back.
- If no key events or revenue were recorded, the report uses engagement and says so everywhere. Fix tracking first to see real value by channel.
- Small sites: expect "too few sessions to compare" often. That's the skill refusing to call chance a trend.
- Demographics need Google signals turned on in GA4. Without it, that section says "not graded".
