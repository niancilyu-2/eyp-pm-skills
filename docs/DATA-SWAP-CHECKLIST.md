# Data-swap checklist

Swapping the mock data (e.g. replacing the Umbraco/personalization scenario with your own set)?
Work through this list **in order** — the skills are gap-agnostic, but several *artifacts around
them* bake in the current scenario's numbers and filenames.

## 1. Replace the data
- [ ] Put the new files in `workshop/mock-data/` (or use `workshop/your-data/` and adjust the
      commands you hand participants). Any mix of `.docx/.xlsx/.pdf/.pptx/.md/.csv` works.
- [ ] Update `workshop/mock-data/README.md` — the file table, the seeded gap, and the headline
      numbers are scenario-specific.
- [ ] If estimating against a different codebase, update `scripts/clone-umbraco.sh` (or replace it)
      and the `--codebase` path in every documented WF3 command.
- [ ] Update `workshop/team-capacity.md` if the team story changes.

## 2. Update the scripted narrative (it does NOT update itself)
- [ ] the facilitator guide (private companion repo) — every "Expected output" block, the headline $ figures,
      account counts, and the money-demo filename (`mv workshop/mock-data/<file> /tmp/`).
- [ ] The **Examples** sections in all three `skills/*/SKILL.md` and each skill's
      `examples/walkthrough.md` + `examples/output-format.md` — these are structural (no scenario,
      no figures), so they normally need no change; just verify the "never copy figures" guard is
      intact.

## 3. Rebuild and verify
- [ ] `python3 scripts/build-codex-skills.py` — resync the Codex mirror (**required** after any
      `skills/` or `references/rigor-checklist.md` edit).
- [ ] `python3 scripts/build-codex-skills.py --check` — confirm no drift.
- [ ] `./scripts/validate.sh` — skill conformance still passes.
- [ ] **Dry-run `pm-ideation` on the new data** and confirm: it surfaces the gap you seeded, cites
      the new sources, and does NOT echo the previous scenario (no stray figures or theme names
      unless your data says so). Then run the chain end-to-end once.
- [ ] Commit + push.

## Design guardrails to preserve in new data
- Triangulation needs ≥2 independent sources for the seeded gap; include counter-signals (segments
  that *don't* want it) and at least one quantitative file so signal strength can be computed. See
  `docs/customizing-mock-data.md` for the soft data contract.
- **Scope hygiene:** the workshop only examines the open-source Umbraco-CMS repo. Keep synthetic
  data free of Umbraco's **commercial product names** (Engage, Forms, Deploy, Workflow, Commerce,
  uMarketingSuite) — describe needs generically ("a third-party add-on", "approval gates") so the
  scenario never points at closed-source code we can't look at. Audit after writing:
  `grep -riE "\bengage\b|heartcore|umarketingsuite|umbraco (forms|deploy|workflow|commerce)" workshop/mock-data/`
  (word-boundary on "engage" so generic terms like "re-engagement" don't false-positive; note plain
  grep won't see inside office files — run it on text extracted via `scripts/ingest/`)
