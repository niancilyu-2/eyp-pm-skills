---
name: pm-plan-and-estimate
description: Turn prototype notes into an eng-ready planning doc plus a codebase-grounded effort and cost estimate. Use when handing a validated idea to engineering with minimal back-and-forth.
intent: >-
  Reduce the friction and handoff loops between Product and Engineering. Take prototype notes and
  assumptions and produce a planning doc, an effort + dollar estimate anchored in the real codebase,
  and optionally a spec — written so an engineer can start after one read and a PM can defend the
  numbers to leadership. Estimates cite actual files/subsystems, use PERT ranges instead of false
  precision, and are debated from two opposing perspectives before being committed. The spec it
  produces is a precursor to `thorough-writing-plans`: it carries a codebase-grounded "Verified
  assumptions" section that the downstream engineering planning skill trusts as ground truth, so the
  PM hands off a spec engineering can plan from directly instead of re-deriving.
type: workflow
theme: delivery-handoff
best_for:
  - "Handing a validated idea to engineering with minimal back-and-forth"
  - "Producing a codebase-grounded effort and dollar estimate with calibrated ranges"
  - "Writing an engineering-ready spec that feeds thorough-writing-plans / writing-plans"
scenarios:
  - "Turn these prototype notes into a planning doc and an estimate against our codebase"
  - "How much would this feature cost and how long would it take, grounded in the real repo?"
  - "Write the eng handoff spec so engineering can run writing-plans against it directly"
estimated_time: "10-15 min"
---

## Purpose

Take prototype notes + assumptions and produce a **planning doc**, an **effort + dollar estimate
anchored in the real codebase**, and optionally a **spec**. The goal is to shrink the Product↔
Engineering handoff: an engineer can read it once and start, and a PM can defend the numbers in a
leadership review.

The accuracy boost over a human guess is **grounding** — estimates cite the actual files and
subsystems the work touches, ranges replace false precision, and two opposing perspectives debate
the number before it's committed.

## Key Concepts

### The rigor layer (load this first)
Apply `.agents/skills/pm-plan-and-estimate/references/rigor-checklist.md` (if unreadable, tell the user before
continuing). Here, **code paths count as citations**.
Calibrate confidence with ranges, run the two-perspective/red-team pass, never invent file paths,
APIs, or numbers — if you didn't read it in the codebase, label it an assumption.

### Codebase grounding
Estimate against the **affected subsystems**, not the whole repo. Measurement commands (and
fallbacks for when `cloc`/`scc` are absent) are in `.agents/skills/pm-plan-and-estimate/references/cost-models.md`.

### Three effort buckets, never blended
**Engineering / Operational / Rollout** are estimated and reported separately; blending them hides
risk. A +20% buffer applies to Engineering only, shown raw vs. buffered.

### PERT ranges, not points
Each estimate is (O + 4M + P)/6 with P10/P50/P90, so the reader sees uncertainty. Math and roll-up
rules are in `.agents/skills/pm-plan-and-estimate/references/pert.md`.

### Two-perspective debate
An "AI-accelerationist" (optimistic) and a "skeptical SRE" (pessimistic) argue the estimate before
it lands, producing a confidence score and exposing the crux of disagreement.

### Spike rule
Any high-impact / low-confidence unknown triggers a recommended 1-hour spike *before* committing a
number, instead of guessing.

### Precursor to `thorough-writing-plans` (the verified-spec contract)
This skill is the **PM-side precursor** to the engineering planning skills `yv01p:thorough-writing-
plans` and `superpowers:writing-plans`. Those skills turn a spec into a verified implementation
plan, and `thorough-writing-plans` enforces a **strict input contract**: it rejects any spec that
lacks a `## Verified assumptions` section and treats the assumptions there as **ground truth** (it
won't re-verify them). Because this skill already grounds its work in the real codebase, those
verified facts (paths, signatures, build/test commands, consumer impact) — each with evidence —
become that section. The PM produces the spec; **engineering** runs the writing-plans skill on it.
This skill **stops at the spec — it does not write code or invoke downstream skills.**

## Application

This is a workflow with sequential phases, gated by a brainstorm on approach.

### Step 0 — Orient in the codebase (grounding)
If a `--codebase` path was given, identify the subsystems/files the feature touches and measure
their size using `.agents/skills/pm-plan-and-estimate/references/cost-models.md`. Exclude generated/vendored code.
Record concrete paths to cite. Keep it scoped — don't analyze the whole repo. **If the codebase path
is missing or unreadable, say so immediately**: offer to proceed ungrounded (everything labeled
[Assumption], no Verified-assumptions section in the spec) or to stop until a path is supplied —
never invent plausible-looking subsystems.

### Step 1 — Brainstorm gate: align on approach (don't skip)
Restate the feature + key assumptions in one line; confirm. Propose 2-3 candidate solution
approaches mapped onto the real architecture from Step 0, each with a one-line trade-off (effort,
risk, blast radius, maintainability). Batch your questions into a single numbered message
(≤3 questions), stress-test with the PM, and converge on one approach to plan/estimate.

### Step 2 — Synthesize requirements & surface RAD
Gather the inputs: the prototype, its `<feature>-prototype-notes.md` (the expected handoff payload
from `pm-prototype`), and the ideation output if present. **If no notes/prototype exist**, say so
and proceed from whatever problem statement is available, labeling the gap — don't reconstruct
context by inventing it. Extract scope, constraints, acceptance criteria. Surface
Risks/Assumptions/Dependencies. If a
**team-capacity note** is supplied (size, sprint length, velocity, PTO, freeze date — e.g.
`workshop/team-capacity.md`), read it and calibrate the estimate from it **instead of asking** —
and account for **every constrained role it lists** (part-time design, QA), not just engineers;
a half-time designer feeding novel screens or a half-time QA owning a correctness guarantee is a
schedule constraint, not a footnote;
otherwise ask the PM ≤3 targeted questions (including capacity). Anything still unknown becomes a
labeled assumption or open question. Recommend a spike for any high-impact/low-confidence unknown.

### Step 3 — Build the planning doc
Use `.agents/skills/pm-plan-and-estimate/references/planning-doc-template.md`. Decompose into milestones, each in one
bucket (Engineering/Operational/Rollout) with: cited code paths, a demo (what's runnable at the
end), an acceptance criterion, and a risk flag 🔴/🟡/🟢. No placeholders — name the real work.
Include the chosen approach + the 2-3 alternatives with a trade-off matrix.

### Step 4 — Estimate (ranges, two perspectives, dollars)
Use `.agents/skills/pm-plan-and-estimate/references/estimate-template.md` + `pert.md` + `cost-models.md`. Effort by
bucket with PERT and P10/P50/P90; +20% eng buffer shown separately. Run the two-perspective debate
and land a confidence score. Compute a **headline dollar range** two independent ways and reconcile them: bottom-up
(task effort × loaded rate) vs. top-down (the full team's burn for the calendar window occupied —
which includes the design/QA/coordination the bottom-up misses); explain the gap. Add a plain-English "why these numbers" and a sensitivity list.
If team capacity is known, **convert effort to a calendar/sprint view** (using effective capacity,
not headcount; account for PTO, single-person bottlenecks, and part-time design/QA constraints) and
**flag if P50/P90 exceeds the freeze runway**.
Label the whole estimate **"needs engineering validation."**

### Step 5 — PM↔Eng translation
For each milestone/requirement, give both a **PM outcome** line and an **eng implementation** line,
so the doc needs no decoding in either direction.

### Step 6 — Engineering handoff spec (the precursor artifact)
Generate a design spec with `.agents/skills/pm-plan-and-estimate/references/spec-template.md`. This is the bridge to
engineering's `thorough-writing-plans`, so it MUST conform to that input contract:
- Include the design body (approach, architecture/components, conventions to reuse).
- Populate a **`## Verified assumptions`** section — and **RE-VERIFY each item now**: re-run the
  evidence command in this turn against the actual codebase and paste its **full** output (no
  elisions; every number next to its command; claims worded as exactly what the output shows —
  interpretations go to the design body or RAD). Include the template's **Verified absences**
  subsection (prove what's missing on the critical path, not just what exists) and the mandatory
  **deprecation check** (quote any `[Obsolete]` on surfaces you build on and date it against the
  project's removal policy). Anything you can't re-run now goes to **Unverified assumptions &
  risks (RAD)** instead — nothing unverified may enter the trusted section.
- Include **Out of scope** and **Known issues / accepted as out of scope** only if there's real
  content (don't fabricate empty sections).
- Add PM detail (P0/P1/P2, INVEST stories, metrics, Given/When/Then) for completeness.
Then **STOP**: hand the spec to engineering to run `thorough-writing-plans` (or
`superpowers:writing-plans`). Do not write code or invoke downstream skills yourself.

### Output
`PLANNING_DOC.md` + `ESTIMATE.md` + `SPEC.md` under `workshop/outputs/` (for real use, save the spec
as `docs/specs/YYYY-MM-DD-<topic>-design.md` and commit it, so the downstream skill can track drift).
The `SPEC.md` conforms to the `thorough-writing-plans` input contract — engineering can plan from it
without reformatting.

## Examples

**Input:** the prototype + its `-notes.md` handoff payload + a team-capacity note, against the
cloned Umbraco repo.

**Run:** `/pm-plan-and-estimate workshop/outputs/<feature>-prototype.html workshop/outputs/<feature>-prototype-notes.md workshop/team-capacity.md --codebase workshop/codebase/Umbraco-CMS`

**What good looks like** (structural only; examples carry no figures from any dataset):
- Step 0 produces a discovery, not just directory sizes: an existing seam, an in-repo analog for
  costing, a deprecation warning — something an engineer would respect as a *finding*.
- Milestones bucketed E/O/R with verified code paths and risk flags, sequenced by what de-risks
  the churn driver first; cross-cutting work (permissions, localization, cache invalidation, test
  strategy) priced or deferred with a reason.
- Estimate: per the PERT reference — three-point inputs shown, buffer separated, the roll-up's
  independence assumption addressed; capacity converted to a sprint/runway view covering **every
  constrained role** in the capacity note, with the critical path named. Bottom-up cost
  cross-checked against the top-down burn of the team for the window occupied, with the gap
  between them explained. "Needs engineering validation" on top.
- `SPEC.md` Verified assumptions are **re-run at emission** — each item is command + full pasted
  output, claims state only what the output shows, and a **Verified absences** subsection proves
  what's *missing* on the critical path. Unverified items go to "Unverified assumptions & risks
  (RAD)" — never into Verified. Engineering runs `thorough-writing-plans` against it directly.
  This skill stops here.

**More examples:** `.agents/skills/pm-plan-and-estimate/examples/walkthrough.md` (one example per step, 0–6) and
`.agents/skills/pm-plan-and-estimate/examples/sample-output.md` (excerpts of the planning doc, estimate, and spec). **These examples are illustrative of one scenario — derive names, paths, and numbers only from the actual inputs of this run; never copy citations or figures from examples.**

## Common Pitfalls

### Pitfall 1: Vibes instead of grounding
**Consequence:** An estimate with no connection to the code is just a guess in a suit; eng demolishes
it in five minutes.
**Fix:** Every estimate cites a real code path or is openly labeled an assumption.

### Pitfall 2: False precision (single numbers)
**Consequence:** "It'll take 42 days" invites a fight and is almost certainly wrong.
**Fix:** Give P10/P50/P90 ranges and a confidence score; lead with the range.

### Pitfall 3: Scanning the whole repo
**Consequence:** Slow, and it inflates the estimate with code the feature never touches.
**Fix:** Scope to affected subsystems; offer the whole-repo figure only as an aside.

### Pitfall 4: Blended buckets / treating it as a commitment
**Consequence:** Eng/Ops/Rollout merged hides risk; presenting the estimate as final reignites the
handoff ping-pong.
**Fix:** Keep buckets separate; label the output "needs engineering validation" — it shortens the
first eng conversation, it doesn't replace it.

## References

### Related skills
- `pm-prototype` — produces the prototype + assumptions this skill consumes.
- `pm-ideation` — upstream source of the problem statement and evidence.
- `yv01p:thorough-writing-plans` / `superpowers:writing-plans` — **downstream (engineering).** They
  turn this skill's spec into a verified implementation plan. `thorough-writing-plans` requires a
  `## Verified assumptions` section in its input — which this skill's `SPEC.md` provides. This skill
  is the PM-side precursor and stops at the spec.

### Bundled references
- `.agents/skills/pm-plan-and-estimate/references/rigor-checklist.md` — the shared accuracy layer.
- `.agents/skills/pm-plan-and-estimate/references/cost-models.md` — measurement + dollar cross-check methods.
- `.agents/skills/pm-plan-and-estimate/references/pert.md` — PERT math and roll-up.
- `.agents/skills/pm-plan-and-estimate/references/planning-doc-template.md`, `estimate-template.md`, `spec-template.md`.

### External frameworks & provenance
PERT; bottom-up vs. top-down (burn-rate) cost reconciliation; RAD; INVEST/MoSCoW (spec); the
verified-spec input contract from yv01p/claude-skills (thorough-writing-plans). Distilled from
obra/superpowers (writing-plans), santoshkasula-rula/sk-claude-skills (estimate-effort),
jbarbier/claude-code-cost-estimate, and anthropics/knowledge-work-plugins (write-spec). Authored via
the `pm-skill-creator` process.
