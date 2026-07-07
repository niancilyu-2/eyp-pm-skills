# Drop your own inputs here

This folder is a ready place to use **your own** data instead of the bundled mock scenario.

1. Drop in any mix of files — `.docx`, `.xlsx`, `.pdf`, `.pptx`, `.md`, `.csv`, `.txt`. No naming
   convention is required.
2. Run the first skill against this folder:
   ```
   /pm-ideation workshop/your-data
   ```
3. Continue the chain as normal — `pm-prototype` then `pm-plan-and-estimate` — they consume
   `pm-ideation`'s output, so they don't care where the raw inputs came from.

The skills are **gap-agnostic and format-agnostic**: they read whatever is here, quantify and
triangulate the signals, and report what's missing instead of inventing it. For what makes a good
input set, see [`../mock-data/README.md`](../mock-data/README.md) and
[`../../docs/customizing-mock-data.md`](../../docs/customizing-mock-data.md).

> This folder is git-tracked but its contents (other than this README) are ignored, so you can drop
> in real/internal documents without committing them. See the repo `.gitignore`.
