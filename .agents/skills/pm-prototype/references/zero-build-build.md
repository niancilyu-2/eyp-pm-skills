# Zero-build prototype — build details & conventions

The default and recommended path. One `.html` file, opens with no server.

## Stack
- **Tailwind via CDN** (`https://cdn.tailwindcss.com`) — the only external dependency. **This means
  full styling needs internet**; the template's inline fallback CSS keeps it legible offline, but
  plain. For an offline/locked-network demo, open it once with network first (browser cache) or
  warn the audience it will render unstyled.
- **Vanilla JS** for interactions — no framework, no bundler.
- **Inline `<style>`** for theme tokens (CSS variables), the offline fallback, and custom CSS.

## How to use the template
1. Copy `templates/prototype-template.html` to `workshop/outputs/<feature>-prototype.html`.
2. Search for `CUSTOMIZE` and replace each marker with real, domain-specific content.
3. Keep these intact (they're the value-adds): the **hypothesis + real/faked panel**, the **control
   bar**, the **feedback overlay**, and the **empty/loading/error** patterns.
4. Add or rename screens: each screen is a `<section data-screen="NAME">`; nav links and buttons
   target it via `data-screen="NAME"` or `data-goto="NAME"`. The runtime handles routing.

## Conventions (don't break these)
- **Every control works.** No `href="#"` dead links, no inert buttons. If a thing isn't built,
  make it a labeled stub that toasts "not in this prototype."
- **States are real.** A button that only toasts while the screen stays frozen is a dead control in
  disguise — segment switchers must swap the previewed content, stop/lock actions must visibly flip
  status, and only confirmations get to be toast-only.
- **Domain-realistic content.** Real-sounding names/numbers, never lorem ipsum. Mark any
  metric/chart/AI output as illustrative in the real/faked panel.
- **Responsive enough.** No horizontal scroll on a phone width; the sidebar hides on small screens.
- **Accessible basics.** Labels on inputs, focus rings (`.accent-ring`), `aria-current` on nav.
- **One file.** Inline everything except the Tailwind CDN. Portability is the point.

## Matching the host product
A prototype lands harder when it reads as a screen of the product it extends. The template supports
per-product themes via CSS variables; set the default with `data-theme="…"` on `<html>`.

**Shipped: `umbraco`** — tokens extracted from Umbraco's real design system (`@umbraco-ui/uui-css`),
so workshop prototypes look native to the backoffice:

| Token | Value | Source |
|-------|-------|--------|
| top bar | `#1b264f` (+ `rgba(255,255,255,.9)` text) | `--uui-color-header-surface/-contrast` |
| primary action | `#3544b1` | `--uui-color-interactive-emphasis` |
| background / surface | `#f3f3f5` / `#fff` | `--uui-color-background` / `--uui-color-surface` |
| text / border | `#060606` / `#d8d7d9` | `--uui-color-text` / `--uui-color-border` |
| focus ring | `#3879ff` | `--uui-color-focus` |
| radius | `3px` | `--uui-border-radius` |
| font | Lato | `--uui-font-family` |

**For another product:** pull its tokens from the codebase (grep for CSS custom properties or a
design-tokens file), a style guide, or its rendered UI; add a `:root[data-theme="<name>"]` block
next to the shipped ones; set `--topbar`, `--font`, and `--radius` if the product defines them.
Cite where the tokens came from in the notes file.

## Running it
- Double-click the file, or open `file://…` in a browser.
- Or serve: `python3 -m http.server 8000` then visit `http://localhost:8000/<file>.html`.

## Feedback loop
Reviewers click **💬 Feedback**, then click any element to pin a numbered comment, then **⬇ Export**
to download `prototype-feedback.json`. To iterate: read that JSON (each comment has `selector`,
`screen`, `text`) and apply the changes.
