# How to Use This Skill

Hey Claude, I just added the "competitor-swot-analyzer" skill. Build a SWOT on my top two competitors and tell me how to position against them.

## What you need

- **The InsightfulPipe MCP connected to Claude, with DataForSEO and Enrichment added.** The skill pulls search, page and company data itself; you don't need screenshots or exports.
- **Your domain and one to three competitor domains.** If you're not sure who your competitors are, the skill proposes the top ones from search and asks you to confirm.
- **Optional:** Ad Libraries for an ads snapshot, Google Play or the App Store if your product is an app, and your own Search Console for real comparison-search numbers.
- **For the change watch:** your last snapshot (pasted, or a Google Sheet connected through InsightfulPipe). The first watch run saves the baseline.
- **Optional, from you:** win/loss reasons, sales objections, review exports (G2, Capterra) and your prices. Public data can't show these.

## Example requests

**Full SWOT**
Hey Claude, I just added the "competitor-swot-analyzer" skill. We sell CRM software for small businesses at oursite.com. Build a full SWOT against competitor-a.com and competitor-b.com, with the opportunities to differentiate.

**Who are my competitors?**
Hey Claude, I just added the "competitor-swot-analyzer" skill. Map the competitive landscape for oursite.com: who competes with us in search, and which three should we watch?

**Messaging and positioning**
Hey Claude, I just added the "competitor-swot-analyzer" skill. How does competitor-a.com position itself, and which messages should we compete on or stay away from?

**Weak spots**
Hey Claude, I just added the "competitor-swot-analyzer" skill. What are competitor-a.com's biggest weaknesses? Here are some of their G2 reviews we exported.

**Pricing comparison**
Hey Claude, I just added the "competitor-swot-analyzer" skill. Compare competitor-a.com's plans and packaging with ours. We charge per seat.

**Battlecard**
Hey Claude, I just added the "competitor-swot-analyzer" skill. Our sales team keeps meeting competitor-a.com. Give them a battlecard: what to say, what not to say, and how to handle their counter.

**Comparison page and ads**
Hey Claude, I just added the "competitor-swot-analyzer" skill. We're writing an "us vs competitor-a" page. Tell us which search to target, which rows to put in the table, and draft search ads for their name.

**Several competitors, white space**
Hey Claude, I just added the "competitor-swot-analyzer" skill. Compare us with three competitors and tell us which message nobody owns yet.

**Launch watch**
Hey Claude, I just added the "competitor-swot-analyzer" skill. What have competitor-a.com and competitor-b.com launched, raised or announced in the last 12 months?

**Honest feedback**
Hey Claude, I just added the "competitor-swot-analyzer" skill. Red-team us against our competitors. Where are we weaker, and what should we fix first?

**Competitor monitoring (change watch)**
Hey Claude, I just added the "competitor-swot-analyzer" skill. Monitor competitor-a.com and competitor-b.com every week: compare against last week's snapshot in our Google Sheet and tell us only what changed (prices, pages, ads, rankings, AI mentions, launches) and what to do about each.

## What you get

1. **An executive summary:** each competitor's biggest strength and weakness, and your best angle against them.
2. **The landscape:** who competes with you in search, and how you do on the keywords you share.
3. **A side-by-side table:** search footprint, comparison searches, positioning, messaging themes, value proposition and key claims, plans, prices and support by plan, proof, and momentum.
4. **A SWOT per competitor,** where every item says whether it was seen or read into, and shows its evidence.
5. **Comparison angles:** who ranks for whose "vs" and "alternative" searches, a watch list, a battlecard, search ad drafts and a vs page outline.
6. **A launch watch:** dated launches, funding and features labelled "New" from the last 12 months.
7. **Honest feedback on you,** with one fix per finding.
8. **A positioning map and a list of gaps:** what couldn't be measured, and what you could add.

In change watch mode you get a shorter report instead: each change since the last snapshot with its before and after values, marked respond, watch or ignore, related changes grouped into one move, what fell below the bar, and the new snapshot for next time.

## What it can change for you

Nothing on any account. Ad drafts and page outlines are drafts for you to check and publish yourself. The only write is in change watch mode: after you confirm, it adds a new dated snapshot tab to your own Google Sheet (it never edits or deletes earlier tabs). That needs a Read & Write connection, and an owner, admin or operator can switch it off; without it, you get the snapshot as a block to save.

## Tips

- Give each competitor's domain, not just its name. Names are often shared by unrelated companies.
- If a competitor's brand is a common word, tell the skill its former name or how people search for it.
- Paste reviews, win/loss notes or sales objections when you have them: they fill the customer voice lens that public pages can't.
- Run the full read every quarter, and the change watch weekly or monthly in between. Keep the watch list and keywords the same between runs so the changes are real.
- To run the watch on a timer, save the request as a scheduled task (for example in Claude Code), with the Sheet named in it. If the saved request says to save the snapshot there, that counts as your go-ahead for every timed run: each one adds its new dated tab without asking. Leave that out and each run prints the snapshot for you to save instead.
