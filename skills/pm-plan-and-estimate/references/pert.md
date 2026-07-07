# PERT estimation & percentiles

Estimate in **ranges**, not single points. For each milestone (and each bucket), get three numbers
from the bottom-up decomposition:

- **O** = optimistic (everything goes right)
- **M** = most likely
- **P** = pessimistic (realistic bad case — not worst-case-ever)

## Expected value & spread
```
Estimate (mean) = (O + 4M + P) / 6
Std dev (σ)     = (P − O) / 6
```

## Percentiles (assume roughly normal around the mean)
```
P10 ≈ mean − 1.28σ      (only 10% chance it's faster than this)
P50 ≈ mean              (coin-flip)
P90 ≈ mean + 1.28σ      (90% chance it lands at or under this)
```
Report **P10 / P50 / P90** so the reader sees the uncertainty, not a false-precise single figure.

## Rolling up
- Sum each milestone's P50 for the bucket P50.
- For the bucket P90, **don't** just sum the P90s (that assumes everything goes wrong at once).
  Approximate the combined σ as `sqrt(Σ σ_i²)` and recompute P90 = ΣP50 + 1.28 × combinedσ.
- Keep the three buckets (Engineering / Operational / Rollout) separate; sum only for a grand total.

## Granularity: per-milestone or per-bucket — pick one and say which
Per-milestone three-points rolled up give finer traceability; a single per-bucket three-point is
coarser but avoids the independence trap below. Either is fine; the estimate must state which was
used.

## The independence trap (read before trusting your P90)
The √Σσ² roll-up assumes milestones fail independently. In practice they usually share failure
modes — same team, same subsystem, same deadline — so the by-the-book roll-up produces an
overconfident (too narrow) P90. When milestones are correlated, either estimate at bucket level,
or report a sensitivity bound using the straight sum of σ (perfect correlation) alongside the
√Σσ² figure. If your P90 looks tighter than your gut, believe your gut and widen it.

## Buffer
Add a **+20% buffer to the Engineering bucket only**, shown **separately** (raw vs. buffered) — never
silently folded in. The buffer scales **both percentiles** (multiply P50 and P90 by 1.2 — i.e., mean
and σ scale together). Ops/Rollout already carry their own pessimistic case via P.

## Worked mini-example
Milestone "personalization rules engine": O=5d, M=8d, P=17d.
mean = (5 + 32 + 17)/6 = 9.0d; σ = (17−5)/6 = 2.0d.
P10 ≈ 6.4d, P50 ≈ 9.0d, P90 ≈ 11.6d. With +20% eng buffer: P50 ≈ 10.8d, P90 ≈ 13.9d.
