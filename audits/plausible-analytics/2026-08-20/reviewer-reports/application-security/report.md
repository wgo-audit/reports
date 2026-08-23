# Application Security

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether source-visible application attack paths can violate authentication, authorization, confidentiality, measurement integrity, or site/team boundaries in ways material to the library's Run/Subscribe/Replace decision. The cutoff is 2026-08-20 at onboarding start, America/Toronto. Evidence is the approved `primary-code` snapshot at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, its repository tests and build inputs, predecessor evidence E-023–E-030, and CodeGraph navigation of the same snapshot.

The review traced the public event route, request/header/replay processing, per-site gating and filtering, OAuth diagnostics, Sentry context, password/2FA/session flows, browser and bearer-API authorization, site/team membership checks, shared/public links, credential creation, representative request construction, query construction, and dependency/build inputs. It did not inspect live traffic, ingress, roles, keys, shared links, diagnostics, hosted systems, dependency scanner results, a deployed image, or replacement code; install/restore, active scanning, exploit execution, penetration testing, and legal conclusions were excluded.

## Coverage And Material Gaps

The source establishes meaningful session, CSRF, OAuth-state, API-scope, membership, site/team, feature, and rate-limit controls. It also exposes three material option-specific paths: privileged ingestion headers, unredacted diagnostics, and weak optional alternate-access credential acceptance. Close ingestion through [OI-011](../../controls/open-items.md#oi-011), OAuth diagnostics through [OI-010](../../controls/open-items.md#oi-010), visitor diagnostics through [OI-012](../../controls/open-items.md#oi-012), and shared-link/API credential hardening through [OI-013](../../controls/open-items.md#oi-013). Governance remains [OI-008](../../controls/open-items.md#oi-008).

No product test was executed: dependencies were absent and restore was prohibited. CodeGraph lifecycle checks completed against the exact absolute source root; its parser indexed JavaScript/TypeScript but not the Elixir request paths, so direct source and repository tests are the authority. No dependency/build-input note was triggered because no approved vulnerability result or source-visible exploitable dependency was established; this is not evidence that dependencies are vulnerability-free.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The unauthenticated ingestion path trusts client-reachable forwarding/classification inputs and claimed-domain fan-out; in EE, replay headers set historical time and bypass the source per-site rate check. | High | M | [E-031](../../evidence/evidence-ledger.md#e-031), [E-026](../../evidence/evidence-ledger.md#e-026), [OI-011](../../controls/open-items.md#oi-011) | High source/test confidence. Live edge stripping, hosted exposure, configured allowlists/limits, and successful poisoning are unknown. Replay behavior is EE-only, not CE Run. | A client that reaches these semantics can fabricate or backdate measurements, bias multiple site reports, and—for the EE replay path—evade the application limiter during a campaign or registration period. | CWE-345 |
| The ingestion controller attaches the complete parsed visitor request to Sentry context, and the configured filter only changes its fingerprint; covered Google OAuth failures separately include complete callback parameters. | High | S | [E-032](../../evidence/evidence-ledger.md#e-032), [E-027](../../evidence/evidence-ledger.md#e-027), [OI-010](../../controls/open-items.md#oi-010), [OI-012](../../controls/open-items.md#oi-012) | High source confidence; Sentry enablement, exception occurrence, SDK scrubbing, actual transmission, retention, and access are unknown. | An application error can expand disclosure of transient IP/User-Agent, URL/query/referrer/properties; OAuth failures can expose a short-lived code and signed state to diagnostics. | CWE-532 |
| Optional alternate-access credentials are weaker than the primary login boundary: shared links have no source-visible password rule or attempt limiter, and API-key creation accepts a client-supplied secret without a strength rule. | Medium | S | [E-033](../../evidence/evidence-ledger.md#e-033), [OI-013](../../controls/open-items.md#oi-013), [OI-008](../../controls/open-items.md#oi-008) | High source confidence. Slug/key inventories, live edge throttling, actual use, and staff practices are unknown; normal API-key UI generation is strong. | A leaked shared-link capability plus a weak password, or a deliberately weakened API key, can reduce protection for analytics exports and dashboards. | CWE-307, CWE-521 |
| Session and API authorization is layered and site/team scoped, but source placement cannot prove complete route coverage or live least privilege. | Low | M | [E-034](../../evidence/evidence-ledger.md#e-034), [E-025](../../evidence/evidence-ledger.md#e-025), [OI-006](../../controls/open-items.md#oi-006), [OI-008](../../controls/open-items.md#oi-008) | High confidence in traced controls; no live identities or exhaustive dynamic authorization matrix were approved. | Treating implemented checks as deployed effectiveness could hide a role, key, link, or route misconfiguration across 18 properties. | ASVS V4 |

## Mandate-Relevant Strengths

- Primary login applies IP/user attempt limits, password verification, optional/forced 2FA flows, session renewal, revocable server-side sessions, and CSRF on browser state changes ([E-034](../../evidence/evidence-ledger.md#e-034)).
- Google OAuth state is signed, limited to one hour, restricted to known contexts, and bound to an existing site; callback handling checks the current user's site permission before token use ([E-034](../../evidence/evidence-ledger.md#e-034)).
- Browser and API paths use site lookup, membership role, shared-link/site binding, team-scoped key matching, explicit scopes, feature availability, and burst/hourly limits ([E-025](../../evidence/evidence-ledger.md#e-025), [E-034](../../evidence/evidence-ledger.md#e-034)).
- Query construction inspected uses Ecto binding/parameterization for representative user-supplied filters and identifiers; no material SQL/template/command injection path was established in the reviewed source. This is bounded, not an exhaustive sink proof.
- Locks, commit-pinned Actions, Dependabot, and digest-producing image workflows reduce build-input uncertainty, while [OI-005](../../controls/open-items.md#oi-005) correctly preserves deployed consumption as unknown ([E-028](../../evidence/evidence-ledger.md#e-028)).

### Decision Insights

1. **Run and Subscribe need different ingestion acceptance proofs.** Run does not compile the EE replay path but still depends on forwarded-header, hostname, rate, and claimed-domain controls. Subscribe adds a source-visible replay-header bypass whose safety depends on an unverified trusted edge/internal-caller boundary. Close [OI-011](../../controls/open-items.md#oi-011) per option before relying on campaign or registration analytics.
2. **Privacy-first storage does not make diagnostics privacy-minimizing.** The request fields excluded from ClickHouse can still be attached to Sentry on errors. Correct [OI-012](../../controls/open-items.md#oi-012) independently of the broader governance choice, and retain [OI-010](../../controls/open-items.md#oi-010) for OAuth callback secrets.
3. **The 25-person access model should avoid optional bearer paths unless needed.** Session/role controls are stronger than weakly configured shared links or client-weakened API secrets. OI-008 should disable unnecessary alternate access; OI-013 should harden any retained path.
4. **Replace is not evidenced as safer.** No alternative source or runtime was approved. Use authenticated privileged ingestion, header trust, diagnostic minimization, credential strength, tenant isolation, and negative authorization tests as replacement-selection criteria.

## Selected Outputs

- [Application attack paths and controls](../../controls/application-security/attack-path-and-control-view.md)

The material authentication, authorization, ingestion, diagnostic, and alternate-access triggers required this view. No dependency/build-input exploitability note was created because the approved evidence did not establish a vulnerable, abandoned, privileged, generated, or build-time input that was materially exploitable; [E-028](../../evidence/evidence-ledger.md#e-028) and [OI-005](../../controls/open-items.md#oi-005) preserve the bounded supply-chain position.

## Material Omissions, Unknowns, And Auditor Questions

No new material auditor question was raised. OI-002 and OI-007 remain unanswered and were not inferred. OI-008 remains a governance decision. Ingress/header rewriting, enabled Sentry/Google integration, hosted replay authorization, effective roles/keys/links, dependency vulnerabilities, and deployed code identity are proof needs routed to OI-001, OI-005, and OI-010–OI-013, not questions the auditor can answer by assertion.

Exact executable boundary: no product command ran because dependency restore/install was prohibited. Working directory was `primary-code:.`. CodeGraph lifecycle and query commands used the resolved source root required by the tool, which is intentionally not persisted; `codegraph status <primary-code-root>` and `codegraph sync <primary-code-root>` passed, and every query used `--path <primary-code-root>`. This navigation check does not compile or test Elixir and is not a security scan.

## Reconciliation

Security and Privacy's OI-010 is confirmed. OI-011 is retained and expanded with same-path evidence for claimed-domain fan-out and the EE replay-header/rate-limit behavior; it remains a verification because effective edge controls are unknown. New OI-012 separates visitor diagnostic minimization from OAuth secrets, and OI-013 addresses optional credential hardening. Security and Privacy's baseline privacy/data-governance ownership and Code Quality's unexecuted/deployed provenance boundaries are preserved. No material source conflict was found; hosted public assertions remain post-cutoff validation only.

## Bounded Conclusion And Downstream Guidance

The reviewed source has substantial authentication, session, API-scope, authorization, and site/team-boundary controls, and no material injection or direct cross-site authorization bypass was established in the traced paths. It does not establish safe live ingestion, privacy-minimizing diagnostics, strong optional shared/API credentials, hosted edge effectiveness, deployed security, or penetration-test coverage. Run remains conditional on CE-specific OI-011 plus OI-010/OI-012/OI-013 as applicable; Subscribe must additionally prove that public clients cannot invoke EE replay semantics. Cloud Security should validate live edge/header/IAM/runtime controls without treating source checks or public claims as effectiveness proof; Maintenance Cost should include these source corrections and recurring negative authorization/ingestion checks.
