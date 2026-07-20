# Planning doc template

Write so an engineer can read it once and start, and a PM can defend it. No placeholders — name the
real work and cite real code paths.

---

# [Feature] — Engineering Planning Doc
**Status:** Draft for eng review · **Date:** [date] · **Author:** [PM] · **Codebase:** [repo @ ref]

## 1. Exec summary
[3–5 lines: what we're building, the chosen approach, rough size/cost range, the biggest risk.]

## 2. Problem & scope
- **Problem / hypothesis:** [from pm-ideation / pm-prototype, cited]
- **In scope:** […]
- **Out of scope (non-goals):** […]
- **Acceptance (definition of done):** […]

## 3. Approach: chosen + alternatives
**Chosen:** [approach], because [reason]. Touches: `path/a`, `path/b` (cited).

| Approach | Effort | Risk | Blast radius | Maintainability | Notes |
|----------|--------|------|--------------|-----------------|-------|
| **A (chosen)** | … | … | … | … | … |
| B | … | … | … | … | why not |
| C | … | … | … | … | why not |

**New vs. reused (one line each — answers "does this need new backend work?" at a glance):**
new DB objects/migrations: […] · new APIs: […] · new UI surfaces: […] · reused/extended: […]

## 4. Milestones (bucketed; each demoable)
> Buckets: **E**ngineering / **O**perational / **R**ollout. Risk: 🔴 high / 🟡 medium / 🟢 low.

| # | Bucket | Milestone | Code paths touched (cited) | Demo at end | Acceptance criterion | Risk |
|---|--------|-----------|----------------------------|-------------|----------------------|------|
| 1 | E | … | `src/…` | … | … | 🟡 |
| 2 | E | … | `src/…` | … | … | 🟢 |
| 3 | O | … | infra/config | … | … | 🔴 |
| 4 | R | … | flags/QA | … | … | 🟡 |

## 4b. Cross-cutting work (price it, defer it, or mark it N/A)
Seasoned engineers carry this list in their heads; the plan must carry it on paper. For each row:
in-scope milestone, explicitly deferred, or N/A with a reason.
| Concern | Covered by | Notes |
|---------|-----------|-------|
| Permissions / auth policies (incl. new sections/areas) | | |
| Localization (UI strings AND the culture × variant matrix) | | |
| Cache / CDN invalidation on every state change | | |
| Test strategy (unit, integration incl. harness caveats, acceptance/E2E) | | |
| API surface (management + delivery) and API-doc regeneration | | |
| Migrations + upgrade-path registration | | |
| Deprecated surfaces you depend on (from the spec's deprecation check) | | |

## 4c. Descope ladder (if the estimate must shrink)
Cut in this order; each rung names what's removed, effort saved, and the risk to the user need.
| Cut (in order) | Effort saved | Risk to the user need |
|----------------|--------------|------------------------|
| … | … | … |

## 5. Risks, Assumptions, Dependencies (RAD)
- **Risks:** [+ mitigation] 🔴/🟡/🟢
- **Assumptions:** [explicitly labeled; these feed the estimate]
- **Dependencies:** [teams/services/external; the human bottlenecks]
- **Spikes recommended:** [any high-impact/low-confidence unknown → 1-hour spike before committing]

## 6. PM ↔ Eng translation
| Item | PM outcome (why it matters) | Eng implementation (what gets built) |
|------|------------------------------|--------------------------------------|
| … | … | … |

## 7. Open questions
[Anything unresolved, with an owner and whether it blocks starting.]
