---
name: pm-ideation
description: Turn mixed product signals into a problem statement and roadmap recommendation. Use when you have any mix of calls, churn data, competitor docs, or a roadmap and need the top gap, evidence-backed.
intent: >-
  Synthesize messy, multi-format product signals (customer call notes, churn/usage data, competitor
  analysis, an internal roadmap — in any mix of .docx/.xlsx/.pdf/.pptx/.md, plus public GitHub) into
  a defensible, user-centered problem statement and a scored roadmap recommendation. Gap-agnostic:
  the evidence drives the conclusion. Every claim is traceable, signals are quantified and
  triangulated, and the recommendation is red-teamed before it ships.
type: workflow
theme: discovery-strategy
best_for:
  - "Synthesizing a pile of mixed-format signals into one defensible direction"
  - "Finding the highest-value gap and proving it with quantified, triangulated evidence"
  - "Producing a roadmap recommendation a PM can defend line-by-line to a CPO and eng lead"
scenarios:
  - "I have call notes, a churn spreadsheet, a competitor PDF and our roadmap — what should we build?"
  - "Turn this folder of customer research into a problem statement and a prioritized recommendation"
  - "Which gap is costing us the most revenue, and is it on our roadmap?"
estimated_time: "8-12 min"
---

## Purpose

Take messy, multi-format product signals and produce two things a PM can stand behind: a sharp,
user-centered **problem statement** and a **roadmap recommendation**. The skill reads every input
regardless of format, quantifies how strong each signal really is, triangulates across sources,
hunts for disconfirming evidence, and shows its work.

Use it at the front of the product cycle, when you have raw signal and need a defensible direction.
It is **gap-agnostic**: it has no opinion about what the answer "should" be; the evidence decides.
The output is built to be checked — every claim cited, every gap named.

## Key Concepts

### The rigor layer (load this first)
Read and apply `${CLAUDE_SKILL_DIR}/references/rigor-checklist.md`. Every rule there is in force:
cite every claim, label evidence vs. inference vs. assumption, never fabricate, quantify signal
strength, run a red-team pass, produce review-ready output. If that file cannot be read, tell the
user the rigor layer failed to load before continuing.

### Triangulation & signal strength
A theme is **VALIDATED** only when ≥2 independent sources agree (e.g., calls + churn, or churn +
competitor analysis). A single-source theme is a **WEAK SIGNAL** — surfaced, but labeled, and not
allowed to anchor a top recommendation alone. Replace volume words with counts and dollars: "7 of
12 accounts, $1.4M ARR," never "lots of customers."

### Root cause over symptom
A light **5-whys** pass gets past the surface complaint ("add an A/B button") to the underlying
user problem. The problem statement targets the cause.

### Transparent RICE
Prioritize with Reach × Impact × Confidence ÷ Effort, **showing the sourced input and math** for
each factor. Confidence is automatically capped for weak/single-source signals.

### Multi-format ingestion
The skill reads .docx/.xlsx/.pdf/.pptx/.md and can pull public GitHub signals. Exact, reliable
commands per type live in `${CLAUDE_SKILL_DIR}/references/ingest.md`.

## Application

This is a workflow with sequential phases. Confirm the input inventory once, then proceed.

### Step 0 — Pre-flight: inventory the inputs
List the files/sources you actually have before reasoning about them; state each type and what you
expect it to contain. If something referenced is missing, say so — don't proceed as if it exists.
Confirm in one line, then continue.

### Step 1 — Ingest every signal (any format)
Parse each input using `${CLAUDE_SKILL_DIR}/references/ingest.md`. For tabular data (churn), extract
the actual numbers in code (sum ARR by reason, count accounts) — don't eyeball. Capture each
ask/quote/figure with its locator (row, slide, page, call #) for later citation. Optionally enrich
with public product signals (e.g., the Umbraco GitHub roadmap/issues), clearly marked external.

### Step 2 — Synthesize themes (weighed by evidence)
Cluster asks into themes. For each, record: sources (→ VALIDATED or WEAK), quantified strength
(accounts + $ARR), the **direct customer value** at stake — what the customer gains if solved,
stated in their units (hours saved, risk removed, outcome enabled) and quantified where the
evidence allows — and **who is NOT asking** (segments/renewed accounts — a required field). Rank by
customer value delivered × commercial impact (ARR/reach), not by who was loudest or most recent:
revenue at risk is the *evidence* that customer value is going unmet, not the value itself.

### Step 3 — Competitive & roadmap gap analysis
Build a feature-comparison matrix from the competitor analysis, rating each capability on a
consistent scale: **Full / Partial / None / Unknown**. Use **Unknown** whenever the source is silent
— never infer a "None". Mark each competitor claim **verified** (from a cited source) vs.
**inferred** (public-source guesswork); note the reliability either way.
Cross-reference the internal roadmap: is the top theme planned, partial, or **absent**? Cite the
slide/section that proves an omission. Note competitor trade-offs (cost, complexity) — **and** their
genuine strengths; don't dismiss them, and don't overclaim their superiority either.

### Step 4 — Frame the problem (root cause + measurable)
Run the 5-whys, then write the statement using
`${CLAUDE_SKILL_DIR}/references/problem-statement-template.md`: the empathy framing (I am / trying
to / but / because / which makes me feel) as the core, a one-line impact/why-now note where the
evidence supports it, and a **Success criteria** table (baseline · target · timeline + a guardrail)
defining what "solved" looks like. Cite every clause; lead with a one-line summary.

### Step 5 — Roadmap recommendation (scored + challenged)
Use `${CLAUDE_SKILL_DIR}/references/roadmap-rec-template.md`: transparent RICE (sourced inputs +
math), a Now/Next/Later placement with what it displaces, a required **red-team / counter-case**
(strongest objection + disconfirming evidence + your response), and **what to validate next**.

### Output
One review-ready markdown doc in this order: Exec summary · Problem statement (incl. a success-
criteria table) · Evidence & signal strength · Competitive & roadmap gap · Recommendation (RICE +
Now/Next/Later) · Red-team/counter-case · Assumptions & open questions · What to validate next ·
Evidence appendix. **Save it to `workshop/outputs/roadmap-recommendation.md` by default** (tell the
user; offer a different path only if they ask) — the downstream skills expect this file. Then hand
off to `pm-prototype`.

## Examples

**Input:** a folder of mixed-format signals — e.g. call notes (.docx), a churn workbook (.xlsx),
support tickets (.csv), a review-site export (.xlsx), public issue/forum evidence (.csv/.pdf),
feature inventories (.docx), and a roadmap deck (.pptx).

**Run:** `/pm-ideation workshop/mock-data`

**What good looks like** (structural only; examples carry no figures from any dataset):
- The top theme emerges as a **cluster of sub-themes, not a keyword match**, VALIDATED across
  multiple independent evidence legs, each leg counted.
- Every headline figure is **computed in code with the arithmetic shown** — including a dedup step
  when the CRM data contains duplicate/child rows (excluded rows named, not silently summed).
- The roadmap omission is **cited to a specific slide**, while adjacent planned items are
  acknowledged; loud-but-wrong candidates are explicitly examined and set aside with reasons
  (different buying center; already planned; zero $ attached).
- The red-team section is allowed to **change the answer** — a partially-accepted objection should
  reshape the recommendation, not just decorate it.

**More examples:** `${CLAUDE_SKILL_DIR}/examples/walkthrough.md` (one example per step, 0–5) and
`${CLAUDE_SKILL_DIR}/examples/sample-output.md` (a full finished deliverable). **These examples are illustrative of one scenario — derive names, paths, and numbers only from the actual inputs of this run; never copy citations or figures from examples.**

## Common Pitfalls

### Pitfall 1: Keyword-matching instead of synthesizing
**Consequence:** You grab the first repeated phrase and miss that the data mixes in
performance, pricing, and workflow asks.
**Fix:** Cluster, weigh by dollars and source-count, and rank — don't pattern-match one word.

### Pitfall 2: Volume words without numbers
**Consequence:** "Customers want X" implies scale you can't defend; the rec collapses under one
question in the room.
**Fix:** Attach counts and $ARR, or explicitly label the signal "qualitative only."

### Pitfall 3: Ignoring counter-signals
**Consequence:** You over-rotate on the loudest segment and recommend something a big slice of the
base doesn't want.
**Fix:** Always record who is NOT asking, and which customers renewed without the feature.

### Pitfall 4: Asserting an omission without proof
**Consequence:** "It's not on the roadmap" is challenged and you can't back it up.
**Fix:** Cite the exact slide/section. If a competitor feature isn't listed in the analysis, it's
"unknown," not "no."

## References

### Related skills
- `pm-prototype` — next step: turn this problem statement into a clickable prototype.
- `pm-plan-and-estimate` — later: scope and price the chosen direction against the codebase.

### Bundled references
- `${CLAUDE_SKILL_DIR}/references/rigor-checklist.md` — the shared accuracy layer.
- `${CLAUDE_SKILL_DIR}/references/ingest.md` — multi-format ingestion commands.
- `${CLAUDE_SKILL_DIR}/references/problem-statement-template.md`
- `${CLAUDE_SKILL_DIR}/references/roadmap-rec-template.md`

### External frameworks & provenance
RICE prioritization; thematic analysis / triangulation; MITRE-style problem framing; Full/Partial/
None/Unknown competitive rating + verified-vs-inferred confidence. Distilled from
anthropics/knowledge-work-plugins (synthesize-research, competitive-brief, roadmap-update),
deanpeters/Product-Manager-Skills (problem-statement), and product-on-purpose/pm-skills
(define-problem-statement, discover-competitive-analysis; Apache-2.0). Authored via the
`pm-skill-creator` process.
