# Rules And Output Semantics

## Evidence Boundary

Rules below are confirmed only for `HC-CODE-001` at the pinned commit. No live
configuration or demonstration exists. Evidence: [E-014](../../evidence/evidence-ledger.md#E-014),
[E-015](../../evidence/evidence-ledger.md#E-015), [E-016](../../evidence/evidence-ledger.md#E-016),
[E-017](../../evidence/evidence-ledger.md#E-017), and [E-018](../../evidence/evidence-ledger.md#E-018).

| Rule/output | Source-bounded meaning | Material edge | Decision consequence |
|---|---|---|---|
| New | No ping has established normal state. | It is not a protected/healthy assertion. | Provisioning alone cannot satisfy acceptance. |
| Up | Latest success arrived before the applicable boundary, or a failure recovered. | A success signal proves request receipt, not business-result correctness. | Critical clients need a business-outcome assertion before signaling success. |
| Late | Expected success boundary passed, but grace remains. | No Down alert is yet eligible. | Grace must leave enough of the 300-second budget for delivery/escalation. |
| Down | Grace elapsed or an explicit failure arrived. | Worker/provider/human delivery is a separate path. | Down state is not proof of actionable human receipt. |
| Paused | Monitoring is intentionally suppressed. | Sticky pause ignores incoming pings until explicit resume. | Pause state needs expiry/review in acceptance controls. |
| Start | Sets the current start timestamp/run ID. | Latest start controls the check-level overrun timer. | Concurrent runs need an explicit policy; RID does not provide all-run timeout alerting. |
| Success | Base endpoint or exit 0; may clear a prior start. | Wrongly placed or unconditional success creates false assurance. | Wrapper design is part of the monitor contract. |
| Failure | `/fail`, nonzero exit, or matching failure keyword. | Fail transitions Down immediately, reducing detection delay. | Prefer explicit failure where clients can guarantee error propagation. |
| Ignored | Method/filter/sticky-pause rule accepted the request but did not change state. | HTTP 200 can accompany an ignored event. | Client acceptance cannot rely on response status alone. |
| Log | Event and body are recorded without state change. | It cannot protect a job by itself. | Treat as diagnostic context only. |
| Duration | Gap between correlated start and completion under 72 hours. | Display correlation and alert monitoring have different overlap semantics. | Do not infer every concurrent execution is protected from a displayed duration. |
| Notification | Down/up flip delivered through selected enabled channels. | Channels are sequential for a flip; retries and quotas consume time or suppress delivery. | OI-006 must measure human receipt under failure and burst. |

## Five-Minute Budget Rule

For critical jobs, `grace + detection/polling + queue + channel attempts + provider
delivery + escalation` must fit within 300 seconds from the approved expected-
completion instant. The repository supports grace as low as 60 seconds, so the
configuration is mechanically capable of reserving delivery time, but no source
proves the complete inequality in operation. Exact closure remains [OI-006](../open-items.md#OI-006).
