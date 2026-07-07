# Design spec template — engineering handoff (precursor to `thorough-writing-plans`)

This spec is the **bridge artifact** between Product and Engineering. It is written to satisfy the
**strict input contract** of `yv01p:thorough-writing-plans` (and to feed `superpowers:writing-plans`):
that skill *rejects* any input lacking a `## Verified assumptions` section, and trusts the
assumptions there as **ground truth** (it won't re-verify them). So the codebase-grounded facts this
skill already verified go into that section, each with evidence.

PM-centric, but engineering-legible. The PM does not write code — this spec lets an engineer run
`thorough-writing-plans` against it and get a real implementation plan with minimal back-and-forth.

> For real use, save to `docs/specs/YYYY-MM-DD-<topic>-design.md` (the convention
> thorough-writing-plans expects) **and commit it** so the downstream skill can track drift. For the
> workshop, `workshop/outputs/SPEC.md` is fine (that folder is git-ignored — don't try to commit it).

---

# [Feature] — Design Spec
**Status:** Ready for eng (`thorough-writing-plans`) · **Date:** [date] · **Author:** [PM] ·
**Repo:** [repo @ ref / HEAD SHA]

## Problem & context
[2–3 sentences, evidence-grounded. Pull from pm-ideation. Why this, why now.]

## Goals / Non-goals
- **Goals (measurable):** […]
- **Non-goals:** […]

## Design
[The design body — this is what the plan will implement. Keep it concrete but not code.]
- **Approach (chosen):** […] — and why, vs. the alternatives considered.
- **Architecture / components:** the pieces and how they fit (data model, services, UI, APIs).
- **Conventions to follow:** existing patterns the implementation must reuse (e.g. "errors use
  `AppError`", "services registered in `…`").

## Verified assumptions
> **Required.** Ground truth for the downstream plan — do NOT make the engineer re-verify these.
> **Re-verify at emission time:** for every item, RE-RUN the evidence command *now* (in this turn,
> against the actual codebase) and paste its real output. Evidence = **command + full pasted
> output — never elided ("…"), never truncated, never from memory or an example.** Every number in
> this section must sit next to the command that produced it. If you cannot re-run it now, the item
> is NOT verified — move it to "Unverified assumptions & risks" below.
> **Claims state only what the output shows.** "5 files reference the interface" is verified;
> "blast radius is 5 files" is an interpretation — interpretations live in the design body or RAD,
> not here. Never copy paths, line numbers, or counts from templates/examples into this section.

- [Verified] <claim, worded as exactly what the output shows> — evidence: `<command>` → `<full output>`
- [Verified] <claim about references/usages> — evidence: `grep -rl "<symbol>" <paths> | wc -l` → `<N>`
- [Verified] build/test commands — evidence: `<command>` → `<real output; if the tool is absent,
  this item belongs in Unverified with the failed command pasted>`

### Verified absences (what is NOT there)
> The costliest planning gaps are usually things that *don't* exist. For every surface the plan
> depends on, prove presence or absence on the critical path — "I searched for X where it would
> have to live and found nothing" is a first-class verified claim.
- [Verified absent] <capability> — evidence: `grep -rn "<pattern>" <the paths where it would live>` → `<0 hits / output>`

### Deprecation & staleness check (mandatory)
> For every surface you build on: is any part `[Obsolete]`/deprecated? Quote the attribute, and
> date it against the project's release/removal policy — "removal in version N" plus the current
> version tells you whether the seam is moving *now*.
- [Verified] <surface> deprecation status — evidence: `grep -n "Obsolete" <file>` → `<output>`;
  current version: `<version-file evidence>`; implication: <one line, e.g. "seam is being redesigned
  in the current major — coordinate with the owning team before building on it">.

## Unverified assumptions & risks (RAD)
> Everything the plan depends on that was **not** verified above. The downstream skill treats these
> as open items, not ground truth. Pull from Step 2's RAD; do not silently promote items upward.
- [Assumption] <claim> — why believed, and how to verify cheaply (candidate 1-hour spike).
- [Risk] <risk> — 🔴/🟡/🟢, mitigation.
- [Dependency] <team/service> — status.

## Requirements (MoSCoW)
- **P0 / Must:** … · **P1 / Should:** … · **P2 / Could:** … · **Won't (this release):** …

## User stories (INVEST) + acceptance criteria
- As a [user], I want [capability], so that [benefit].
  - Given [context], When [action], Then [result].

## Success metrics
- **Leading:** [signal, target] · **Lagging:** [outcome, target, baseline]

## Out of scope
(Conditional — include only if there is real content. thorough-writing-plans preserves this
verbatim as "Tasks NOT in this plan". Don't fabricate an empty section.)
- […]

## Known issues / accepted as out of scope
(Conditional — preserved verbatim downstream; the plan won't silently "fix" these.)
- […]

## Open questions
- [tagged by owner; blocking vs. non-blocking]

## Handoff
**Next step (engineering):** run `thorough-writing-plans` (or `superpowers:writing-plans`) against
this spec to produce the implementation plan. The effort/cost lives in `ESTIMATE.md` — don't
duplicate numbers here.
