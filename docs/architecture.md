# Architecture

## What this is
A single **Claude Code plugin** (`eyp-pm-skills`) that also acts as its own **marketplace**, so
participants install it in one step. It bundles three PM skills, a shared rigor layer, a mock-data
scenario, and a facilitator guide.

## Repo layout
```
eyp-pm-skills/
├── AGENTS.md                # Codex entry point (project context + how to run the skills)
├── .claude-plugin/
│   ├── plugin.json          # Claude Code plugin manifest
│   └── marketplace.json     # single-plugin marketplace -> source "./"
├── .agents/
│   └── skills/              # GENERATED Codex skill tree (mirror of skills/, self-contained)
├── skills/
│   ├── pm-ideation/                 # Workflow 1 — signals → problem statement + roadmap rec
│   │   ├── SKILL.md
│   │   └── references/              # ingest cheat-sheet, problem-statement & roadmap templates
│   ├── pm-prototype/                # Workflow 2 — problem → clickable prototype
│   │   ├── SKILL.md
│   │   ├── templates/              # the zero-build single-file HTML scaffold
│   │   ├── references/              # zero-build, anti-slop, react-escalation docs
│   │   └── scripts/
│   │       ├── lite/               # lean Vite single-file React path (mine)
│   │       └── web-artifacts-builder/  # Anthropic's tool, vendored (Apache-2.0)
│   └── pm-plan-and-estimate/        # Workflow 3 — prototype → planning doc + estimate + spec
│       ├── SKILL.md
│       └── references/             # planning/estimate/spec templates, pert.md, cost-models.md
├── references/
│   └── rigor-checklist.md           # SHARED accuracy layer, cited by all three skills
├── workshop/
│   ├── mock-data/                   # 10 mixed-format [MOCK DATA] files (+ README = data contract)
│   ├── team-capacity.md             # capacity inputs for pm-plan-and-estimate
│   ├── your-data/                   # drop-in folder for your own inputs (git-ignored contents)
│   ├── codebase/                    # the cloned Umbraco-CMS (git-ignored, large)
│   ├── outputs/                     # skill-generated artifacts (git-ignored contents)
├── scripts/                         # clone-umbraco.sh + mock-data generators
└── docs/                            # this documentation
```

## How a skill is wired
Each skill is a folder with a `SKILL.md` (YAML frontmatter + body). Claude Code **auto-discovers**
skills from `skills/<name>/SKILL.md` — nothing needs to be declared in `plugin.json`. The folder name
must equal the frontmatter `name`.

Skills reference their bundled files via `${CLAUDE_SKILL_DIR}` (that skill's own folder — its
`references/`, `templates/`, `scripts/`). The shared rigor layer is **authored once** at
`references/rigor-checklist.md` and **synced into each skill's `references/`** by
`scripts/build-codex-skills.py`, so every skill is self-contained and the reference works
identically in Claude Code (plugin install) and Codex.

## Skill format
Authored via the deanpeters `pm-skill-creator` process and conformant to its validators:
frontmatter has `name` / `description` (≤200 chars, with a "Use when…" trigger) / `intent` / `type`
(`component` | `interactive` | `workflow`) / `theme` / `best_for` / `scenarios` / `estimated_time`;
the body has the six required H2 sections **in order**: Purpose → Key Concepts → Application →
Examples → Common Pitfalls → References.

## Design principle: gap-agnostic skills, scenario-carrying data
The skills hardcode **no** company, feature, competitor, or conclusion. They are general-purpose PM
tools. The workshop's narrative lives entirely in the **mock data** (see
[customizing-mock-data.md](customizing-mock-data.md)). Swap the data and the same skills work on your inputs.

## Dual-agent: Claude Code + Codex
The same skills run in both agents, from one source of truth.

| | Claude Code | Codex |
|---|---|---|
| Location | `skills/<name>/SKILL.md` (a plugin) | `.agents/skills/<name>/SKILL.md` (auto-discovered) |
| Entry point | `.claude-plugin/` (plugin + marketplace) | `AGENTS.md` |
| Path variables | `${CLAUDE_SKILL_DIR}` | none — repo-root-relative paths |
| Shared rigor layer | master synced into each skill's `references/` | same per-skill copy |
| Invoke | `/pm-ideation …` | `$pm-ideation …` or `/skills` |

**Single source of truth:** `skills/` (the Claude plugin), with the rigor master at
`references/rigor-checklist.md`. The Codex tree is **generated** by `scripts/build-codex-skills.py`,
which first syncs the rigor master into every skill's `references/`, then copies each skill and
rewrites `${CLAUDE_SKILL_DIR}/…` to explicit repo-root paths (`.agents/skills/<name>/…`), because
Codex resolves commands from the workspace root. The vendored Apache-2.0 `web-artifacts-builder` is
copied verbatim. Re-run the script after editing `skills/` or the rigor file (`--check` verifies the
mirror is in sync without writing). The generated tree is committed so participants don't build it.

## The chain (and the boundary with engineering)
```
pm-ideation  →  pm-prototype  →  pm-plan-and-estimate  ┊→  thorough-writing-plans (engineering)
 (signals)       (prototype)      (plan + estimate + spec)    (verified implementation plan)
```
The PM skills stop at a verified **spec**; they never write code. The dotted handoff is the
engineering planning skill, which consumes the spec's `## Verified assumptions` section. See
[engineering-handoff.md](engineering-handoff.md).
