# Scoring Rubric

Lock weights **before** generation begins. Score each surviving candidate **1–5**
on each criterion, multiply by the weight, and sum to a weighted composite
(max 5.0). Use the composite to drop the bottom half of a wave — not to produce a
public ranking of the finalists (present finalists as an unranked portfolio).

## Default rubric

| Criterion | Weight | 1 (poor) | 5 (excellent) |
|---|---|---|---|
| **Memorability** | 0.20 | Forgettable, interchangeable | Sticks after one exposure |
| **Pronounceability (EN + target langs)** | 0.15 | Ambiguous, multiple readings | One obvious reading, easy to say |
| **Trademark potential** | 0.20 | Generic/descriptive, crowded | Arbitrary/coined, distinctive, defensible |
| **Distinctiveness** | 0.15 | Looks/sounds like competitors | Stands out in the category |
| **Emotional resonance** | 0.10 | Flat, clinical | Evokes the intended feeling |
| **Visual readability** | 0.10 | Ambiguous letterforms, bad at small size | Clean in caps/lower, favicon-safe |
| **Domain / handle availability** | 0.10 | Blocked everywhere | .com or strong alt + handles plausibly free |

Weights sum to 1.00. The **Domain/handle** score is the one criterion that becomes
*data-backed* later — it is provisional during generation and is corrected by the
**name-availability-check** skill once the winners are screened.

## Tuning the weights by purpose

- **Long-term brand / well-funded:** raise Trademark potential + Distinctiveness
  + Emotional resonance; lower Domain availability (a great name justifies buying
  a domain).
- **Bootstrapped / SEO-led / single market:** raise Pronounceability + Domain
  availability; you may tolerate a more descriptive, lower-TM name.
- **GitHub repo / package (see github-repo-naming.md):** swap *Emotional
  resonance* down and add a **"Slug cleanliness / typeability"** criterion;
  Domain availability becomes "package-registry availability".

## Scoring discipline

- Score against the **brief**, not personal taste.
- Don't let a single dazzling criterion rescue a name that fails SCRATCH on
  spelling or pronounceability — those are near-veto failures. This includes
  **sound-alikes**: a name that, spoken aloud, resembles a negative/taboo word
  (Engree ≈ angry, Keel ≈ kill) is capped on **Pronounceability** no matter how
  high it scores on Memorability or Distinctiveness (see `sound-alike-screen.md`).
- When two candidates tie, prefer the one with the stronger distinctiveness level
  (arbitrary/coined over suggestive over descriptive), all else equal.
- Record the per-criterion scores in `candidates.md` so the filtering is auditable.
- **Keepers are score-immune.** A name already in the keepers ledger (the user liked
  it in some round — see `iterative-refinement.md`) is *not* dropped by "bottom half"
  scoring. Score it for information and **flag** a low score for the user, but only
  the user removes a keeper. Scoring prunes *new* candidates; it never overrides a
  human Keep.

## Target verification (benchmark vs. comparable startups)

Scoring tells you a name is good *in the abstract*. **Target verification** tells
you it is good *against the field it will actually compete in*. Run it as a gate on
the survivors of each round, before presenting them:

1. **Assemble the comparison set.** From the brief's industry and positioning, list
   5–15 **comparable / adjacent startups and brands** (direct competitors plus the
   names users will mentally file this next to). This is the "previous startups"
   benchmark.
2. **Caliber check (is it on target?).** Held next to that set, does the candidate
   read as the same *tier* of name — same level of distinctiveness, polish, and
   construction sophistication? A suggestive coinage standing in a field of crisp
   two-word crosses (or vice-versa) looks off-target. The strongest crosses borrow
   the *pattern* of the winners in the set (place + object, attitude + craft) while
   landing on fresh words.
3. **Collision / derivative check (is it distinct?).** Reject or flag any candidate
   that is confusingly close to a name in the set — same root, same blend, rhyme,
   or shared distinctive syllable (launching "HomeBnB" next to Airbnb starts
   beaten). Borrowing a *pattern* is fine; echoing a *name* is not.
4. **Record the verdict** in `candidates.md`: the comparison set used, and per
   survivor a short note — on-target / off-target, distinct / too-close-to-`<X>`.

This is an AI knockout pre-screen against *known* startups in training data and the
brief, **not** a trademark search — recent/unindexed launches will be missed.
Full clearance stays a human/attorney step (see `process-stages.md` Stage 4).

## Word-count balance (verify before finalizing a wave)

Before locking a round's survivors, **verify the word-count spread** — the shortlist
must not be 100% one-word names unless the brief explicitly demands single tokens
(e.g., a one-word repo slug). Modern memorable brands skew toward the two-word
"idea × idea" cross (see `name-memorability.md` §4), so a portfolio with *no*
two-word options is under-explored, not refined. If the survivors collapsed to
one-word only, run a two-word cross pass (technique 10) before presenting.
