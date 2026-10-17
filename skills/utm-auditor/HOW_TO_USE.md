# How to Use This Skill

Hey Claude, I just added the "utm-auditor" skill. Audit the UTM tags on my ads and in GA4, and tell me what's breaking my channel reports.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your GA4 property added.** The skill pulls the data itself; you don't need to export anything.
- **Your ad accounts added too** (Google Ads, Meta, LinkedIn) if you want the skill to check what each one sends. A platform that isn't connected is listed as not checked.
- **Your current naming convention,** if you have one. Without it, the skill proposes one.

## Example requests

**Full audit**
Hey Claude, I just added the "utm-auditor" skill. Check every UTM tag that reached GA4 in the last 30 days, and the tagging set in my ad accounts.

**Paid traffic in the wrong channel**
Hey Claude, I just added the "utm-auditor" skill. Half my traffic shows as Unassigned in GA4. Find the tags causing it.

**Meta ads only**
Hey Claude, I just added the "utm-auditor" skill. Check that every live Meta ad has URL tags and that they land in Paid Social.

**Build a convention**
Hey Claude, I just added the "utm-auditor" skill. Look at the UTMs we already use and write one naming convention for the team, with a template for each platform.

## What you get

1. **A grade out of 100,** with the math shown.
2. **A scorecard for five areas:** naming hygiene, channel mapping, Google Ads, Meta and LinkedIn.
3. **The top fixes,** ranked by the sessions or spend they affect, each with the numbers behind it.
4. **A naming convention** built from your own data, with a ready template per platform and a map from old spellings to new ones.
5. **A list of what couldn't be checked,** and why.

## What it can change for you

With your yes on the exact change, it can:
- set a Google Ads campaign's tracking template or final URL suffix
- give a Meta ad a new creative with URL tags
- add a rule to a custom GA4 channel group for traffic you can't re-tag

It never renames campaigns or edits your default channel group.

## Tips

- The audit reads the 30 days that end 2 days ago, because GA4 can take up to 48 hours to attribute a day's sessions. Until then they show as (not set) or Cross-network. If you ask for yesterday, the report marks those days as not final.
- Run it before a big launch, and again a week after, to catch tags lost on the way.
- Agree the convention with your team before re-tagging old campaigns, because renamed values report separately in GA4.
- If your ads land on several sites, say which GA4 property belongs to which site.
