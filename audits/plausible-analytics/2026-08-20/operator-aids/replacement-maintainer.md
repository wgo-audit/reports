# Replacement Maintainer Transition Guide

- Status: untested
- Selected precursor: [time-to-safety and care envelope](../controls/maintenance/time-to-safety-and-care-envelope.md), [ownership and successor map](../controls/contributors/ownership-successor-and-vendor-dependency-map.md), and [OI-015/OI-020](../controls/open-items.md#oi-015)

## Purpose And Evidence Boundary

Operator question: Can a named successor safely assume the library's retained Plausible duties without relying on one person's memory?

This guide covers both the Run and Subscribe paths because the successor duties differ. It does not select an option, confer access, approve staffing, or prove that one maintainer is sufficient. No library account, deployment, staff capability, contract, support case, or handoff was inspected, and this procedure has not been executed. The planning assumptions remain 18 sites, 25 dashboard users, and a synthetic non-production search/registration fixture; all require validation.

## Existing Runbook And Coverage

No applicable library production-maintainer or handoff runbook was found in the approved documentation catalog or source. The repository's `primary-code:CONTRIBUTING.md:1-63` is the primary development setup procedure and covers local PostgreSQL/ClickHouse, dependencies, migrations, assets, tracker builds, seed data, and a local server. `primary-code:README.md:84-123` assigns CE operating responsibility and describes the hosted/CE support split. `primary-code:SECURITY.md:1-13` defines the latest-major.minor patch boundary. These sources do not cover the library's deployment, ownership, recovery, hosted administration, or successor acceptance, so this guide supplies only that missing transition layer.

## Authority And Preconditions

The Director of Digital Services must name the primary and successor. Library IT/operations must authorize any Run access; procurement or the SaaS account owner must authorize Subscribe access. Privacy/records and security authorities must approve the information visible to the successor.

Before starting:

1. Record the selected option and scope. If no option is selected, perform separate, clearly labelled Run and Subscribe walkthroughs.
2. Use [OI-015](../controls/open-items.md#oi-015) to assign primary and successor owners by control domain. Do not store secret values in the matrix.
3. For Run, obtain the redacted inventory required by [OI-001](../controls/open-items.md#oi-001), the exact tag/digest and provenance route in [OI-005](../controls/open-items.md#oi-005), and the recovery boundaries in [OI-004](../controls/open-items.md#oi-004).
4. For Subscribe, obtain the accepted team/site/member topology, account/admin/billing/support owners, current quote/terms, assurance locators, escalation path, and export/exit boundary under [OI-015](../controls/open-items.md#oi-015) and [OI-017](../controls/open-items.md#oi-017).
5. Approve a non-production support route, test identities, fixture, time box, and evidence location. The successor must not inspect live visitor traffic.
6. Mark the accepted loss/outage tolerance, journey requirement, and analytics governance contract as `UNKNOWN` until [OI-002](../controls/open-items.md#oi-002), [OI-007](../controls/open-items.md#oi-007), and [OI-008](../controls/open-items.md#oi-008) are decided.

## Procedure And Stop Conditions

1. **Orient to the service outcome.** The primary explains which search and registration decisions the monthly outputs support, the 18-site/25-user assumptions, the data minimization boundary, and what must remain available during seasonal peaks. The successor restates the outcome and identifies every unresolved acceptance decision.
2. **Trace control and ownership.** The successor locates the current responsibility matrix, approved data/access rules, service calendar, incident/escalation contacts, and evidence store. Each control domain must have a primary and successor; a vendor name alone is not an owner.
3. **Demonstrate the option-specific path without changing it.**
   - Run: locate the deployed digest, redacted topology, configuration sources, PostgreSQL and ClickHouse boundaries, queues, health/telemetry surfaces, backups, migration controls, registry, DNS/edge, and external integrations. Map the digest to reviewed source and applicable green evidence.
   - Subscribe: locate team/site membership administration, MFA policy, usage/quota reporting, monthly outputs, assurance/terms, billing/renewal, support escalation, and export/termination controls.
4. **Use the approved synthetic fixture.** In the authorized non-production route only, the successor follows the linked [functional acceptance route](../controls/open-items.md#oi-006) to explain how a test search/registration event would be reconciled across goals, dashboard, CSV/API, email, and roles. Execution requires separate authorization; this document does not grant it.
5. **Walk through change and recovery gates.** The successor identifies the conditions that permit or stop an upgrade, restart, restore, role change, credential change, or vendor escalation. For Run, cross-link the [recovery guide](recovery.md); for access, cross-link the [IAM and credential guide](iam-and-credential-control.md).
6. **Time and assess the handoff.** Record elapsed and active time once by activity, assistance needed, unresolved dependency, and whether the successor could locate—not execute—each control. Compare the outcome with [OI-020](../controls/open-items.md#oi-020); do not convert the provisional care bands into measured staffing or cash.

Stop immediately if authority or option scope is unclear; the only usable owner would be removed or locked out; a secret, recovery code, personal identifier, live visitor payload, or sensitive contract term would enter the audit; the successor is asked to deploy, restore, rotate, buy, or modify a system; or the exact environment/digest cannot be distinguished from the assessed source. Record the blocker and escalate instead of improvising.

## Expected Evidence And Records

Retain a dated, access-controlled handoff record containing the option, participants and accountable authorities by role, time box, redacted control-domain matrix, source/artifact/version locators, non-production fixture identifier, tasks located, assistance required, stop conditions encountered, and remaining `UNKNOWN` items. Record no credentials or visitor data.

The handoff supports closing [OI-020](../controls/open-items.md#oi-020) only when a named successor completes every authorized option-specific task within the approved service/recovery window using current documentation. A walkthrough, source read, or account invitation alone is not successful transfer evidence.

## Escalation, Recovery, And Unknowns

Escalate missing Run topology/provenance to Library IT under OI-001/OI-005; missing recovery proof to IT/continuity under OI-004; missing hosted account, assurance, support, billing, or exit evidence to procurement under OI-015/OI-017; and data/access questions to privacy/records and security under OI-008. If the successor cannot complete the bounded handoff, retain the current owner, narrow the option, improve the source-linked documentation, and repeat only after the blocker is resolved.

The present owner roster, staff skill coverage, service window, non-production environment, test identities, accepted thresholds, hosted contract, and recovery evidence are all `UNKNOWN`.
