# Provenance & licensing

## What's combined here
These skills tailor and combine the best of several public skill collections, cut to fit a PM
persona and the workshop scenario:

| Source | What we drew from it |
|--------|----------------------|
| anthropics/knowledge-work-plugins | synthesize-research, competitive-brief, roadmap-update, write-spec — structure & frameworks for `pm-ideation` and the spec |
| anthropics/skills (**web-artifacts-builder**) | the full React/shadcn prototype path (vendored — see below) + anti-slop design rules |
| kurenn/claude-prototype | control bar, pin-to-element feedback, domain-realistic content rule for `pm-prototype` |
| deanpeters/Product-Manager-Skills | the **pm-skill-creator** authoring process + validators; lean-ux-canvas & problem-statement framing |
| obra/superpowers | `brainstorming` (the gates) and `writing-plans` patterns |
| santoshkasula-rula/sk-claude-skills | estimate-effort: Eng/Ops/Rollout buckets, PERT, RAD, "why these numbers" |
| jbarbier/claude-code-cost-estimate | estimate-honesty patterns: percentile ranges (P10/P50/P90), artifact-safety guardrails |
| yv01p/claude-skills (**thorough-writing-plans**) | the verified-spec input contract our `SPEC.md` targets (downstream, engineering) |
| product-on-purpose/pm-skills | frontmatter/evidence-confidence patterns; **define-problem-statement** (Apache-2.0) — quantified-impact, "why now", success-criteria-table patterns; **discover-competitive-analysis** (Apache-2.0) — Full/Partial/None/Unknown rating scale + verified-vs-inferred confidence in `pm-ideation`'s Step 3 |

The three skills were authored via the deanpeters **pm-skill-creator** process and pass its
validators (`check-skill-metadata.py`, `check-skill-triggers.py`, `test-a-skill.sh`).

## License
The repository is MIT-licensed (see the root `LICENSE`), with one exception below.

## Vendored third-party code (Apache-2.0)
`skills/pm-prototype/scripts/web-artifacts-builder/` contains Anthropic's **web-artifacts-builder**
skill tooling (`init-artifact.sh`, `bundle-artifact.sh`, `shadcn-components.tar.gz`), vendored
**unmodified** so the full React-prototype path works from a single install.
- License: **Apache License 2.0** — retained at
  `skills/pm-prototype/scripts/web-artifacts-builder/LICENSE.txt`.
- Attribution / modification note: `skills/pm-prototype/scripts/web-artifacts-builder/NOTICE.md`.
- Source: https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder
- To upgrade: re-fetch from the source and keep `LICENSE.txt` + `NOTICE.md` in place.

Everything else in this repo is the workshop authors' own work. The mock company **Umbraco** and its
codebase are referenced for an educational workshop; Umbraco-CMS is cloned on demand and is not
redistributed here (it's git-ignored).

## Note on `yv01p/claude-skills`
Early notes in this project claimed that repo didn't exist; that was wrong. It does exist, and its
`thorough-writing-plans` skill defines the verified-spec input contract our `pm-plan-and-estimate`
spec is built to satisfy. See [engineering-handoff.md](engineering-handoff.md).
