#!/usr/bin/env bash
# Bundle a Vite React app (created by init-artifact.sh) into ONE self-contained HTML file.
# Output: <name>/dist/index.html  (inline JS + CSS, shareable like the zero-build output).
set -euo pipefail

NAME="${1:-react-proto}"
if [ ! -d "$NAME" ]; then echo "Directory '$NAME' not found. Run init-artifact.sh first."; exit 1; fi

cd "$NAME"
echo "Building single-file bundle for $NAME…"
npm run build

if [ -f dist/index.html ]; then
  SIZE=$(du -h dist/index.html | cut -f1)
  echo "Done -> $NAME/dist/index.html ($SIZE). Open it directly in a browser."
else
  echo "Build finished but dist/index.html not found — check the build output above." >&2
  exit 1
fi
