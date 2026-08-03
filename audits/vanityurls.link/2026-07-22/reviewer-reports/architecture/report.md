# Architecture

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether the technical boundary and material decisions are understood well enough for a new maintainer or third party to evolve and operate vanityURLs. Evidence is bounded to the four public repositories pinned in [E-001](../../evidence/evidence-ledger.md), public GitHub history through July 22, 2026, and approved public documentation. CodeGraph preflight was used for code navigation, with direct source/configuration inspection for completeness; it returned only narrow symbol context and could not index Terraform. No build, deployment, authenticated setting, live request, log, plan/apply, or recovery exercise was approved.

## Coverage And Material Gaps

The review covered repository/component boundaries, source and generated artifacts, runtime/data flow, delivery/release, edge trust controls, identity/secrets, infrastructure state, recovery, dependencies, and capacity/cost boundaries. The source architecture is unusually well documented for a small OSS project, but the existing service’s external control plane is not publicly reconstructible: owners, repository rules, Cloudflare/registrar authority, Terraform state, secrets, deployment connections, alerting, and recovery evidence remain unknown. These are routed through [OI-001, OI-002, and OI-006](../../controls/open-items.md).

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| The code/data architecture is portable: human-authored Git configuration is transformed into a read-only Worker registry and static assets, with no application database or authenticated edit API. | [ADR-002](../../controls/architecture/adr/ADR-002-source-ownership-and-generated-artifacts.md), [ADR-003](../../controls/architecture/adr/ADR-003-cloudflare-worker-runtime.md), [E-004](../../evidence/evidence-ledger.md) | High for implementation and documented intent; no clean build or live request observed. | A third party can understand and recreate the core software on independently controlled infrastructure with relatively little hidden application state. |
| Product, instance, infrastructure, and documentation authority are split across four repositories, but only the product and website have material public change/release histories. | [ADR-001](../../controls/architecture/adr/ADR-001-cross-repository-authority-boundary.md), [GitHub packet](../../evidence/packets/github-history-and-hosted-ci.md), [cross-repository diagram](../../controls/architecture/diagrams/cross-repository-control-boundary.md) | High for public source/history; private/external coordination unknown. | Safe takeover requires a cross-repository map and control transfer. Public evidence is weakest exactly where live instance and infrastructure changes occur. |
| The release design combines broad checks, automated preparation, and human-signed tags, but actual rule enforcement, signer recovery, and external deployment are unproved. | [ADR-005](../../controls/architecture/adr/ADR-005-release-and-delivery-trust-chain.md), [delivery packet](../../evidence/packets/delivery-and-quality.md) | High for declarations and selected hosted records; low for enforcement and deployment. | A successor can reproduce a release process, but cannot be assumed able to preserve the existing project’s trusted release lineage. |
| Terraform makes significant demo-instance edge controls reviewable, yet state/backend/import coverage and account authority are external and unknown. | [ADR-006](../../controls/architecture/adr/ADR-006-terraform-control-plane-and-external-state.md), [recovery packet](../../evidence/packets/recovery-and-operations.md) | High for declared resources; no plan, apply, state, or drift evidence. | The repository can guide a new deployment; it cannot by itself support safe takeover or recovery of the existing Cloudflare environment. |
| Cloudflare and GitHub absorb runtime scaling and delivery concerns, but no public workload, quota, SLO, alert, failover, cost, or recovery proof bounds the operational envelope. | [ADR-004](../../controls/architecture/adr/ADR-004-layered-edge-and-operational-access-controls.md), [ADR-007](../../controls/architecture/adr/ADR-007-git-backed-instance-data-and-recovery-boundary.md), [vendor packet](../../evidence/packets/vendor-ownership-commercial.md) | Source-bounded only; live and commercial evidence excluded. | The design is simple, but simplicity must not be mistaken for proven resilience or transfer readiness. |

### Decision Insights

- **Decide whether “third-party operable” means a new independent instance or continuity of the existing project/domain.** Git-backed source makes the first plausible, while external account/domain/release authority blocks proof of the second. Treating them as one decision would overstate readiness and expose community trust. Smallest action: approve the distinction in OI-001 and define transfer scope.
- **Prioritize control-plane recovery before deeper product refactoring.** The core runtime has little mutable state, while the unproved failure path sits in GitHub/Cloudflare/registrar/Terraform authority. Refactoring code first would not remove the harmful failure in the brief. Smallest proof: complete OI-002/OI-006 and run a successor exercise.

## Selected Outputs

- Required [ADR candidate inventory](../../controls/architecture/adr-candidate-inventory.md) and [ADR register](../../controls/architecture/adr-register.md), with seven material records.
- Triggered [cross-repository control boundary](../../controls/architecture/diagrams/cross-repository-control-boundary.md) and [build, deploy, and request path](../../controls/architecture/diagrams/build-deploy-request-path.md).
- The live-evidence-only DevOps infrastructure view and named deployment/runtime path were not triggered because authenticated live environment, deployment artifact, and runtime evidence were outside the approved boundary. Their material unknown edges are shown in the two source-bounded diagrams instead.

An ephemeral artifact-quality review found the two diagrams decision-useful because they separate repository portability from external control and show the unobserved deployment/alerting handoffs; labels were tightened to prevent solid source/configuration edges from being read as live proof.

## Material Omissions, Unknowns, And Stakeholder Questions

- Who can currently administer and recover each GitHub repository/organization, protected branch/tag, release signer, Cloudflare account/zone/Worker/Access configuration, Terraform state, domain registration, and public contact? See OI-002/OI-006.
- Does the community intend successor continuity under the same repositories/domain/trust root, or only license-based forkability? See OI-001.
- Can a non-creator rebuild, release, deploy, observe, roll back, and recover a representative instance using only the documented handover packet? See OI-004.

## Reconciliation

Source documentation says Terraform should own represented Cloudflare controls, while the same README records incomplete discovery and missing Access permission. This was reconciled as **intended authority, not verified live authority**. Repository rule documents similarly describe desired settings and explicitly say administrative application is required; they are not treated as enforcement proof. Public organization Projects became visible only in a post-cutoff observation, so it is not used as cutoff architecture approval evidence.

## Bounded Conclusion And Downstream Guidance

The architecture is understandable, low-state, source-controlled, and technically forkable. It is not yet evidenced as transferable or independently operable under the existing project identity and domain because the decisive external control, state, and recovery boundaries remain unproved. Product Value may use the runtime/configuration path as implemented behavior; Security, Scalability, Business Continuity, and Maintenance Cost may use the boundary diagrams, but none may assume live deployment, effective controls, recoverability, owner availability, or cost from source presence.
