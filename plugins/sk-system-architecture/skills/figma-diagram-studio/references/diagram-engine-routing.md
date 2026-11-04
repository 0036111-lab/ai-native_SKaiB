# Diagram engine routing

The final deliverable remains editable in Figma or FigJam. A text-to-diagram engine may supply topology, detect omissions, or provide a layout reference.

## Choose by diagram type

- **D2 with ELK:** dense structural architecture, grouped systems, many orthogonal connections, or a draft whose main problem is layout.
- **Mermaid:** sequence, state, flow, entity relationship, and simple topology drafts that benefit from a compact textual source.
- **LikeC4 or Structurizr:** a maintained architecture model that must generate multiple consistent C4 views over time.
- **Figma directly:** executive diagrams, capability maps, early ambiguous thinking, or any case where visual hierarchy matters more than automatic layout.

Do not introduce another source format for a one-off diagram unless it saves enough layout or maintenance work to justify it.

## Draft-to-Figma handoff

1. Preserve the generated source when it will remain the architecture source of truth.
2. Inspect the rendered draft; successful parsing is not visual verification.
3. Extract node order, groups, relationship directions, and useful routing.
4. Rebuild or restyle with semantic Figma components, project typography, and the approved icon policy.
5. Do not deliver a flattened screenshot. Imported SVG is acceptable only when the user does not need semantic component-level editing.

References:
- D2-oriented render-and-check workflow: https://github.com/asabirov/diagrams-skill
- LikeC4 architecture-as-code: https://github.com/likec4/likec4
- Figma diagram tooling: https://github.com/figma/mcp-server-guide/tree/main/skills/figma-generate-diagram
