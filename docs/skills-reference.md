# Skills reference

Three skills, one chain. Each is independently usable; together they cover signals → direction →
prototype → engineering handoff. All three apply the shared
[rigor layer](rigor-and-accuracy.md).

---

## 1. `pm-ideation` — signals → problem statement + roadmap recommendation
**Type:** workflow · **Invoke:** `/pm-ideation <folder-or-description>`

**Input:** a folder of mixed-format signals — `.docx` call notes, `.xlsx` churn/usage, `.pdf`
competitor analysis, `.pptx` roadmap, `.md` notes — plus optional public GitHub (roadmap, issues).

**What it does:**
1. Inventories and parses every input regardless of format (see the skill's `references/ingest.md`).
2. Quantifies signals (e.g. sums ARR by reason in the churn sheet) and **triangulates** — a theme is
   "validated" only with ≥2 independent sources; single-source = weak signal.
3. Builds a competitive matrix and finds gaps vs. the internal roadmap (citing the omission).
4. Frames a user-centered **problem statement** (root cause via 5-whys).
5. Recommends a direction with **transparent RICE**, a Now/Next/Later placement, a **red-team /
   counter-case**, and "what to validate next."

**Output:** one review-ready markdown doc (exec summary, problem statement, evidence with signal
strength, competitive/roadmap gap, recommendation, red-team, assumptions/open questions, evidence
appendix). Every claim cites its source.

**Hand off to:** `pm-prototype`.

---

## 2. `pm-prototype` — problem → clickable prototype
**Type:** interactive · **Invoke:** `/pm-prototype <problem statement / idea / file>`

**Input:** a problem statement (ideally `pm-ideation`'s output) or a one-line idea.

**What it does:**
0. **Brainstorm gate** — proposes 2–3 genuinely different directions; you pick one.
1. Frames the hypothesis + the 2–5 screens of the core flow.
2. Scaffolds a single self-contained `.html` from `templates/prototype-template.html` (Tailwind via
   CDN + vanilla JS): control bar, theme toggle, **pin-to-element feedback with JSON export**, and a
   **hypothesis + "real vs. faked"** panel.
3. Adds empty/loading/error states and wires at least one edge case.
4. You open it in a browser (no server) and iterate from exported feedback.
5. **Optional React escalation**, two paths: `scripts/lite/` (fast Vite single-file) or
   `scripts/web-artifacts-builder/` (Anthropic's vendored shadcn/ui tool). Zero-build stays default.

**Output:** `workshop/outputs/<feature>-prototype.html` (self-contained, clickable).

**Hand off to:** `pm-plan-and-estimate`.

---

## 3. `pm-plan-and-estimate` — prototype → planning doc + estimate + spec
**Type:** workflow · **Invoke:**
`/pm-plan-and-estimate <notes> --codebase <path>`

**Input:** prototype notes + assumptions, and a path to the codebase to estimate against.

**What it does:**
0. **Brainstorm gate** — 2–3 solution approaches mapped onto the real architecture; converge on one.
1. Orients in the codebase, **scoped to affected subsystems** (measurement commands + fallbacks in
   `references/cost-models.md`).
2. Surfaces Risks/Assumptions/Dependencies; recommends a spike for any high-impact/low-confidence
   unknown.
3. Builds a **planning doc** — milestones bucketed Engineering/Operational/Rollout, each with cited
   code paths, a demo, an acceptance criterion, and a risk flag.
4. **Estimates** with PERT (P10/P50/P90), a +20% eng buffer shown separately, an optimist-vs-
   skeptical-SRE debate, and a **dollar range** cross-checked by ≥2 methods. Labeled "needs eng
   validation."
5. **PM↔Eng translation** — every item in both PM-outcome and eng-implementation language.
6. Produces an engineering **spec** with a `## Verified assumptions` section — the precursor to
   `thorough-writing-plans` (see [engineering-handoff.md](engineering-handoff.md)).

**Output:** `PLANNING_DOC.md` + `ESTIMATE.md` + `SPEC.md` under `workshop/outputs/`.

**Hand off to:** engineering's `thorough-writing-plans` / `superpowers:writing-plans`. The PM skills
stop here — they never write code.

## Where requirements live in the chain

There is deliberately no user-story/requirements step between ideation and prototype. WF1 frames
the problem and success criteria; the prototype's `-notes.md` records the hypothesis, chosen
scope, and assumptions (the editable interim artifact); formal requirements — MoSCoW priorities,
user stories, acceptance criteria — land in WF3's spec, *after* the prototype has taught you what
to require. Generating requirements before anything clickable exists tends to produce documents
nobody rereads.
