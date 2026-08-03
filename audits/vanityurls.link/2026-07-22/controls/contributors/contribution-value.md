# Contributor Value Assessment

## Evidence Boundary And Attribution Rules

- Audit cutoff: 2026-07-22 23:59:59 America/Toronto.
- Included source types: the four cutoff-pinned repositories in
  [E-001](../../evidence/evidence-ledger.md), public GitHub PR/commit/review
  records in [E-002](../../evidence/evidence-ledger.md), public GitHub profiles,
  approved documentation, and linked Product Value, Revenue Risk, Project
  Health, Maintenance Cost, and Business Continuity outputs.
- Excluded or inaccessible source types: private planning, time records,
  contracts, live outcome/adoption evidence, unlinked chats, and work not
  attributable from approved evidence. Automated release/dependency/badge PRs
  receive no contributor-value units.
- Feature grouping rule: linked PRs/commits and follow-up fixes form one unit
  only when they deliver one coherent product, safety, operability, or
  documentation outcome.
- Attribution rule: credit only a public profile or authored record with a
  material, source-linked contribution. `bhdicaire`/Benoît H. Dicaire,
  `felleg`/Félix Léger, `slig`/Tiago Serafim, and `XVII`/Jake Edwards are linked
  by their public GitHub profiles. A merge, release bot, acknowledgement, or
  bare approval is not material credit by itself.

The value bands are an ordering aid, not a performance or hours-worked score:
`critical = 8`, `high = 5`, `meaningful = 3`, `bounded = 2`, `minor = 1`.
Outcome, task magnitude, delivery quality, contribution share, and confidence
remain separate below.

## Feature/Change Units

| Unit | Outcome and value band | Task magnitude | Delivery quality | Credited contributors and share | Evidence | Confidence/limit |
|---|---|---|---|---|---|---|
| CV-001 | `critical = 8`: initial public redirector, build, configuration, and contributor baseline | Cross-cutting product/build foundation | Public source and contributor/governance material exist; no executed operation was observed | Benoît H. Dicaire 100% | [`13df43c`](https://github.com/vanityURLs/code/commit/13df43c45e17c4d574dc683a2969123b3407c71a); [E-004](../../evidence/evidence-ledger.md) | High for authored foundation; outcome is implementation/documentation only |
| CV-002 | `high = 5`: dynamic redirects, collision testing, and user configuration | Multi-file redirect/configuration workflow | PR describes collision testing and configuration; no independent runtime exercise | Félix Léger 100% | [code PR #8](https://github.com/vanityURLs/code/pull/8) | High for authored change; no material review record |
| CV-003 | `meaningful = 3`: duplicate-target warning and repository sync | Bounded CLI/configuration behavior | Explicit PR purpose; no demonstrated operator use | Félix Léger 100% | [code PR #12](https://github.com/vanityURLs/code/pull/12) | High for authored PR; outcome is not live-verified |
| CV-004 | `meaningful = 3`: later link-command reliability fixes and operator guidance | Bounded CLI/configuration behavior with follow-up fixes/docs | Dated follow-up Git history; no demonstrated operator use | Félix Léger 100% | commits [`3427f865`](https://github.com/vanityURLs/code/commit/3427f865dd41fe40e8e0e1b9479040209a55a8e6), [`1ee0565c`](https://github.com/vanityURLs/code/commit/1ee0565cf381f4c35fbf9c3126b6786e74a9b2d6) | Moderate-high; outcome is not live-verified |
| CV-005 | `meaningful = 3`: default root redirect application | One customer-visible fallback route and static asset | PR includes purpose, visual evidence, and one recorded approval; approval alone receives no share | Félix Léger 100% | [code PR #29](https://github.com/vanityURLs/code/pull/29) | High for authored implementation; customer adoption unknown |
| CV-006 | `critical = 8`: maintainable setup/upgrade and release-control foundation | Cross-cutting build, setup, release-signing, complexity, tests, and refactoring work | Public PRs include source/test changes and documented release workflow; no end-to-end execution was approved | Benoît H. Dicaire 100% | [code PR #64](https://github.com/vanityURLs/code/pull/64), [#66](https://github.com/vanityURLs/code/pull/66), [#69](https://github.com/vanityURLs/code/pull/69); [E-006](../../evidence/evidence-ledger.md) | High for authored change; hosted checks do not prove safe takeover |
| CV-007 | `high = 5`: runtime registry, safe target handling, localization, and custom-page security hardening | Cross-cutting runtime, policy, security, and test boundaries | Source changes include explicit security/runtime fixes; no live request or security test was observed | Benoît H. Dicaire 100% | commits [`1722f568`](https://github.com/vanityURLs/code/commit/1722f5687ea6e3a3b2a0d7f9611e99e43bd0a7b2), [`20ea4479`](https://github.com/vanityURLs/code/commit/20ea4479addccb5baa579f72db850425f3997f24); [E-014](../../evidence/evidence-ledger.md) | High for implementation; effectiveness remains unknown |
| CV-008 | `meaningful = 3`: signed documentation history and current setup guidance | Multi-document operator/onboarding surface | Public documentation and release PRs; website build/review rigor is unproved | Benoît H. Dicaire 100% | [website PR #32](https://github.com/vanityURLs/website/pull/32), [#41](https://github.com/vanityURLs/website/pull/41); [E-005](../../evidence/evidence-ledger.md) | High for authored documentation; onboarding success unknown |
| CV-009 | `meaningful = 3`: public Terraform and example-instance operating baseline | Cross-repository infrastructure/instance boundary | Reviewable source exists; no PR, state, deploy, or recovery exercise was public | Benoît H. Dicaire 100% | [`v8s-config@a24eac8`](https://github.com/vanityURLs/v8s-config/commit/a24eac8585be9fd1a7fff81b0a0dd7bd535ea063); [`v8s-link@2159e433`](https://github.com/vanityURLs/v8s-link/commit/2159e433a408e76b71308b12b2daae703b7f63c3); [E-004](../../evidence/evidence-ledger.md) | High for source authorship; live operability unknown |
| CV-010 | `minor = 1` each: bounded public configuration correction and README documentation correction | Single-file corrective changes | Public merged commits; no outcome evidence beyond the correction | Tiago Serafim 100%; Jake Edwards 100% | [code PR #10](https://github.com/vanityURLs/code/pull/10); [`8334229a`](https://github.com/vanityURLs/code/commit/8334229ac32a02e05151b8ca8bb5b1fa538e2080) | High for authored records; minor scope |

## Project-Lifetime Top-80% Contributors

Supported feature-value total: 43 units. The smallest contributor set reaching
approximately 80% is two people (41 units; 95.3%).

| Contributor | Attributed feature-value units | Share of supported total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Benoît H. Dicaire ([`bhdicaire`](https://github.com/bhdicaire)) | 27 | 62.8% | CV-001, CV-006–CV-009 | High for public authorship and source; outcome/operation evidence varies by unit |
| Félix Léger ([`felleg`](https://github.com/felleg)) | 14 | 32.6% | CV-002–CV-005 | High for public PR authorship; no live outcome or material review evidence |

Long tail: Tiago Serafim and Jake Edwards account for 2 supported units (4.7%).
Brian J. Adams (`0xBJA`) is publicly acknowledged for ideas/user testing, but
the approved evidence does not link those contributions to a feature/change
unit; no numeric credit is assigned.

## Cutoff-Anchored 12-Month Periods

### 2025-07-23 to 2026-07-22

Supported period total: 22 units. Benoît H. Dicaire alone reaches 86.4%.

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Benoît H. Dicaire | 19 | 86.4% | CV-006–CV-009 | High for source authorship; no live operation proof |

Long tail: Félix Léger, CV-005, 3 units (13.6%).

### 2024-07-23 to 2025-07-22

Supported period total: 3 units. Félix Léger alone reaches 100.0%.

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Félix Léger | 3 | 100.0% | CV-004 | Moderate-high; dated source changes, no observed use |

### 2023-11-11 to 2024-07-22 (partial period)

Supported period total: 18 units. Benoît H. Dicaire and Félix Léger together
reach 88.9%.

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Benoît H. Dicaire | 8 | 53.3% | CV-001 | High for source authorship; operational outcome unknown |
| Félix Léger | 8 | 44.4% | CV-002–CV-003 | High for PR authorship; no material review record |

Long tail: Tiago Serafim and Jake Edwards, 2 units (11.1%).

## Material Unknowns And Closure Routes

- Public evidence cannot establish hours, hidden work, private design/review,
  employment relationship, compensation, or contractual acceptance.
- Most PRs lack a linked issue/acceptance record; source proves implementation,
  not customer value, adoption, or task effort in hours.
- Review endpoints show no material third-party review evidence for the selected
  feature units. A bare approval on PR #29 is intentionally not attributed.
- No public evidence establishes whether acknowledged ideas/user-testing
  contributors changed a particular feature. Preserve that acknowledgement
  without inventing a value share.
- These limits make this assessment useful for continuity and onboarding
  planning, but unsuitable for employment, compensation, or vendor-performance
  decisions.
