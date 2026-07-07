#!/usr/bin/env bash
# Scaffold a Vite + React + TS + Tailwind app that bundles to a single HTML file.
# Advanced/optional path — see references/react-escalation.md. Requires Node 18+ and npm.
set -euo pipefail

NAME="${1:-react-proto}"
if [ -d "$NAME" ]; then echo "Directory '$NAME' already exists — aborting."; exit 1; fi

echo "Scaffolding Vite React-TS app: $NAME"
npm create vite@latest "$NAME" -- --template react-ts
cd "$NAME"

echo "Installing deps (this needs network)…"
npm install
npm install -D tailwindcss@3 postcss autoprefixer vite-plugin-singlefile
npx tailwindcss init -p

# Tailwind content globs
cat > tailwind.config.js <<'EOF'
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: { extend: {} },
  plugins: [],
}
EOF

# Tailwind directives
cat > src/index.css <<'EOF'
@tailwind base;
@tailwind components;
@tailwind utilities;
EOF

# Vite config with single-file plugin
cat > vite.config.ts <<'EOF'
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { viteSingleFile } from "vite-plugin-singlefile";

export default defineConfig({
  plugins: [react(), viteSingleFile()],
  build: { cssCodeSplit: false, assetsInlineLimit: 100000000 },
});
EOF

echo ""
echo "Done. Next:"
echo "  cd $NAME && npm run dev      # live preview"
echo "  (edit src/App.tsx — carry over hypothesis panel + honest states + feedback)"
echo "  bash <skill>/scripts/lite/bundle-artifact.sh $NAME   # -> dist/index.html (single file)"
