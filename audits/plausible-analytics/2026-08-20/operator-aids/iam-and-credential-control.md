# IAM And Credential Control Guide

- Status: untested
- Selected precursor: [identity, secret, and analytics data flow](../controls/security/identity-secret-and-data-flow.md), [cloud/IAM/runtime view](../controls/cloud-security/cloud-iam-network-runtime-control-view.md), and [OI-008/OI-015](../controls/open-items.md#oi-008)

## Purpose And Evidence Boundary

Operator question: How should the library assign, review, transfer, and retire Plausible access and credentials without exposing secret values or losing administrative control?

This is an untested control guide. It does not authorize access, create or revoke an account, rotate a key, inspect a secret, change billing, or assert least privilege. No library identity provider, roster, role assignment, 2FA state, key/link inventory, secret store, cloud IAM, database privilege, hosted admin, or audit log was inspected. The guide covers Run and Subscribe library-retained controls; vendor-internal hosted identities require dated assurance rather than library administration.

## Existing Runbook And Coverage

No applicable library IAM, credential-custody, or offboarding runbook was found in the approved catalog or source. `primary-code:lib/plausible/teams/membership.ex:1-28` defines guest/viewer/editor/admin/owner/billing roles. `primary-code:lib/plausible/teams.ex:323-368` implements team-enforced 2FA. `primary-code:lib/plausible/site/shared_link.ex:1-56` implements shared-link capabilities, and `primary-code:lib/plausible/auth/auth.ex:255-320` exposes API-key creation/deletion paths. `primary-code:lib/plausible/helpers/config.ex:1-52` and `primary-code:config/runtime.exs:21-115` load configuration from secret files or environment and define `ADMIN_USER_IDS`. Ownership-transfer mechanisms are recorded in [E-039](../evidence/evidence-ledger.md#e-039). These sources do not define the library's approval, custody, review, rotation, break-glass, or offboarding process.

## Authority And Preconditions

The Director of Digital Services owns business-role approval; security owns credential standards and emergency access; privacy/records owns analytics-output recipients and data-purpose constraints; IT owns Run infrastructure/service identities; procurement and the SaaS account owner own Subscribe administration, billing, support, and vendor assurance.

Before any authorized identity or credential action:

1. Verify the requester and approving authority through an independent organizational channel.
2. Identify the exact option, environment, team/site scope, requested outcome, duration, and role. Default to no access where authority or scope is `UNKNOWN`.
3. Confirm at least two accountable owner-capable people or an approved break-glass/successor route before reducing privileged access.
4. Use the OI-008 governance contract to determine whether public dashboards, shared links, API keys, report recipients, and optional integrations are permitted at all.
5. For Run, use OI-001/OI-015 to identify cloud/project, workload, registry, DNS/edge, database, backup, secret-store, mail, monitoring, and application admin domains. For Subscribe, identify team owner/admin, billing/procurement, support, assurance, export, and termination domains.
6. Use an approved secret manager or equivalent protected channel. Never place secret values, recovery codes, tokens, password reset links, callback parameters, or private keys in this audit or a general handoff record.

## Procedure And Stop Conditions

1. **Maintain a redacted access register.** For each human, service, API key, shared link, report recipient, integration, and emergency path, record only a stable redacted identifier, owner, successor, system/team/site scope, role/permission, purpose, approval, creation/review/expiry dates, authentication/MFA expectation, credential-store locator, and revocation owner.
2. **Apply least retained access.** Use viewer for dashboard-only needs; reserve editor/admin/owner/billing for evidenced duties. Keep guest access site-scoped. Prohibit public/shared dashboards, API keys, or arbitrary report recipients unless OI-008 explicitly permits them. Do not infer that source role checks prove live assignments.
3. **Harden intentional alternate access.** Until [OI-013](../controls/open-items.md#oi-013) is closed, avoid shared links and client-supplied API secrets where possible; otherwise require library-approved strong generation, narrow scope, an expiry/review date, protected delivery, and documented revocation. Inventory and retire unused paths.
4. **Protect privileged and service identities.** Enforce MFA where supported; separate daily and recovery administration; avoid shared human accounts; assign primary/successor custody for `ADMIN_USER_IDS`, infrastructure, registry, DNS, datastore, backup, mail, telemetry, billing, support, and secret-store paths. Confirm separate ClickHouse client roles with effective database permissions rather than assuming source separation.
5. **Control secrets and integrations.** Prefer mounted secret files over image or source embedding for Run. Record provider, ACL owner, injection route, rotation/expiry metadata, fallback-key removal, and dependent services without recording the value. Keep Google OAuth/Sentry combinations disabled or independently scrubbed until OI-010 closes; keep ingestion Sentry disabled or scrubbed until OI-012 closes.
6. **Authorize onboarding or change.** Obtain the required business, security, privacy, IT, or procurement approval; have a second authorized person verify scope; execute through the system's canonical interface under a separate change record; and confirm access with a test identity that cannot see unintended sites or settings. This guide does not grant that execution authority.
7. **Offboard or transfer.** Preserve successor control first, then revoke sessions, membership, API keys, shared links, report recipients, service credentials, support/billing access, and integration grants that are no longer required. For ownership transfer, verify the recipient has accepted and can administer the intended scope before removing the prior owner. Rotate only credentials whose custody or exposure boundary changed, using a separately approved rollback path.
8. **Review and reconcile.** On join/leave/service change and at the approved periodic cadence, compare the access register with effective memberships, keys, links, recipients, privileged configuration, cloud/service identities, and vendor accounts. Record orphaned, overbroad, stale, or unverified items as findings; do not silently normalize them.

Stop if identity or authority cannot be independently verified; a change could remove the only usable owner or recovery path; the exact option/environment is unclear; a secret must be copied into an unsafe channel; visitor data would be exposed; effective access cannot be tested without production/live traffic; a privileged header, edge, or service identity boundary is unproved; or rollback would require an unavailable credential. Preserve existing access and escalate rather than improvising.

## Expected Evidence And Records

Retain approvals, redacted before/after access-register entries, option/environment/team/site scope, effective role/permission evidence, MFA status without recovery material, change record, second-person verification, negative-access result, session/key/link revocation evidence, owner/successor acknowledgement, and next review/expiry date. For hosted evidence, retain restricted assurance/contract locators rather than copying non-public content into the audit.

Mark this aid `executed-successfully` only when an authorized canonical record shows that required identities and credentials were reconciled, negative access was tested, no owner/recovery path was lost, and all exceptions have accountable owners. A source role list or account roster alone is insufficient.

## Escalation, Recovery, And Unknowns

Escalate role/data-purpose questions to Digital Services plus privacy/records under OI-008; Run infrastructure/secret/edge gaps to IT/security under OI-001/OI-011/OI-015; shared-link/API weaknesses under OI-013; diagnostic credential exposure under OI-010/OI-012; and hosted account/billing/support/assurance gaps to procurement under OI-015/OI-017. If control is lost, invoke the approved organizational identity-recovery process and the [recovery guide](recovery.md); this audit does not define or prove that external process.

The current roster, MFA state, owner count, emergency access, API/shared-link/report-recipient inventory, secret store, rotation cadence, cloud/database privileges, hosted admin/support owners, vendor internal IAM, and legal access requirements are `UNKNOWN`.
