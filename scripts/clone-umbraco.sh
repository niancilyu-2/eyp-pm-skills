#!/usr/bin/env bash
# Clone the real Umbraco-CMS codebase for the pm-plan-and-estimate skill.
# The repo is large; it is git-ignored and lives under workshop/codebase/.
#
# Usage:
#   ./scripts/clone-umbraco.sh           # shallow clone (fast, recommended for workshop)
#   ./scripts/clone-umbraco.sh --full    # full history
set -euo pipefail

REPO="https://github.com/umbraco/Umbraco-CMS.git"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$HERE/workshop/codebase/Umbraco-CMS"

if [ -d "$DEST/.git" ]; then
  echo "Umbraco-CMS already present at $DEST — skipping. (Delete it to re-clone.)"
  exit 0
fi

mkdir -p "$HERE/workshop/codebase"

if [ "${1:-}" == "--full" ]; then
  echo "Full clone of $REPO -> $DEST ..."
  git clone "$REPO" "$DEST"
else
  echo "Shallow clone (depth 1) of $REPO -> $DEST ..."
  git clone --depth 1 "$REPO" "$DEST"
fi

echo "Done. Umbraco-CMS is at: $DEST"
echo "Tip: pm-plan-and-estimate scopes its analysis to the affected subsystems, not the whole repo."
