# PDR-005: Destination Policy And Blocking

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

vanityURLs validates link destinations and compiles a runtime blocklist from either product defaults or an instance-owned replacement policy; narrow allow rules may override domain blocks but not malformed, unsafe-scheme, or credentialed URLs.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Operators can review/customize trust-and-safety policy and validate links before deployment. | Blocklist customization/reference docs | No abuse outcome or false-positive data. |
| Implementation | Policy libraries, generator, target checker, build, and Worker scanner handling exist. | `scripts/blocklist-policy.mjs`; `generate-blocklist.mjs`; `check-targets.mjs`; Worker source | Checks were not run. |
| Runtime/demonstration | Instance includes a selected policy/runtime source. | `v8s-link/defaults/` and `custom/` | Effective live WAF/runtime policy unknown. |
| Approval/specialist sign-off | Source ADR 0003 records full custom replacement behavior. | `docs/adr/0003-*` | No trust-and-safety specialist approval. |

## Constraints, Options, And Tradeoffs

Full replacement makes local policy authority explicit but can discard upstream decisions. Allow lists create reputation risk if overbroad; generated feeds can drift.

## Impacts And Boundaries

Policy is product value and community trust, not only a code check. Security assesses bypass/exposure; operators must own review cadence and incident decisions.

## Change, Reversal, And Follow-Up

Require reviewable policy diffs and an identified policy owner. Specialist sign-off is needed before claims of abuse prevention or safety effectiveness.
