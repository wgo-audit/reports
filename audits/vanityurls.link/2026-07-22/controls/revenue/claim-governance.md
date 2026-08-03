# Public Claim And Demo Governance

## Evidence Boundary

vanityURLs is community-maintained OSS with no company, customer contract, sales pipeline, subscription, or revenue evidence. This register therefore governs adoption, onboarding, demo, and community-trust exposure. Claims are compared with cutoff-pinned source/documentation through July 22, 2026; no live demo, customer acceptance, performance test, billing, or legal/security certification was approved.

## Claim Register

| Public claim/promise | Supporting evidence | Contradicting or missing evidence | Safe claim status | Closure |
|---|---|---|---|---|
| Open-source software runs on an operator’s own domain and Cloudflare | MIT source, setup/detach/upgrade code, Worker/Terraform/config docs | Non-creator execution unobserved | **Implemented and documented; independently unverified** | OI-004 |
| Product is “free” | MIT software is provided without license fee; optional analytics can be disabled | Domain, Cloudflare/GitHub plans, labor, renewals, and other operating costs unknown | **Qualify as software-license cost only** | OI-013 and wording update |
| Product is “fast” | Stateless Worker/tree lookup is source-visible | No latency, load, quota, or production metric | **Unsubstantiated performance claim** | OI-011 or remove/qualify |
| Product is “always under your control” | Git-backed source, detachment, local configuration, MIT forkability | Existing service depends on GitHub/Cloudflare/registrar/state/secrets; transfer/ownership unproved | **Overbroad; qualify as source/configuration control for an independently owned instance** | OI-001/OI-002/OI-006 |
| Quickstart leads to a first deployed redirect | Detailed steps and implemented setup/build/check path | No approved non-creator golden-path observation | **Documented path, not demonstrated ease** | OI-004 |
| `v8s.link` is the official live demo and its table shows current links from the source repository | Demo docs and public instance repository exist | Approved source contains three starter links; docs list a different/larger “current” inventory; no live cutoff observation | **Not decision-safe until reconciled** | OI-014 |
| Private operations are protected and runtime assets hidden | Access/Worker/Terraform source and source tests | Applied Access/WAF/DNS state and live reachability unknown | **Implemented/intended, not live-verified** | OI-006/OI-004 |
| Privacy/security/accessibility commitments | Detailed policies, source controls, transparent accessibility limitations | Live publication/configuration, contact monitoring, provider retention, and specialist sign-off not fully evidenced | **Scope each claim to source/site evidence and named limitations** | OI-006/OI-012 plus specialist review if retained |
| Community can continue the project | Public source/license/history/tests/docs support forking | Canonical maintainer authority, accounts, domain, state, alerts, and recovery unproved | **Fork continuity plausible; canonical/service continuity not ready** | OI-001 through OI-006/OI-012 |

## Claim Stop Conditions

- Do not claim easy/low-touch maintainer onboarding until OI-004 succeeds with measured assistance.
- Do not claim third-party operation of the existing service until OI-002/OI-006/OI-012/OI-013 are closed.
- Do not use the demo as proof until its documented inventory, public source, deployed commit, and representative paths are reconciled.
- Do not make numeric performance, availability, cost, adoption, or security claims without the corresponding approved evidence.
