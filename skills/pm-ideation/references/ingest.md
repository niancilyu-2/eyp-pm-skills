# Multi-format ingestion cheat-sheet

Reliable ways to extract text/data from each input type. Prefer the simplest that works. Always
keep locators (row, slide, page, call #) so claims can be cited.

> **Quote your paths.** Input filenames often contain spaces/brackets (e.g. `[MOCK DATA] ….xlsx`) —
> always wrap the path in double quotes or the command will silently fail.

## .md / .txt / .csv
Read directly with the Read tool. CSV: treat row 1 as headers; cite `[file.csv, row N]`.

## .pdf
1. Best: the **Read tool** supports PDFs directly (`Read` with the file path; use `pages` for long
   files). It preserves layout reasonably and is the default.
2. CLI fallback: `pdftotext -layout input.pdf -` (if poppler-utils is installed) for raw text.
Cite `[file.pdf, p.N]` or by section heading.

## .xlsx  (extract the real numbers — don't estimate)
Preferred — the repo ships a reader that the workshop allowlist pre-approves (no permission prompt):
```bash
python3 scripts/ingest/read_xlsx.py <folder>/<sheet>.xlsx
```
(Repo-relative — run from the repo root; use `.venv-workshop/bin/python` if libs live in the venv.
If the script is absent in this project, fall back to a python+openpyxl one-liner.)
Then compute sums/counts yourself in code (e.g. ARR by reason) rather than adding in your head.
Cite `[<sheet>.xlsx, row N]` and name the sheet.

## .docx
Preferred (pre-approved reader):
```bash
python3 scripts/ingest/read_docx.py <folder>/<doc>.docx
```
Cite by the call/section heading, e.g. `[<doc>.docx, <section heading>]`.

## .pptx
Preferred (pre-approved reader):
```bash
python3 scripts/ingest/read_pptx.py <folder>/<deck>.pptx
```
Cite `[<deck>.pptx, slide N: "<title>"]`.

## Public GitHub (optional enrichment)
- Roadmap / issues via `gh`:
  `gh search issues --repo <owner>/<repo> --label "feature" --sort reactions --limit 20`
  `gh issue list --repo <owner>/<repo> --search "<theme keyword>" --limit 20`
- Or `WebFetch` the public roadmap / docs pages.
Mark anything from here as **external signal**, and cite the URL.

## Environment note
If a python library is missing, create/use the workshop venv:
`python3 -m venv .venv-workshop && .venv-workshop/bin/pip install openpyxl python-docx python-pptx`
then call `.venv-workshop/bin/python` in the snippets above. As a last resort, `.docx/.xlsx/.pptx`
are zip files: `unzip -p file.docx word/document.xml` (etc.) yields the raw XML.
