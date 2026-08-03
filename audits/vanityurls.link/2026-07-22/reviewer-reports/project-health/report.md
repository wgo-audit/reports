# Project Health

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether a small community team can understand, prioritize, review, accept, release, and learn from work across all four repositories. It uses public Git/GitHub history, PR/issues/releases, the latest-100 cutoff-filtered Actions samples, governance files, declared commands/workflows, Architecture and Product Value handoffs, and public documentation through July 22, 2026. No private planning, authenticated rules, local checks, deployment, runtime acceptance, maintainer interview, or staffing commitment was available.

## Coverage And Material Gaps

The review covers work visibility, review/acceptance, release/change control, cadence evidence, cross-repository consistency, and learning/recovery records. `code` has a substantial public delivery record and detailed release procedure. `website` has substantial history but lacks a hosted quality gate. The two operational repositories have almost no public change-control history. Public Projects evidence is post-cutoff and cannot establish cutoff prioritization. Actual review requirements, bypasses, administrator ownership, and deployment acceptance remain unknown.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| `code` demonstrates sustained public maintenance: 75 PRs, 38 releases, a broad declared check, and exact successful hosted runs. | [GitHub packet](../../evidence/packets/github-history-and-hosted-ci.md), [delivery packet](../../evidence/packets/delivery-and-quality.md), [release view](../../controls/project-health/release-change-control.md) | High for counts/declarations; latest-100 sample and selected review evidence do not establish population-wide rigor. | A new maintainer can study a real delivery history rather than an abandoned code dump. |
| Desired PR, CODEOWNERS, signed-commit/tag, and required-check rules are documented but explicitly require administrative application; public enforcement is unreadable. | [E-013](../../evidence/evidence-ledger.md), repository-rules files | High for intended controls; actual settings unknown. | Process documentation cannot guarantee that a successor will inherit the same safeguards or authority. |
| `website` is actively changed and released, but its hosted workflows do not run declared build/test/lint/link checks; dependency resolution is unlocked and manifest versions diverge. | [E-012](../../evidence/evidence-ledger.md), [release view](../../controls/project-health/release-change-control.md) | High for source/hosted facts; no build was executed. | Documentation—the primary operator source of truth—can change without publicly evidenced quality acceptance. |
| `v8s-config` and `v8s-link` expose no public PR, issue, Actions, or release history and have three and one commits respectively. | [E-010](../../evidence/evidence-ledger.md) | High for public surfaces/history; private/external work unknown. | The most operationally sensitive repositories provide the least evidence of review, learning, and successor-ready change control. |
| Governance is inconsistent across repositories and contribution guidance contains an obsolete issue URL. | [documentation packet](../../evidence/packets/documentation-alignment.md), [vendor packet](../../evidence/packets/vendor-ownership-commercial.md) | High for public files; actual role practice unknown. | Prospective contributors cannot derive one authoritative path from issue to maintainer role across the whole project. |

### Decision Insights

- **Prioritize operational-repository change control over increasing product release cadence.** The product already has substantial release history; harmful continuity risk is concentrated in `v8s-config` and `v8s-link`, where public review/CI/history is absent. Smallest action: OI-007.
- **Treat the website as a production dependency for onboarding.** It is the declared source of truth, yet lacks a hosted package quality gate and locked npm resolution. A broken or drifting docs build directly harms third-party operation. Smallest action: OI-008.
- **Do not use release counts as a health proxy.** They demonstrate activity, not independent review, deployment acceptance, or recoverability. Smallest proof: OI-002/OI-004, including successor-controlled release and rollback.

## Selected Outputs

The material cross-repository delivery boundary triggered [release and change-control position](../../controls/project-health/release-change-control.md), which compares all four repositories and traces the declared product release path.

## Material Omissions, Unknowns, And Stakeholder Questions

- Actual GitHub branch/tag rules, administrator bypass, required reviewers/checks, and release authority: OI-002.
- Cutoff roadmap priorities and work ownership: the public organization Project was observed only after cutoff and its history/membership were not established.
- Whether operational repository changes are reviewed/tested elsewhere: no public evidence; OI-007.
- Whether the published docs build and link corpus pass reproducibly: no approved execution; OI-008 and later Code Quality review.

## Reconciliation

High commit/release volume in `code` and `website` was reconciled with sparse public review examples and absent enforcement evidence: the conclusion is **active public delivery**, not **proven healthy governance**. Repository-specific Projects pages supplied no cutoff evidence; a public organization roadmap observed after cutoff is recorded only as post-cutoff visibility, not historical prioritization. The `website` workflow successes were reconciled as release/reminder automation, not package quality gates.

## Bounded Conclusion And Downstream Guidance

The project is visibly active and the product release process is much stronger than its size suggests. Project health is uneven: operational repositories, documentation quality gating, enforceable governance, and successor authority are not strong enough to support low-risk sudden handover. Code Quality should use declared-versus-executed check evidence; Business Continuity and Contributor/Vendor Value should use cross-repository concentration and authority gaps. They must not infer staffing, review rigor, deployment success, or roadmap approval from commits/releases alone.
