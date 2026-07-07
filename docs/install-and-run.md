# Install & run

## Prerequisites
- **Claude Code** (CLI, desktop, or IDE).
- **git** (to clone the Umbraco codebase for the estimation skill).
- For regenerating mock data (optional): **Python 3** with `openpyxl`, `python-docx`, `python-pptx`,
  `fpdf2`.
- For the React-prototype escalation paths (optional): **Node 18+** and `npm`.

## 1a. Install — Claude Code
From a local clone of this repo:
```
/plugin marketplace add ./eyp-pm-skills   # (or whatever directory you cloned into)
/plugin install eyp-pm-skills@eyp-pm-skills
```
From GitHub:
```
/plugin marketplace add niancilyu-2/eyp-pm-skills
/plugin install eyp-pm-skills@eyp-pm-skills
```
(One name everywhere: repo, marketplace, and plugin are all `eyp-pm-skills`.)
The three skills auto-register. Invoke them as `/pm-ideation`, `/pm-prototype`,
`/pm-plan-and-estimate` — or just describe the task and they trigger from their descriptions.

## 1b. Install — Codex
No plugin step. Just clone the repo and run Codex from inside it:
```
git clone https://github.com/niancilyu-2/eyp-pm-skills.git
cd eyp-pm-skills
codex
```
Codex auto-discovers the skills from `.agents/skills/` and reads `AGENTS.md` for project context.
Invoke a skill with `$pm-ideation` (or browse `/skills`), or just describe the task. The run-the-chain
commands below are the same — replace the leading `/` with `$` for explicit invocation if you like.

> `.agents/skills/` is **generated** from `skills/` by `scripts/build-codex-skills.py`. It's
> committed, so participants don't need to build it. Maintainers re-run that script after editing
> `skills/` or `references/rigor-checklist.md`.

> **Important:** installing the plugin does NOT deliver the workshop data — the documented commands
> use repo-relative paths (`workshop/mock-data`, `workshop/outputs`). Clone the repo and **run your
> agent from the repo root**. Never run it from inside `workshop/codebase/Umbraco-CMS` — that clone
> contains its own agent config (`CLAUDE.md`, `.mcp.json`) and will hijack your session.

## 2. Workshop setup
```bash
# clone the real Umbraco codebase (large; git-ignored) — needed for pm-plan-and-estimate
./scripts/clone-umbraco.sh           # add --full for full history

# mock data is authored and committed under workshop/mock-data/ — nothing to generate.
# (python3 + openpyxl/python-docx/python-pptx are still needed so pm-ideation can READ the
#  office formats: pip install openpyxl python-docx python-pptx)
```

## 3. Run the chain
```
# 1) signals → problem statement + roadmap recommendation
/pm-ideation workshop/mock-data
#    (or your own inputs: /pm-ideation workshop/your-data)

# 2) problem → clickable prototype
/pm-prototype workshop/outputs/roadmap-recommendation.md
#    open the resulting workshop/outputs/<feature>-prototype.html in a browser

# 3) prototype → planning doc + estimate + spec
/pm-plan-and-estimate workshop/outputs/<feature>-prototype.html --codebase workshop/codebase/Umbraco-CMS
```

## Viewing a prototype
Double-click the `.html`, or serve it: `python3 -m http.server 8000` then open
`http://localhost:8000/workshop/outputs/<feature>-prototype.html`. Use the 💬 control to pin feedback
and **Export** it as JSON.

## Troubleshooting
- **A skill can't read a file** — check `skills/pm-ideation/references/ingest.md` for per-format
  commands and fallbacks. Office files are zips (`unzip -p file.docx word/document.xml`); PDFs work
  with the Read tool or `pdftotext`.
- **Estimation is slow** — `pm-plan-and-estimate` should scope to affected subsystems, not the whole
  146MB repo. If it scans everything, narrow the paths (see `references/cost-models.md`).
- **React escalation fails** — both paths need Node 18+ and network for `npm install`. The full
  (web-artifacts-builder) path also runs Parcel and extracts shadcn components, so it's heavier.
  For a live workshop, prefer the zero-build HTML default.
- **Plugin doesn't appear** — confirm the marketplace was added and the install command used
  `@eyp-pm-skills`. Skills live at `skills/<name>/SKILL.md`.
