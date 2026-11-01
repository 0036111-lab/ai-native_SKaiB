---
name: novaya-vysota-template
description: >-
  Создаёт или обновляет медийный story-site по архитектуре проекта «Новая
  высота»: герой и видео, доказанная история роста, большая спортивная цель,
  программа поддержки, культурный или семейный контекст, предложение партнёрам,
  команда, контакты, форма заявки и SEO/GEO. Используй, когда нужно быстро
  собрать следующий сайт для спортсмена, команды или социально-спортивного
  проекта, сохранив драматургию и визуальный язык, но заменив все факты и медиа.
---

# Novaya Vysota Template

## Purpose

Build a high-impact, mobile-first story-site in which a person's path makes a
larger project understandable. Preserve the two-contour model:

1. **Hero contour** — a specific person, ambition, history, evidence, next step.
2. **Platform contour** — the people, partners and infrastructure that turn an
   individual opportunity into a repeatable system.

Never copy personal data, claims, contacts, photographs or video from the
original case. The reusable asset is the structure and interaction logic.

## Required inputs

Collect the minimum viable brief. Make safe assumptions for presentation and
motion; stop only when a missing fact would make a public claim misleading.

- hero name, discipline, location and verified status;
- one primary goal and its time horizon;
- 3–7 dated achievements with sources;
- immediate program stage and what support unlocks;
- platform purpose, founders/team and public contacts;
- approved photographs, video and credits;
- application destination or backend route;
- partner audience and desired action.

Create four working registers before writing: `facts`, `content`, `media`, and
`decisions`. Label every fact `confirmed`, `needs-check`, or `do-not-publish`.

## Page architecture

Use the content model in `references/content-model.md`. Default sequence:

1. Video hero: identity, discipline, strongest proof, future goal, two CTAs.
2. Proof strip: compact verified signals.
3. Who the hero is: human story plus six-year or multi-season growth arc.
4. Timeline: progression, national results, international experience.
5. The target: what the next cycle means and why the opportunity matters.
6. Program: stages, current milestone and measurable deliverables.
7. Invitation or third-party validation without publishing private terms.
8. Cultural/family context: where the story comes from.
9. About the platform: philosophy and operating model.
10. Partner value: contribution, media/brand value, reporting, participation.
11. Team and contacts.
12. Final CTA and application modal/form.

The hero must remain dominant. Introduce the platform only after the visitor
understands whom and what they are supporting.

## Visual and motion language

- Editorial sports aesthetic: oversized condensed headings, hard grids, black,
  warm off-white, signal red and one acid accent.
- Full-bleed photography and short muted autoplay video with a poster fallback.
- Scroll reveals, kinetic ticker, timeline progress and restrained parallax.
- Motion must clarify hierarchy; respect `prefers-reduced-motion`.
- Use `clamp()` typography and test 320, 375, 768, 1440 and 1920 px widths.
- No horizontal overflow. Large headlines must wrap inside the viewport.
- Keep CTA contrast high and tap targets at least 44 px.

Start from `assets/site-template/` when a static prototype is sufficient. For an
existing framework, port its tokens, sections and behaviors instead of forcing
the static files into the codebase.

## Copy rules

- Lead with facts and action, not slogans.
- Replace guarantees with sourced probability or clearly attributed ambition.
- Explain why the opportunity matters to sport, partners and the wider project.
- Keep private commercial terms behind “Получить условия”.
- Prefer “государственные и муниципальные институты” over vague political wording.
- Avoid claims such as “first”, “only”, “best” or “Olympic participant” unless
  directly verified and current.
- For sensitive participation rules, link the official governing body and date
  the statement.

## SEO/GEO baseline

Create one unambiguous H1, descriptive title and meta description, canonical,
Open Graph image, meaningful alt text, sitemap and robots file. Add JSON-LD for
`Person`, `SportsOrganization`, `WebSite`, `BreadcrumbList` and only factual
`Event` records. Include a concise FAQ that answers named queries in complete
sentences. Do not keyword-stuff. Distinguish the platform entity from the athlete
entity and connect claims to sources. Read `references/customization.md` before
launch.

## Form and publication

- The form must disclose data processing and have a real delivery route.
- If no backend/Gateway route exists, do not claim that requests are delivered.
  Provide a visible fallback contact.
- Never expose Telegram bot tokens in frontend code.
- Optimize hero video to a short loop and provide poster/WebM/MP4 variants.
- Run mobile, keyboard, reduced-motion, metadata and form-delivery checks.
- Do not say the site is published until the production URL loads successfully.

## Deliverables

Return the deployed URL when actually deployed, repository/branch or artifact
location, a confirmed-vs-unverified fact list, media replacements still needed,
form delivery status and the next safe update path.

<!-- gateway-skill-telemetry:v1 -->
## Телеметрия

Если GatewayMCP предоставляет инструменты телеметрии, при содержательном запуске
вызови `gateway_telemetry_skill_started`, сохрани `correlation_id` и заверши
событием `gateway_telemetry_skill_completed` или
`gateway_telemetry_skill_failed`. Передавай только безопасные метаданные: тип
операции, статус и числовые счётчики. Не передавай содержимое форм, персональные
данные, токены, закрытые условия партнёрства или приватные URL медиа.
Недоступность телеметрии не блокирует работу.
