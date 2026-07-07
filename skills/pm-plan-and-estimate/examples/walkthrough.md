# pm-plan-and-estimate — step-by-step walkthrough

The shape of a good run, one example per step. **Structural only — derive names, paths, and
every number from the actual inputs of your run.**

### Step 0 — Orient in the codebase (grounded)
> Scoped to the affected subsystems (~NNk LOC each, measured with commands kept for the spec).
> Three kinds of discovery, not just directory sizes: an **existing dormant seam** (an interface
> with a no-op default, off by default, referenced by only a handful of files); an **in-repo
> analog** (a shipped vertical slice of comparable shape, measured for the estimate ledger); and a
> **deprecation warning** on the seam, dated against the current version.

### Step 1 — Brainstorm gate (approach)
> Approaches grounded in Step 0: activate the seam / bolt onto an add-on surface / middleware
> swap — trade-offs on blast radius, trust fixes, fragility. → Converge with the PM.

### Step 2 — Requirements & RAD
> Inputs: prototype + `-notes.md` + team-capacity note (read, not asked — **every constrained role
> counted**, including part-time design and QA). Unknowns become labeled assumptions with spikes;
> **verified absences** (what does NOT exist on the critical path) become milestones up front
> rather than findings in sprint one.

### Step 3 — Planning doc (bucketed, cited)
> Milestones E/O/R with grounding, demos, acceptance, risk flags — plus the **cross-cutting table**
> (permissions, localization, cache/CDN invalidation, tests incl. harness caveats, API docs,
> migrations, deprecated surfaces): each row priced, deferred, or N/A with a reason.

### Step 4 — Estimate (ranges, two perspectives, $, runway)
> PERT with the granularity stated (per-bucket here); buffer scales both percentiles; the √Σσ²
> roll-up reported **with its correlated bound** (buckets share the team and the deadline).
> Capacity → sprints for every role; single-person bottlenecks and design lead time named.
> Dollars two ways: bottom-up task cost vs. **top-down burn for the window occupied** —
> reconciled, with the gap explained (the envelope is the budget number; the floor is the task
> cost). Analog ledger:
> analog, measured size (command → output), multiplier + reasoning, and the **anchor scope**
> (which milestones it may price). **Needs engineering validation.**

### Step 5 — PM↔Eng translation
> Every milestone in both languages (outcome ↔ implementation).

### Step 6 — Spec (precursor to thorough-writing-plans)
> Verified assumptions **re-run at emission**: command + full output, no elisions, claims worded
> as exactly what the output shows. Verified-absences subsection + the deprecation check included.
> Unverified items (including tools that would not run in this environment) quarantined in RAD
> with the failed command pasted. Hand to engineering. **Stop — no code.**
