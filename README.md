<a id="readme-top"></a>

<h1 align="center">PM AI Workshop</h1>

<h4 align="center">Three plug-and-play product management skills for Claude Code and Codex — ideation, rapid prototyping, and engineering handoff — with a complete mock-company scenario, captured sample outputs, and a facilitator guide for running them as a hands-on workshop.</h4>

<p align="center">
  <a href="https://github.com/niancilyu-2/eyp-pm-skills/issues/new?labels=bug">Report a Bug</a>
  ·
  <a href="https://github.com/niancilyu-2/eyp-pm-skills/issues/new?labels=enhancement">Request a Feature</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-3-brightgreen?style=flat-square" alt="Skills: 3">
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex-blue?style=flat-square" alt="Works with Claude Code and Codex">
  <img src="https://img.shields.io/badge/version-0.2.0-blue?style=flat-square" alt="Version 0.2.0">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License: MIT"></a>
</p>

## Table of Contents

- [Quick Start](#quick-start)
- [The Big Idea](#the-big-idea)
- [Installation and Setup](#installation-and-setup)
- [How the Skills Work](#how-the-skills-work)
- [The Skill Library](#the-skill-library)
- [The Workshop](#the-workshop)
- [Project Status](#project-status)

## Quick Start

```bash
git clone https://github.com/niancilyu-2/eyp-pm-skills.git
cd eyp-pm-skills
```

**Claude Code** — install the plugin, then run the first skill:
```
/plugin marketplace add ./eyp-pm-skills
/plugin install eyp-pm-skills@eyp-pm-skills
/pm-ideation workshop/mock-data
```

**Codex** — no install step; skills are auto-discovered from `.agents/skills/`:
```
codex
$pm-ideation workshop/mock-data
```

Run your agent from the repo root: the documented paths are repo-relative.

## The Big Idea

AI can make PM work more accurate and more thorough, not just faster. Each skill in this repo
cites its evidence, quantifies its claims, labels inference vs. assumption, and critiques its own
output before presenting it — so the result survives scrutiny in a leadership room. The three
skills chain into one product motion: messy signals → a defensible direction → a clickable
prototype → an engineering-ready plan, estimate, and spec.

### Who Is This For

- **PMs and CPOs** trying agent-assisted workflows on realistic product-management work.
- **Workshop facilitators** who need a self-contained, rehearsable session: mock data, expected
  outputs, timings, talking points, and pre-staged fallbacks.
- **Teams** who want a starting point for their own skills — everything is general-purpose and
  MIT-licensed.

### Key Features

- **A shared rigor checklist** applied by all three skills: traceable citations, quantified signal
  strength, calibrated confidence, a required red-team pass, and a no-fabrication rule you can
  test by deleting an input file.
- **Gap-agnostic skills, scenario-carrying data** — no company, feature, or conclusion is
  hardcoded; swap the data and the same skills work on your inputs.
- **Real codebase grounding** — the estimation skill cites actual files and re-runs its evidence
  commands at spec time, against a real open-source codebase.
- **Dual-agent support** — one source of truth in `skills/`, with a generated Codex mirror in
  `.agents/skills/`.
- **Captured sample outputs** from a full run of the chain, used as workshop fallbacks and as the
  quality bar.

### Founded On

Adapted from and inspired by: anthropics/knowledge-work-plugins (synthesize-research,
competitive-brief, roadmap-update, write-spec) · anthropics/skills (web-artifacts-builder) ·
kurenn/claude-prototype · deanpeters/Product-Manager-Skills (lean-ux-canvas, problem-statement,
pm-skill-creator) · obra/superpowers (brainstorming, writing-plans) ·
jbarbier/claude-code-cost-estimate · santoshkasula-rula/sk-claude-skills (estimate-effort) ·
product-on-purpose/pm-skills. Details in
[docs/provenance-and-licensing.md](docs/provenance-and-licensing.md).

## Installation and Setup

### Tool Compatibility

| Tool | How skills load | Invoke |
|------|-----------------|--------|
| **Claude Code** | Plugin install (marketplace + plugin are both `eyp-pm-skills`) | `/pm-ideation …` |
| **Codex** | Auto-discovered from `.agents/skills/`; `AGENTS.md` provides project context | `$pm-ideation …` |

### Setup

```bash
# clone the real Umbraco codebase for the estimation skill (large; git-ignored)
./scripts/clone-umbraco.sh

# Python readers for the Office-format mock data
pip install openpyxl python-docx python-pptx
```

Full requirements (per participant machine) are in [docs/prerequisites.md](docs/prerequisites.md);
troubleshooting in [docs/install-and-run.md](docs/install-and-run.md).

## How the Skills Work

Each skill is a folder with a `SKILL.md` (instructions the agent follows), bundled `references/`
(templates, cheat-sheets, the rigor checklist), and `examples/` (a per-step walkthrough and a
sample deliverable). The three chain end to end, and each also works alone:

```
pm-ideation  →  pm-prototype  →  pm-plan-and-estimate  →  engineering
 (signals)       (prototype)      (plan + estimate + spec)
```

The chain stops at a verified spec. The PM skills never write code; the spec's
`## Verified assumptions` section satisfies the input contract of engineering planning skills like
`thorough-writing-plans` (see [docs/engineering-handoff.md](docs/engineering-handoff.md)).

## The Skill Library

| Skill | Type | In → Out |
|-------|------|----------|
| [`pm-ideation`](skills/pm-ideation/SKILL.md) | workflow | Mixed-format signals (calls, churn, tickets, reviews, competitor docs, roadmap) → problem statement + roadmap recommendation |
| [`pm-prototype`](skills/pm-prototype/SKILL.md) | interactive | A problem statement or idea → a clickable, self-contained HTML prototype + handoff notes |
| [`pm-plan-and-estimate`](skills/pm-plan-and-estimate/SKILL.md) | workflow | Prototype notes + a real codebase → planning doc, PERT effort + cost estimate, spec |

**`pm-ideation`** reads any mix of `.docx/.xlsx/.pdf/.pptx/.md/.csv`, computes signal strength in
code, requires two or more independent sources before calling a theme validated, ranks by customer
value with commercial impact as its evidence, and red-teams its own recommendation.

**`pm-prototype`** gates on a brainstorm (pick a direction before building), then produces a
single zero-build HTML file with an on-screen hypothesis, a "real vs. faked" panel, and working
empty/loading/error states. React escalation paths are bundled for heavier prototypes.

**`pm-plan-and-estimate`** scopes the real codebase, estimates with PERT ranges (never single
numbers), debates the estimate from optimistic and skeptical perspectives, converts effort to a
sprint/runway view from a team-capacity note, and emits a spec whose verified assumptions show
commands re-run at write time.

Full details: [docs/skills-reference.md](docs/skills-reference.md) ·
[docs/rigor-and-accuracy.md](docs/rigor-and-accuracy.md).

## The Workshop

The repo doubles as a ready-to-run workshop built on a mock company: **Umbraco**, a real
open-source CMS, with a fully synthetic evidence set layered on top.

- **Mock data** — ten `[MOCK DATA]`-prefixed files in
  [`workshop/mock-data/`](workshop/mock-data/README.md): call notes, a churn workbook, support
  tickets, review-site exports, public issue/forum evidence, feature inventories, and a roadmap
  deck. The set is messy on purpose (duplicate CRM rows, inconsistent dates, decoy asks) and no
  file grades itself; the synthesis is left to the run.
- **Participant pre-read** — [`workshop/PRE_READ.md`](workshop/PRE_READ.md): a 10-minute intro to
  Umbraco and the codebase, written to be sent out before the session.
- **Facilitator materials** — run-of-show, expected outputs, and pre-staged fallbacks live in a
  separate private repo so neither participants nor their agents see them ahead of time.
- **Second scenario** — [`workshop/sample-data/`](workshop/sample-data/README.md): a text-only
  dataset for a different fictional company, to show the skills aren't tied to one scenario.
- **Bring your own data** — drop files in [`workshop/your-data/`](workshop/your-data/) (git-ignored)
  and run `/pm-ideation workshop/your-data`; see
  [docs/customizing-mock-data.md](docs/customizing-mock-data.md) and
  [docs/DATA-SWAP-CHECKLIST.md](docs/DATA-SWAP-CHECKLIST.md).

## Project Status

### Repo Structure

```
.claude-plugin/      plugin.json + marketplace.json (Claude Code)
.agents/skills/      generated Codex mirror of skills/
skills/              pm-ideation · pm-prototype · pm-plan-and-estimate
references/          rigor-checklist.md (shared accuracy layer)
workshop/            mock-data/ · sample-data/ · your-data/ · team-capacity.md · PRE_READ.md
docs/                architecture, skills reference, install, customization, handoff, provenance
scripts/             clone-umbraco.sh · build-codex-skills.py · validate.sh · ingest readers
```

CI runs skill validation (conformance, trigger readiness, Codex-mirror drift) on every push.

### License

[MIT](LICENSE), with one exception: `skills/pm-prototype/scripts/web-artifacts-builder/` vendors
Anthropic's web-artifacts-builder unmodified under Apache-2.0 (its `LICENSE.txt` and `NOTICE.md`
are retained in that directory).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
