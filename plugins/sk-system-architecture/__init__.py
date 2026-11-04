"""Hermes plugin generated from the shared agent skill pack."""

from pathlib import Path


def register(ctx):
    base_dir = Path(__file__).parent
    # Hermes exposes these as namespaced skills, e.g. plugin-name:skill-name.
    ctx.register_skill('ai-system-architect', base_dir / 'skills' / 'ai-system-architect' / 'SKILL.md')
    ctx.register_skill('system-map', base_dir / 'skills' / 'system-map' / 'SKILL.md')
    ctx.register_skill('context-engineering', base_dir / 'skills' / 'context-engineering' / 'SKILL.md')
    ctx.register_skill('figma-diagram-studio', base_dir / 'skills' / 'figma-diagram-studio' / 'SKILL.md')
