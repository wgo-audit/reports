# PDR-005: Alert Routing And Five-Minute Budget

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Healthchecks routes Down/Up flips to selected enabled project channels and records
delivery errors/timing. Acme separately requires actionable human receipt within 300
seconds of missed expected completion; the source does not establish that outcome.

For the acceptance test, `T0` is the first instant a critical job is late against its
Acme-approved expected-completion schedule. `T1` is the first instant a responsible
human receives enough job identity, failure context, and response routing to act.
Every selected option must pass required fault cases with `T1 - T0 <= 300 seconds`
and no silently lost alert.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Multiple channels and redundancy are documented; state flips trigger eligible channels. | [E-017](../../../evidence/evidence-ledger.md#E-017) | Provider/human receipt unproven. |
| Implementation | Channels for a flip are sequential; failures are recorded; HTTP transports can retry. | [E-003](../../../evidence/evidence-ledger.md#E-003), [E-017](../../../evidence/evidence-ledger.md#E-017) | Processed-before-delivery creates silent-loss risk. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#OI-006) | No live or fault test. |
| Approval/specialist sign-off | Acme approved T1−T0 ≤300 seconds with actionable identity, context, and response route. | [audit brief](../../../audit-brief.md), [OI-006](../../open-items.md#OI-006) | Concrete channels/responders unknown. |

## Constraints, Options, And Tradeoffs

Grace, polling, queueing, channel attempts, provider transit, and escalation all share
the 300-second budget. More channels add redundancy but sequential attempts can add delay.

## Impacts And Boundaries

Pull and make both need Acme-operated delivery proof. Buy may transfer service operation
but still needs hosted evidence and Acme-controlled human receipt testing.

## Change, Reversal, And Follow-Up

Close [OI-006](../../open-items.md#OI-006) for every viable option. Do not fork until
fault evidence shows an unfixable source-level deficit; otherwise use resilient topology,
independent watchdog, and provider diversity.
