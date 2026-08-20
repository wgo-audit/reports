# Claim Governance

## Evidence Boundary

This control governs how Acme may describe Healthchecks before and after option
selection. It uses [E-051](../../evidence/evidence-ledger.md#E-051),
[E-052](../../evidence/evidence-ledger.md#E-052), and
[E-053](../../evidence/evidence-ledger.md#E-053), plus the already registered
capability and continuity evidence. No Acme sales material, contract, demo,
production configuration, customer commitment, or human-receipt observation was
approved. Public product language is not an Acme promise or operational proof.

## Evidence Dimensions Used

| Dimension | Present evidence | Material limit |
|---|---|
| Implementation | Pinned source implements ping intake, state transitions, alert workers, and transport calls. | Does not prove deployed behavior, provider delivery, or human action. |
| Product documentation | Documentation describes monitoring, alerts, onboarding, retries, grace, and redundant channels. | Generic guidance is not an Acme job contract, service level, or completed onboarding. |
| Observed operation | unknown | No safe demo fixture or live option was approved; OI-006/OI-009 own observation. |
| Ownership/approval | unknown | No claim owner, approval record, or customer-communications owner was supplied. |
| Commercial/contract | Public hosted terms only through E-036/E-037. | No Acme agreement, claim, customer commitment, remedy, or liability evidence. |

## Claim Boundary

| Claim area | Evidence-supported wording now | Wording not supported now | Proof required to expand the claim | Route |
|---|---|---|---|---|
| Product function | “Healthchecks implements passive schedule/failure monitoring and invokes configured notification integrations.” | “Healthchecks reliably protects our important jobs.” | Critical-job outcome contracts and production-shaped failure tests. | OI-006, OI-009 |
| Alert timing | “A configured grace period determines when a check becomes Down and alert processing starts.” | “A responsible human will always know within five minutes.” | T0/T1 evidence for every required fault case and independent escalation. | OI-006 |
| Delivery status | “The application recorded that its transport call returned without an application-level error.” | “Delivered to,” “seen by,” or “acknowledged by” a responsible human. | Provider receipt plus human acknowledgement/escalation evidence. | OI-006, OI-020 |
| Job outcome | “A success, failure, start, exit-status, or missing signal was recorded under the configured monitor contract.” | “The customer/business outcome completed correctly.” | A job-specific business-outcome assertion independent of the heartbeat call. | OI-009, OI-021 |
| Continuity | “Acme has set a 30-minute monitoring-service RTO target and a 5-minute RPO target.” | “The monitoring service meets 30-minute recovery” or “alerts remain available during recovery.” | Measured recovery and independent-alert-path exercises. | OI-006, OI-007, OI-013 |
| Hosted service | “Healthchecks.io publishes the listed plan, public terms, and status view observed at cutoff.” | “The hosted service is SLA-backed, highly available, secure, or contractually guaranteed for Acme.” | Vendor/security review, negotiated commitments if required, live tests, and exit proof. | OI-004, OI-012 |
| Demo/readiness | “No safe golden-path demo was run in this audit.” | “Demo-ready,” “production-ready,” or “customer-ready.” | Approved non-production fixture, scripted success/failure cases, and retained observation. | OI-006, OI-009 |

## Approval And Correction Control

Before Acme uses a material claim in an executive decision, operating policy,
demo, onboarding guide, sales statement, or customer communication, record:

1. the exact wording and audience;
2. its option, configuration, job class, and time boundary;
3. the direct evidence and most recent validation date;
4. the accountable claim owner and approver; and
5. the correction/notification path if an incident disproves it.

Claims must fall back to the evidence-supported wording when proof expires,
configuration changes, the selected option changes, or a material delivery or
recovery test fails. [OI-020](../open-items.md#OI-020) owns implementation.

## Material Unknowns And Closure Routes

- Existing Acme internal or customer-facing claims are unknown; inspect only
  approved claim-bearing records if the CTO expands scope.
- Customer commitments and contractual language are unknown; do not infer them.
- No demo-readiness artifact was produced because no safe demo identity or fixture
  was approved. A future approved observation would route through OI-006/OI-009.
