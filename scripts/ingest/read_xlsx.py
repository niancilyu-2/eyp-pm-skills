#!/usr/bin/env python3
"""Print every sheet of an .xlsx with row numbers (for citation as [file, sheet, row N]).

Usage: python3 scripts/ingest/read_xlsx.py <file.xlsx>
Exists so the workshop allowlist can pre-approve THIS script instead of arbitrary python.
"""
import sys

try:
    import openpyxl
except ImportError:
    sys.exit("Missing openpyxl. Install: pip install openpyxl  (or use the workshop venv)")

if len(sys.argv) != 2:
    sys.exit(__doc__)

wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
for ws in wb.worksheets:
    print(f"== sheet: {ws.title}")
    for i, row in enumerate(ws.iter_rows(values_only=True), 1):
        print(i, row)
