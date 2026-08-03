# Expense Exposure

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what actual or potential cash and interruption exposure comes from infrastructure, software, labor, commitments, renewals, quotas, and failure modes. It uses public dependency/configuration evidence, the vendor packet, and Architecture/Scalability/Business Continuity/Contributor handoffs through July 22, 2026. No billing, invoice, contract, usage, plan entitlement, payment, renewal, donation, budget, rate, or private commitment evidence was approved.

## Coverage And Material Gaps

Coverage includes the short domain, registrar, GitHub, Cloudflare DNS/Workers/Access/WAF/logs, website hosting/toolchain, optional analytics, volunteer labor, and incident/recovery exposure. No monetary amount, period, commitment, or owner can be established. The material decision is therefore not “how much does it cost,” but whether renewal/billing ownership and service-interruption thresholds are known. They are not.

## Key Findings

| Finding | Evidence links | Confidence and limitation | Consequence |
|---|---|---|---|
| No approved evidence supports a cash burn, liability, contract, or funding amount. | [Vendor packet](../../evidence/packets/vendor-ownership-commercial.md), [burn/renewal register](../../controls/expense/burn-and-renewal.md) | High for approved evidence boundary; private costs may exist. | Any numeric cost estimate would be invented and decision-unsafe. |
| The domain has the clearest renewal interruption exposure, but registrar, expiry, payment, owner, backup, and transfer are unknown. | [Continuity matrix](../../controls/continuity/continuity-and-transfer-matrix.md), [burn register](../../controls/expense/burn-and-renewal.md) | High for dependency/unknowns; no registrar evidence. | A small unknown renewal can cause disproportionate community harm by breaking durable short links. |
| Cloudflare and GitHub are critical service dependencies, but current plans, quotas, billing owners, support, and terms are unknown. | [Vendor map](../../controls/contributors/ownership-and-successor.md), [capacity envelope](../../controls/scalability/capacity-and-degradation.md) | High for technical dependence; no commercial fact. | A third party cannot budget, verify entitlements, or ensure uninterrupted transfer of the existing service. |
| Public docs describe Free-plan-compatible configurations, but this does not prove the existing accounts are free, sufficient, or free of payment-method/overage/renewal obligations. | Website Access/network-protection docs; [vendor packet](../../evidence/packets/vendor-ownership-commercial.md) | High for documentation; live plan/usage absent. | “Can run cheaply” remains a design possibility, not an audited expense conclusion. |
| Analytics is optional and disabled in the reference source, so it can be excluded from the minimum successor operating baseline. | [PDR-007](../../controls/product/pdr/PDR-007-private-operations-and-optional-analytics.md), [burn register](../../controls/expense/burn-and-renewal.md) | High for source default; live state unknown. | This is the clearest immediate way to avoid adding provider cost/privacy/quota exposure. |
| Volunteer/best-effort support is public, but no labor hours or rates exist. | SUPPORT/maintainer docs; [Maintenance Cost report](../maintenance-cost/report.md) | High for stated model; actual effort unavailable. | Maintenance burden cannot be converted into financial staffing cost or obligation. |

### Decision Insights

- **Do not defer the renewal inventory because cash amounts may be small.** Domain lapse has asymmetric continuity/trust impact. Smallest proof: OI-013 with redacted expiry, payment backup, recipients, and transfer/recovery.
- **Budget the minimum successor baseline before optional services.** GitHub, domain, and Cloudflare core controls come first; analytics remains disabled until purpose, plan, owner, retention, and limits are approved.
- **Keep cost and effort separate.** OI-004 can measure time/assistance; only approved rates or contracts can turn that into cash exposure.

## Selected Outputs

Material renewal, quota, and vendor-interruption boundaries triggered [burn, renewal, and interruption register](../../controls/expense/burn-and-renewal.md). Every monetary field remains `unknown` rather than inferred.

## Material Omissions, Unknowns, And Stakeholder Questions

- Registrar/domain expiry, renewal, payment, transfer, and owner: OI-013.
- GitHub/Cloudflare/website/analytics plan, quota, usage, billing owner, support, term, and commitment: OI-013 and OI-006/OI-011.
- Labor time/rates, donations, sponsorships, liabilities, insurance, tax, and incident cost: no approved evidence.
- Any customer SLA/credit or revenue consequence: no evidence; Revenue Risk owns claim exposure.

## Reconciliation

Free-plan guidance was reconciled as operator configuration advice, not proof of current entitlement or zero cost. Named vendors are not treated as paid dependencies. The absence of public invoices/contracts is treated as an evidence limit, not proof that no costs exist.

## Bounded Conclusion And Downstream Guidance

Expense exposure cannot be quantified from public evidence. The material risk is unowned renewal/billing/quota interruption—especially the domain and Cloudflare control plane—not a demonstrated high burn. Revenue Risk may use interruption boundaries but not infer revenue amount; synthesis should require a redacted renewal/plan owner register before claiming third-party operability.
