# Product Provenance Notes

## Evidence Boundary

The approved Git clone is shallow and no product-specific GitHub history packet was
needed to establish the current durable contracts. The record set therefore uses
current source/documentation as implementation evidence, the 2026-08-19 audit brief
as Acme authority for the five-minute requirement, and labels rationale/approval
unknown elsewhere. No live or customer-acceptance evidence exists.

## Provenance Chain

| Claim/output | Provenance present | Provenance absent | Correct interpretation |
|---|---|---|---|
| Check state | Persisted check fields, ping events, calculated schedule/grace, flips | Producer clock, job correctness, deployed database durability | Source-backed state calculation only. |
| Duration | Stored start/completion events, timestamp, optional RID, 72-hour pairing cap | Monotonic client timing, complete concurrent-run enforcement | Diagnostic runtime estimate, not an all-run SLO. |
| Exit result | Numeric path segment retained with ping | Meaning of each job's exit code and wrapper correctness | Transported client assertion. |
| Payload/log | Request metadata and bounded body/object reference | Data classification, redaction, full original beyond cap, business-result validity | Diagnostic evidence with privacy/retention risk. |
| Alert | Flip, selected channel, notification row, last error/timing | Provider acceptance-to-human receipt, acknowledgement, escalation ownership | Dispatch evidence, not actionable-human evidence. |
| Hosted capability | Repository documentation using generated site placeholders | Hosted deployment, plan, SLO, controls, feature parity, retention, support | Do not project self-hosted source behavior onto buy. |

## History And Rationale Limit

No material conclusion relies on inferred maintainer intent. The overlapping-run
caveat and monitoring guidance are explicit in repository documentation; most other
rationales remain unknown. A targeted history collection should be added only if a
future fork proposal needs to distinguish deliberate contract from incidental
implementation.

## External Pointers

**Documented outside audited scope; not independently verified.** The PowerShell and
C# pages point to platform HTTP-client documentation, and the logs page points to
Runitor. These sources cannot establish Acme's Windows Task Scheduler procedure or
third-party wrapper suitability. The smallest expansion is a reviewed Acme wrapper
and golden-path execution under [OI-009](../open-items.md#OI-009), not a broad ecosystem scan.
