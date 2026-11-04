---
name: figma-diagram-studio
description: "Design or redesign professional, editable diagrams in Figma or FigJam: system architecture, C4, process maps, operating models, ecosystems, roadmaps, and relationship maps. Use when a diagram must look presentation-ready rather than like a default FigJam/Miro export."
---

# Figma Diagram Studio

Produce a designed information graphic, not a pile of equal boxes. Preserve factual uncertainty and keep every label, connector, and group editable.

## Choose the canvas

- Use **Figma Design** for polished diagrams intended for decks, reports, websites, or executive review.
- Use **FigJam** for workshops, collaborative mapping, and evolving working boards.
- Use Mermaid/`generate_diagram` only as a topology draft when it saves time. Do not treat its default rendering as the final visual.

Load the applicable official Figma skills before using their tools when the client provides them: `figma-use`; `figma-generate-design` for visible changes; `figma-use-figjam` for boards; `figma-generate-diagram` before `generate_diagram`. In another client, inspect the current Figma MCP tool contracts and preserve the same safety and verification requirements.

## Workflow

1. Inspect the source and the target file. Identify the audience, decision, reading order, verified facts, hypotheses, and missing links.
2. Write the diagram's single sentence: what should a reader understand in five seconds?
3. Choose one grammar from [references/diagram-grammar.md](references/diagram-grammar.md). Do not mix grammars without a reason.
   - For C4 or software architecture, also read [references/c4-review.md](references/c4-review.md).
4. Establish hierarchy before styling: title, primary path or system, secondary context, evidence/caveats.
5. If automatic layout could reduce crossings or reveal missing relationships, choose a draft engine using [references/diagram-engine-routing.md](references/diagram-engine-routing.md). Treat its output as topology, not finished art.
6. Build semantic editable nodes. Use sections for domains, components for repeated cards when supported, labelled connectors, and real icons selected according to [references/icon-policy.md](references/icon-policy.md). Never use emoji as icons.
7. Apply a restrained visual system: one neutral foundation, one accent, semantic status colors only when they encode meaning. Use consistent type, radii, strokes, and spacing.
8. Use external models only for work they improve. Read [references/model-routing.md](references/model-routing.md) before generating imagery or invoking Weave.
9. Validate structure and then screenshot the complete diagram. Fix clipping, overlaps, weak contrast, tangled connectors, tiny type, and ambiguous reading order before handoff.

## Non-negotiable design rules

- One visual hierarchy. Do not give every node the same weight.
- Prefer 3–7 primary groups; move detail into drill-down diagrams or an appendix zone.
- Keep the main reading path obvious without reading every label.
- Align to a grid. Repeated gaps must be genuinely repeated.
- Route connectors orthogonally where possible and treat routing as a layout constraint, not decoration. No connector may pass through a node, section title, connector label, or unrelated text. Before styling lines, reorder nodes, align source and target ports, and reserve clear horizontal or vertical routing lanes. Replace repeated parallel arrows with containment, a shared bus, or one aggregate relationship when the individual edges add no information. Connector-to-connector crossings are acceptable only when the topology makes them genuinely unavoidable.
- In FigJam sections, reserve a clear top safe area for the native section-name/number badge shown when the section is selected. Place an internal heading at least about 100–120 px from the section top and place the first card below it; increase the section height instead of compressing the content. The ordinary canvas export does not render this editor overlay, so validate the safe area in the editor with the section selected (or from a user screenshot), not from an export alone. A native section badge must never cover a heading, card, connector label, or other meaningful content.
- Separate **existing**, **proposed**, **external**, and **uncertain** using a legend and consistent treatment.
- Use provider or product logos only for actual external products. Use neutral functional icons for internal capabilities so the diagram does not imply an implementation choice.
- Do not shrink type to rescue density. Split the diagram or add a second level.
- Do not use screenshots of diagrams as the deliverable. The result must remain editable.

## Acceptance gate

The diagram is complete only when:

- its point is recognizable at fit-to-screen;
- labels are readable at a normal review zoom;
- no text is clipped and no nodes overlap;
- no connector intersects a card or label, and avoidable connector crossings have been removed by changing the layout;
- every FigJam section badge has visible clearance from its internal heading and content while that section is selected in the editor;
- colors and line styles have explicit meanings;
- the most important path is visually dominant;
- a screenshot has been inspected after the final relevant change;
- factual gaps remain visibly marked rather than invented.

<!-- gateway-skill-telemetry:v1 -->
## Telemetry

When Gateway telemetry tools are available, call `gateway_telemetry_skill_started` with `skill_id=figma-diagram-studio` and retain its `correlation_id`. On success call `gateway_telemetry_skill_completed`; on failure call `gateway_telemetry_skill_failed` with the same identifier. Send only safe metadata, statuses, and counts; never prompts, document contents, personal data, or secrets. Telemetry availability must not block the diagram task.
