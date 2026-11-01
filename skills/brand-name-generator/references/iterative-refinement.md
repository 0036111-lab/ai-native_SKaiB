# Iterative Refinement — Keepers, Granular Reactions & Seeded Regeneration

This file details the heart of the skill: how the **generate → present → react →
regenerate** loop (SKILL.md Steps 4–6) actually *converges* instead of just
churning out fresh lists. Three mechanisms make it work:

1. **The Keepers ledger** — selection is *remembered*, never just subtracted.
2. **Granular reactions** — a tier scale, not a binary like/dislike.
3. **Seeded regeneration** — each new wave is *bred from what the user kept*, in
   the same *form*.

The three reinforce each other: bigger waves only help if selection is granular
enough to pick the best sibling; granular selection only helps if there are dense
clusters of near-variants to choose *within*; and dense clusters only appear if you
breed them from the keepers. Run all three together.

---

## 1. The Keepers ledger (carry-forward — nothing good is lost)

The cardinal rule: **a name the user liked at any round is a name that can win.**
If a candidate earns a positive reaction in round 1, it must still be eligible for
the final winners list in round 5 — even if it never appears in another wave.
Liking is **sticky**; the user should never have to re-discover a name they already
loved, and a good early name must not be quietly filtered out by a later round's
scoring.

Maintain `keepers.md` (human-readable) and `keepers.json` (machine-readable) in the
working folder. Every round, **append** the names that earned a Keep-or-better
reaction. Keepers are **immune to automatic filtering** — rubric scoring and
knockout screens may *flag* a keeper (e.g., a late trademark or sound-alike concern)
but must not silently drop it. Only the user, told the reason, removes a keeper.

Each keeper row records:

| name | tier | round first liked | technique | territory | words | phonetic shape | note / why kept |

`keepers.json` shape (the seed bank for regeneration *and* the source of the final
winners):

```json
{
  "project": "<slug>",
  "keepers": [
    {
      "name": "Ingrain",
      "tier": "lock",
      "roundFirstLiked": 1,
      "technique": "real word",
      "territory": "roots / embedding",
      "words": 1,
      "shape": "VC-CCVC, 2 syll, stress-2",
      "note": "loved the 'settle deep in' meaning"
    }
  ]
}
```

## 2. Granular reactions (replace like/dislike with a tier scale)

When you present a wave, do **not** ask "which do you like?" Capture a **graded
reaction per name** so the loop knows both *what to keep* and *what to breed*:

| Tier | Symbol | Meaning | → Keepers? | → Breed siblings? |
|---|---|---|---|---|
| **Lock** | ★★ | Finalist-track — love it | Yes | Yes — **many** (this is the form to chase) |
| **Keep** | ★ | Like it; carry it forward | Yes | Yes — some |
| **Explore** | ~ | Not the name, but the *form / angle* is right | No | Yes — breed from its *pattern* |
| **Pass** | · | Neutral / not it | No | No |
| **Veto** | ✗ | Actively wrong (sound, meaning, vibe) | No | No — and avoid its neighbourhood |

Push for the *finer* signal. When a user likes a name, ask the one question that
makes regeneration precise instead of random: is it the **specific word** they like
(→ Lock / Keep) or the **shape / angle** (→ Explore)? Record the reaction tier next
to each candidate in `candidates.md`, and copy every Lock/Keep row into the keepers
ledger (§1). Log Vetoes too — they define neighbourhoods to *avoid* when breeding.

### Capture reactions in-process (AskUserQuestion — no copy-paste)

Collect the tiers with the **AskUserQuestion** tool so reacting is a *click*, not a
typed command. This keeps the whole loop UI-native and matches how the brief was
gathered in Step 1.

**Shape of the call.** One **question per name**, batched **up to 4 names per call**
(the tool allows 1–4 questions per call). For each name:

- `header`: the name (the short chip — truncate to ≤ 12 chars if long).
- `question`: `Your reaction to <Name>? — <technique> · <territory> · /<phonetic>/`
- `options` (4) — the four routine reactions, **each with a description of its
  downstream consequence** so the user picks with eyes open:
  - **★★ Lock** — "Finalist-track — love it. Carried to the keepers ledger; bred heavily next round."
  - **★ Keep** — "Like it — carried forward, eligible for the final list; bred some."
  - **~ Explore** — "Not this word, but the form/angle is right — breed siblings from its pattern."
  - **· Pass** — "No strong reaction — skip it."

Sketch of one call (4 names → 4 questions):

```
AskUserQuestion({ questions: [
  { header: "Lumora", question: "Your reaction to Lumora? — coined · light · /lu-MOR-a/",
    multiSelect: false, options: [
      { label: "★★ Lock",   description: "Finalist-track — love it. Kept + bred heavily." },
      { label: "★ Keep",    description: "Like it — carried forward, eligible for the final list." },
      { label: "~ Explore", description: "Not this word, but the form/angle is right — breed from it." },
      { label: "· Pass",    description: "No strong reaction — skip it." } ] },
  // …up to 3 more names…
]})
```

**Why these four are the buttons.** The tool caps options at 4 (+ an automatic
"Other"). **Pass** earns a button because it is the frequent one-click dismissal —
without it the user is forced into "Other" for every name they skip. **Veto** rides
on **"Other"**: the user types the reason ("veto — sounds like *angry*"), which is
exactly the *neighbourhood-to-avoid* note the ledger needs anyway. (If a project
expects more vetoes than passes, swap them — make **✗ Veto** the 4th button and let
Pass be the unspoken no-op.)

**Batching.** Present the portfolio as scannable text first (grouped by territory),
*then* walk the names through forms in territory-sized batches of ≤ 4. The user can
stop early once they've flagged enough — not every name needs a form pass. Free text
still works for power users ("lock 3, 7, 12"); the form is the **default**, not the
only, path.

**Sharpening follow-up (also a form).** For the Lock/Keep names, fire one more
question — batchable up to 4 names per call:

- `question`: `<Name> — is it the word, or the shape/angle?`
- `options`: **The exact word** ("keep as-is") · **The shape/angle** ("also breed siblings") · **Both**

so §3's regeneration targets the right dimension.

**After the form — map answers → actions.** Lock/Keep → append to the keepers ledger
(§1); Explore → record the form/angle to breed; Veto ("Other") → record the
neighbourhood to avoid; write **every** tier into `candidates.md`.

## 3. Seeded regeneration — breed the next wave from the keepers, "in the same form"

After round 1, a wave is **not** a fresh brainstorm — it is **mostly bred from the
keepers and the Explore picks.** For each seed name, generate a **sibling cluster**
that holds the seed's *form* fixed and varies **one dimension at a time.** "Same
form" means:

- **Same construction technique** — a coined seed breeds more coinages; an
  idea × idea cross breeds more crosses; a real-word seed breeds adjacent real words.
- **Same syllable count & stress pattern** — keep the rhythm in the ear.
- **Same phonetic shape** — same onset consonant class, same vowel colour, same
  terminal stop / affix (seed ends `-ora` → siblings in `-ora / -ura / -eya`).
- **Same morpheme / root family** — swap the *root* for an adjacent root in the same
  territory, **or** swap the *affix* for a sibling affix — keep the other fixed.
- **Same word-count** — a two-word keeper breeds **two ways**: *anchor fixed, vary
  the angle* (Free × People → Free × Hours, Free × Range) **and** *angle fixed, vary
  the anchor*.

Per seed, aim for a **cluster of ~8–12 siblings.** Keep a **fresh-exploration quota
of ~20–30%** of each wave for genuinely new territories/techniques so convergence
doesn't become tunnel vision — but the **majority of every post-round-1 wave is
sibling clusters of the keepers.** Append the whole wave (siblings + fresh) to
`candidates.md`, **tagging each sibling with the seed it came from**, so the lineage
is auditable.

Net effect: each round the pool **converges in form** (more of what the user loves)
while still **widening coverage** of that form (many near-variants to pick the *best*
instance from). That is what "more granular and refined" means in practice — later
rounds choose between **close siblings**, not between unrelated strangers.

---

## Counts per stage (scaled up)

| Stage | Old | New |
|---|---|---|
| Round-1 wave | 40–60 | **80–120** (broad) |
| Each later wave | 40–60 | **60–100** (mostly sibling clusters) |
| Survivors presented per round | tight shortlist | **24–40**, grouped by territory |
| Total across the effort | 150–300 | **300–600+** |
| Keepers ledger at convergence | — | **15–30** |
| Final winners | 5–12 | **8–15** |

## Convergence schedule (how a typical effort runs)

- **Round 1 — broad.** 80–120 across all territories/techniques. Capture graded
  reactions. Seed the keepers ledger.
- **Rounds 2–3 — converge.** Waves are mostly sibling clusters of the keepers +
  20–30% fresh. Keepers grow; present 24–40 each round; the Lock vs Keep distinction
  starts to matter.
- **Rounds 4–5 — refine.** Tight sibling clusters around the Locks; the user is now
  choosing between near-twins. Lock the keepers ledger.
- **Compile.** Winners = the keepers, curated *with* the user (SKILL.md Step 7) — the
  list is already assembled because it was accumulated all along, not reconstructed
  at the end.
