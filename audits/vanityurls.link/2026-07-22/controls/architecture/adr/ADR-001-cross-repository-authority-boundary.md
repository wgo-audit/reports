# ADR-001: Cross-Repository Authority Boundary

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

vanityURLs separates upstream product source (`code`), a public reference instance (`v8s-link`), its Cloudflare control-plane intent (`v8s-config`), and website/documentation (`website`) into four repositories.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Each repository contains a distinct source-of-truth declaration and artifact set. | [E-001/E-004](../../../evidence/evidence-ledger.md); repository READMEs | Does not identify all live integrations. |
| Runtime/live state | `v8s-link` declares the custom-domain Worker and `v8s-config` declares edge controls. | Wrangler and Terraform files | Deployment and drift are unknown. |
| Rationale | The separation isolates reusable product defaults from instance choices and public documentation. | `docs/README.md`; source ADRs 0002, 0004, 0009, 0014 | No single cross-repository rationale record existed. |
| Approval | Product ADRs document several boundaries as accepted; repository creation/history is public. | `docs/adr/`; [GitHub packet](../../../evidence/packets/github-history-and-hosted-ci.md) | Organization-wide approval and current owners are unknown. |

## Constraints, Options, And Tradeoffs

Separation reduces accidental coupling between product releases and instance-owned changes, but every release, documentation, infrastructure, and demo change now crosses distinct histories and owners. A monorepository could centralize controls but would weaken deliberate instance detachment.

## Impacts And Boundaries

A successor needs a repository map, authority in all four repositories, and the external GitHub/Cloudflare/domain relationships. Public source is sufficient to fork each component; it is not sufficient to inherit the existing assets.

## Change, Reversal, And Follow-Up

Keep the split unless maintainers explicitly decide otherwise. Close OI-001 and OI-002 with a cross-repository ownership, administrator, transfer, and recovery inventory plus a successor exercise.
