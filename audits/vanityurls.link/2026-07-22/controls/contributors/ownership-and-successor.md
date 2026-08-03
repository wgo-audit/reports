# Contribution, Vendor, And Successor Map

## Evidence Boundary

This map uses public role declarations, cutoff-pinned Git history, repository artifacts, and vendor/configuration evidence through July 22, 2026. Commit volume is used only as a concentration signal; it is not performance, value, identity, availability, legal ownership, or account-control evidence. No private staffing, contract, support, succession, or acceptance record was approved.

## Contribution And Ownership Position

| Boundary | Usable public output | Declared accountable role | Concentration evidence | Successor evidence | Material limitation |
|---|---|---|---|---|---|
| Product `code` | MIT source, broad tests, 19 ADRs, 38 releases, 75 PRs, detailed release workflow | Two maintainers/CODEOWNERS and two trusted signer identities | Leading human authored 319 of 402 main commits; other humans and bots contributed | Governance says active contributors may be invited | Invitation authority/process, admin access, availability, handover, and successor exercise unknown; governance contradicts itself on one versus two maintainers |
| Website/docs | Public site source, 97 catalogued operator docs across code/website, 38 releases, 42 PRs | One maintainer/default CODEOWNER | Leading human authored 412 of 452 main commits | Generic “may be invited” language | No second declared owner, reproducible hosted quality gate, or exercised docs handover |
| Demo infrastructure | Public Terraform for significant Cloudflare controls | No repository-local maintainer/governance declaration | All 3 commits attributed to one human alias | None found | Account/state/deploy ownership and review path unknown |
| Demo instance | Public instance source and operator configuration | No repository-local maintainer/governance declaration | Sole commit attributed to one human alias | Product detachment model supports independent instances | Existing repository/domain/Cloudflare/deploy transfer unknown |
| Community contribution | README recognizes code, docs, security, ideas, user testing, promotion, and feedback roles | Contributor and user roles in governance | Contributor badge and rendered table counts do not align; contribution histories exist | Contributor-to-maintainer concept is stated | No competency, probation, nomination, voting/approval, access, conflict, or offboarding procedure |

## Vendor Dependency Position

| Vendor/control surface | Value supplied | Substitutability | Current owner/support evidence | Successor consequence |
|---|---|---|---|---|
| GitHub | Public source, history, issues/PRs, Actions, releases, Projects, identity/signing integration | Source can be mirrored; canonical links/history/trust require migration | Owner/admin and support entitlement unknown; no commercial commitment evidenced | Fork is possible; canonical takeover/migration needs authority and trust communication |
| Cloudflare | DNS/TLS, Worker/assets, Access, WAF/rate limits, logs/security events | Product is implemented specifically for Cloudflare Workers; replacement would be a material architecture change | Account/plan/admin/support/transfer unknown | Largest vendor concentration for operating the existing service |
| Domain registrar | Public `v8s.link` identity and renewal | Domain can be replaced for a fork, not transparently for continuity | Registrar, owner, renewal/payment/recovery unknown | Loss breaks public trust/links even if source survives |
| Terraform/Cloudflare provider | Reviewable infrastructure declarations | Provider/tool can be updated, but live state/import must be known | Public lock exists; state/backend/support unknown | Reproduction is possible; safe takeover is not |
| Analytics providers | Optional events/metrics | High: disabled baseline or either documented provider | Reference instance declares disabled; account/support/retention unknown | Not required for successor baseline; enabling adds custody/privacy/cost |

## Successor Minimum

A credible successor needs: publicly approved role/authority; cross-repository write/admin coverage; release signing and verification; GitHub/Cloudflare/registrar/Terraform-state custody; documentation/build competence; alert/incident responsibility; and an observed independent exercise. OI-001/OI-002/OI-003/OI-004/OI-005/OI-006/OI-012 are the closure path.
