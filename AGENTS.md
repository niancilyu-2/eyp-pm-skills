# AGENTS.md — PM AI Workshop

This repo provides three Product-Manager workflow **skills**, usable from both **Codex** and
**Claude Code**. For Codex they live in `.agents/skills/` (auto-discovered); for Claude Code they
live in `skills/` (a plugin). Both are generated from the same source — see "Repo notes" below.

## The three skills (Codex auto-discovers them from `.agents/skills/`)
- **`pm-ideation`** — mixed-format signals (calls, churn, competitor docs, roadmap) → a problem
  statement + roadmap recommendation. Invoke with `$pm-ideation` or just describe the task.
- **`pm-prototype`** — a problem statement/idea → a single clickable, self-contained HTML prototype.
- **`pm-plan-and-estimate`** — prototype notes + a codebase → a planning doc, an effort + dollar
  estimate, and an engineering-ready spec (a precursor to `thorough-writing-plans`).

They form a chain (`pm-ideation` → `pm-prototype` → `pm-plan-and-estimate`) but each works alone.

## How to behave when running these
- **Always apply the rigor layer.** Each skill loads `references/rigor-checklist.md` (a copy lives in
  every skill folder). Cite every claim, label evidence vs. inference vs. assumption, never
  fabricate, quantify signals, run the red-team pass, produce review-ready output.
- **Honor the brainstorm/approach gates** in `pm-prototype` and `pm-plan-and-estimate` — don't
  one-shot a deliverable; present options and let the user choose.
- **Stop at the spec.** The PM skills never write code; `pm-plan-and-estimate` hands a verified spec
  to engineering's `thorough-writing-plans`.

## Data & codebase
- Default workshop inputs: `workshop/mock-data/` (mixed `.docx/.xlsx/.pdf/.pptx/.md`). The skills are
  **gap- and format-agnostic**; the scenario is carried entirely by the data.
- Use your own inputs: drop them in `workshop/your-data/` (git-ignored) and run
  `$pm-ideation workshop/your-data`. See `docs/customizing-mock-data.md`.
- Estimation needs a real codebase: `./scripts/clone-umbraco.sh` populates `workshop/codebase/`.

## Prerequisites
Python 3 with `openpyxl`, `python-docx`, `python-pptx` (so `pm-ideation` can read Office files);
git; a browser (to open prototypes); Node 18+ only for the optional React prototype paths. See
`docs/prerequisites.md`.

## Repo notes (for maintainers)
- **Single source of truth:** `skills/` (the Claude Code plugin). The Codex tree `.agents/skills/`
  is **generated** from it by `scripts/build-codex-skills.py` (it copies each skill, inlines the
  shared rigor file, and rewrites Claude's `${CLAUDE_*}` path variables to relative paths).
- **After editing anything in `skills/` or `references/rigor-checklist.md`, re-run**
  `python3 scripts/build-codex-skills.py` to refresh `.agents/skills/`.
- Full docs in `docs/`. License/attribution for the vendored web-artifacts-builder is under
  `.agents/skills/pm-prototype/scripts/web-artifacts-builder/` (Apache-2.0).
