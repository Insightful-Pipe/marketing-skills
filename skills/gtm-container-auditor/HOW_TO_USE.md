# How to Use This Skill

Hey Claude, I just added the "gtm-container-auditor" skill. Audit my Google Tag Manager container and tell me what to clean up before I add anything new.

## What you need

- **The InsightfulPipe MCP connected to Claude, with your Google Tag Manager account added** (and Google Analytics for tracking builds). The skill reads the container itself; you don't need to export anything. No connection? Paste a container export (Admin > Export container) instead, or for a tracking build just list what you want to track.
- **Your website address,** if the container name doesn't show it. The skill checks that the site really loads the container.
- **Whether you have visitors in the EEA or UK.** It decides how strict the consent checks are.
- **For a build:** what you want to track, whether a developer can change the site's code, which booking, form or video tools are embedded, and any other domains in the journey (checkout or app). Connect GA4 too, or have your G- measurement id ready.

## Example requests

**Full audit**
Hey Claude, I just added the "gtm-container-auditor" skill. Audit the container for example.com and grade it.

**Cleanup list**
Hey Claude, I just added the "gtm-container-auditor" skill. List every paused tag, tag with no trigger, and trigger or variable nothing uses.

**Consent check**
Hey Claude, I just added the "gtm-container-auditor" skill. We have UK visitors. Check our Consent Mode setup and list the tags that fire without a consent check.

**Before you publish**
Hey Claude, I just added the "gtm-container-auditor" skill. Check our workspaces for conflicts and show me what changed in the last two versions.

**Build mode: track what's missing**
Hey Claude, I just added the "gtm-container-auditor" skill. Set up tracking for clicks on our Book a demo button, bookings in the scheduling widget on /demo/, scroll depth on blog posts and purchases on our app domain. Give my developer the dataLayer code and me a preview check for each event.

**Build a GA4 event**
Hey Claude, I just added the "gtm-container-auditor" skill. Set up a GA4 sign_up event with a method parameter from the data layer, and put it in a GA4 folder. Show me the payloads first.

## What you get

1. **A grade out of 100,** with the math shown, once the container has published tags.
2. **A scorecard for seven areas:** installation and live state, inventory and cleanup, trigger logic, Consent Mode, naming and organisation, version history, and workspaces and conflicts.
3. **The top fixes,** each with the tags, triggers and calls behind it.
4. **A cleanup list and a change log** between your last two versions.
5. **A server-side tagging readiness checklist.**
6. **A tracking build,** when you ask for one or the container is empty: what is already tracked (by the container or by GA4 enhanced measurement), how each new event fires, a GA4 limits check, the exact payloads, the dataLayer code for your developer, and a click-by-click preview check per event.

## What it can change for you

With your yes on the exact change, it can:
- create a new workspace for the build
- create triggers, data layer variables, GA4 event tags (including purchase) and a listener for an embedded widget
- create folders and move tags, triggers and variables into them
- pause a dead tag, or add a consent check to a tag
- turn on built-in variables such as Click URL
- run a compile check on the workspace before you preview it
- in GA4, register new parameters as custom dimensions and mark lead or purchase events as key events

Every Tag Manager change lands in a workspace draft. It never publishes and never deletes: you preview, test and submit in Tag Manager. GA4 changes apply to the property as soon as you say yes.

## Tips

- Run it before every big publish, and after an agency or developer hands the container over.
- Name your versions when you publish; the change log is only as readable as the names.
- For conversion tags and the Conversion Linker, use the conversion-tracking-auditor skill if you have it.
