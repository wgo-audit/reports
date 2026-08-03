# PDR-006: Localized Public And Trust Pages

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

The build generates localized home, lookup, missing-link, lifecycle, privacy, terms, abuse, security, and operator-facing pages from defaults plus instance configuration, with controlled `custom/public/` overrides.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public pages communicate identity, trust, link outcomes, and lookup across supported languages. | Public-pages, i18n, jurisdiction, security docs | Content accuracy and accessibility not independently reviewed here. |
| Implementation | Build/site-core renders pages, operator data, legal deferral, security.txt, localization, and CSP profiles. | `scripts/build.mjs`; build-core libraries; defaults/public | Build not executed. |
| Runtime/demonstration | Instance source contains localized generated/default assets and operator config. | `v8s-link` tree | Live rendering and contacts unobserved; personal values omitted. |
| Approval/specialist sign-off | Source ADRs 0005, 0008, 0018, 0019 record aspects. | `docs/adr/` | No legal, accessibility, localization, or privacy specialist sign-off. |

## Constraints, Options, And Tradeoffs

Rich trust surfaces improve accountability but create translation, legal, contact, and override-maintenance obligations. Sandboxed custom HTML intentionally trades same-origin capability for isolation.

## Impacts And Boundaries

A new operator must replace identity/contact/jurisdiction values and verify every supported language. Documentation breadth does not prove those outputs are correct for a new jurisdiction.

## Change, Reversal, And Follow-Up

Keep operator-specific claims configurable and require explicit specialist review where legal/accessibility/privacy assertions matter.
