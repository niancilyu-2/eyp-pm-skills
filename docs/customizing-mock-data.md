# Customizing the mock data (swapping in your own)

The bundled scenario is a **default**, not a dependency. The skills are
**gap-agnostic** (they hardcode no company, feature, or conclusion) and **format-agnostic** (they
read `.docx/.xlsx/.pdf/.pptx/.md/.csv/.txt`, plus public GitHub). So you can replace the data with
your own — including the set you're creating separately — and everything downstream keeps working.

> Design contract: the **narrative lives only in the data**. The skills read whatever inputs exist,
> quantify and triangulate them, and report what's missing rather than inventing it.

## A second ready-to-run dataset (for testing generalization)
`workshop/sample-data/` is a second, **text-only** scenario in a different domain (fictional
collaboration app "Tideflow"). Run
`/pm-ideation workshop/sample-data` to confirm the skills aren't Umbraco-specific. Because it's
`.md` + `.csv` only, it also runs **without** the Python office-format libraries — handy for a quick
smoke test. It's built with the same rigor (triangulating numbers, counter-signals, a roadmap that
omits the gap) and doubles as a copyable template. See `workshop/sample-data/README.md`.

Each skill also ships an **`examples/`** folder: `walkthrough.md` (one worked example per step on the
Umbraco scenario) and `sample-output.md` (a full finished deliverable) — useful for knowing what
"good" output looks like before you point a skill at your own data.

## Three ways to swap

### 1. Drop-in folder (recommended, zero-risk)
Put your files in [`../workshop/your-data/`](../workshop/your-data/) and point the first skill at it:
```
/pm-ideation workshop/your-data
```
Nothing else changes. The contents of `your-data/` are git-ignored (only its README is tracked), so
you can drop in real/internal documents without committing them.

### 2. Replace in place
Overwrite the files in `workshop/mock-data/` with your own (any formats, any names), then run
`/pm-ideation workshop/mock-data` as usual. Keep `workshop/mock-data/README.md` updated if you want
the data-contract notes to match your scenario.

### 3. Author a new synthetic scenario
The current set is facilitator-authored (there is no generator script; originals live in git
history). To seed a new scenario, follow the design guardrails in `DATA-SWAP-CHECKLIST.md` —
triangulation across ≥2 legs, counter-signals, a wanted-but-already-planned decoy, and no
self-grading labels in the data.

## What makes a good input set (the soft contract)
No schema is required. For a strong `pm-ideation` run, aim for a mix:

| Signal type | Examples | Why it helps |
|-------------|----------|--------------|
| **Qualitative** | call notes, interviews, support themes | the "what users say" — themes |
| **Quantitative** | churn, usage, revenue with real numbers | lets the skill quantify ($/accounts) |
| **Competitive** | competitor feature list / analysis | gap vs. market |
| **Internal direction** | current roadmap / plan | gap vs. what you're already doing |

Any subset works. More **independent** sources → stronger ("validated") themes; a lone source is
flagged as a weak signal. Numbers (a spreadsheet) are what let the skill say "$1.4M across 7
accounts" instead of "customers want this."

## Does swapping data affect the other two skills?
No. `pm-prototype` consumes `pm-ideation`'s **output** (a problem statement), and
`pm-plan-and-estimate` consumes the prototype + the codebase. None of them read `workshop/mock-data/`
directly except via the first skill's argument. Swap the inputs, run the chain, done.

## Tips for using *real* internal data
- Use the git-ignored `workshop/your-data/` folder so sensitive docs never get committed.
- The skills cite sources by filename + locator — keep filenames meaningful.
- If a format is unusual, the skill's ingest cheat-sheet (`skills/pm-ideation/references/ingest.md`)
  has fallbacks (e.g. `unzip` Office XML, `pdftotext`).
- Estimation (`pm-plan-and-estimate`) needs a real codebase path; point `--codebase` at yours.
