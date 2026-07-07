# Team capacity (for pm-plan-and-estimate)

Workshop-level context so the estimate can produce a calendar/sprint view instead of asking live.
This is NOT an ideation input — point `pm-plan-and-estimate` at it, not `pm-ideation`.

## Team
US-based; blended fully loaded rate ≈ **$1,400/day** (use this for both cost methods).
- 2 backend engineers (C# / .NET)
- 1 frontend engineer (Lit / TypeScript backoffice)
- 1 full-stack engineer
- Designer: 50% allocated
- QA: 50% allocated

## Cadence & capacity
- Sprint length: **2 weeks**
- Effective capacity: ~**7 working days per engineer per sprint** (after meetings/support)
- Recent velocity: ~**24 story points/sprint** (team), historically ±15%

## Constraints
- **PTO:** one backend engineer out for 1 week during the window
- **Feature freeze in 8 weeks** (≈4 sprints) before the next release train
- Backoffice (Lit/TS) work is bottlenecked on the single frontend engineer

## How the estimate should use this
- Convert PERT person-days into **sprints / calendar time** using effective capacity (not headcount).
- Account for the PTO week and the frontend single-point bottleneck.
- Treat the **50% designer and 50% QA as schedule constraints**: novel screens
  stall a full-time FE if design specs lag, and a half-time QA owning a correctness guarantee is
  a P90 driver. Model their availability; include them in the top-down burn.
- Flag explicitly if the P50 (or P90) effort **exceeds the 8-week freeze runway**.
