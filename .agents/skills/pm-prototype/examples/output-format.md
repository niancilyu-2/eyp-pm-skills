# Output format — pm-prototype (what a finished build contains)

The deliverable is a single self-contained `.html` plus a `-notes.md` handoff payload.
**Structural only** — never copy content into your own build; the scaffold it starts from is
`../templates/prototype-template.html`.

## On-screen hypothesis + real/faked panel (top banner)
- **Hypothesis:** one sentence, the riskiest assumption restated as testable.
- **✅ Real:** the core click-through; nav; status chips; empty/loading/error states.
- **🟡 Faked:** every metric and any backend behavior — labeled sample; open questions named
  right in the panel.

## Screens (3-5, all wired — no dead links)
1. A **list view** with realistic status variety (including the locked/stopped state) and an
   empty-state hint.
2. A **create flow** that walks the real decision order and ends in a labeled demo action.
3. The **trust-moment screen** — whatever view the hypothesis actually hinges on, with a failure
   + retry state.
4. A **results/outcome view** with the demo-moment action, sample-labeled numbers, and a loading
   skeleton.

## Host-product look
The file opens in the host product's theme (the template ships `umbraco` as the workshop
default): product top bar, real fonts and radii, primary-action colors from the product's design
tokens — so the prototype reads as a native screen rather than a generic page.

## What "done" looks like
Opens with no server; every control works; the scope guardrail held; anti-slop rules followed;
feedback overlay exports JSON. Hand the prototype + notes to `pm-plan-and-estimate`.
