# Pre-read: Umbraco and the workshop codebase

A 10-minute read before the workshop. Section 1 is for everyone (PM/CPO and CTO sessions);
section 2 adds the technical background for the CTO session. Everything below refers to the
open-source Umbraco CMS only — the workshop does not touch any closed-source or commercial code.

---

## 1. Umbraco in ten minutes (all participants)

### What it is
[Umbraco](https://umbraco.com) is an open-source content management system, MIT-licensed and in
development since 2005, maintained by Umbraco HQ (Denmark) together with a large community. It
powers hundreds of thousands of sites, typically mid-market and enterprise web estates. In the
workshop it plays the role of "our company's product": you'll act as a PM (or CTO) at a company
that ships this codebase.

### How it works, in one pass
- **Editors work in the backoffice** — a web UI where content is organized as a tree of pages
  and media. This is the surface most workshop exercises look at.
- **Developers define the schema** — "document types" declare what fields a page has (a blog
  post has a title, hero image, body). Editors then fill those fields; they never touch code.
- **The site renders two ways** — traditionally through server-side templates (Razor/.NET), or
  headless: the **Delivery API** serves content as JSON to any frontend (React, mobile, etc.).
- **Everything is extensible** — the backoffice itself is a plugin surface; packages add
  property editors, dashboards, and whole sections.

### See it for yourself (optional, ~15 minutes)
- **Click around a real backoffice:** [free 14-day Umbraco Cloud trial](https://umbraco.com/try-umbraco-cms/) —
  a hosted site in about 5 minutes, no install or credit card. Create a page, edit a field,
  publish. That's the editor experience our mock scenario is built around.
- **Documentation:** [docs.umbraco.com](https://docs.umbraco.com/umbraco-cms) — skim
  "Get Started" and "Model Your Content" if you want the concepts in Umbraco's own words.
- **The source code:** [github.com/umbraco/Umbraco-CMS](https://github.com/umbraco/Umbraco-CMS) —
  the repo the workshop clones. No need to read it beforehand.

### What the workshop does with it
You get a set of synthetic company signals (call notes, churn data, support tickets, a roadmap
deck — all clearly marked `[MOCK DATA]`) and a set of Claude Code / Codex skills. The PM/CPO
session runs the chain: signals → a defensible problem statement → a clickable prototype in
Umbraco's real design language → a planning doc, estimate, and spec grounded in the actual
code. No coding experience needed; if you can write an email, you can run the skills.

---

## 2. Technical need-to-knows (CTO session)

The CTO session uses the same codebase but a different toolkit —
[Superpowers](https://github.com/obra/superpowers), an open-source methodology layer for coding
agents — to work modernization and refactoring problems against a real, 20-year-old production
codebase. Useful context going in:

### The shape of the codebase
A .NET monorepo with a TypeScript frontend. The pieces you'll hear referenced:

| Area | What it is |
|------|-----------|
| `Umbraco.Core` | Domain models, services, interfaces — the heart (~50k lines of C#) |
| `Umbraco.Infrastructure` | Implementations: persistence, search, caching, messaging |
| `Umbraco.Cms.Api.Management` | REST API behind the backoffice |
| `Umbraco.Cms.Api.Delivery` | The headless content API |
| `Umbraco.Web.UI.Client` | The backoffice frontend — Lit/TypeScript web components (~40k lines) |
| `tests/` | Unit, integration, acceptance (Playwright), and benchmark suites |

Toolchain: **.NET 10** (SDK pinned via `global.json`), **Node ≥ 22** for the client. The clone
we use is tagged `18.1.0-rc`.

### Why it's a good modernization subject
This is not a toy repo — it carries the honest scars of two decades of shipping, and they're
exactly what the session works on:

- **Two persistence layers side by side:** the historical NPoco-based data layer and a newer
  EF Core layer (`Umbraco.Cms.Persistence.EFCore*`) coexist mid-migration.
- **Parallel dependency versions:** two ImageSharp integrations
  (`Umbraco.Cms.Imaging.ImageSharp` and `...ImageSharp2`) shipped simultaneously to manage a
  breaking upgrade.
- **A live deprecation program:** over a hundred files in Core alone carry `[Obsolete]`
  markers, many with scheduled removal versions — API surface being redesigned while users
  depend on it.

Deciding what to migrate, in what order, with what test safety net, at what cost — that's the
refactoring conversation, and it's the one we'll have with agents doing the legwork.

### What Superpowers adds
Superpowers packages an engineering workflow as skills the agent follows instead of improvising:
**brainstorming** (interrogate the approach before code), **writing-plans** (small, reviewable
task breakdowns), **test-driven-development** (red–green–refactor, enforced), **systematic
debugging**, and subagent-driven execution with code review between steps. In the session we'll
point this at a real seam in the Umbraco code — plan a migration step, let agents execute it
under TDD, and review what comes back. The point mirrors the PM session's: the win is
discipline and traceability, not raw speed.

### Before you arrive
- Machine setup is in [docs/prerequisites.md](../docs/prerequisites.md) — Claude Code or Codex
  installed and authenticated is the one thing that saves real time on the day.
- Optional skims: the [Umbraco repo](https://github.com/umbraco/Umbraco-CMS) README and the
  [Superpowers](https://github.com/obra/superpowers) README (5 minutes each).
- If you want to preview the component vocabulary the backoffice is built from:
  [uui.umbraco.com](https://uui.umbraco.com) — Umbraco's UI library storybook.
