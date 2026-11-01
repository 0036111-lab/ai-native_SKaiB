# Naming a GitHub Repository / Open-Source Project / Package

When the target is a repo or package (not — or in addition to — a consumer brand),
layer these conventions on top of the general naming rules. The goal shifts from
"emotional brandability" toward "typeable, greppable, collision-free, and clear
about what it does".

## Hard conventions

- **Lowercase, kebab-case.** `my-cool-tool`, not `MyCoolTool` or `my_cool_tool`.
  GitHub repo names allow letters, digits, `-`, `_`, `.`; kebab-case is the de-facto
  norm and the safest for URLs, npm, and CLI invocation.
- **Short and typeable.** Aim ≤ 2–3 words. It will be typed in `git clone`, import
  paths, and CLI commands. Avoid characters that need shift-key gymnastics.
- **ASCII only.** No spaces, no diacritics, no emoji.
- **Greppable / unique enough to search.** A repo called `core` or `utils` is
  invisible in search results; a slightly coined token (`ripgrep`, `esbuild`,
  `vite`) is findable and ownable.
- **Avoid leading numbers and reserved-ish words** that clash with package-manager
  or language keywords.

## Brandable vs. descriptive trade-off (for repos)

- **Descriptive** (`json-schema-validator`) — instantly clear, great for
  discoverability/SEO, but generic and crowded; hard to "own".
- **Coined/suggestive** (`zod`, `prettier`, `deno`, `vite`) — ownable, brandable,
  memorable; needs a tagline because it doesn't self-describe.
- A common winning pattern: **a coined/short name + a descriptive tagline** in the
  repo description (`vite — next generation frontend tooling`).

## Collision surface to screen (this is what to check)

A repo/package name is "available" only if it's clean across the registries its
users live in. Screen via the **name-availability-check** skill with `--type repo`:

- **GitHub** user/org namespace (and, if a target org is known, `owner/repo`).
- **npm** (`registry.npmjs.org`) — even non-JS projects should check; squatting is rife.
- **PyPI** — for anything Python-adjacent.
- **crates.io** — for Rust.
- (Add language-specific registries as relevant: pkg.go.dev, RubyGems, Packagist, Maven.)
- A **domain** is still nice-to-have for docs/landing (`.dev`, `.io`, `.sh` are
  popular for tools) — keep it in the check unless the user opts out.

## Scoring tweaks

When scoring repo names (see `scoring-rubric.md`), replace **Emotional resonance**
with **Slug cleanliness / typeability**, and reinterpret **Domain availability**
as **package-registry availability**. Keep Distinctiveness and Memorability high —
a tool nobody can recall or find is a dead tool.

## "Both" targets

If the user wants one name to serve as **both** a brand and a repo, every candidate
must simultaneously: read as a brand (pronounceable, evocative, distinctive) AND
reduce to a clean kebab-case slug with plausibly-free package + GitHub namespaces.
Reject candidates that only satisfy one side. The availability checker's default
`--type both` screens domains, social handles, and dev registries together.
