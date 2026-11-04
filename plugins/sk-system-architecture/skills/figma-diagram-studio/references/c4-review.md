# C4 architecture review

Use this check when the diagram describes software or AI-system architecture.

## Select the view before drawing

- **Context (C1):** people, the system of interest, and external systems. Do not show internal services.
- **Container (C2):** deployable or independently running applications and data stores inside the system boundary.
- **Component (C3):** major responsibilities inside one selected container. Do not expand every container at once.
- **Dynamic:** one scenario or use case in numbered interaction order.
- **Deployment:** runtime instances, infrastructure nodes, zones, and the mapping of containers onto them.

If the source mixes levels, split it into views rather than preserving the accidental mixture.

## Semantic checks

- Every element has a concise name, type, and responsibility.
- Every relationship has a direction and a verb-led label. Add protocol or medium only when it matters.
- System and trust boundaries are explicit; visual proximity alone is not a boundary.
- External systems are visually distinct from owned systems.
- Proposed, current, uncertain, and deprecated elements are not silently mixed.
- A technology logo never substitutes for a responsibility label.
- The diagram answers one stakeholder question; unrelated detail moves to another view.

## AI-system additions

- Distinguish model, agent/orchestrator, tool, knowledge source, memory/state, evaluation, and human approval.
- Mark where sensitive data crosses a boundary and where prompts, context, or generated output are stored.
- Show fallback, escalation, and observability paths when they affect the decision being explained.
- Do not imply that an LLM directly performs an action if an application, gateway, or human approval mediates it.

Use the C4 Agent Skill and Structurizr concepts as references, not as mandatory output formats:
- https://github.com/BenIsenstein/c4-agent-skill
- https://github.com/structurizr/structurizr
