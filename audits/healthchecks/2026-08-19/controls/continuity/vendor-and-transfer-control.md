# Vendor And Transfer Control

## Purpose And Boundary

This view separates product portability from operating continuity. It uses
[E-026](../../evidence/evidence-ledger.md#E-026),
[E-029](../../evidence/evidence-ledger.md#E-029), and
[E-030](../../evidence/evidence-ledger.md#E-030). Public vendor pages are
declarations and a current snapshot, not contractual or historical
availability proof.

## Pull / Make / Buy Transfer Position

| Scenario | Control retained by Acme | External dependency | Transfer or exit strength | Stop condition |
|---|---|---|---|---|
| Pull | Source pin, deployment, data, accounts, notification configuration, release timing | Upstream source/releases, infrastructure and notification providers | BSD-3-Clause permits continued operation and modification; a database backup can preserve application state if proven restorable. | Do not approve until OI-005..OI-013 close for the selected design. |
| Make | All pull controls plus fork repository, merge policy, build, security patches, and release support | Upstream changes plus every pull dependency | Maximum code autonomy, but Acme becomes the successor maintainer and must prove its rebuild/merge/release capacity. | Do not fork until a source-level need survives pull controls and ownership is accepted. |
| Buy | Job-side instrumentation, account/billing, memberships, integration destinations, data minimization, independent watchdog, and exit copy | Healthchecks.io runtime, vendor staff, subprocessors, terms, and support | API can enumerate checks, ping history/status changes, and integration identities; it does not document a full-fidelity export/import or credential-preserving failover. | Do not approve on public status/terms alone; close OI-004, OI-006, OI-011..OI-013. |

## Hosted Evidence And Exit Minimum

The public status page separates Ping API, Notification Sender, Email Delivery,
and Dashboard and publishes current queue/throughput metrics. This is useful
visibility, but it is vendor-controlled and only a snapshot. Standard terms
disclaim uninterrupted or secure availability, and no Acme-negotiated SLA,
support escalation, incident evidence, recovery objective, or exit assistance
was approved.

Before buy approval, Acme needs:

1. Contract/security evidence through [OI-004](../open-items.md#OI-004).
2. A regularly tested, Acme-controlled copy of monitor definitions and routing
   metadata that does not store vendor secrets in audit artifacts.
3. A rehearsed replacement procedure, including new ping capabilities and
   producer cutover, because vendor UUID URLs are bearer capabilities.
4. Independent detection that does not depend on the hosted Ping API,
   Notification Sender, or the same downstream provider.
5. Named billing/account deputies and an explicit nonpayment or vendor-exit
   trigger under [OI-012](../open-items.md#OI-012).

Detailed maintainer concentration and commercial value remain owned by
Contributor and Vendor Value; expense commitments remain owned by Expense
Exposure.
