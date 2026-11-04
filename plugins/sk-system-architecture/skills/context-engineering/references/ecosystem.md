# Sources and implementation landscape

Этот обзор подготовлен 4 ноября 2026 года. Перед технологическим выбором перепроверяйте актуальные версии, лицензии и эксплуатационные ограничения.

## Primary guidance

- [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents): минимальный высокосигнальный контекст, just-in-time retrieval, progressive disclosure, compaction, structured notes и изоляция работы subagents.
- [Anthropic — Writing effective tools for AI agents](https://www.anthropic.com/research/writing-tools-for-agents): ясные контракты инструментов, минимальное пересечение функций и evaluation-driven design.
- [Anthropic SDK memory example](https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py): файловая memory и автоматическая очистка старых tool results.
- [OpenAI — Short-term memory management](https://developers.openai.com/cookbook/examples/agents_sdk/session_memory): trimming и summarization для истории сессии.
- [OpenAI — Building reliable agents with memory and compaction](https://developers.openai.com/cookbook/examples/agents_sdk/building_reliable_agents_memory_compaction): разделение compaction текущего run, reusable memory и human-reviewed artifacts.
- [OpenAI deployment checklist](https://developers.openai.com/api/docs/guides/deployment-checklist): compaction и управление длинными цепочками Responses.
- [Google Cloud — core concepts of AI agents](https://cloud.google.com/resources/core-concepts-ai-agents): разделение working memory, persistent user memory, knowledge base и operational data.
- [Google Cloud — agentic architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components): session/state, long-term memory, tools, runtime и orchestration как отдельные части.
- [Microsoft Semantic Kernel — contextual function selection](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-contextual-function-selection): динамический выбор небольшого набора tools вместо передачи всех функций модели.

## Open-source implementations observed on GitHub

| Проект | Что даёт | Когда рассматривать | Ограничение/вопрос |
|---|---|---|---|
| [LangGraph/LangChain](https://github.com/langchain-ai/langgraph) | stateful workflows, checkpoints, trimming/summarization middleware | Нужен явный orchestration graph и контроль состояния | Требует спроектировать semantics памяти, не решает их автоматически |
| [LangMem](https://github.com/langchain-ai/langmem) | short/long-term memory helpers и summarization | Уже используется LangGraph ecosystem | Проверять качество extraction и write policy |
| [Letta](https://github.com/letta-ai/letta) | in-context memory blocks, archival/recall memory, persistent agent identity | Нужны stateful long-lived agents | Более сильная модель управления агентом и инфраструктурой |
| [Mem0](https://github.com/mem0ai/mem0) | извлечение и retrieval пользовательской/agent memory | Нужен подключаемый memory layer | Различать open-source и managed capabilities; проверять privacy и evals |
| [Graphiti](https://github.com/getzep/graphiti) | bi-temporal knowledge graph, provenance и hybrid retrieval | Факты меняются во времени, важны связи и история | Сложнее эксплуатации, чем обычный vector/FTS индекс |
| [LLMLingua](https://github.com/microsoft/LLMLingua) | prompt/RAG compression | Большие retrieved contexts после измерения потерь | Compression может удалить критичные детали; нужен task-specific eval |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel) | plugins, agent state, contextual tool selection | Microsoft/.NET ecosystem или много tools | Некоторые memory/context features экспериментальны |

## What the ecosystem agrees on

1. Большое окно не отменяет отбора: лишний контекст ухудшает фокус и стоимость.
2. История, рабочее состояние, долговременная память и проверяемые артефакты — разные сущности.
3. Retrieval должен быть scoped, metadata-aware и измеряемым; embeddings сами по себе недостаточны.
4. Tools тоже занимают контекст, поэтому их нужно выбирать динамически и проектировать экономными.
5. Long-running agents нуждаются в compaction/checkpoints и внешнем рабочем состоянии.
6. Memory write — отдельный рискованный pipeline, а не автоматическое сохранение всего разговора.
7. Качество подтверждается evals и traces, а не наличием RAG/vector DB/memory framework.

## Selection heuristic

- Для первого контура начните с обычного project-scoped storage, hybrid search, структурированного working state и прозрачного compaction.
- Добавляйте memory framework, graph memory или model-based compression только после конкретного наблюдаемого failure mode.
- Не привязывайте context contract к одному model provider: Anthropic, OpenAI, Gemini и локальные модели должны получать одинаково определённые identity, scope, purpose, evidence и budget, даже если transport/API различаются.
