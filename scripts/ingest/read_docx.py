#!/usr/bin/env python3
"""Print a .docx as text with heading markers (for citation as [file, <section heading>]).

Usage: python3 scripts/ingest/read_docx.py <file.docx>
Exists so the workshop allowlist can pre-approve THIS script instead of arbitrary python.
"""
import sys

try:
    import docx
except ImportError:
    sys.exit("Missing python-docx. Install: pip install python-docx  (or use the workshop venv)")

if len(sys.argv) != 2:
    sys.exit(__doc__)

d = docx.Document(sys.argv[1])
for p in d.paragraphs:
    if p.text.strip():
        prefix = "# " if p.style.name.startswith("Heading") else ""
        print(prefix + p.text)
