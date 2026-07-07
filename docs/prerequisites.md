# On-site prerequisites (participants)

The skills run in **either Claude Code or Codex**. Pick one per machine; the prerequisites are
nearly identical.

## Required (core three-skill flow)
1. **An agent CLI** — **Claude Code** *or* **Codex** (latest). The skills run inside it.
2. **Git** — to get the plugin/skills and clone the mock codebase.
3. **Python 3.10+** with three libraries — so `pm-ideation` can read the Office-format inputs
   (`.xlsx/.docx/.pptx`):
   ```
   pip install openpyxl python-docx python-pptx
   ```
4. **A modern web browser** — to open the clickable HTML prototype from `pm-prototype`.
5. **A clone of this repo** — `niancilyu-2/eyp-pm-skills` is public:
   `git clone https://github.com/niancilyu-2/eyp-pm-skills.git` then run your agent **from the repo
   root** (the plugin install alone does not deliver the workshop data — paths are repo-relative).

## Optional (only beyond the core path)
6. **Node 18+ and npm** — only for `pm-prototype`'s React escalation paths (zero-build HTML needs none).
7. **poppler-utils (`pdftotext`)** — PDF fallback; skip if the agent's file reader handles PDFs.
8. **GitHub CLI (`gh`)** — handy if `pm-ideation` pulls live Umbraco GitHub signals.
9. **~300 MB free disk** — Umbraco clone (~150 MB) + npm if the React paths are used.

## How each agent finds the skills
- **Claude Code:** install the plugin —
  `/plugin marketplace add niancilyu-2/eyp-pm-skills` then `/plugin install eyp-pm-skills@eyp-pm-skills`.
- **Codex:** clone the repo and work inside it — Codex auto-discovers skills from `.agents/skills/`.
  Invoke with `$pm-ideation` (or `/skills`), or just describe the task. `AGENTS.md` gives Codex the
  project context.

## Windows
All documented commands are bash/POSIX. On Windows, use **WSL** (or Git Bash for the simple ones) —
native PowerShell is not supported by the docs as written.

## Facilitator pre-stage
- Pre-clone Umbraco (`./scripts/clone-umbraco.sh`) or hand out a snapshot.
- Verify the Python libs install cleanly on the workshop image (a shared venv is fine). **This is the
  prerequisite most likely to trip people up** — without it, the spreadsheet/Word/PowerPoint inputs
  won't parse cleanly.
- Have everyone clone the repo **before** the session (venue Wi-Fi + 30 simultaneous clones is the
  bottleneck; the repo itself is small, but the optional Umbraco clone is ~150 MB — pre-stage that
  or run WF3 as a facilitator-only demo).
