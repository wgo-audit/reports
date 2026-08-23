# Observability And Response Transition Aid

- Status: untested
- Selected precursor: [Observability And Response Path](../controls/business-continuity/diagrams/observability-and-response-path.md), [Recovery And Operations Packet](../evidence/packets/recovery-and-operations.md), [Business Continuity Report](../reviewer-reports/business-continuity/report.md), and [OI-012](../controls/open-items.md)

## Purpose And Evidence Boundary

This aid answers one operator question: **how should a successor detect, route, triage, and evidence a vanityURLs interruption or abuse event when signals span GitHub, Cloudflare, the domain, and public contacts?**

Source and documentation identify observation surfaces, but no public evidence establishes active monitors, alert rules, recipients, acknowledgement, on-call rotation, severity thresholds, escalation timing, status communications, retention, renewal alerts, or a completed exercise. Those details are **UNKNOWN**.

No monitor, alert, probe, contact, or incident workflow was configured or tested during the audit. Optional Umami/Fathom analytics is not required for service continuity and should remain disabled unless separately governed.

## Existing Runbook And Coverage

No existing document provides an end-to-end observability and incident-response runbook.

Use these partial sources:

- [Reading the admin dashboard](../documentation/tmp/website/content/blog/reading-your-admin-dashboard.en.md) is the primary procedure for inspecting deployed route count, lifecycle state, metadata quality, expiry, and registry timestamp. It is a read-only routing view, not an alert system.
- [Analytics reference](../documentation/tmp/website/content/docs/reference/analytics.en.md) identifies Cloudflare Security Events, Workers analytics, DNS Analytics, and optional provider events. It explains that traffic blocked before the Worker is absent from Worker/provider analytics.
- [Network protection](../documentation/tmp/website/content/docs/customize/network-protection.en.md) is the primary edge-control inspection procedure.
- [Access control](../documentation/tmp/website/content/docs/customize/access-control.en.md) and [Cloudflare Access operations](../documentation/tmp/website/content/blog/operating-cloudflare-access-for-a-short-link-domain.en.md) identify Access tests and logs.
- The deployment checklist at `product-code:RELEASE_WORKFLOW.md` requires deployment-log observation, custom-domain checks, first-request Worker logs, smoke checks, and incident recording.
- `product-code:.github/SECURITY.md` publishes one security-reporting route, but monitoring, backup recipient, response objective, and offboarding are not evidenced.

This aid connects those surfaces to ownership, routing, and evidence without duplicating their inspection steps.

## Authority And Preconditions

Before enabling or changing monitoring, establish:

| Precondition | Required state | Current evidence |
|---|---|---|
| Accountable operations owner | Can approve monitors, incidents, and communications | **UNKNOWN** |
| Backup responder | Independent recipient with sufficient authority | **UNKNOWN** |
| Monitored service scope | Canonical `v8s.link`, independent instance, website, or all | **UNKNOWN** |
| Provider/account scope | Correct GitHub, Cloudflare, registrar, DNS, deployment, and optional analytics accounts | Names known; current accounts/owners **UNKNOWN** |
| Alert destinations | Two independent, recoverable routes without exposing personal data in this packet | **UNKNOWN** |
| Severity model | Impact classes and numeric/time thresholds | Draft classes below; thresholds **UNKNOWN** |
| Acknowledgement/escalation objective | Time allowed before escalation | **UNKNOWN** |
| Public communication authority | Person and channel allowed to publish incident updates | **UNKNOWN** |
| Evidence retention | Redacted log/incident record location and retention period | **UNKNOWN** |
| Renewal ownership | Domain/certificate/provider renewal recipient and backup | **UNKNOWN** |
| Privacy boundary | Approved fields, recipients, access, retention, and deletion for any analytics/log export | **UNKNOWN** |

Use the [IAM And Credential Control Aid](iam-and-credential-control.md) for access and the [Recovery Aid](recovery.md) for corrective action.

## Procedure And Stop Conditions

### 1. Build the signal-to-owner matrix

Assign a primary and backup recipient to each surface:

| Surface | What it can establish | Primary source | Owner/threshold |
|---|---|---|---|
| Public domain/DNS/TLS probe | Reachability, delegation, certificate, basic redirect behavior | Authorized external probe plus Cloudflare DNS Analytics | **UNKNOWN** |
| Worker/deployment | Request volume, errors, duration, CPU/wall time, build/deploy result | Cloudflare Workers analytics/logs and deployment history | **UNKNOWN** |
| Edge security | WAF, rate-limit, Access, bot, crawler, DNS/TLS blocks | Cloudflare Security Events and Access logs | **UNKNOWN** |
| Deployed registry | Route count, states, expiry, metadata, generated timestamp | Protected `/<lang>/_stats/` dashboard | **UNKNOWN** |
| Source and delivery | Pull-request checks, release automation, deployment-trigger failures | GitHub Actions/checks/releases | **UNKNOWN** |
| Domain/provider continuity | Expiry, renewal, plan/quota/payment failure | Registrar and provider notifications | **UNKNOWN** |
| Public intake | Security, abuse, privacy, broken-link, and contributor reports | Published contacts and issue/security routes | **UNKNOWN** |
| Optional analytics | Redirect/page/miss trends after Worker execution | Umami/Fathom only when approved | Disabled baseline; owner **UNKNOWN** |

Do not infer Worker health from optional analytics alone. Requests blocked at Access/WAF/DNS/TLS layers never create Worker or provider events.

**Stop** before declaring monitoring operational if any public-availability, domain-renewal, deploy-failure, or security-intake path lacks an accountable primary and backup recipient.

### 2. Approve impact classes and thresholds

Use this draft classification only as a decision aid:

- **Critical:** public domain or redirects broadly unavailable, domain/registrar control lost, unauthorized deployment/control change, exposed secret, or compromise suspected.
- **High:** material redirect errors, deployment/rollback failure, Access/private surface exposed, certificate/DNS degradation, or security intake unowned.
- **Moderate:** partial link/configuration drift, protected dashboard unavailable while redirects work, recurring rate-limit/abuse issue, or release/documentation delivery failure.
- **Advisory:** expiry/renewal warning, upstream release available, metadata quality issue, or non-urgent policy/contact drift.

Numeric error, latency, traffic, expiry, quota, and time-to-acknowledge thresholds are **UNKNOWN** and must be approved from [OI-011](../controls/open-items.md) and [OI-013](../controls/open-items.md). Do not invent service-level objectives.

### 3. Configure routing without exposing secrets

For each signal:

- identify the authoritative provider surface;
- select two independent recipients;
- define acknowledgement and escalation;
- define after-hours behavior, if any;
- identify the responder role with required authority;
- identify the public communication decision;
- record privacy/retention limits.

Keep recipient addresses, tokens, webhook secrets, provider IDs, and personal recovery data outside this public aid. Reference their approved secret-manager or account locators only.

**Stop** if the same unrecoverable identity owns the monitor, alert destination, and affected platform, or if a test would send production traffic/change without authorization.

### 4. Exercise one signal per critical layer

In an approved isolated environment, use safe provider test functions or a tabletop input to exercise:

- public availability/DNS/TLS;
- Worker/deploy failure;
- Access/security event;
- domain/renewal warning;
- public security/abuse intake;
- recovery escalation.

Record event creation, receipt by both routes, acknowledgement, classification, responder authority, escalation, recovery decision, and closure. Exact test events, destinations, timing, and success thresholds are **UNKNOWN** until approved.

Do not create real abuse, expose a private path, expire a domain, disable production, or rotate a secret merely to generate evidence.

### 5. Triage and hand off

For an actual event:

1. Confirm the target service and observation layer.
2. Preserve redacted evidence and assign an incident identifier.
3. Classify impact using the approved model.
4. Confirm the responder has authority before changing state.
5. Use the primary linked source for the affected layer.
6. Invoke the [Recovery Aid](recovery.md) if rollback or restoration is required.
7. Publish only approved, evidence-bounded communications.
8. Close after smoke, ownership, and follow-up evidence are recorded.

**Stop** remediation when authority, target, rollback, or evidence preservation is **UNKNOWN**. Escalate rather than experimenting on the existing service.

## Expected Evidence And Records

Retain:

- redacted signal-to-owner matrix;
- approved impact classes and thresholds;
- primary/backup routing and recovery-path evidence;
- alert test records with sent, received, acknowledged, escalated, and closed timestamps;
- responder authority and access confirmation;
- incident identifier, source layer, evidence links, decisions, communications, and recovery result;
- domain/renewal notification evidence;
- public-contact monitoring and backup ownership;
- privacy, retention, and deletion decision for logs/analytics;
- unresolved gaps linked to [OI-006](../controls/open-items.md), [OI-011](../controls/open-items.md), [OI-012](../controls/open-items.md), and [OI-013](../controls/open-items.md).

Canonical incident system, record owner, retention period, alert tool, status channel, on-call schedule, and communication approver are **UNKNOWN**.

## Escalation, Recovery, And Unknowns

- If no responder has authority, stop changes and use the [IAM And Credential Control Aid](iam-and-credential-control.md).
- If live state or rollback cannot be identified, use the [Recovery Aid](recovery.md) and [OI-006](../controls/open-items.md).
- If a security issue is reported, preserve confidentiality and use the published security route; backup recipient and response objective remain **UNKNOWN**.
- If domain/renewal notification has no backup owner, treat it as a continuity stop condition under [OI-002](../controls/open-items.md) and [OI-013](../controls/open-items.md).
- If an alert exercise has not completed, the observability posture remains `untested`; documentation alone is not evidence of detection.

Current monitors, recipients, thresholds, acknowledgement objectives, escalation paths, public status channel, retention, incident owner, and exercise result remain **UNKNOWN**.
