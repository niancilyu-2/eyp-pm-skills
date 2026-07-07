# Anti-"AI slop" design rules

A prototype that screams "an AI made this" undermines the PM in the room. Make it look *designed*.
(Distilled from anthropics/skills web-artifacts-builder guidance.)

## Avoid
- **Purple/violet gradients** and gradient fills generally — the #1 AI tell.
- **Everything centered** — vertically and horizontally centered hero blocks on every screen.
- **Uniform giant rounded corners** on every element (`rounded-3xl` everywhere).
- **Default Inter on everything** with no hierarchy.
- **Emoji as the entire visual design.**
- **Lorem ipsum** and obviously-fake names ("John Doe", "Acme").

## Do
- **One accent color**, chosen for the domain (the template uses a teal/amber; change it to fit).
  Use it sparingly for primary actions and active state — not everywhere.
- **A real type hierarchy** — distinct sizes/weights for h1 / section / body / muted.
- **Left-aligned, scannable layouts**; whitespace and alignment over decoration.
- **Restrained radius and shadow** — subtle, consistent, not maximal.
- **Realistic content** — plausible names, numbers, and copy for the actual domain.
- **Clear states** — hover, focus, active, disabled, empty, loading, error.

## Quick gut-check before shipping
- Would a designer at the mock company be okay demoing this to a customer?
- Is the primary action on each screen obvious within 2 seconds?
- Does anything look templated/generic rather than specific to this product?
