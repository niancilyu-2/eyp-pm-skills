# Engineering handoff — precursor to `thorough-writing-plans`

`pm-plan-and-estimate` is the **PM-side precursor** to the engineering planning skills
`yv01p:thorough-writing-plans` and `superpowers:writing-plans`. It is catered to PMs but written with
engineering's specs and plans in mind, so the handoff is clean.

## The chain
```
pm-ideation → pm-prototype → pm-plan-and-estimate ──(SPEC.md)──▶ thorough-writing-plans ──▶ impl plan
   PM             PM              PM                                  Engineering
```
The PM skills stop at a verified **spec**. Engineering runs the writing-plans skill against it to
produce a verified, minimal implementation plan. No code is written by the PM skills.

## Why our spec drops straight in
`thorough-writing-plans` enforces a **strict input contract**: it rejects any input that lacks a
`## Verified assumptions` section, and it **trusts that section as ground truth** (it won't re-verify
it — it only verifies the *new* assumptions the plan introduces).

### The contract, pinned (retrieved from the upstream SKILL.md, 2026-06)
Because the upstream repo can change or become unreachable, the key details are recorded
here; re-verify against upstream before a real engineering rollout:
- **Acceptance check:** the spec must contain "a `## Verified assumptions` section (or close variant
  containing 'Verified' in a heading)" — otherwise it is rejected with no best-effort fallback.
- **Trust rule:** "`Verified assumptions` … **Ground truth. Do NOT re-verify.**"
- **Conditional sections:** `Out of scope` → preserved as "Tasks NOT in this plan," original form
  kept; `Known issues / accepted as out of scope` → preserved verbatim. Absent sections are not
  fabricated ("no template forcing").
- **Naming convention:** specs live at `docs/specs/YYYY-MM-DD-<topic>-design.md`, committed (drift
  is detected via the spec file's last commit vs. HEAD).

`pm-plan-and-estimate` already grounds its work in the real codebase. Those verified facts — exact
paths, function signatures, build/test commands, consumer impact — each with evidence, become the
spec's `## Verified assumptions` section. So an engineer can run `thorough-writing-plans` against our
`SPEC.md` directly: **no rejection, no reformatting.**

## What the spec includes (the contract)
Produced from [`spec-template.md`](../skills/pm-plan-and-estimate/references/spec-template.md):
- **Design body** — approach, architecture/components, conventions to reuse (drives task decomposition).
- **`## Verified assumptions`** — required; codebase-grounded facts, each with `path:line` / grep /
  command-output evidence.
- **Out of scope** and **Known issues / accepted as out of scope** — only if there's real content
  (preserved verbatim downstream; no empty template sections).
- PM detail — P0/P1/P2 (MoSCoW), INVEST stories, metrics, Given/When/Then acceptance criteria.

For real use, save it where the downstream skill expects and commit it so drift can be tracked:
`docs/specs/YYYY-MM-DD-<topic>-design.md`. In the workshop it's written to `workshop/outputs/SPEC.md`.

## The boundary
- **PM owns:** problem framing, prototype, planning doc, estimate, and the verified spec.
- **Engineering owns:** turning the spec into an implementation plan (and the code).
- The estimate is explicitly labeled **"needs engineering validation"** — it shortens the first eng
  conversation; it does not replace it.

## If your team doesn't use thorough-writing-plans
The same `SPEC.md` is a perfectly good standalone PRD/design spec. The `## Verified assumptions`
section is useful to *any* engineer regardless of tooling — it tells them exactly which facts were
checked against the codebase and where.
