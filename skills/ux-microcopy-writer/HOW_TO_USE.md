# How to Use This Skill

Hey Claude, I just added the "ux-microcopy-writer" skill. Review the buttons, labels and error messages on our signup page and rewrite the ones that confuse people.

## What you need

- **The strings to work on.** Any of these: paste them, upload your locale file (CSV or JSON), share screenshots, or give a URL. To write from scratch, describe the screen and what it does.
- **Your house style,** if you have one. Without it, the skill uses sentence case, "you" and "we", contractions and no exclamation marks.
- **Your character limits,** if your design system has them, and whether the interface is translated. Without them, the skill uses its starting limits per component and says so.
- **Words that must not change:** plan and product names, legal and consent text.
- Optional, through the InsightfulPipe MCP: **GA4** (forms started and not sent, 404 views, site search terms), **DataForSEO** (reads the button, link and label text on a page), the **site crawler** (checks your 404 page) and **Microsoft Clarity** (dead clicks, rage clicks and quick backs by page; untested until a Clarity project is connected). With these, the skill starts from the pages where people get stuck.

## Example requests

**Review a page**
Hey Claude, I just added the "ux-microcopy-writer" skill. Here is our checkout page URL. Check every button, label and error message and give me the rewrites with character counts.

**Write every state for a component**
Hey Claude, I just added the "ux-microcopy-writer" skill. We're adding a "Saved reports" list. Write the empty state, the no-results state, the delete dialog and the toasts.

**Error messages**
Hey Claude, I just added the "ux-microcopy-writer" skill. Here are our form validation messages. Rewrite them so people know what to fix. Errors can be 80 characters at most.

**Find the words that are failing**
Hey Claude, I just added the "ux-microcopy-writer" skill. Use GA4 and Clarity to find the pages where people get stuck, then fix the interface text on them.

**One glossary**
Hey Claude, I just added the "ux-microcopy-writer" skill. Here's our en.json. Our app calls the same thing an appointment, a booking and a reservation. Pick one name for each thing and rewrite the file.

## What you get

1. **Where the words fail** (when connected): pages with dead clicks, rage clicks or quick backs well above your own site's rate, forms people start and don't send, the 404 page's views and broken links, and searches for words your navigation never uses.
2. **A UI glossary:** one term for each thing, the words to avoid, and where they were found.
3. **Every string in one table:** where it lives, the component, the state, before and after, its length against its limit, the checks it failed and the reason. Strings that already work are kept and listed as kept.
4. **The missing states written:** loading buttons, empty and no-results states, per-field errors, success messages.
5. **A hand-off file** keyed by string id for your locale file or design tool, plus any `aria-label` that has to change with the visible text.
6. **Questions** for facts it won't invent (reply times, refund terms, whether a client is notified) and legal wording it left alone.

## What it can change for you

Nothing. It reads, and it writes text for you to ship. It never edits your site, app, locale file or design file, and it never submits a form.

## Tips

- Screenshots of error, loading and empty states help most: a page reader can't see a state that needs a click or a bad entry.
- Give your real limits when you have them; the starting limits are a guess at a typical layout.
- For an app behind a login, paste the locale file. The page reader can only read public pages.
- Test rewrites on high-traffic strings (a signup button, a pricing button) before rolling them out everywhere.
