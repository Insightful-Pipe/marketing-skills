# How to Use This Skill

Hey Claude, I just added the "app-attribution-auditor" skill. Audit our mobile app install attribution and tell me which install and event numbers we can trust before we move budget.

## What you need

- **Your measurement partner's exports:** the integration settings per network, installs by network and platform, the iOS conversion value schema, the SKAdNetwork postback report by campaign, and a cohort with revenue by day. AppsFlyer, Adjust, Branch and Singular all work.
- **Store console numbers:** App Store Connect first-time downloads and Play Console users acquired for the same days.
- **Your networks' numbers:** with Google Ads, Meta, TikTok, Snapchat and GA4 connected through the InsightfulPipe MCP, the skill pulls them itself. Otherwise paste or upload each network's campaign export. Apple Ads and other networks come from their own exports.
- **28 install days that ended at least 42 days ago.** That is when every SKAN 4 postback for those installs has arrived.

## Example requests

**Full audit**
Hey Claude, I just added the "app-attribution-auditor" skill. Here are our AppsFlyer exports and store console numbers for August 21 to September 17. Pull Google Ads, Meta, TikTok and Snapchat yourself and run the full audit.

**Conversion value schema only**
Hey Claude, I just added the "app-attribution-auditor" skill. Test our SKAdNetwork conversion value schema against this cohort. Do the fine values rank users by what they're worth, and do postbacks 2 and 3 catch our trial conversions?

**Numbers don't match**
Hey Claude, I just added the "app-attribution-auditor" skill. Meta says 2,950 iOS installs, Adjust says 1,750 and App Store Connect says something else again. Reconcile installs by platform and tell me which number to budget on.

**Privacy thresholds**
Hey Claude, I just added the "app-attribution-auditor" skill. Which of our iOS campaigns get postbacks with no conversion value, and how much spend sits in them?

**Audit, then fix Google Ads**
Hey Claude, I just added the "app-attribution-auditor" skill. Check whether Google Ads counts our Android first opens twice, and if it does, show me the change before you make it.

## What you get

1. **A scorecard for five areas:** partner wiring, platform counting, the conversion value schema, privacy thresholds and install reconciliation.
2. **Ranked fixes,** ordered by the ad spend each one touches, with the numbers behind it and who makes the change.
3. **A schema test:** every fine value with its users, average 35-day revenue and day 7 retention, the values ranked out of order, and a proposed order and postback mapping.
4. **A privacy table** of every iOS campaign: the share of first postbacks with no value, coarse only and fine.
5. **Reconciliation tables** for iOS and Android: store console, measurement partner, GA4 and each network's claim.
6. **A budget readiness verdict** for every network and platform: fix first, too small to read on iOS, use partner numbers only, or ready.

## What it can change for you

With your yes on the exact change, in Google Ads only, it can:
- stop counting a duplicate install conversion action
- point an App campaign at one conversion action

Everything else, including the schema and your partner's settings, comes as a recommendation for you to make.

## Tips

- Run it before every quarterly budget plan, and after any change to the schema, the SDK or a network integration.
- Send the schema exactly as it is set in your partner, including the coarse mapping for all three postbacks.
- The cohort only needs Android users and iOS users who allowed tracking. That is enough to test what the iOS values mean.
