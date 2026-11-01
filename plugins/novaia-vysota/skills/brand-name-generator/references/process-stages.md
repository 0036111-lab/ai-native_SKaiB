# The Stage-by-Stage Naming Process

The professional workflow, synthesised from Lexicon, Zenmark, NameStormers, and
Interbrand. The SKILL.md operating procedure is a compressed, interactive version
of this. Use this file when you need the full rationale for a stage.

| Phase | Who | AI potential | Output |
|---|---|---|---|
| 1. Strategic brief | Human + AI | High | Brand brief, rubric, target name type |
| 2. Generation | AI | Very high | 150–500 candidates, categorised |
| 3. Internal filtering | AI | Very high | Top 30–50 |
| 4. Knockout trademark screen | API + human | Medium | Traffic-light per name → ~10–20 |
| 5. Linguistic pre-screen | AI | Low–medium | Risk rating per language → ~10–15 |
| 6. Human linguistic validation | Native speakers | — | Cleared shortlist → 5–8 |
| 7. Stakeholder presentation | Human + AI | Medium | 2–3 finalists |
| 8. Full legal clearance | TM attorney | Low | Cleared opinion → 1–2 |
| 9. Selection + asset acquisition | Human + API | Low | Owned domain/handles, filed mark |

**This skill covers Phases 1–3 deeply and prepares Phase 4–5 data. The
name-availability-check skill covers the digital-occupancy slice of Phases 3–4.
Phases 6–9 are human/attorney work — flag them, don't fake them.**

---

## Stage 1 — Strategic brief & discovery

Define the criteria before generating. Deliverables: brand-essence summary,
positioning statement, target-audience profile (incl. languages), competitive
landscape audit, **naming-strategy selection**, **weighted scoring rubric** (set
weights now), market/linguistic context, and scope (how many candidates, how many
finalists). Without a clear brief, naming devolves into preference arguments.

## Stage 2 — Generation

Agencies generate **200–800** candidates before filtering, because attrition is
steep. Approaches: association mapping (explore the *concept*, not the word),
linguistic construction (the techniques in `construction-techniques.md`),
cross-language mining, phonetic construction, metaphor/narrative, and the
**two-stage "idea × idea" cross** (Stage 1: a strong anchor word; Stage 2: cross it
with an *angle* — a second word that adds tension/context — producing a two-word
name). Rules: **defer judgment**, aim **300–600+** across the effort (round-1 wave
**80–120**, later waves **60–100**) over 5–8 territories, small-team discipline
(don't converge on the obvious), **don't anchor on the brief's keywords**, and keep
**word-count diversity** — a healthy wave is a mix of one-word *and* two-word
candidates, never one-word only.

**After round 1, generation is seeded, not fresh.** Each later wave is *mostly
sibling clusters bred from the keepers* — names in the **same form** (technique,
syllable count & stress, phonetic shape, root/affix family, word-count) as what the
user already liked — plus a ~20–30% fresh-exploration quota. This is the convergence
engine; full mechanics in `iterative-refinement.md`.

## Stage 3 — Preliminary internal filtering

Filtering here is **additive, not just subtractive**: it feeds a persistent
**keepers ledger** that carries every liked name forward across all rounds (immune
to later auto-filtering), and presents a **wider field (24–40 survivors) with graded
reactions** (★★ Lock / ★ Keep / ~ Explore / · Pass / ✗ Veto) rather than a tight
binary shortlist. Keepers seed the next wave and become the winners list. See
`iterative-refinement.md`. The cheap-before-expensive filters still set who gets
*presented* each round; reduce the raw wave → ~30–50 shown via:
1. **Exclusion criteria** — competitor clashes; generic/descriptive-unprotectable;
   obvious negative English meaning; unpronounceable on first read; visual/double-
   meaning ambiguity; already a common word in the category.
2. **Rubric scoring** — score 1–5 per criterion, drop the bottom half.
3. **Target verification** — benchmark survivors against a set of **comparable /
   previous startups** in the category (the field they'll compete in). Two questions:
   is the candidate the same *caliber/pattern* as the winners in that set
   (on-target), and is it *distinct* from every name in it (no shared root, blend,
   or distinctive syllable)? Borrow patterns, never names. AI knockout pre-screen
   only — not a trademark search. Detail in `scoring-rubric.md` §Target verification.
4. **Word-count balance check** — confirm the survivors are not 100% one-word names
   (unless the brief demands single tokens). If they are, run a two-word cross pass
   before continuing — see `construction-techniques.md` technique 10.
5. **Domain & handle pre-check** — `.com/.co/.io/.ai` + 4–5 social platforms. Zero
   viable digital options is a flag, not an automatic kill (a great name is worth
   acquiring a domain). *(This is exactly what name-availability-check automates.)*
6. **Basic web-search conflict check** — a name returning pages of an established
   competitor is a red flag.

## Stage 4 — Knockout trademark screening

A knockout search (not a clearance opinion): USPTO, EUIPO (TMView), WIPO Global
Brand DB, plus primary-market registries. Look for identical and confusingly
similar marks in the relevant Nice classes (SaaS typically needs class 42, often
9, sometimes 35). Output a **traffic-light** per name: green / amber / red.

> Note: since Nov 2023 the USPTO retired TESS for a system with **no public API**
> and anti-bot protection. Real-time automated USPTO search is no longer simple —
> options are third-party APIs (Corsearch, TrademarkNow, Markify), the USPTO bulk
> XML feed, or manual search. **Do not claim to have run a real trademark search
> you didn't run.** Flag this as a manual/attorney step.

## Stage 5 — Linguistic & cultural pre-screen

For each target-market language (always include Spanish, Mandarin, French, German,
Arabic, Japanese, Portuguese), assess: **phonetic resemblance to negative/vulgar/
competitor words — said aloud, slurred/fast, and in the local accent** (the
sound-alike "stop-word" screen, applied per language; see `sound-alike-screen.md`);
semantic associations; cultural connotations (numbers, colours, animals carry
market-specific meaning — 4 ≈ death in CN/JP; white = mourning in parts of Asia);
written/romanised form; and the **run-together** reading of the slug. Start in
English — a name that sounds like *angry* or *kill* fails before any translation —
then widen to each market. **AI flags candidates for attention; it does not replace
in-country native speakers.**

## Stages 6–9 — Human & legal

Native-speaker validation, stakeholder portfolio presentation (never ranked),
full attorney clearance ($2–10k/name for a real search), then final selection,
domain acquisition (.com > .co > .io > .ai > category TLD; register defensive
variants), handle reservation, and trademark filing (USPTO + Madrid Protocol;
"TM" while pending, "®" only once registered). These are out of scope for the
skill — name them so the user knows what remains.
