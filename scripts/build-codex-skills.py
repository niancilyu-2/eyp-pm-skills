#!/usr/bin/env python3
"""
Generate a Codex-compatible skill tree at .agents/skills/ from the Claude source in skills/.

Why this exists
---------------
The same three skills target two agents:
- **Claude Code** reads `skills/<name>/SKILL.md` (a plugin) and expands `${CLAUDE_SKILL_DIR}`.
- **Codex** reads `.agents/skills/<name>/SKILL.md`, has NO such variables, and resolves paths and
  shell commands from the WORKSPACE ROOT — so rewritten paths must be explicit repo-root paths
  (bare relative paths would collide with the real root-level `scripts/` and `references/`).

`skills/` stays the single source of truth. This script:
1. syncs the rigor master (`references/rigor-checklist.md`) into every skill's own `references/`
   (in the SOURCE tree — both Claude and Codex then use the same per-skill copy),
2. copies each skill folder into `.agents/skills/<name>/`,
3. rewrites `${CLAUDE_SKILL_DIR}/X` (and the bare variable) to `.agents/skills/<name>/X` in all
   copied markdown files (scripts, incl. the vendored Apache-2.0 web-artifacts-builder, are copied
   verbatim),
4. FAILS (exit 1) if any `${CLAUDE_*}` variable survives anywhere in the generated tree.

Usage:
  python3 scripts/build-codex-skills.py           # build/refresh the mirror
  python3 scripts/build-codex-skills.py --check   # verify mirror is in sync; exit 1 on drift
"""
import filecmp
import os
import re
import shutil
import sys
import tempfile

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SRC = os.path.join(ROOT, "skills")
DST = os.path.join(ROOT, ".agents", "skills")
RIGOR = os.path.join(ROOT, "references", "rigor-checklist.md")

VAR_RE = re.compile(r"\$\{CLAUDE_[A-Z_]+\}")
SCAN_EXT = {".md", ".sh", ".html", ".css", ".js", ".ts", ".tsx", ".txt", ".json", ".yaml", ".yml"}


def rewrite_paths(text: str, skill_name: str) -> str:
    """${CLAUDE_SKILL_DIR}[/]X -> .agents/skills/<name>/X (explicit repo-root path for Codex)."""
    return re.sub(r"\$\{CLAUDE_SKILL_DIR\}/?", f".agents/skills/{skill_name}/", text)


def sync_rigor_into_source(skills: list) -> None:
    """Keep each skill's references/rigor-checklist.md identical to the master."""
    for name in skills:
        ref_dir = os.path.join(SRC, name, "references")
        os.makedirs(ref_dir, exist_ok=True)
        dst = os.path.join(ref_dir, "rigor-checklist.md")
        if not (os.path.exists(dst) and filecmp.cmp(RIGOR, dst, shallow=False)):
            shutil.copy2(RIGOR, dst)
            print(f"  synced rigor -> skills/{name}/references/")


def build(dst_root: str, skills: list) -> list:
    """Build the mirror under dst_root; return [(path, vars)] problems."""
    problems = []
    os.makedirs(dst_root, exist_ok=True)
    for name in skills:
        s = os.path.join(SRC, name)
        d = os.path.join(dst_root, name)
        if os.path.isdir(d):
            shutil.rmtree(d)
        shutil.copytree(s, d)

        # Rewrite path variables in every markdown file; scripts stay verbatim.
        for dirpath, _dirs, files in os.walk(d):
            for fn in files:
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(dirpath, fn)
                with open(p, encoding="utf-8") as f:
                    text = f.read()
                new = rewrite_paths(text, name)
                if new != text:
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(new)

        # Scan ALL text files for surviving ${CLAUDE_*} vars — must fail, not warn.
        for dirpath, _dirs, files in os.walk(d):
            for fn in files:
                if os.path.splitext(fn)[1].lower() not in SCAN_EXT:
                    continue
                p = os.path.join(dirpath, fn)
                with open(p, encoding="utf-8", errors="ignore") as f:
                    found = set(VAR_RE.findall(f.read()))
                if found:
                    problems.append((os.path.relpath(p, ROOT), found))
        print(f"  generated {os.path.relpath(d, ROOT)}")
    return problems


def dirs_differ(a: str, b: str) -> list:
    """Recursive diff; returns list of differing/missing relative paths."""
    diffs = []
    cmp = filecmp.dircmp(a, b)
    def walk(c, rel=""):
        for n in c.left_only:
            diffs.append(os.path.join(rel, n) + " (missing in mirror)")
        for n in c.right_only:
            diffs.append(os.path.join(rel, n) + " (extra in mirror)")
        for n in c.diff_files + c.funny_files:
            diffs.append(os.path.join(rel, n))
        for n, sub in c.subdirs.items():
            walk(sub, os.path.join(rel, n))
    walk(cmp)
    return diffs


def main(argv: list) -> int:
    if not os.path.isdir(SRC):
        print("No skills/ directory found."); return 1
    skills = sorted(d for d in os.listdir(SRC)
                    if os.path.isfile(os.path.join(SRC, d, "SKILL.md")))

    if "--check" in argv:
        # Rebuild into a temp dir and compare against the committed mirror.
        with tempfile.TemporaryDirectory() as tmp:
            sync_rigor_into_source(skills)
            problems = build(tmp, skills)
            if problems:
                print("FAILED: unresolved ${CLAUDE_*} variables:")
                for path, found in problems:
                    print(f"  {path}: {sorted(found)}")
                return 1
            diffs = dirs_differ(tmp, DST)
            if diffs:
                print("\nDRIFT: .agents/skills/ is out of sync with skills/ — re-run this script:")
                for x in diffs[:20]:
                    print("  ", x)
                return 1
        print("\nMirror in sync.")
        return 0

    sync_rigor_into_source(skills)
    problems = build(DST, skills)
    if problems:
        print("\nFAILED: unresolved ${CLAUDE_*} variables in the generated Codex tree:")
        for path, found in problems:
            print(f"  {path}: {sorted(found)}")
        return 1
    print(f"\nDone. {len(skills)} skills written to .agents/skills/ for Codex.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
