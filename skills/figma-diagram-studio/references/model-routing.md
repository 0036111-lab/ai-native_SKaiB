# Model routing for Figma work

Use models as specialists; keep layout and labels editable in Figma.

## Routing

- **Current reasoning model or Claude, when available:** synthesize source material, define hierarchy, name relationships, check contradictions, and draft the narrative. Never imply Claude is connected until availability is verified.
- **Nano Banana or another approved image model:** create a hero illustration, conceptual metaphor, texture, or isolated visual asset. Do not use it to render diagram labels, tables, or architecture topology.
- **Figma Plugin API / `use_figma`:** assemble final editable nodes, text, grids, connectors, styles, and components.
- **`generate_diagram`:** create a fast editable topology draft for supported Mermaid types; restyle or rebuild for presentation-grade output.
- **Image generation fallback:** prefer a model already connected to Figma/Weave. If unavailable, use another approved image tool only after the user accepts the provider.

## Weave and cost controls

1. Call `weave_find_model` by human model name; never hardcode a model ID.
2. Inspect the returned contract before preparing inputs.
3. Request a quote with no `acknowledgedCost`.
4. Show the price and get explicit approval before every paid run or rerun.
5. Poll output, download the selected asset, and place only the useful asset in Figma.

Linking Figma to Weave or another provider changes account access. Prepare the flow, but get confirmation immediately before the OAuth authorization or permission-granting action. Never request or store API keys in the skill.
