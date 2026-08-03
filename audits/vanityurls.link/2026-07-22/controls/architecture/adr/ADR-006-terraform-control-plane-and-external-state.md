# ADR-006: Terraform Control Plane And External State

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

The public `v8s-config` repository declares Terraform as the intended authority for significant Cloudflare controls, while credentials, variable values, state, imports, and live account ownership remain outside the repository.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Terraform defines Access, redirect, WAF, and rate-limit resources with pinned provider constraints. | `v8s-config/main.tf`, `variables.tf`, `outputs.tf`, `versions.tf` | CodeGraph cannot index Terraform here; direct file inspection was used. |
| Runtime/live state | README records incomplete discovery and intended import/reconciliation behavior. | `v8s-config/README.md` | No state, backend, plan, apply, import, or drift evidence was approved. |
| Rationale | Avoid dashboard configuration becoming a second source of truth. | `v8s-config/README.md`; source ADR 0014 | Some platform-only controls intentionally remain external. |
| Approval | The repository is public and described as the demo configuration source of truth. | [E-004](../../../evidence/evidence-ledger.md) | Current account owner and Terraform authority are unknown. |

## Constraints, Options, And Tradeoffs

Infrastructure as code improves reviewability, but a repository without known state custody and import history cannot alone reproduce or safely take over an existing zone. Creating a new account/zone is simpler than inheriting the existing one.

## Impacts And Boundaries

Business Continuity must treat Terraform state, account roles, tokens, and domain authority as first-class handover assets. Security must avoid publishing their sensitive values.

## Change, Reversal, And Follow-Up

Close OI-006 with a redacted backend/state inventory, import coverage, plan-to-live comparison, recovery procedure, and successor dry run under authorized conditions.
