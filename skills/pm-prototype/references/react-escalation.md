# React escalation (advanced / optional) — two paths

Use **only** when the zero-build single HTML file genuinely can't carry the prototype: lots of
interdependent state, real routing across many views, complex forms, or reusable component logic.
For a live workshop, prefer staying zero-build — both React paths need Node and add time.

There are **two** React paths. Pick by how polished/component-heavy the prototype needs to be.

## When to escalate at all (all should be true)
- The flow has many screens with shared, changing state.
- You'd be reimplementing a mini-framework in vanilla JS to keep it sane.
- The audience will tolerate a short build step.

---

## Path A — Lite (fast, fewer deps): Vite single-file
Best when you want React + Tailwind quickly, with no component library overhead. Bundles to one
self-contained HTML via `vite-plugin-singlefile`.

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/lite/init-artifact.sh my-proto   # Vite + React + TS + Tailwind
cd my-proto && npm run dev                                        # live preview at :5173
# edit src/App.tsx — carry over hypothesis panel + empty/loading/error states + feedback
bash ${CLAUDE_SKILL_DIR}/scripts/lite/bundle-artifact.sh my-proto # -> my-proto/dist/index.html
```

## Path B — Full (polished, component-rich): web-artifacts-builder
Best when you want shadcn/ui components, Radix primitives, and a production-grade look. This is
Anthropic's `web-artifacts-builder`, vendored under `scripts/web-artifacts-builder/` (Apache-2.0;
see its `LICENSE.txt` + `NOTICE.md`). Stack: React 18 + TS + Vite + **Parcel** (bundling) + Tailwind
+ **shadcn/ui** (40+ components pre-installed).

```bash
bash ${CLAUDE_SKILL_DIR}/scripts/web-artifacts-builder/init-artifact.sh my-proto   # + 40 shadcn components
cd my-proto && npm run dev
# build the artifact by editing the generated code (shadcn components live in src/)
bash ${CLAUDE_SKILL_DIR}/scripts/web-artifacts-builder/bundle-artifact.sh          # -> bundle.html (single file)
```
Requirements: an `index.html` in the project root (the init script sets this up). The bundle script
installs Parcel + html-inline and inlines everything into one shareable `bundle.html`.

shadcn/ui component reference: https://ui.shadcn.com/docs/components

## Choosing between A and B
| | Path A — Lite | Path B — web-artifacts-builder |
|---|---|---|
| Setup weight | Lighter (Vite only) | Heavier (Parcel + shadcn extract) |
| Components | roll your own + Tailwind | 40+ shadcn/ui + Radix |
| Bundler | vite-plugin-singlefile | Parcel + html-inline |
| Output | `dist/index.html` | `bundle.html` |
| Use when | quick stateful prototype | polished, component-rich UI |

## Keep the value-adds (either path)
Carry over the **hypothesis + real/faked panel**, the empty/loading/error states, and a
**feedback affordance**. The medium changed; the rigor didn't.

## Anti-slop applies everywhere
Follow `${CLAUDE_SKILL_DIR}/references/anti-slop.md` — web-artifacts-builder's own guidance says the
same: avoid excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Trade-offs to state to the PM
- Both need Node 18+ and `npm install` (network). Path B installs more.
- Slower to iterate than editing one HTML file; more moving parts can break live.
- Worth it only for genuinely stateful/polished prototypes.
