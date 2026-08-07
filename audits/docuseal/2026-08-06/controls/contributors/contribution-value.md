# Contributor Value Assessment

Reader question: Which Git author-name groups account for most of the bounded, evidenced feature attribution, and where are the limits?

## Evidence Boundary And Attribution Rules

- Audit cutoff: onboarding start on 2026-08-06, America/Toronto; pinned release `3.1.7`, commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`.
- Included source types: pinned local Git/source, exact public commit and PR locators, [shared GitHub/history packet](../../evidence/packets/github-history-and-hosted-ci.md), [feature-level evidence packet](../../evidence/packets/contributor-vendor-value-feature-contribution.md), and Product Value outcome context.
- Excluded/inaccessible source types: private `docusealco/wip` history/reviews, private repository settings, unlinked design/test/support/operations work, personnel records, account authority, contracts, time records, customer acceptance, and live target evidence.
- Feature grouping rule: 16 representative coherent units with a dated implementation outcome and exact source locator. This is not an exhaustive reconstruction of 2,879 commits.
- Attribution rule: value bands (`critical 8`, `high 5`, `meaningful 3`, `bounded 2`, `minor 1`) order supported feature outcomes; points are allocated only to documented material sub-deliveries. Identical author names across different email labels are intentionally grouped; that does not establish one person, account, role, or continuing identity. Points are not hours, effort, merit, ownership, compensation, performance, or a universal score.

## Feature/Change Units

The evidence packet contains every exact commit, PR/issue, file/symbol, delivery-quality observation, share rationale, and limitation. This table preserves the complete unit set while keeping navigation compact.

| Unit | Outcome and value band | Task magnitude | Delivery quality | Credited contributors and share | Evidence | Confidence/limit |
|---|---|---|---|---|---|---|
| FC-01 | Initial account, template/form, signing/submission, storage, mail, PDF and CI foundation — `critical 8` | Cross-layer product bootstrap | Quality configuration present; no retained contemporaneous run/review | Alex Turchyn 100% | [FC-01](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High authorship; medium contemporary quality |
| FC-02 | PDF/signature output, submitter API and webhook settings — `high 5` | Material output/integration surface | No linked public review or artifact result | Alex Turchyn 100% | [FC-02](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High attribution; medium demonstrated outcome |
| FC-03 | Operator TOTP/2FA and authorization structure — `high 5` | Crosses authentication and account authorization | No unit-specific negative-test result | Alex Turchyn 100% | [FC-03](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High implementation; medium assurance |
| FC-04 | Custom certificate, TSA, protected blob delivery and encryption-key path — `high 5` | Crosses artifact trust, delivery and secrets | No retained artifact/key/external-verifier proof | Pete Matsyburka 80%; Alex Turchyn 20% | [FC-04](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High dated sub-delivery; medium operation |
| FC-05 | API/template-webhook lifecycle and webhook secret — `high 5` | Material integration breadth/authentication | `DocuSeal` author-name mapping unresolved; no public review | Pete Matsyburka 80%; `DocuSeal` 20% | [FC-05](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High commits; medium mapping/outcome |
| FC-06 | Sidekiq completion/email/webhook execution — `high 5` | Cross-cutting execution/retry change | Test wiring present; no recovery/backlog proof | Pete Matsyburka 100% | [FC-06](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High implementation; low-medium effectiveness |
| FC-07 | PDF verification, Event Log UI and audit timezone — `high 5` | Material evidence inspection/verification | No independent verifier or artifact acceptance | Pete Matsyburka 60%; Alex Turchyn 40% | [FC-07](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High attribution; low independent assurance |
| FC-08 | Operator email OTP and signer verification settings — `high 5` | Material operator/signer assurance | System spec exists; target assurance not accepted | Alex Turchyn 70%; Pete Matsyburka 30% | [FC-08](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High direct evidence; medium assurance |
| FC-09 | Brakeman CI and masked-field behavior — `meaningful 3` | Bounded application-security and sensitive-field change | Direct CI/spec evidence; broader scan limits remain | Pete Matsyburka 50%; Alex Turchyn 50% | [FC-09](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High bounded change; low overall assurance |
| FC-10 | PWA/shared-link/disclosure affordances — `meaningful 3` | Useful web/mobile and disclosure surface | No device/customer/legal acceptance | Alex Turchyn 100% | [FC-10](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High attribution; low-medium target outcome |
| FC-11 | Durable webhook event/attempt, retry/status UI and job specs — `high 5` | Material integration delivery evidence | Broad specs; no target receiver/reconciliation run | Alex Turchyn 60%; Pete Matsyburka 40% | [FC-11](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High regression scope; medium operation |
| FC-12 | Dynamic documents and document editor — `critical 8` | Two large cross-layer authoring capabilities | No direct fixture/review evidence identified | Pete Matsyburka 100% | [FC-12](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High implementation; low-medium demonstrated quality |
| FC-13 | MCP integration surface — `high 5` | Material new integration; non-mandatory path | No protocol/target integration test | Alex Turchyn 90%; Pete Matsyburka 10% | [FC-13](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High attribution; low target value evidence |
| FC-14 | Signer email 2FA and KBA state/evidence — `high 5` | Material signer-assurance mechanisms | System coverage; no provider/specialist result | Alex Turchyn 50%; Pete Matsyburka 50% | [FC-14](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High source; low-medium assurance outcome |
| FC-15 | Webhook HMAC/retries and submission completion state — `high 5` | Material authenticity/retry/state semantics | Specs/source; no remote reconciliation result | Pete Matsyburka 100% | [FC-15](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High bounded implementation; medium operation |
| FC-16 | README SMS/database corrections — `minor 1` | Isolated public-documentation accuracy | Traceable merged public PR; no submitted review returned | `aqilaziz` 100% | [FC-16](../../evidence/packets/contributor-vendor-value-feature-contribution.md) | High attribution; intentionally minor outcome |

## Project-Lifetime Top-80% Contributors

The denominator is only the `78.0` points supported by the selected units.

| Contributor | Attributed feature-value units | Share of supported total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Alex Turchyn | `39.0` | 50.0% | FC-01–FC-05, FC-07–FC-11, FC-13–FC-14 | [Exact unit evidence](../../evidence/packets/contributor-vendor-value-feature-contribution.md); high for listed commits, not a person/account/role conclusion |
| Pete Matsyburka | `37.0` | 47.4% | FC-04–FC-09, FC-11–FC-15 | [Exact unit evidence](../../evidence/packets/contributor-vendor-value-feature-contribution.md); high for listed commits, not a person/account/role conclusion |

This smallest two-author-name-group set reaches `76.0/78.0` (97.4%). The long tail is `2.0` (2.6%): unmapped Git author-name groups `DocuSeal` and `aqilaziz`, `1.0` each.

## Cutoff-Anchored 12-Month Periods

### 2025-08-07 to 2026-08-06

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Pete Matsyburka | `16.0` | 66.7% | FC-12–FC-15 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |
| Alex Turchyn | `7.0` | 29.2% | FC-13–FC-14 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |

Smallest >=80% set: Pete + Alex, `23.0/24.0` (95.8%); long tail `aqilaziz`, `1.0` (4.2%).

### 2024-08-07 to 2025-08-06

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Alex Turchyn | `13.0` | 61.9% | FC-07–FC-11 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |
| Pete Matsyburka | `8.0` | 38.1% | FC-07–FC-09, FC-11 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |

Smallest >=80% set: Alex + Pete, `21.0/21.0` (100%); no long tail within selected units.

### 2023-08-07 to 2024-08-06

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Pete Matsyburka | `13.0` | 65.0% | FC-04–FC-06 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |
| Alex Turchyn | `6.0` | 30.0% | FC-03–FC-04 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |

Smallest >=80% set: Pete + Alex author-name groups, `19.0/20.0` (95.0%); long tail unmapped author-name group `DocuSeal`, `1.0` (5.0%).

### Partial 2023-05-21 to 2023-08-06

| Contributor | Attributed feature-value units | Share of supported period total | Material feature/change units | Evidence and confidence |
|---|---:|---:|---|---|
| Alex Turchyn | `13.0` | 100% | FC-01–FC-02 | [Period aggregate](../../evidence/packets/contributor-vendor-value-feature-contribution.md) |

Smallest >=80% set: Alex, `13.0/13.0` (100%); no long tail within selected units.

## Material Unknowns And Closure Routes

- The selected units support concentrated attribution in two author-name groups within this judgment-selected sample. They do **not** establish knowledge concentration, staffing, employment, authority, vendor ownership, review quality, performance, person dependency, or bus factor; private `wip`, design, support, operations, and uncredited work remain unavailable.
- Identical author names across different email labels were grouped deliberately. `DocuSeal` is not merged into another group; no group proves one person, account, role, continuing identity, employment, or authority.
- Most units lack a public PR/review trail. Repository-level green CI does not retroactively establish each unit's quality, coverage, live behavior, or target acceptance.
- No distinct open item is created from the points. OI-015 must include two trained source/application successors and retained knowledge-transfer evidence; OI-016 must exercise control transfer. Maintenance Cost owns the replacement-maintainer burden and must not convert these points into hours or cost.
