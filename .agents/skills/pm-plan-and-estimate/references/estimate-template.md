# Estimate template

Ranges, two perspectives, dollars cross-checked. Leads with "needs engineering validation."

---

# [Feature] — Effort & Cost Estimate
**⚠ Needs engineering validation** — this is a grounded starting point to shorten the first eng
conversation, not a commitment. **Date / Codebase @ ref / Author.**

## 1. Headline
- **Effort:** ~[P50] person-days (range [P10]–[P90], +20% eng buffer → [buffered P50]–[P90]).
- **Cost:** **$[X]–$[Y]** (Method A P50→P90), cross-checked vs. Method B $[Z].
- **Confidence:** [High/Med/Low] — [one line why].

## 2. Effort by bucket (PERT, person-days)
| Bucket | O | M | P | P50 | P90 | Notes |
|--------|---|---|---|-----|-----|-------|
| Engineering (raw) | … | … | … | … | … | … |
| Engineering (+20% buffer) | | | | … | … | shown separately |
| Operational | … | … | … | … | … | … |
| Rollout | … | … | … | … | … | … |
| **Total (buffered)** | | | | **…** | **…** | |

(See `pert.md` for the math and the correct way to roll up P90.)

## 3. Two-perspective debate
- **AI-accelerationist (optimistic):** [why it could be at the low end — reuse, AI assist, etc.]
- **Skeptical SRE (pessimistic):** [why it could blow out — legacy coupling, test debt, infra,
  security review, integration].
- **Where they disagree:** [the crux].
- **Landing:** [the number we'd defend, and the confidence score it earns].

## 4. Dollar cost — bottom-up vs. top-down, reconciled
| Method | Approach | Result | What it prices |
|--------|----------|--------|----------------|
| A — bottom-up | buffered person-days × loaded rate ($[rate]/day [Assumption]) | $[…] | the tasks enumerated |
| B — top-down | full team burn × calendar window occupied (ALL roles: eng + design + QA) | $[…] | the team you occupy |

**Reconciliation:** B − A = $[delta] — [unpriced roles / coordination / utilization / missed work].
**Budget envelope: $[B range]. Task-cost floor: $[A range].**
*(Optional value context, not a cost check: budget vs. $[evidence-backed value at stake].)*

## 5. Why these numbers (for PMs/leadership)
[Plain-English paragraph: what was measured (cite the paths/LOC), what assumptions drive it, why the
range is as wide as it is.]

## 6. Sensitivity — what moves the number most
1. [assumption → impact if wrong]
2. […]
3. […]

## 7. Reproducibility & analog ledger
- Measured paths: [`src/…`, …] · Method: [cloc/scc/fallback] · Excluded: [generated/vendored].
- Analog used: [slice] · size: [command → output] · multiplier: [×N because …] ·
  **anchor scope:** prices milestones […] only; […] priced by PERT judgment (correctness/design-driven).
