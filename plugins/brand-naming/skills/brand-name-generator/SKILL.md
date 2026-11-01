---
name: brand-name-generator
description: >-
  Проводит профессиональный процесс нейминга для бренда, продукта, стартапа,
  проекта или GitHub-репозитория: короткий стратегический бриф, смысловые
  территории, большие сгруппированные волны вариантов, журнал фаворитов,
  уточняющие итерации и итоговый шорт-лист. Используй, когда нужно придумать,
  уточнить или сменить название компании, продукта, проекта или репозитория.
---

# Brand Name Generator

## Language and project context

- Work in the user's language. For a Russian-language brief, conduct the interview,
  explanations, group labels, rationales, and deliverables in Russian.
- For Russian-market names, record both the intended Cyrillic form and a practical
  Latin transliteration when a domain, handle, or repository slug may be needed.
- Screen pronunciation in Russian first, then in every target-market language from
  the brief. Mark the stressed syllable for names whose reading is not obvious.
- Keep project artifacts inside the current project. Do not write to a user's global
  skill directory and do not publish, register, buy, or reserve names or domains.

You are acting as a senior naming consultant from a world-class naming agency
(think Lexicon, Interbrand, NameStormers). Naming is a **process with stages and
checkpoints**, not a single brainstorm. Run the process; do not just dump a list
of words. A name generator that takes a keyword and returns a list is a toy — the
strategic brief and the iterative filtering are what make this professional.

## What this skill does (and what it deliberately does not)

This skill automates the early, AI-strong stages of naming:

- **Does:** brief synthesis, high-volume generation, rubric scoring, iterative
  shortlisting, preliminary linguistic risk flags, and handoff to availability
  checking.
- **Does NOT replace:** a trademark attorney (legal clearance), a native-speaker
  linguist (cultural screening), or the human's final pick. Always say so when it
  matters. AI cannot guarantee a name is unregistered — training data has a cutoff.

The companion skill **name-availability-check** performs the domain / social /
dev-platform occupancy screen on the winners. Keep generation and checking
separate: choose first (slowly, over several rounds), screen second.

## Reference material (load on demand — do not paste it all in)

Read these from `references/` only when you reach the relevant step:

- `references/process-stages.md` — the full stage-by-stage workflow and timeline.
- `references/construction-techniques.md` — the 10 ways to build a name (incl. the two-word "idea × idea" cross), with examples.
- `references/naming-rules.md` — SMILE/SCRATCH, phonetics, word count, the taxonomy of distinctiveness, failure modes.
- `references/name-memorability.md` — the science of memorable names (fluency × distinctiveness, sound symbolism, the idea × idea engine).
- `references/sound-alike-screen.md` — pronunciation / sound-alike "stop-word" screen (say-it-aloud test, stop-word list, run-together & vowel-flip patterns).
- `references/scoring-rubric.md` — the default weighted rubric, target verification, and how to score.
- `references/iterative-refinement.md` — the convergence engine: the **Keepers ledger** (carry-forward of early favorites), the **graded reaction tiers** (Lock / Keep / Explore / Pass / Veto), **seeded sibling-cluster regeneration**, and the scaled-up counts per stage. Read this before Step 5.
- `references/github-repo-naming.md` — extra rules when the target is a repo / package, not a brand.

Templates live in `assets/`: `brief-template.md`, `winners-template.md`, `keepers-template.md`.

---

## Operating procedure

Work through these steps in order. Steps 4–6 form a **loop** — that is the
"choose slowly over several iterations" part. Do not rush to a final list.

### Default working mode — the fast in-chat loop

This is the **preferred rhythm** (use it unless the user explicitly asks for the
heavier scored portfolio):

1. **Quick intake** (Step 1) — a short AskUserQuestion questionnaire with sensible
   defaults. Don't over-ask.
2. **Generate a big wave** (Step 4) — **~150–200 candidates**, and **post the whole
   wave in chat**, split into **labelled groups** (by conceptual territory, technique,
   or sound-feel — e.g. "A — pilot stem", "F1 — alive/liquid"). Also append it to
   `candidates.md`. Defer judgment; flag risky names inline with ⚠ rather than dropping.
3. **User tags winners in chat** (Step 5, light path) — the user just names the ones
   they like ("Pilax, Braio — winner"). Append those to the **keepers ledger** as
   Locks. No mandatory per-name forms.
4. **Breed the next wave from the winners** (Step 6) — ~150–200 siblings that hold a
   winner's form, plus any new theme or constraint the user throws in (e.g. "more
   abstract", "≤5 letters", "lean neuro/autopilot"). Post in chat, grouped. Repeat.
5. **Compile & screen** (Steps 7–8) — when the user is happy, sync `winners.json` from
   the keepers ledger and hand off to `/name-availability-check`.

Non-negotiables every wave, regardless of speed: **say each name aloud** (sound-alike
screen), **dedup against all prior waves** (for a hard constraint like a length cap,
verify programmatically — a quick script that checks the rule and greps the pool), and
**keep the raw pool + keepers on disk**.

### Step 0 — Set up a working folder

Create `brand-naming/<project-slug>/` in the current project (slug = a short
kebab-case label for the effort, e.g. `acme-fintech`). All artifacts go here:
`brief.md`, `candidates.md`, `keepers.md`, `keepers.json`, `winners.md`,
`winners.json`. This is the durable record and the handoff point to availability
checking. The **keepers** files are the carry-forward ledger — every name the user
likes at any round is appended there and stays eligible for the final list (see
Step 6 and `references/iterative-refinement.md`).

### Step 1 — Intake & strategic brief

Before generating a single name, establish the criteria every candidate will be
judged against. Use the **AskUserQuestion** tool to gather the brief efficiently
(batch related questions; offer sensible defaults). Cover:

1. **Purpose / target of the name** — this drives everything downstream. Ask
   explicitly which of these you are naming:
   - **Brand / company / product** — full brandability, emotional resonance, domain + handles matter most.
   - **GitHub repository / open-source project / package** — also read `references/github-repo-naming.md`; conventions differ (lowercase, hyphenated, package-registry collisions, descriptive-but-distinct).
   - **Both** — generate names that satisfy *both* constraint sets simultaneously (brandable AND a clean repo slug).
2. **What it is** — industry, one-line description of the product/service/project.
3. **Audience** — who it's for (demographics + psychographics), and the languages they speak.
4. **Personality** — 3–5 adjectives for the desired tone.
5. **Positioning** — what space it occupies vs. competitors; what it promises.
6. **Competitors / names to avoid** — so you can differentiate and dodge look-alikes.
7. **Geographic / language markets** — for linguistic screening later.
8. **Naming-strategy preference** — descriptive / suggestive / arbitrary / coined,
   or "advise me" (then you recommend, see Step 2).
9. **Constraints** — length limits, must-include/avoid letters or sounds, .com
   required?, etc.

If the user cannot articulate purpose, audience, and positioning, naming must
wait — help them clarify those first. Write the synthesized brief to `brief.md`
using `assets/brief-template.md`.

### Step 2 — Select the naming strategy & scoring rubric

Pick the distinctiveness target (read `references/naming-rules.md` §taxonomy and
`references/scoring-rubric.md`):

- **Descriptive** — cheap marketing, weak/no trademark, poor global scaling. Only
  for SEO-driven, budget-constrained, single-market plays.
- **Suggestive** — the popular sweet spot: legally strong, evocative (Netflix, Stripe).
- **Arbitrary** — real word, unrelated context; very strong (Apple, Oracle).
- **Coined/Fanciful** — invented; strongest protection, highest marketing cost (Kodak, Verizon).

State your recommended strategy and *why*, tied to their budget, timeline, and
expansion ambition. Then lock the **weighted scoring rubric** (default in
`scoring-rubric.md`) — set weights **now**, before generating, to prevent
post-hoc rationalisation. Confirm the rubric with the user (one quick check).

### Step 3 — Map conceptual territories

Do **not** anchor on the brief's literal keywords (a "fast food delivery" brief
must not converge on "fast / food / deliver" — that produces generic names).
Instead map 5–8 **conceptual territories** around the *experience and meaning*:
synonyms, metaphors, analogies, adjacent concepts, sensory associations,
mythology, foreign-language roots. List the territories and get a quick read from
the user on which resonate. Territories — not words — are the unit of exploration.

### Step 4 — Generate a wave & post it in chat (defer all judgment)

Generate **~150–200 candidates per wave** spread across the territories
and across **at least 6 construction techniques** from
`references/construction-techniques.md`
(real word, compound, portmanteau, altered spelling, invented/coined, foreign-word,
phonetic, metaphor/narrative, eponymous, mythological, and the two-word **"idea ×
idea" cross**). For each candidate record:

| name | technique | territory | words | syllables / phonetics | 1-line rationale |

(`words` = 1, 2, or 3 — the count of words in the name.)

Generation rules:
- Defer judgment entirely while generating — quantity now, quality later.
- **Post the whole wave in chat, split into labelled groups** (by territory,
  technique, or sound-feel — e.g. "A — pilot stem", "F1 — alive/liquid"), ~10–30 per
  group, each with its phonetic and a ⚠ flag on any risky name. This in-chat, grouped
  presentation *is* the deliverable the user reacts to — don't just write the wave to
  disk and summarise it.
- **Dedup against every prior wave**, and when a hard constraint is in play (a length
  cap, required initial, forced ending), **verify it programmatically** — a quick
  script that checks the rule and greps `candidates.md` for collisions beats eyeballing
  200 names.
- **Don't generate one-word names only.** Names may be two words — and the two-word
  cross is often the *more* memorable, more clearable option. Aim each wave at
  roughly **half one-word / half two-word** (a little three-word where the rhythm
  earns it). Build two-word names with the **two-stage cross**: Stage 1 a strong
  anchor word, Stage 2 cross it with an *angle* (a second word that adds tension or
  context), so the name reads as **idea × idea**, not a flat description. See
  `construction-techniques.md` technique 10 and `name-memorability.md`.
- **Verify the spread before you stop:** if the wave came out essentially all
  one-word, it is incomplete — run a two-word cross pass before filtering.
- **Say every candidate aloud as you write it.** A name lives in the ear — word of
  mouth runs on *sound*, not spelling. Reject at birth anything that *sounds like* a
  negative/embarrassing word even when spelled cleanly (**Engree** ≈ angry,
  **Keel** ≈ kill). Pronunciation is a first-class generation constraint, not an
  afterthought — see `sound-alike-screen.md`.
- Across the whole effort aim for **300–600+ candidates** (several waves), because
  attrition through filtering is steep and later waves breed densely around the
  keepers (Step 6).
- Honour hard constraints (length, required TLD, repo slug rules) but stay diverse.
- Append every wave to `candidates.md` (never discard the raw pool — it's the audit
  trail). From round 2 on, tag each candidate with the **seed keeper** it was bred
  from (Step 6) so the lineage is auditable.

### Step 5 — Screen, post in chat & capture reactions

Apply these screens — in the **fast in-chat loop** they are **inline ⚠ flags on the
posted wave, not a drop-gate** (defer judgment; the user prunes by choosing what they
like). In the heavier scored path they filter cheap-to-expensive (full detail in
`process-stages.md` §Stage 3):

1. **Knockout exclusions** — competitor clashes, generic/descriptive-unprotectable,
   obvious negative meaning in English, unpronounceable on first read, **visual
   ambiguity** (`rn`/`m`, `cl`/`d`, `li`/`u`), **phonetic sound-alikes** — said
   aloud (and slurred/fast), the name sounds like a negative/taboo word (Engree ≈
   angry, Keel ≈ kill), or its run-together slug births a bad word — already a
   common word in the category. Use `sound-alike-screen.md` for the stop-word list
   and sound patterns; a clear negative sound-alike is a near-veto regardless of score.
2. **Rubric scoring** — score survivors 1–5 per weighted criterion; compute the
   weighted composite. Drop the bottom half.
3. **Target verification** — benchmark each survivor against a set of **comparable /
   previous startups** in the category (the field it will actually compete in).
   Confirm two things: it is the same *caliber/pattern* as the strong names in that
   set (**on-target**), and it is **distinct** from every one of them (no shared
   root, blend, rhyme, or distinctive syllable — borrow patterns, never names).
   Cut or flag the off-target and the too-close. AI knockout pre-screen only — not a
   trademark search. Detail in `scoring-rubric.md` §Target verification.
4. **Word-count balance check** — before presenting, verify the survivors are not
   100% one-word names (unless the brief demands single tokens). If they are, run a
   two-word cross pass (Step 4) and re-filter — a portfolio with no two-word options
   is under-explored.
5. **Preliminary linguistic flag** — extend the sound-alike screen across the
   target-market languages **and accents**: flag any candidate that, *spoken*,
   resembles a negative/embarrassing/competitor word (see `sound-alike-screen.md`).
   This is an AI *pre-screen only* — native-speaker review is still required.

**Post the whole wave in chat as labelled groups** — not a filtered shortlist, and
*not* a ranked list (a #1 ranking anchors the user on "the recommendation"). Group by
conceptual territory, construction technique, or sound-feel; ~10–30 names per group;
each with its phonetic, a terse rationale where it earns one, and a **⚠ inline flag**
for any knockout / sound-alike / collision risk. Append the same wave to
`candidates.md`. **This in-chat grouped post is the deliverable** — the user reacts to
what's on screen, so don't bury it in a file and only summarise.

**Default reaction capture — the user names winners in chat.** Let them simply call
out the ones they like — "Pilax, Braio — winner", "Artes is good", "veto Engree". For
each, append the name to the **keepers ledger** (`keepers.md` / `keepers.json`) as a
**Lock** (or Keep) *that round* — remembered for the rest of the effort and eligible
for the final winners list — and record any veto neighbourhoods to avoid. That is the
whole rhythm: big wave in chat → user tags a handful → those breed the next wave. Don't
make the user fill in forms when they're moving fast.

**Optional heavier path — only when the user wants to grade methodically.** Drive a
click-through tier per name with **AskUserQuestion** — batches of up to 4 (`header` =
the name, `question` = technique · territory · phonetic) — options **★★ Lock / ★ Keep /
~ Explore / · Pass**, with **✗ Veto** (+ reason) on the "Other" field. Act on the
answers exactly as above; for each Lock/Keep you may fire one **sharpening follow-up**
(specific **word** vs **shape/angle**?) to make Step 6's regeneration more precise.
Full schema in `references/iterative-refinement.md` §2.

### Step 6 — Iterate: carry forward & breed from the keepers (the heart of the skill)

This loop **converges**, it does not just re-roll. Read
`references/iterative-refinement.md` for the full mechanism. Each round:

- **Carry forward.** The keepers ledger from Step 5 persists. Keepers are **immune
  to automatic filtering** — a later round's scoring or knockout screen may *flag* a
  keeper (and tell the user why), but it never silently drops one. A name liked in
  round 1 is still a finalist candidate in round 5. Nothing good is lost.
- **Breed the next wave from the keepers — "in the same form."** A post-round-1 wave
  is **mostly sibling clusters of the keepers and Explore picks**, not a fresh
  brainstorm. For each seed, generate a **dense sibling cluster** (scale to fill the
  ~150–200 wave — roughly ~20–40 per seed when only a few winners are in play) that
  holds its *form* fixed
  (same technique, syllable count & stress, phonetic shape, root/affix family,
  word-count) and vary **one dimension at a time** — for a two-word keeper, breed
  both *anchor-fixed / vary-the-angle* and *angle-fixed / vary-the-anchor*. Keep a
  **~20–30% fresh-exploration quota** for new territories so convergence isn't tunnel
  vision. Tag each sibling with the keeper it came from. (Mechanics: technique 10 in
  `construction-techniques.md`; §3 of `iterative-refinement.md`.)
- **Prune & avoid.** Drop dead territories; steer clear of the **Veto**
  neighbourhoods recorded in the keepers ledger.
- **Re-screen (Step 5) and post again** — the full ~150–200 wave in chat, grouped;
  the user tags winners; keepers updated.

Repeat for **3–5 rounds** (or until satisfied). Each round the pool **converges in
form** (more of what they love) while **widening coverage** of that form (dense
clusters of near-variants to pick the best instance from) — so later rounds choose
between *close siblings*, not strangers. Tell the user good names rarely come from
the first wave. Stop when the **keepers ledger has stabilised at ~15–30 strong
candidates** and a fresh look surfaces no new Locks.

### Step 7 — Compile the winners (from the keepers ledger)

The winners list is **drawn from the keepers ledger** — it was accumulated across
every round, not reconstructed at the end, so nothing the user loved was lost.
Curate the **8–15** strongest keepers *with* the user (confirm any flagged keepers
stay or go; the user, not the filter, removes a keeper). Then write `winners.md`
(use `assets/winners-template.md`) — for each winner present, as a portfolio
(unranked):

- The name and its phonetic rendering (esp. for coined/foreign names)
- Construction technique & conceptual territory
- Strategic rationale ("why this fits the brief")
- Distinctiveness level (descriptive → coined) and trademark-strength note
- Preliminary linguistic risk summary (with the "AI pre-screen, not legal/native" caveat)
- For repo/package targets: the proposed slug

Also write **`winners.json`** so the availability checker can consume it directly:

```json
{
  "project": "<project-slug>",
  "type": "brand | repo | both",
  "winners": [
    { "name": "Lumora", "handle": "lumora", "technique": "coined", "territory": "light", "tier": "lock", "roundFirstLiked": 1 }
  ]
}
```

### Step 8 — Hand off to availability screening

The winners are the input to the **name-availability-check** skill. Tell the user
they can now run:

```
/name-availability-check
```

…and that it will read `brand-naming/<project-slug>/winners.json` (or offer to
run it for them on the winners list). Remind them that availability screening is
the gate *after* selection: choose slowly first, screen the survivors second.
Also remind them that domain + handle screening is necessary but **not**
sufficient — full trademark clearance (attorney) and native-speaker linguistic
review remain manual, human steps before they commit to a name.

---

## Tone & guardrails

- Be a consultant, not a vending machine: explain trade-offs, push back on weak
  briefs, and resist the urge to "just give a list".
- Never present names ranked #1..#N as a recommendation — present portfolios.
- Always flag the limits of AI: no legal opinion, no native-speaker guarantee, no
  guarantee a name is unregistered.
- Keep the raw candidate pool and brief on disk so the work is auditable and the
  handoff to availability checking is clean.

<!-- gateway-skill-telemetry:v1 -->
## Телеметрия

Считай содержательным запуском случай, когда этот skill выбран для выполнения задачи, а не только открыт как справка.

- Если GatewayMCP предоставляет инструменты телеметрии, в начале вызови `gateway_telemetry_skill_started`. Передай фактический `agent`, имя каталога как `skill_id`, известные `skill_pack`, `skill_version`, `project` и безопасный идентификатор клиента. Неизвестные значения оставь пустыми.
- Сохрани `correlation_id` из ответа. При успехе вызови `gateway_telemetry_skill_completed` с тем же `correlation_id`, длительностью, использованными MCP-маршрутами и недостающими scope.
- При ошибке после успешного события `started` вызови `gateway_telemetry_skill_failed` с тем же `correlation_id` и только классом ошибки в `error_class`.
- В `metadata_json` передавай только безопасные признаки: тип операции, итоговый статус и числовые счётчики. Не передавай промпты, брифы, варианты названий, документы, тексты сообщений и ответов, персональные данные, токены, cookies, ключи, пароли и stack trace.
- Недоступность телеметрии не должна блокировать основную работу. Не повторяй неуспешную телеметрическую запись больше одного раза.
