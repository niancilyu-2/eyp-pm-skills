# Measuring the codebase & estimating cost

Goal: anchor effort/cost in the **real, affected** code — not the whole repo, and not vibes.

## 1. Scope first
From the planning step you know which subsystems the feature touches. List those directories/files.
Estimate against **those**, and mention the whole-repo number only as an aside.

## 2. Measure size (use what's installed)
Preferred (if available): `cloc <paths>` or `scc <paths>` — gives code/comment/blank by language.

Fallback (git repos):
```bash
# total tracked lines in the affected paths (exclude generated/vendored)
cd <codebase-path>
git ls-files -- '<affected-subsystem>/**' \
  | grep -Ev '/(node_modules|dist|vendor|build|bin|obj|.+\.min\.)' \
  | grep -E '\.(<relevant-extensions>)$' \
  | xargs wc -l | tail -1
```
Fallback for non-git checkouts (e.g. a zip snapshot — `git ls-files` won't work there):
```bash
find <affected-subsystem> -type f -regextype posix-extended -regex '.*\.(<relevant-extensions>)' \
  | grep -Ev '/(node_modules|dist|vendor|build|bin|obj)/' | xargs wc -l | tail -1
```
Adjust the glob to the subsystems you scoped. **Exclude** generated, vendored, minified, and build
output — code humans didn't hand-write shouldn't inflate the estimate. Derive paths and extensions
from the actual repo you were given — never from an example.

## 3. Translate size → effort (bottom-up, anchored, auditable)
Don't estimate from raw LOC alone. Decompose the milestones (from the planning doc) and size each in
person-days using PERT (see `pert.md`).

**The analog ledger (required when using in-repo analogs).** The strongest anchor is a comparable,
already-shipped vertical slice in the same codebase ("one complete entity + API + UI feature costs
X LOC here"). If you use one, record in the estimate: the analog chosen, its measured size
(command + output), the multiplier applied, and one line of reasoning for the multiplier. The
LOC→days leap is the least auditable step in the estimate — the ledger is what makes it
challengeable instead of vibes.

**Anchor scope (declare it).** State which milestones the analog is allowed to price. LOC analogs
speak for structural CRUD-shaped work (models, APIs, standard UI). They do NOT price:
- correctness/guarantee milestones (enforcement, caching, security) — driven by review and edge
  cases, not lines;
- novel product surfaces — driven by design iteration;
- integration milestones on unverified surfaces — priced only after their spike.
Price those with PERT judgment and say so.

## 4. Dollar cost — bottom-up vs. top-down, reconciled
Compute the cost two independent ways and present both. The gap between them is information, not an
error.

- **Method A — bottom-up (task cost).** `person-days (P50 and P90, buffered) × loaded daily rate`.
  State the rate and its basis (e.g. blended $700–$1,100/day fully loaded [Assumption]). This prices
  the *tasks you enumerated*.
- **Method B — top-down (burn for the window).** `full team burn per sprint × calendar window
  occupied` — from the capacity conversion, counting **every** person the window ties up: engineers,
  part-time design, part-time QA. This prices the *team you occupy* regardless of task lists.
- **Reconcile:** Method B is normally higher. The delta = unpriced roles, coordination, <100%
  utilization, and work the task list missed. Report both numbers, explain the delta, and use
  Method B as the budget envelope and Method A as the task-cost floor.
- **Optional value-context line (not a cost check):** payback framing against the evidence, e.g.
  "budget $X vs. $Y ARR at risk" — useful for leadership, but it validates the *decision*, not the
  estimate.

## 5. Honesty guardrails
- Overly precise figures signal false confidence — round, and lead with the range.
- LOC is a proxy; cross-validate against the bottom-up decomposition.
- Cite the paths you measured so the number is reproducible.
- If a key area couldn't be measured, say so and treat its cost as an explicit assumption.
