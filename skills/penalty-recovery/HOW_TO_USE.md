# How to Use This Skill

Hey Claude, I just added the "penalty-recovery" skill. Our Google traffic dropped. Work out whether it's a penalty or an update, and plan the recovery.

## What you need

- **The Manual actions and Security issues messages,** copied from Search Console (Security & Manual Actions). Paste them, or say both read "No issues detected". Google doesn't share these reports through its API, so the skill can't fetch them.
- **Your daily Search Console data:** the Dates tab of a Performance export, or Search Console connected through the InsightfulPipe MCP so the skill pulls it.
- **Your link history,** if anyone ever bought or built links for the site, and the agency's report if there is one.
- **Optional connections** through the InsightfulPipe MCP: DataForSEO for the backlink profile, the site crawler for page checks, and GA4 to rule out a tracking break.

## Example requests

**Manual action for links**
Hey Claude, I just added the "penalty-recovery" skill. We got a manual action for unnatural links. Here's the message and our old agency's link report. Build the cleanup list and write the reconsideration request.

**Sudden drop, no message**
Hey Claude, I just added the "penalty-recovery" skill. Our clicks fell 40% last month and the Manual actions report says no issues. Was it a core update, a spam update or something on our side?

**Hacked site warning**
Hey Claude, I just added the "penalty-recovery" skill. Search Console shows "Hacked: URL injection" with these sample URLs. Find the injected pages and draft the review request.

**Negative SEO worry**
Hey Claude, I just added the "penalty-recovery" skill. Hundreds of spammy sites started linking to us. Do I need a disavow file?

## What you get

1. **The case in one line:** manual action, security issue, algorithmic, or a cause outside Google.
2. **A timeline** of your daily clicks, with each Google update, message date and site change marked "lines up", "demand", "unclear" or "no clear effect".
3. **Checks that rule out lookalikes:** a tracking break, pages dropped from the index, or fewer people searching.
4. **Where the loss sits,** section by section, compared with the scope in the message.
5. **The fix plan** for your case type, built from your own pages and links.
6. **For a link problem only:** every linking domain in a class (remove, disavow, review, no action, keep), with the reasons, and a disavow file in Google's format.
7. **The reconsideration or review request,** in three parts, with brackets for anything not yet done.
8. **Dated recovery checks.**

## What it never does

It doesn't upload the disavow file, send the request, email site owners or change your site. You do those from your own Search Console and inbox.

## Tips

- Check both reports before anything else. With no manual action, most sites never need a disavow file.
- Fix every issue on every page before you send the request. A partial fix doesn't bring a partial return.
- Send one request and wait for the answer. Google says most reviews take several days or weeks, and link reviews can take longer.
