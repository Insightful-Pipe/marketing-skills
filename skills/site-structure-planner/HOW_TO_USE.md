# How to Use This Skill

Hey Claude, I just added the "site-structure-planner" skill. Plan my site structure for SEO from my keywords and my Search Console data, and don't move any page that ranks without a redirect.

## What you need

- **Your keywords,** pasted or as a keyword tool export, with monthly searches. Cluster labels help; without them, Claude groups the keywords itself. For a new site, a list of the pages you plan works too.
- **What you sell and who you sell to,** so clusters for things you don't offer are dropped.
- **For an existing site, one of these:**
  - the InsightfulPipe MCP connected to Claude with Google Search Console, GA4 and the Web Crawler, so it reads your pages, traffic, key events, redirects and click depth itself, or
  - a page list, a sitemap or a Search Console pages export with clicks.
- **Any host questions:** a help center, docs, an app, a second product or a country site, and the tool that would host it.

DataForSEO is optional: if your list has no volumes, it can fetch them (billed to your DataForSEO account).

## Example requests

**New site from a keyword list**
Hey Claude, I just added the "site-structure-planner" skill. We're launching a booking app for salons and clinics. Here's our keyword export. Give me the sections, the URLs, the menu and the breadcrumbs.

**Growing an existing site**
Hey Claude, I just added the "site-structure-planner" skill. We're adding industry and comparison pages. Plan where they go, which pages need a hub, and which existing URLs should move.

**SEO friendly URL structure**
Hey Claude, I just added the "site-structure-planner" skill. Check our URLs against clean slug rules and give me the redirect map for any that should change, with the traffic each one carries.

**Subdomain vs subfolder**
Hey Claude, I just added the "site-structure-planner" skill. Should our help center and our UK site sit on a subdomain, a subfolder or a separate domain?

## What you get

1. **A section tree:** each section with its hub, its search demand and its pages.
2. **A URL map:** one row per planned page with its cluster, searches, URL, status (keep, new or move), click depth now and planned, and the clicks and key events it already earns.
3. **Navigation:** the header menu ordered by demand, the footer, and a breadcrumb trail for every page.
4. **A redirect map** for an existing site: every moved URL with its 301, the traffic at stake, chains repointed, rules to remove first, and the internal links to update.
5. **Click depth and orphans:** pages buried too deep, pages no link reaches, and folders with no hub, each with its fix.
6. **Host decisions:** subfolder, subdomain or separate domain for each question, with the reason.
7. **Unknowns,** and what each next step needs.

## What it changes

Nothing. It hands you the plan; you or your developer apply it.

## Tips

- Pages that already rank keep their URL unless the URL itself is broken (uppercase, underscores, dates, file extensions). The plan places them in the right section through the menu and breadcrumbs instead.
- Change the thresholds if they don't fit your site: 10 clicks or 1 key event to protect a URL, 30 monthly searches for a page of its own, and 3 clicks as the depth limit.
- Move URLs in batches and keep the redirects for at least a year.
