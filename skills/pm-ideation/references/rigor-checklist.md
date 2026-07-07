# Rigor Checklist — the shared accuracy layer

Every skill in this plugin loads this file and applies it. The goal: be more rigorous than a
rushed PM, and show the work so every line can be defended to a CPO or an eng lead.

The failure mode to guard against is confident, plausible, well-formatted output that is wrong —
a fabricated quote, a number nobody can trace, a "customers want X" built on a single loud call,
an estimate with false precision. Don't produce it.

---

## The 9 rigor primitives (apply all, every time)

### 1. Traceable evidence
Every factual claim cites its source inline: the file name **and** the locator (row, slide, page,
line, code path, or URL). Format: `[customer-call-notes.docx, call 2]` or
`[churn-data.xlsx, row 7]` or `[src/Umbraco.Core/Services/ContentService.cs]`.
**If you can't cite it, it isn't a claim — it's an assumption or an open question. Label it.**

### 2. Evidence vs. inference vs. assumption — labeled
Tag every non-trivial statement as one of:
- **[Evidence]** — directly stated in a source (with citation).
- **[Inference]** — your reasoning *from* cited evidence (show the link).
- **[Assumption]** — not in any source; you're filling a gap. State it as such.

Never let an inference or assumption masquerade as evidence. When the inputs are silent on
something, it becomes a **named open question**, never an invented fact.

### 3. Anti-fabrication guardrail
Do **not** invent: customer quotes, names, numbers, ARR figures, competitor features, dates, file
paths, or API names. If the data doesn't contain it, say "not present in the provided inputs" and
add it to the open-questions list. A correct "I don't know" beats a confident fabrication.

### 4. Quantified signal strength
Replace vague volume words with counts and magnitudes:
- ❌ "customers want personalization"
- ✅ "7 of 12 accounts raised it [churn-data.xlsx]; $1.4M ARR across those accounts"

A theme is only **VALIDATED** when it triangulates across **≥2 independent sources** (e.g. calls +
churn, or churn + competitor analysis). A single-source theme is a **WEAK SIGNAL** — surface it,
but label it, and don't let it anchor a top recommendation on its own.

### 5. Calibrated confidence
Tag conclusions **High / Medium / Low** and state *why* (which evidence earns the tag). Where a
percentage is needed (e.g. RICE), use one consistent mapping: **High = 85–100%, Medium = 60–80%,
Low = <60%**. Weak/single-source signals are **capped at Low (≤60%)**; strong multi-source
triangulation earns High — don't let everything land on the same number. Prefer ranges over point
estimates. For every key conclusion, add a one-line **"What would change this answer"** — the
specific new evidence that would flip it.

### 6. Built-in red-team pass (the biggest lever)
Before presenting the final artifact, argue **against** your own output in a dedicated section:
- The single strongest objection a skeptical exec or eng would raise.
- Any **disconfirming evidence** you found while researching (data that argues the *other* way).
- What you might be wrong about.
Sometimes the objection wins and you revise. Either way, the counter-case appears in the output
alongside the recommendation.

### 7. Bias checks
Actively counter:
- **Recency bias** — is this just the loudest *recent* voice? Weight by volume, not volume × recency.
- **Selection bias** — you're hearing from who churned/complained; what about who stayed silent or renewed?
- **Happy-path bias** — did you only consider the success case? Name the error/edge/empty cases.
- **Confirmation bias** — did you look as hard for disconfirming evidence as confirming?

### 8. Human checkpoints
Don't one-shot a deliverable. Pause at the defined gates (e.g. brainstorm / approach selection) and
get the PM's confirmation before producing the heavy artifact. **Batch a gate's few questions into
one numbered message** (multiple-choice where possible) rather than interrogating serially — in a
live session, round-trips are the scarce resource. Analysis-only skills with no defined gate (e.g.
pm-ideation) run end-to-end after the one-line inventory confirmation; the gate rule applies where
gates are defined. The PM should feel they *shaped* the output, not received it.

### 9. Review-ready output
Structure every deliverable so it survives scrutiny and drives action:
- **Exec summary** up top (the answer, in 3–5 lines).
- **Body** with cited claims and labels.
- **Evidence appendix** (the receipts).
- **Assumptions & open questions** (what you didn't know).
- **What to validate next / how to use this** (so it leads somewhere).

---

## Pre-flight (start of every skill)
- Confirm what inputs actually exist before reasoning about them. List them back.
- If a referenced input is missing, say so — do not proceed as if it were there.

## Pre-submit self-audit (end of every skill — run silently, then fix)
Before showing the artifact, verify:
- [ ] Every claim has a citation, or is labeled [Inference]/[Assumption]/open-question.
- [ ] No fabricated quotes, numbers, names, features, or paths.
- [ ] Signal strength is quantified; single-source themes are flagged WEAK.
- [ ] Confidence tags present with reasons; ranges where appropriate.
- [ ] A red-team / counter-case section exists.
- [ ] Bias checks considered (recency, selection, happy-path, confirmation).
- [ ] Open questions and "what to validate next" are listed.
If any box fails, fix it before presenting.
