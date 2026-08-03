# Continuity And Transfer Matrix

## Evidence Boundary

This matrix uses public, cutoff-pinned evidence through July 22, 2026. “Portable” means public source can support recreation; it does not mean the current asset can be transferred. No authenticated owner/admin, live service, private recovery, secret, billing, registrar, Terraform state, alert, or drill evidence was approved.

## Continuity Position

| Capability/asset | Publicly reconstructible? | Existing control transferable on evidence? | Sudden-departure consequence | Minimum closure evidence |
|---|---|---|---|---|
| Product source/history | Yes; MIT-licensed source, tests, ADRs, releases, public history | Repository ownership/admin transfer unknown | A successor can fork/evolve code, but may lose canonical project identity and trusted release path | OI-001 scope plus OI-002 owner/admin/signer successor exercise |
| Website/documentation source | Yes; broad bilingual corpus | One declared maintainer; admin/deployment transfer unknown | Docs can be forked, but canonical site/update path may stall | OI-002/OI-008 plus cross-repository maintainer assignment |
| Instance source/link registry | Yes; public Git source and build model | Repository/deploy connection/current deployed commit unknown | Links can be recreated, but current domain service may not continue | OI-002/OI-004/OI-007 |
| Terraform configuration | Partly; significant edge controls are public | State/backend/import coverage/account authority unknown | Rebuilding may duplicate/conflict with live resources; safe takeover not established | OI-006 redacted state/import/drift inventory and restore exercise |
| Domain/DNS/TLS | Configuration intent partly documented | Owner, renewal, recovery, transfer unknown | Existing public identity can expire or become unreachable | OI-002/OI-006 with two recoverable custodians, renewal proof, transfer test |
| Cloudflare Worker/Access/WAF/rate limits | Source intent is public | Account/admin, secrets, applied state, deployment authority unknown | Redirects, private operations, and protection may become unchangeable or unrecoverable | OI-002/OI-006 applied-state and successor-access proof |
| Release trust | Procedure and two signer identities declared | Signer/admin recovery and tag-rule enforcement unknown | Successor can publish a fork but not necessarily a trusted canonical release | OI-002 plus OI-010 signed-upgrade/release exercise |
| Link data recovery | Git source is durable; generated artifacts disposable | Existing latest deployed state/equivalence unknown | Core links can be rebuilt from known commit; uncommitted/dashboard drift may be lost | OI-004/OI-006 clean rebuild, deploy equivalence, rollback evidence |
| Secrets/provider credentials | Variable roles and storage boundaries documented | Custody, inventory, rotation, revocation, recovery unknown | Private operations/analytics/deploys may fail or remain accessible to departed people | OI-002/OI-003 redacted inventory and offboarding exercise |
| Logs/alerts/incidents | Invocation logging/intake declared | Alert routes, recipients, on-call, acknowledgement, retention unknown | Outage/abuse may persist unnoticed after departure | OI-012 alert delivery and incident-response evidence |
| Costs/renewals | Dependencies named | Plans, invoices, payment owners, commitments unknown | Domain/vendor services may lapse even if code is recoverable | Expense Exposure verification plus OI-002 renewal ownership |
| Maintainer onboarding | Contribution, governance, release, and operator docs exist | No observed non-creator maintainer appointment/handover | New maintainer faces creator-dependent authority and cross-repo ambiguity | OI-003 packet plus OI-004 timed non-creator walkthrough |

## Readiness Conclusions

| Question | Evidence-bounded answer |
|---|---|
| Can someone fork and evolve the software after abandonment? | **Yes, probably with moderate effort.** Source, license, tests, ADRs, releases, and documentation are public; execution by a successor remains unproved. |
| Can a new maintainer take over the canonical project with minimal creator involvement? | **No.** Appointment authority, cross-repository roles, admin/rules/signers, and an exercised handover are missing. |
| Can a third party create and operate a new independent instance? | **Plausible but not proven easy.** The product is designed for detachment and low-state operation; a clean independent exercise is missing. |
| Can a third party operate the existing project/domain/demo after sudden departure? | **No, not on current evidence.** Domain, GitHub, Cloudflare, Terraform state, secrets, deploy, alerts, renewals, and recovery are not transfer-proven. |
