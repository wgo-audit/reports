# Access And Ownership Boundary

## Purpose And Evidence Boundary

This source-bounded control view identifies the human and account dependencies
that must remain transferable when Acme operates Healthchecks as pull, make, or
buy. It uses [E-020](../../evidence/evidence-ledger.md#E-020),
[E-029](../../evidence/evidence-ledger.md#E-029), and
[E-030](../../evidence/evidence-ledger.md#E-030). It is not an Acme account or
owner inventory. No production administrator, vendor account, billing owner,
domain, DNS, certificate, secret-store, database, object-store, registry,
notification-provider, or on-call owner was observed.

## Control And Transfer Matrix

| Control boundary | Source-backed mechanism | Pull / make dependency | Buy dependency | Required transfer proof | Current status |
|---|---|---|---|---|---|
| Project ownership | The application has one project owner; an owner can initiate transfer to an existing member, who must accept. | Acme controls the runtime and database, but the supported UI transfer still depends on the current owner. | The hosted account and owner remain vendor-mediated. | Two named accountable owners, tested transfer, and emergency recovery that does not depend on the departing person. | Unknown; [OI-012](../open-items.md#OI-012) |
| Team administration | Managers can add/remove members; regular members can change checks, integrations, and project API/ping keys. | Access continuity must cover application admins and platform operators. | Access continuity must cover vendor login, project manager, and billing account. | Least-privilege roster, MFA/recovery, periodic review, and departure drill. | Unknown; [OI-011](../open-items.md#OI-011) and [OI-012](../open-items.md#OI-012) |
| Runtime and data control | Self-hosting requires infrastructure, database, secrets, image/registry, TLS, backup, and provider accounts. | Every dependency needs an Acme owner and replacement path; make also needs repository/release ownership. | Vendor owns runtime/data-plane recovery; Acme still owns producer credentials, integrations, account, billing, and exit. | Account inventory with primary/deputy, break-glass custody, renewal dates, and transfer rehearsal. | Unknown; [OI-002](../open-items.md#OI-002) and [OI-012](../open-items.md#OI-012) |
| Notification and response | Integrations are project-scoped and contain destination credentials; source records sends/errors but not human receipt. | Acme owns provider contracts, routes, escalation, and independent watchdog. | Vendor sends through selected providers, but Acme owns destinations, responders, and independent route. | Test primary and independent routes through acknowledgement and handoff. | Unknown; [OI-006](../open-items.md#OI-006) |
| Upstream/source stewardship | BSD-3-Clause permits continued source/binary use and modification. The public security policy names one reporting address. | Pull can remain pinned if upstream disappears; make requires Acme merge, patch, and release ownership immediately. | Hosted continuation and successor operation depend on vendor evidence/terms. | Immutable source/artifact custody, rebuild evidence, named security/update owner, and exit trigger. | Source right confirmed; readiness unknown |

## Minimum Ownership Standard

Production approval requires a named primary and deputy for every row, with
credentials held in an Acme-controlled recovery mechanism. The transfer drill
must cover loss of the primary person, not merely cooperative handoff. The
source-supported project transfer is useful but does not establish emergency
recovery because it requires current-owner initiation and recipient acceptance.

No conclusion about Acme's present team ability is made.
