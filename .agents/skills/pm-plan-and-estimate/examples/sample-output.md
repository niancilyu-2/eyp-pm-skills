# EXAMPLE OUTPUT — pm-plan-and-estimate (excerpts)

The parts to imitate, with figures kept generic. **Never copy paths, numbers, or citations
from examples.**

## PLANNING_DOC.md
- The chosen approach names a **discovery** ("activate the dormant seam") — and the milestones
  include what the **verified absences** forced into scope (the gap an engineering review would
  otherwise catch).
- Milestones bucketed E/O/R with grounding, demos, acceptance, risk flags; the **cross-cutting
  table** prices permissions, localization, invalidation, tests, API docs, migrations, and
  deprecated-surface dependencies instead of assuming them free.

## ESTIMATE.md
- PERT with granularity stated; buffer shown separately and scaling both percentiles; P90 reported
  with its **correlated bound** next to the √Σσ² figure.
- Capacity converted for **every constrained role** — the single-FE path, the half-time designer's
  lead time, the half-time QA owning the correctness suite — with freeze-runway slack stated.
- Dollars reconciled: bottom-up task floor vs. **top-down burn envelope**, delta explained;
  the analog ledger records the slice, its measured size, the multiplier, and the anchor scope.

## SPEC.md
```
## Verified assumptions        (command + FULL output, re-run at emission)
- [Verified] <exactly what the output shows> — evidence: <command> → <output>
### Verified absences          (what is NOT there, with the search that shows it)
- [Verified absent] <capability> — evidence: <search where it would live> → 0 hits
### Deprecation & staleness check
- [Verified] <surface> — [Obsolete] quoted + current version + one-line implication
## Unverified assumptions & risks (RAD)
- [Assumption] <tool absent → failed command pasted, item quarantined here>
```
Claims state only what outputs show; interpretations live in the design body. The spec ends with
the handoff and **stops — no code**.
