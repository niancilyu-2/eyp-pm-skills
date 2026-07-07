---
name: pm-prototype
description: Turn a problem statement or idea into a single clickable, self-contained HTML prototype. Use when you want to make an idea tangible for stakeholder review or to test a hypothesis before a spec.
intent: >-
  Help a PM make an idea tangible fast: a guided brainstorm to pick the right direction, then a
  single self-contained .html prototype (Tailwind via CDN + vanilla JS) that opens in any browser
  with no build step. Prototypes state the hypothesis they test, label what is real vs. faked, and
  include empty/loading/error states, not just the happy path. Escalates to
  React only when heavy state genuinely demands it.
type: interactive
theme: prototyping-validation
best_for:
  - "Making a problem statement tangible for stakeholder review in minutes"
  - "Testing a riskiest assumption with a clickable artifact before writing a spec"
  - "Exploring 2-3 UX directions and converging on one with the PM"
scenarios:
  - "Turn this problem statement into a clickable prototype I can demo"
  - "Build me a quick mockup of this feature to get feedback"
  - "I want to try a couple of directions for this flow before we commit"
estimated_time: "8-12 min"
---

## Purpose

Make an idea **tangible** in minutes: one self-contained `.html` file that opens directly in a
browser, is fully clickable, and can be emailed or dropped on any static host — no Node, no build,
no backend. Use it to turn a problem statement (ideally from `pm-ideation`) or a raw idea into
something stakeholders can click through and react to.

The skill is **interactive**: it diverges with you on direction first, then builds. And it makes the
prototype label its own assumptions — a prototype that hides them gets mistaken for a commitment.

## Key Concepts

### The rigor layer (load this first)
Apply `${CLAUDE_SKILL_DIR}/references/rigor-checklist.md` (if unreadable, tell the user before
continuing). Most relevant here: anti-fabrication
(realistic but clearly-labeled placeholder data, never imply real metrics), human checkpoints (the
brainstorm gate), happy-path bias (build the empty/error states), and review-ready output (the
on-screen "what's real vs. faked" panel).

### A prototype is a question, not an answer
Every prototype is tied to the **riskiest assumption** it exists to test. The hypothesis is stated
on-screen, and the "real vs. faked" panel says exactly what is illustrative.

### Brainstorm before building
Adapted from obra/superpowers `brainstorming`: diverge on 2-3 genuinely different directions and let
the PM choose before any HTML is written. This is what makes you prototype the *right* thing.

### Zero-build by default, React only when needed (two escalation paths)
Default output is one HTML file (Tailwind CDN + vanilla JS) — see
`${CLAUDE_SKILL_DIR}/references/zero-build-build.md`. Escalate to React only for genuinely heavy
state/routing, choosing one of two bundled paths (see
`${CLAUDE_SKILL_DIR}/references/react-escalation.md`):
- **Lite** — `scripts/lite/` (Vite + React + Tailwind, single-file via vite-plugin-singlefile).
  Faster, fewer deps.
- **Full** — `scripts/web-artifacts-builder/` — Anthropic's `web-artifacts-builder`, vendored
  (Apache-2.0): React + TS + Vite + Parcel + Tailwind + **shadcn/ui** (40+ components). Polished and
  component-rich, heavier setup.

### Anti-"AI slop" design
Follow `${CLAUDE_SKILL_DIR}/references/anti-slop.md`: no purple gradients, no everything-centered
layout, no uniform giant corners, domain-appropriate type, real content, clear hierarchy.

## Application

This is an interactive skill: ask questions one at a time, recommend a default, and gate on the
brainstorm before building.

### Step 0 — Brainstorm gate (do not skip)
Restate the problem in one line and confirm. Then ask, one question at a time:

**"What must be true for this to work?"** — capture the riskiest assumption; the prototype exists to
test it.

Then propose **2-3 genuinely different directions** and ask **"Which direction should we
prototype?"** with numbered options, e.g.:
1. **Direction A** — [a distinct core flow/layout/UX bet] · trade-off: […]
2. **Direction B** — [a different bet] · trade-off: […]
3. **Direction C** — [a third bet] · trade-off: […]
4. **Other** — describe your own.

Recommend one, but only proceed once the PM picks.

### Step 1 — Frame the scope
The hypothesis IS the riskiest assumption from Step 0, restated as testable — don't ask for it
again; state it and confirm. Then ask, in one batched numbered message: **"Which 2-5 screens make
up the core flow?"** and **"Who's the persona and context?"** Offer numbered defaults where helpful:
1. The smallest flow that tests the hypothesis (recommended)
2. A broader flow covering edge cases
3. A single hero screen
Keep scope to what tests the hypothesis. **Scope rule (always, not just in workshops):** adjacent
governance/admin surfaces — audit consoles, approval chains, lifecycle admin — are represented by
at most **one status chip + one caption line**; if the evidence pulls you toward plumbing, record it
in the `-notes.md` for planning instead of building it.

### Step 2 — Scaffold the single file
Start from `${CLAUDE_SKILL_DIR}/templates/prototype-template.html` and customize for the feature.
The template already provides the hypothesis + "real vs. faked" panel, a product top bar, a control
bar (screen nav + theme), a feedback overlay (pin a comment, export JSON), and empty/loading/error
patterns. Replace demo content with domain-realistic content, wire **every** control (no dead
links), and fill the hypothesis + real/faked lists accurately.
**Match the host product:** a prototype should read as a screen of the product, not a generic page.
If a host product exists, set its theme as the default — the template ships an `umbraco` theme with
tokens extracted from Umbraco's real design system (set `data-theme="umbraco"` on `<html>`; this is
the workshop default). For another product, derive its tokens (colors, font, radius) and add a
theme block the same way — see "Matching the host product" in
`${CLAUDE_SKILL_DIR}/references/zero-build-build.md`. Put the product name in the top bar.

### Step 3 — States, edge cases, and labels
Include empty, loading, and error states for the main flow. Ask the PM about the 2-3 edge cases most
likely to break the flow and wire at least one. Verify the hypothesis is visible and the real/faked
panel is accurate. **States must be real:** a control that only fires a toast is a dead control in
disguise — prefer a visible state change (swap the previewed content, flip a status chip, append a
line); reserve toasts for confirmations of changes the screen already shows.

### Step 4 — Open, review, iterate
Tell the PM to open the file directly (double-click / `file://`) or serve with `python3 -m
http.server`. Reviewers use the 💬 overlay to pin comments and **Export feedback** (JSON); iterate
from that JSON.

### Step 5 — (Optional) React escalation
Only if heavy state/routing genuinely demands it. Choose a path (details in
`${CLAUDE_SKILL_DIR}/references/react-escalation.md`):
- **Lite:** `bash ${CLAUDE_SKILL_DIR}/scripts/lite/init-artifact.sh <name>` →
  `bash ${CLAUDE_SKILL_DIR}/scripts/lite/bundle-artifact.sh <name>` (→ `dist/index.html`).
- **Full (shadcn/ui):** `bash ${CLAUDE_SKILL_DIR}/scripts/web-artifacts-builder/init-artifact.sh
  <name>` → `bash ${CLAUDE_SKILL_DIR}/scripts/web-artifacts-builder/bundle-artifact.sh` (→
  `bundle.html`).
Carry over the hypothesis/real-faked panel and the empty/loading/error states either way. Warn the PM it needs Node and
adds time; for a live workshop, stay zero-build.

### Output
Two files, saved by default:
1. `workshop/outputs/<feature>-prototype.html` (self-contained).
2. `workshop/outputs/<feature>-prototype-notes.md` — scaffold it from
   `${CLAUDE_SKILL_DIR}/templates/prototype-notes-template.md` (hypothesis, chosen + rejected
   directions, persona, assumptions, open questions, wired vs. deferred).
**Mandatory self-check before handing off:** extract the inline script to a temp file and
`node --check` it (piping to stdin can fail in sandboxes — use a file); grep for leftover
`CUSTOMIZE` markers; audit that every `<a>`/`<button>` carries `data-nav-target`, `data-goto`,
`onclick`, or `type="submit"`. Then offer to hand off to `pm-plan-and-estimate` with both files.

## Examples

**Input:** the problem statement from `pm-ideation` (one line: who is blocked, doing what, with
what consequence).

**Run:** `/pm-prototype workshop/outputs/roadmap-recommendation.md`

**What good looks like** (structural only; examples carry no scenario):
- Brainstorm offers genuinely different directions — typically the direct happy-path build, an
  adjacent governance/admin surface, and a dependent future idea — with trade-offs; the PM picks,
  and the **scope guardrail** holds: the adjacent concern shows up as one status chip + one line,
  not a whole surface.
- The hypothesis is on-screen, restating the riskiest assumption as something testable; the
  real/faked panel labels every metric as sample.
- Produces a small wired build (a list screen, a create flow, the trust-moment screen, a results
  screen with the demo-moment action) + the `-notes.md` handoff payload — opens with no server,
  no dead links, no purple gradients.

**More examples:** `${CLAUDE_SKILL_DIR}/examples/walkthrough.md` (one example per step, 0–5) and
`${CLAUDE_SKILL_DIR}/examples/output-format.md` (what a finished prototype contains). **Examples are structural only — derive names, paths, and numbers from the actual inputs of this run; never copy citations or figures from examples.**

## Common Pitfalls

### Pitfall 1: Skipping the brainstorm gate
**Consequence:** You build the first obvious thing and miss a better direction; the PM feels handed
an answer, not a choice.
**Fix:** Always present 2-3 distinct directions and get an explicit pick before building.

### Pitfall 2: A prototype that hides what's faked
**Consequence:** Stakeholders mistake faked charts/metrics for real capability and treat the mockup
as a commitment.
**Fix:** State the hypothesis on-screen and keep the "real vs. faked" panel accurate. Label every
illustrative number.

### Pitfall 3: Happy-path only
**Consequence:** The demo looks great until someone asks "what if it's empty / fails?" and there's
nothing there.
**Fix:** Build empty, loading, and error states; wire at least one likely edge case.

### Pitfall 4: Over-building / breaking portability
**Consequence:** Ten half-wired screens, or a multi-file app that won't open without a server —
fragile in a live demo.
**Fix:** Match scope to the hypothesis (3 working screens beat 10 stubs). Keep it one file; CDN for
Tailwind only. Escalate to React only when the flow demands it.

## References

### Related skills
- `pm-ideation` — produces the problem statement this skill consumes.
- `pm-plan-and-estimate` — next step: scope and price the prototyped idea against the codebase.

### Bundled references
- `${CLAUDE_SKILL_DIR}/references/rigor-checklist.md` — the shared accuracy layer.
- `${CLAUDE_SKILL_DIR}/templates/prototype-template.html` — the zero-build scaffold.
- `${CLAUDE_SKILL_DIR}/references/zero-build-build.md`, `references/anti-slop.md`,
  `references/react-escalation.md`.
- `${CLAUDE_SKILL_DIR}/scripts/lite/` — lite Vite single-file React path.
- `${CLAUDE_SKILL_DIR}/scripts/web-artifacts-builder/` — Anthropic's web-artifacts-builder, vendored
  unmodified (Apache-2.0; see its `LICENSE.txt` + `NOTICE.md`). Full shadcn/ui React path.

### External frameworks & provenance
Lean UX hypothesis framing; obra/superpowers `brainstorming`. Distilled from kurenn/claude-prototype
(control bar, pin-to-element feedback) and deanpeters/Product-Manager-Skills (lean-ux-canvas).
Bundles anthropics/skills **web-artifacts-builder** (Apache-2.0) verbatim as the full React path,
and its anti-slop guidance informs `references/anti-slop.md`. Authored via the `pm-skill-creator`
process.
