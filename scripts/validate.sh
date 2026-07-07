#!/usr/bin/env bash
# Reproducible skill validation: fetches the deanpeters validators (shallow, to a temp dir)
# and runs metadata + trigger checks against our three skills, plus the Codex-mirror drift check.
# Requires: git, python3 with pyyaml (pip install pyyaml).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Pinned validator version — bump deliberately after reviewing upstream changes.
PMS_SHA="23ede8ccc44a097c4a6a6fcfcdf3df8415e3aa16"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
echo "Fetching validators (deanpeters/Product-Manager-Skills @ ${PMS_SHA:0:12})..."
git init -q "$TMP/pms"
git -C "$TMP/pms" remote add origin https://github.com/deanpeters/Product-Manager-Skills.git
git -C "$TMP/pms" fetch -q --depth 1 origin "$PMS_SHA"
git -C "$TMP/pms" checkout -q "$PMS_SHA"

SKILLS=("$HERE"/skills/*/SKILL.md)
echo "== metadata conformance =="
python3 "$TMP/pms/scripts/check-skill-metadata.py" "${SKILLS[@]}"
echo "== trigger readiness =="
python3 "$TMP/pms/scripts/check-skill-triggers.py" "${SKILLS[@]}"
echo "== codex mirror drift =="
python3 "$HERE/scripts/build-codex-skills.py" --check

echo ""
echo "All validations passed."
