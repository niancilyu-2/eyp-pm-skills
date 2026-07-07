# .agents/skills — Codex skill tree (GENERATED)

This directory is the **Codex-compatible** mirror of the skills. Codex auto-discovers skills from
`.agents/skills/<name>/SKILL.md`.

**Do not edit these files by hand.** They are generated from the single source of truth in
`../skills/` (the Claude Code plugin) by `../scripts/build-codex-skills.py`, which:
1. copies each skill folder here,
2. inlines the shared rigor layer (`references/rigor-checklist.md`) into every skill so each is
   self-contained (Codex has no shared "plugin root"),
3. rewrites Claude Code's `${CLAUDE_PLUGIN_ROOT}` / `${CLAUDE_SKILL_DIR}` path variables to relative
   paths (Codex uses relative paths only).

To update after editing `../skills/` or `../references/rigor-checklist.md`:
```bash
python3 scripts/build-codex-skills.py
```

The vendored `pm-prototype/scripts/web-artifacts-builder/` (Apache-2.0) is copied **verbatim** —
its `LICENSE.txt` and `NOTICE.md` are preserved.
