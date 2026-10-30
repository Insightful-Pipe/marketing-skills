# How to Use This Skill

Hey Claude, I just added the "repo-readme-optimizer" skill. Audit the README of my open-source booking widget and rewrite it so the repo ranks and gets cited. Here's the current file.

## What you need

- **The README:** paste it, upload it, or give the public repo URL. For a new project, a short brief is enough: what it does, for whom, the install command and one example.
- **Optional, the InsightfulPipe MCP** with DataForSEO, Search Console or GA4 connected. Without them the skill still audits and rewrites from the text. With them it picks the wording from real search volume, checks which repos Google and AI answers already show for your category, adds the questions people search, and shows which README links send visitors.

## Example requests

**Audit and rewrite**
Hey Claude, I just added the "repo-readme-optimizer" skill. Audit this README section by section and give me the fixes in order, then the rewrite.

**New README from a brief**
Hey Claude, I just added the "repo-readme-optimizer" skill. Write a README for our new Python SDK. Install is `pip install example-sdk`, it needs Python 3.10 or later, and here's the quickstart.

**Repo card only**
Hey Claude, I just added the "repo-readme-optimizer" skill. Write the About line, topics and social preview brief for this repo, using the phrases people actually search.

**Why does a rival repo get cited?**
Hey Claude, I just added the "repo-readme-optimizer" skill. ChatGPT recommends another repo when people ask for a tool like ours. Check what AI answers cite for our category and fix our README.

## What you get

1. **The words to use:** candidate phrases with search volume, which ones honestly describe the tool, and where each goes.
2. **Who answers today:** the repos and pages Google and AI answers show for the category, and whether yours is among them.
3. **An audit of seven parts:** repo card, first screen, start, proof, answers, links, and safety, each with the line that decides it.
4. **Fixes in order:** secrets first, then anything that blocks a first run, then unsourced claims, wording, questions and polish.
5. **The finished repo card and README,** plus a list of claims you need to back with a source and a list of the gaps the draft marks for you to fill (it never invents an import, a link or a screenshot).

## What it can change for you

Nothing on its own. It hands over the README text, or writes README.md in your local copy after you approve the diff, and drafts a `gh repo edit` command for the About line, website and topics for you to run.

## Tips

- Give the skill your real install command and versions; it won't invent them.
- Keep a link or source for every number you want in the README.
- Re-run it 4 to 6 weeks after the change to see whether the repo shows up in Google or AI answers.
