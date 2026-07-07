# Mock data — the workshop inputs (and how to swap them)

Ten facilitator-authored synthetic files (every filename carries a `[MOCK DATA]` prefix, and each
document opens with a synthetic-data notice). **You can replace them with your own data at any
time** — see `docs/customizing-mock-data.md` and `docs/DATA-SWAP-CHECKLIST.md`.

> The skills are **gap-agnostic and format-agnostic** — they hardcode no company, feature, or
> conclusion, and read any mix of `.docx/.xlsx/.pdf/.pptx/.md/.csv` (plus public GitHub). The
> narrative lives *only* in this data.

## The files
Mock company: **Umbraco** (a real open-source .NET CMS playing the workshop's fictional vendor).
What the signals add up to is the exercise — no file grades itself, and this README won't either.

| File | Format | What it is |
|------|--------|-----------|
| `…Umbraco Customer Call Notes.docx` | Word | 16 call write-ups, messy and mixed |
| `…Umbraco Churn and Expansion Workbook.xlsx` | Excel | 41 account rows with ARR, status, and reason codes |
| `…Support Ticket Log.csv` | CSV | 41 internal tickets, cross-referencing the workbook |
| `…Umbraco G2 Capterra Review Export.xlsx` | Excel | 49 review-site entries |
| `…Public Issue Tracker Export.csv` | CSV | 20 public issues with vote counts |
| `…Community Forum Digest.pdf` | PDF | 7 forum threads with reply counts |
| `…Evidence Packet README.md` | Markdown | cover note for the two public-evidence files |
| `…Umbraco Feature Inventory.docx` | Word | what the product offers today |
| `…Competitor(Optimizely) Feature Inventory.docx` | Word | competitor benchmark |
| `…Umbraco Roadmap Deck.pptx` | PowerPoint | internal Now/Next/Later deck |

Expect the set to be imperfect on purpose: duplicate CRM rows, inconsistent dates, asks that pull
in different directions. Working through that is part of the exercise.

> `team-capacity.md` lives one level up in `workshop/` — it's an input for `pm-plan-and-estimate`,
> not an ideation signal.

## Swapping in your own data
1. **Drop-in folder:** put files in `../your-data/` (git-ignored) and run `/pm-ideation workshop/your-data`.
2. **Replace in place:** overwrite this folder and update this README.
Then follow `docs/DATA-SWAP-CHECKLIST.md` (guide numbers, examples, mirror, scope-hygiene grep,
dry run). This set is authored, not script-generated — keep a copy before overwriting.
