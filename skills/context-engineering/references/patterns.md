# Patterns for context engineering

Читайте этот файл при проектировании архитектуры или выборе механизмов.

## 1. Context is a compiled runtime object

Полезная модель: контекст — не transcript и не база знаний, а объект, который компилируется заново для каждого model call.

```text
task envelope
  + policies / role / selected skills
  + current working state
  + selected conversation turns or compaction
  + retrieved evidence
  + selected tool schemas
  + relevant tool observations
  = context pack → model call
```

Компилятор контекста должен быть детерминирован там, где речь идёт о правах, лимитах и обязательных инструкциях; модель может помогать с query rewriting, summarization и reranking, но не должна самостоятельно расширять свои полномочия.

## 2. Preload, retrieval and just-in-time discovery

| Механизм | Использовать когда | Основной риск |
|---|---|---|
| Preload | Небольшие правила и состояние нужны почти на каждом шаге | Контекстное загрязнение |
| Deterministic lookup | Ключ и источник известны | Хрупкие идентификаторы |
| RAG | Нужно найти релевантные фрагменты в корпусе | Ошибки chunking/retrieval |
| Agentic search | Путь заранее неизвестен, агент способен уточнять поиск | Лишние вызовы и блуждание |
| Progressive disclosure | Корпус большой, но навигационные метаданные компактны | Плохие индексы и названия |

Часто лучший вариант гибридный: компактная карта источников загружается сразу, первичный retrieval даёт стартовые доказательства, затем агент точечно открывает полные материалы.

## 3. Memory taxonomy

| Тип | Срок жизни | Что хранить | Чего не хранить |
|---|---|---|---|
| Session history | одна беседа | последние взаимодействия | весь архив без отбора |
| Working state | одна задача | план, прогресс, блокеры, промежуточные IDs | общие факты о пользователе |
| Episodic memory | много задач | события и результаты с временем | неизменяемую истину без provenance |
| Semantic/project memory | длительно | устойчивые решения, правила, сущности | непроверенные выводы агента |
| User profile | длительно | подтверждённые предпочтения и полномочия | чувствительные данные без основания |
| Artifact | по политике проекта | документ, отчёт, код, утверждённое решение | скрытые рассуждения и сырой шум |

Memory extraction и memory retrieval — разные задачи. Запись требует отдельного качества: scope, durability, provenance, conflict handling и permission.

## 4. Compaction contract

Хороший checkpoint сохраняет:

- цель и критерий завершения;
- принятые решения и причины;
- действующие ограничения и права;
- подтверждённые факты со ссылками;
- незавершённые действия, блокеры и следующий шаг;
- идентификаторы артефактов и источников;
- существенные ошибки и уже отвергнутые пути.

Он удаляет:

- повторения;
- сырые tool outputs, уже превращённые в вывод;
- неактуальные ветви рассуждения;
- временные данные без дальнейшей ценности.

После compaction запускайте checkpoint eval: может ли новый контекст продолжить задачу без повторного discovery и без изменения решений.

## 5. Tool context

- Показывайте модели только инструменты, релевантные текущей задаче и правам.
- Описания должны различать функции, входы, последствия и условия применения.
- Большие результаты возвращайте как summary + stable reference; полный payload храните вне окна.
- Результат mutating tool должен содержать наблюдаемое подтверждение изменения.
- Tool cache обязан учитывать user/tenant, project, query, permissions и версию источника.

## 6. Retrieval pipeline

```text
query understanding / rewrite
→ access and metadata filters
→ candidate retrieval
→ rerank / temporal weighting / dedup
→ evidence diversification
→ context compression
→ citations and source references
```

Не оптимизируйте только similarity score. В реальной системе значимы правильный scope, актуальность, полнота, противоречия, авторитетность источника и пригодность фрагмента для решения задачи.

## 7. Shared Context Gateway

В multi-agent системе gateway может централизовать:

- identity, tenant/project ACL;
- source registry и adapters;
- retrieval, reranking и context budgets;
- session/working state и разрешённую память;
- cache с изоляцией областей;
- provenance, tracing и eval hooks.

Но role, purpose и task phase должны приходить от worker. Один универсальный context pack для всех исполнителей обычно ухудшает точность и увеличивает токены.

## 8. Budgeting

Не задавайте универсальный процент без измерений. Явно резервируйте:

- обязательные инструкции и policy;
- task + current state;
- retrieved evidence;
- tool schemas и ближайшие tool results;
- запас для model output и следующего шага.

При превышении лимита сначала удаляйте дубли и устаревшие tool results, затем сжимайте историю и доказательства. Не обрезайте обязательные политики и незавершённое состояние задачи.
