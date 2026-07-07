# PM AI Workshop — Documentation

Documentation for the **PM AI Workshop** plugin: three Product Manager skills built around a
shared rigor checklist.

## Start here
- **[Prerequisites](prerequisites.md)** — what each participant's machine needs (Claude Code *or* Codex).
- **[Install & run](install-and-run.md)** — install for Claude Code or Codex, set up, run each skill.
- **[Architecture](architecture.md)** — repo layout, the plugin/marketplace, the gap-agnostic design.
- **[Skills reference](skills-reference.md)** — what each of the three skills does, in/out, the chain.

> Works in both Claude Code and Codex. Claude Code uses the plugin in `skills/`; Codex uses the
> auto-generated mirror in `.agents/skills/` + `AGENTS.md`. One source of truth; see
> [architecture](architecture.md#dual-agent-claude-code--codex).

## Core ideas
- **[Rigor & accuracy](rigor-and-accuracy.md)** — the shared rigor checklist and how each skill
  applies it.
- **[Customizing the mock data](customizing-mock-data.md)** — swap the bundled scenario for your own
  inputs. The skills are gap- and format-agnostic.
- **[Engineering handoff](engineering-handoff.md)** — how `pm-plan-and-estimate` is a precursor to
  the engineering planning skills (`thorough-writing-plans` / `writing-plans`).

## Reference
- **[Provenance & licensing](provenance-and-licensing.md)** — sources combined, and the vendored
  Apache-2.0 component.
- **Facilitator guide** — lives in a private companion repo along with the answer key and
  pre-staged fallbacks, so participants don't see expected outputs ahead of the session.
- **[Top-level README](../README.md)** — the short version.

## The three skills at a glance

| Skill | Type | Workflow | In → Out |
|-------|------|----------|----------|
| `pm-ideation` | workflow | signals → direction | mixed-format signals → problem statement + roadmap rec |
| `pm-prototype` | interactive | problem → preview | a problem statement/idea → clickable self-contained HTML prototype |
| `pm-plan-and-estimate` | workflow | prototype → handoff | prototype notes + codebase → planning doc + estimate + eng-ready spec |

They form a chain — `pm-ideation` → `pm-prototype` → `pm-plan-and-estimate` → (engineering's
`thorough-writing-plans`) — but each is independently usable on its own inputs.
