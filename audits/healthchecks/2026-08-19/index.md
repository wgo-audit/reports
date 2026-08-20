# Audit Index

## Start Here

Start with the [Executive Summary](executive-summary.md). Its decision is
conditional: pursue **buy first as a bounded acceptance track**, retain **pull as
the fallback and exit path**, and keep **make stopped** unless testing proves a
narrow source-level need. No option is approved for core production use yet.

Canonical evidence and unresolved work remain in the [evidence ledger](evidence/evidence-ledger.md)
and [open-items register](controls/open-items.md). The evidence cutoff is
2026-08-19.

The required API-equivalent audit cost closeout is [Final](controls/cost-estimate.md):
all 31 audit descendants and the root reconcile to an exact machine-readable
estimate of `$103.0189036` (`$103.02` displayed).

## Audience Routes

| Reader | Route | Purpose |
|---|---|---|
| CEO / CTO | [Executive Summary](executive-summary.md) | Recommendation, decision gates, major risks, and 30–90 day plan |
| Product / service owner | [Product Manager Notes](product-manager-notes.md) | Capability, onboarding, promise, and sign-off boundaries |
| Technical / platform lead | [Technical Lead Notes](technical-lead-notes.md) | Architecture, alert path, recovery, security, capacity, quality, and safe evolution |
| Specialist reviewer | [Reviewer reports](reviewer-reports/) | Eleven detailed, quality-reviewed assessments and handoffs |
| Evidence reviewer | [Evidence ledger](evidence/evidence-ledger.md), [source-access register](evidence/source-access-register.md), and [packets](evidence/packets/) | Source provenance, access limits, and reusable observations |
| Decision owner | [Open items](controls/open-items.md) | Canonical decisions, verification, and implementation corrections |

## Evidence Boundary

This was a source- and public-evidence audit, not a deployment assessment. It
used Healthchecks commit `fafac59eeb00cfdc87166242544fa071ecad1723`, repository
history and hosted CI, public Healthchecks.io documentation, and the approved
Acme context. It did not inspect Acme infrastructure, job definitions, team
ability, contracts, production metrics, or hosted internals; it did not deploy
or load-test any option. Missing evidence is recorded as unknown or as a
production gate, never as reassurance.
