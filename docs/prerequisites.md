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
   Never used git or a terminal? Follow the appendix at the bottom, step by step.
6. **Agent settings** — use your agent's strongest reasoning tier (Claude Code: the default
   Opus/Sonnet model is fine; Codex: GPT-5-class at Medium reasoning or higher — a tester ran the
   full chain on GPT-5.5/Medium successfully). Workflow 3 benefits most from stronger reasoning.

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
native PowerShell is not supported by the docs as written. Two Windows-specific notes:
- **Long paths:** before cloning the Umbraco codebase, run `git config --global core.longpaths true`
  (the clone script also sets it per-clone). Without it, checkout fails on deeply nested frontend
  files even though the clone appears to succeed.
- If IT policy blocks WSL, Git Bash (installed with Git for Windows) covers everything in the core
  path.

## Facilitator pre-stage
- Pre-clone Umbraco (`./scripts/clone-umbraco.sh`) or hand out a snapshot.
- Verify the Python libs install cleanly on the workshop image (a shared venv is fine). **This is the
  prerequisite most likely to trip people up** — without it, the spreadsheet/Word/PowerPoint inputs
  won't parse cleanly.
- Have everyone clone the repo **before** the session (venue Wi-Fi + 30 simultaneous clones is the
  bottleneck; the repo itself is small, but the optional Umbraco clone is ~150 MB — pre-stage that
  or run WF3 as a facilitator-only demo).

## Appendix — never used git or a terminal?

Type these lines one at a time, pressing Enter after each. Lines starting with `#` are comments —
don't type those.

**Windows** (open *Git Bash* from the Start menu — it comes with Git for Windows):
```bash
cd ~/Documents
git config --global core.longpaths true
git clone https://github.com/niancilyu-2/eyp-pm-skills.git
cd eyp-pm-skills
# now start your agent from this folder: `claude` (Claude Code) or `codex`
```

**Mac** (open *Terminal* from Spotlight — press Cmd+Space, type "Terminal"):
```bash
cd ~/Documents
git clone https://github.com/niancilyu-2/eyp-pm-skills.git
cd eyp-pm-skills
# now start your agent from this folder: `claude` (Claude Code) or `codex`
```

If `git` says "command not found", install it first: Windows — https://git-scm.com/download/win
(accept the defaults); Mac — type `xcode-select --install` and accept the prompt. Then repeat the
steps above.
