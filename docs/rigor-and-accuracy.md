# Rigor & accuracy

The skills are built to make PM output more accurate and more traceable.
The failure mode they guard against is confident, plausible, wrong output: a fabricated quote, an
untraceable number, a "customers want X" claim built on one loud call, an estimate with false
precision. Output like that costs a PM their credibility the moment it is challenged.

## The shared rigor checklist
All three skills load [`../references/rigor-checklist.md`](../references/rigor-checklist.md) (a
copy ships inside each skill) and apply its nine rules:

1. **Traceable evidence** — every claim cites file + locator (row/slide/page/line), code path, or URL.
2. **Evidence vs. inference vs. assumption, labeled** — anything not in the inputs becomes a named
   open question, never an invention.
3. **Anti-fabrication** — never invent quotes, numbers, customers, features, or code; report
   missing data as missing.
4. **Quantified signal strength** — counts and dollars instead of volume words; a theme is
   "validated" only with two or more independent sources, otherwise flagged weak.
5. **Calibrated confidence** — High/Med/Low with the supporting evidence, ranges over point
   estimates, and a note on what would change the answer.
6. **Red-team pass** — the strongest objection and any disconfirming evidence, presented before
   the recommendation is final.
7. **Bias checks** — recency, selection, happy-path, confirmation.
8. **Human checkpoints** — pause at the brainstorm/approach gates instead of producing a
   deliverable in one shot.
9. **Review-ready output** — exec summary, evidence appendix, open questions, next validations.

## How each skill applies it
- **pm-ideation:** triangulation across sources, quantified ARR, a scan for disconfirming
  evidence, RICE scoring with the math shown, and a counter-case section.
- **pm-prototype:** an on-screen hypothesis plus a "real vs. faked" panel, working
  empty/loading/error states, and a brainstorm gate before anything is built.
- **pm-plan-and-estimate:** estimates that cite real files, PERT ranges instead of single numbers,
  an optimist-vs-skeptic debate, and a "needs eng validation" label.

## Missing-input behavior
A useful check: hide one input and re-run `pm-ideation`.
```bash
mv "workshop/mock-data/[MOCK DATA] Umbraco Churn and Expansion Workbook.xlsx" /tmp/
# /pm-ideation workshop/mock-data   → reports the workbook as missing, downgrades confidence,
#                                      and does NOT invent the at-risk dollar figure
mv "/tmp/[MOCK DATA] Umbraco Churn and Expansion Workbook.xlsx" workshop/mock-data/
```
The expected behavior is a clear "that data is missing" plus downgraded signal strength, rather
than a fabricated figure.

## Why this matters
A senior PM's main risk with AI output is signing their name to wrong work in front of leadership.
These skills are built so the output is defensible: traceable, calibrated, and self-critiqued.
