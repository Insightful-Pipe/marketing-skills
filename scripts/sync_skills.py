#!/usr/bin/env python3
"""Mirror the skills published on insightfulpipe.com into skills/<slug>/ and refresh the README list.

The source is the public catalogue that the website and the InsightfulPipe CLI read
(https://insightfulpipe.com/api/skills), so each folder holds exactly the files the site serves
for that skill. Skills the catalogue no longer lists are removed. When anything changes, the
plugin version becomes today's date, so Claude Code sees an update.

Usage: python3 scripts/sync_skills.py   (run from the repository root; no dependencies)
"""
import base64
import datetime
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.request

SITE = "https://insightfulpipe.com"
PAGES = f"{SITE}/marketing-claude-skills"
# The site refuses the default Python user agent.
USER_AGENT = "InsightfulPipe-skills-mirror/1.0 (+https://github.com/Insightful-Pipe/marketing-skills)"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
README = os.path.join(ROOT, "README.md")
PLUGIN = os.path.join(ROOT, ".claude-plugin", "plugin.json")
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
START, END = "<!-- SKILLS:START -->", "<!-- SKILLS:END -->"
# Refuse to delete more than this share of the mirrored skills in one run: a short catalogue
# is far more likely to be a site problem than a mass unpublish.
MAX_REMOVED_SHARE = 0.2


def get_json(path):
    for attempt in range(4):
        try:
            req = urllib.request.Request(f"{SITE}{path}", headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except Exception as exc:  # network blips and deploys in progress
            if attempt == 3:
                raise RuntimeError(f"{path}: {exc}") from exc
            time.sleep(5 * (attempt + 1))


def safe_path(folder, rel):
    full = os.path.normpath(os.path.join(folder, rel))
    if not full.startswith(folder + os.sep):
        raise RuntimeError(f"unsafe file path in the catalogue: {rel!r}")
    return full


def tree_digest(paths):
    h = hashlib.sha256()
    for base in paths:
        if os.path.isfile(base):
            h.update(base.encode())
            h.update(open(base, "rb").read())
            continue
        for dirpath, dirnames, filenames in sorted(os.walk(base)):
            dirnames.sort()
            for name in sorted(filenames):
                p = os.path.join(dirpath, name)
                h.update(os.path.relpath(p, ROOT).encode())
                h.update(open(p, "rb").read())
    return h.hexdigest()


def first_sentence(text, limit=170):
    text = " ".join(text.split())
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    sentence = m.group(1) if m else text
    if len(sentence) <= limit:
        return sentence
    cut = sentence[: limit - 1]
    return cut[: cut.rfind(" ")].rstrip(",;:") + "…"


def cell(text):
    return text.replace("|", "\\|").replace("\n", " ")


def sync_files(skill):
    data = get_json(f"/api/skills/{skill['category']}/{skill['slug']}/files")
    folder = os.path.join(SKILLS_DIR, skill["slug"])
    os.makedirs(folder, exist_ok=True)
    keep = set()
    for f in data["files"]:
        raw = base64.b64decode(f["content"]) if f.get("encoding") == "base64" else f["content"].encode("utf-8")
        if f.get("sha256") and hashlib.sha256(raw).hexdigest() != f["sha256"]:
            raise RuntimeError(f"{skill['slug']}/{f['path']}: checksum does not match the catalogue")
        target = safe_path(folder, f["path"])
        os.makedirs(os.path.dirname(target), exist_ok=True)
        if not os.path.exists(target) or open(target, "rb").read() != raw:
            with open(target, "wb") as out:
                out.write(raw)
        keep.add(os.path.relpath(target, folder))
    for dirpath, _, filenames in os.walk(folder):
        for name in filenames:
            p = os.path.join(dirpath, name)
            if os.path.relpath(p, folder) not in keep:
                os.remove(p)


def skills_section(catalogue, skills):
    cats = catalogue.get("categories", {})
    order = list(cats) + sorted({s["category"] for s in skills} - set(cats))
    lines = [
        START,
        f"**{len(skills)} skills in {len({s['category'] for s in skills})} categories.** "
        "The skill name opens its folder here; **Page** opens it on insightfulpipe.com with the full sample run and a ZIP download.",
        "",
    ]
    for key in order:
        group = sorted((s for s in skills if s["category"] == key), key=lambda s: s["displayName"].lower())
        if not group:
            continue
        meta = cats.get(key, {})
        lines += [f"### {meta.get('displayName', group[0]['categoryDisplayName'])}", ""]
        if meta.get("description"):
            lines += [meta["description"].rstrip(".") + ".", ""]
        lines += ["| Skill | What it does | |", "|---|---|---|"]
        for s in group:
            lines.append(
                f"| [{cell(s['displayName'])}](skills/{s['slug']}/) | {cell(first_sentence(s['description']))} "
                f"| [Page]({PAGES}/{s['category']}/{s['slug']}) |"
            )
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def set_version(path, version, keys):
    data = json.load(open(path))
    node = data
    for k in keys[:-1]:
        node = node.setdefault(k, {})
    node[keys[-1]] = version
    with open(path, "w") as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
        out.write("\n")


def main():
    catalogue = get_json("/api/skills")
    skills = catalogue.get("skills") or []
    if not skills:
        sys.exit("The catalogue lists no skills; leaving the mirror as it is.")
    slugs = {s["slug"] for s in skills}
    if len(slugs) != len(skills):
        sys.exit("Two published skills share a slug; folders here are named by slug, so stopping.")

    os.makedirs(SKILLS_DIR, exist_ok=True)
    existing = {d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))}
    removed = existing - slugs
    if existing and len(removed) > MAX_REMOVED_SHARE * len(existing):
        sys.exit(f"The catalogue dropped {len(removed)} of {len(existing)} mirrored skills; stopping without changes.")

    before = tree_digest([SKILLS_DIR, README])
    for s in sorted(skills, key=lambda s: s["slug"]):
        sync_files(s)
    for slug in removed:
        shutil.rmtree(os.path.join(SKILLS_DIR, slug))

    readme = open(README).read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        sys.exit("README.md has no skills markers.")
    readme = pattern.sub(lambda _: skills_section(catalogue, skills), readme)
    with open(README, "w") as out:
        out.write(readme)

    if tree_digest([SKILLS_DIR, README]) != before:
        today = datetime.datetime.now(datetime.timezone.utc).date()
        version = f"{today.year}.{today.month}.{today.day}"
        set_version(PLUGIN, version, ["version"])
        set_version(MARKETPLACE, version, ["metadata", "version"])
        print(f"Updated: {len(skills)} skills ({len(removed)} removed), version {version}.")
    else:
        print(f"No changes: {len(skills)} skills.")


if __name__ == "__main__":
    main()
