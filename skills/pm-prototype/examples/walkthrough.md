# pm-prototype — step-by-step walkthrough

The shape of a good run, one example per step. **Structural only** — derive directions, screens,
and copy from the actual problem statement of your run.

### Step 0 — Brainstorm gate
> Restate the problem in one line, then the riskiest assumption underneath it. Offer 2-3 genuinely
> different directions (the direct happy-path build; the adjacent governance/plumbing surface —
> often a real need but a weak prototype; the dependent future idea that presupposes the first).
> The PM picks. Apply the scope guardrail: adjacent concerns appear as one status chip + one line,
> not their own screens.

### Step 1 — Frame the scope
> Confirm the hypothesis (the riskiest assumption, restated as testable). List the screens —
> usually 3-5: a list view, a create flow, the trust-moment screen the hypothesis hinges on, and
> a results/outcome view. Name the persona in one line. Close with a ~10-line flow map (screen →
> key elements → next action) and get an OK before any HTML.

### Step 2 — Scaffold the single file
> Copy `templates/prototype-template.html` → `workshop/outputs/<feature>-prototype.html`.
> Domain-realistic content (labeled sample), every control wired, hypothesis + real/faked panel
> filled in. Set the host product's theme if one ships.

### Step 3 — States and edge cases
> Wire the states that make the flow believable: the locked/stopped state, a failure + retry, a
> loading skeleton, an empty state. The real/faked panel names the open questions.

### Step 4 — Open & iterate
> Double-click to open — no server. Rehearse the demo moment (the one click that tests the
> hypothesis). Reviewers pin 💬 comments → Export → `prototype-feedback.json`; also emit the
> `-notes.md` handoff payload.

### Step 5 — React escalation
> Usually not needed for 3-5 screens of light state. Escalate only when the flow genuinely
> demands heavy state or routing.
