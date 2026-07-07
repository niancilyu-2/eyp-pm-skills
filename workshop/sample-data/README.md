# sample-data — a second test scenario (different domain)

A ready-to-run **alternative** dataset, to confirm the skills aren't tied to the Umbraco scenario.
Different fictional company, different gap, and **text-only** (`.md` + `.csv`) — so it also runs
**without** the Python office-format libraries (`openpyxl`/`python-docx`/`python-pptx`).

Mock company **Tideflow**, a fictional team collaboration & docs app. What the signals point to is
for the run to find.

| File | Format | Role |
|------|--------|------|
| `customer-interviews.md` | Markdown | 4 interview write-ups |
| `churn.csv` | CSV | 10 accounts with ARR and churn reasons |
| `competitor-scan.md` | Markdown | Tideflow vs. two competitors, feature matrix |
| `roadmap.md` | Markdown | internal Now/Next/Later |

## Run it
```
/pm-ideation workshop/sample-data
```
Then continue the chain with `pm-prototype` and `pm-plan-and-estimate` as usual.

> Want to make your own? Copy this folder (or use `workshop/your-data/`) and follow
> [`../../docs/customizing-mock-data.md`](../../docs/customizing-mock-data.md). The skills are gap-
> and format-agnostic — they read whatever is there and report what's missing.
