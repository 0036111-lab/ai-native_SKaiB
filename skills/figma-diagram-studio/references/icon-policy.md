# Icon policy for diagrams

Icons help scanning; they do not carry architecture semantics by themselves. Every important node still needs a text label.

## Approved sources

- **Lucide:** default for people, actions, files, security, data, infrastructure, and abstract capabilities. Keep one stroke weight and optical size within a diagram. https://github.com/lucide-icons/lucide
- **Simple Icons:** brands and named external products only. Check the individual brand's trademark or license guidance. https://github.com/simple-icons/simple-icons
- **Official provider packs:** AWS, Azure, GCP, or another provider only in deployment or infrastructure views where the provider is a verified fact.
- **Material Symbols:** fallback when Lucide lacks a needed generic concept; do not mix styles casually. https://github.com/google/material-design-icons
- **Iconify for Figma:** discovery and vector import interface. Prefer the approved sets above and inspect the displayed license. https://github.com/iconify/iconify-figma

## Visual rules

- Use a consistent 24 px or 32 px icon box per component family.
- Use one icon style per semantic role; do not mix outline, filled, multicolor, and hand-drawn icons in one layer of the architecture.
- Keep internal capabilities neutral and monochrome. Reserve brand color for verified external products when recognition adds value.
- Never use emoji, decorative 3D icons, or AI-generated pseudo-logos in technical diagrams.
- If an icon cannot be recognized without the label, the label remains primary and the icon stays subordinate.

## Recommended component slots

Create reusable Figma components with a swappable icon slot for: Human, System, Service, Agent, Model, Gateway, Tool, Data Store, Knowledge Source, Queue, Approval, External Product, Risk, and Unknown.
