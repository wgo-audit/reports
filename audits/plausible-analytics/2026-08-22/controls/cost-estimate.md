# API-Equivalent Audit Cost Estimate

| Field | Value |
|---|---|
| Coverage | audit |
| Reconciliation status | Final |
| Rate-card/basis date | 2026-08-07 |
| Currency | USD |
| Pricing basis | OpenAI API-equivalent estimate; not a Codex invoice |

## Pricing Basis And Dated Data

The checked-in rate card uses the [OpenAI API pricing basis](https://platform.openai.com/docs/pricing), dated 2026-08-07, in USD per one million tokens. Every included row used the declared API-equivalent `standard` tier because the rollout records did not return a service tier. Every row used the threshold-derived `short` context band because recorded request input was at or below 272,000 tokens. These are reproducible pricing assumptions, not observed Codex backend billing.

The exact formula is: `uncached input × input rate + cached input × cached-input rate + output × output rate`. Reasoning tokens are already part of output and are shown only for information. Cache-write input is excluded by the prescribed formula; included requests reported zero cache-write tokens. Exact decimals are retained in [cost-calculation.json](cost-calculation.json).

## Frozen Manifest And Exclusions

The immutable temporary manifest contains 35 provenance-linked sessions and is frozen at the audit-complete marker. Its SHA-256 is `35a4c4281d3664af80f5ecc4cd49257d6270c3b7d463fbddafc9a2faeee31cc9`. The public alias-only [calculation receipt](cost-calculation.json) records phase boundaries, aliased sessions and requests, exact token rows, duplicate suppression, pricing, totals, and both verification digests without exposing provider-native identifiers.

### Phase Boundaries

| Phase | Session | Marker and record boundary | Included or excluded |
|---|---|---|---|
| Unattributed | `session-001` | Before onboarding marker at line 29 | Included |
| Onboarding | `session-001` | `WGO_PHASE_ONBOARDING_START`, line 29 | Included after marker |
| Audit | `session-001` | `WGO_PHASE_AUDIT_START`, line 342 | Included after marker |
| Summary | `session-001` | `WGO_PHASE_SUMMARY_START`, line 2,151 | Included after marker |
| Cost estimation | `session-001` | `WGO_AUDIT_COMPLETE_COST_PHASE_STARTS`, line 2,315 | Excluded after marker |

### Session And Request Exclusions

| Session/request | Phase | Rationale |
|---|---|---|
| None before the frozen cutoff | Included phases | All 35 recursively provenance-linked sessions were available and lifecycle-bounded; no included request was unpriced or disputed. |
| 29 unchanged legacy-state echoes | Included phases | Suppressed as duplicate observations of the preceding unchanged `last_token_usage` state; not separate priced requests. |
| All later cost-calculation requests | Cost estimation | Excluded by the frozen completion marker. |

## Token Totals By Session And Model

| Phase | WGO role/task | Session | Model/provider | Service tier/basis | Uncached/new input | Cache read | Cache write | Cache-write detail | Output | Reasoning (informational) | Cost |
|---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|
| unattributed | `Terra audit coordinator` | `session-001` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 15,076 | 52,480 | 0 | none reported | 785 | 161 | $0.13 |
| **unattributed subtotal** |  |  |  |  | **15,076** | **52,480** | **0** |  | **785** | **161** | **$0.13** |
| onboarding | `Terra audit coordinator` | `session-001` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 113,499 | 1,873,664 | 0 | none reported | 18,258 | 4,122 | $2.05 |
| onboarding | `documentation_prep` | `session-002` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 134,512 | 1,721,600 | 0 | none reported | 19,840 | 3,626 | $0.85 |
| **onboarding subtotal** |  |  |  |  | **248,011** | **3,595,264** | **0** |  | **38,098** | **7,748** | **$2.90** |
| audit | `Terra audit coordinator` | `session-001` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 503,338 | 42,493,952 | 0 | none reported | 40,838 | 8,157 | $24.99 |
| audit | `architecture_reviewer` | `session-003` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 252,800 | 8,916,224 | 0 | none reported | 39,695 | 6,310 | $6.91 |
| audit | `architecture_reviewer/architecture_artifact_quality` | `session-004` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 37,544 | 236,544 | 0 | none reported | 5,801 | 3,227 | $0.19 |
| audit | `code_quality_reviewer` | `session-005` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 215,827 | 7,291,136 | 0 | none reported | 31,261 | 6,725 | $5.66 |
| audit | `code_quality_reviewer/code_quality_artifact_quality` | `session-006` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 55,616 | 203,264 | 0 | none reported | 5,037 | 2,437 | $0.21 |
| audit | `product_value_reviewer` | `session-007` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 325,403 | 6,174,208 | 0 | none reported | 51,910 | 5,649 | $6.27 |
| audit | `product_value_reviewer/product_evidence_collector` | `session-008` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 149,114 | 1,292,544 | 0 | none reported | 9,675 | 2,373 | $0.67 |
| audit | `product_value_reviewer/product_github_history` | `session-009` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 123,118 | 792,576 | 0 | none reported | 14,421 | 3,368 | $0.58 |
| audit | `product_value_reviewer/product_artifact_quality` | `session-010` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 45,663 | 291,072 | 0 | none reported | 7,372 | 4,150 | $0.24 |
| audit | `security_privacy_reviewer` | `session-011` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 328,405 | 5,776,128 | 0 | none reported | 36,094 | 5,706 | $5.61 |
| audit | `security_privacy_reviewer/security_artifact_quality` | `session-012` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 76,920 | 355,072 | 0 | none reported | 8,007 | 4,106 | $0.32 |
| audit | `application_security_reviewer` | `session-013` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 347,213 | 6,524,928 | 0 | none reported | 34,278 | 4,842 | $6.03 |
| audit | `application_security_reviewer/appsec_quality` | `session-014` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 48,539 | 292,352 | 0 | none reported | 5,096 | 2,520 | $0.22 |
| audit | `business_continuity_reviewer` | `session-015` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 297,726 | 6,124,032 | 0 | none reported | 32,813 | 8,233 | $5.54 |
| audit | `business_continuity_reviewer/continuity_quality` | `session-016` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 26,946 | 129,792 | 0 | none reported | 2,801 | 1,701 | $0.11 |
| audit | `cloud_security_reviewer` | `session-017` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 203,866 | 7,173,888 | 0 | none reported | 33,635 | 6,537 | $5.62 |
| audit | `cloud_security_reviewer/cloud_iam_collector` | `session-018` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 135,550 | 1,298,688 | 0 | none reported | 8,018 | 1,709 | $0.63 |
| audit | `cloud_security_reviewer/cloud_security_quality` | `session-019` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 55,755 | 441,600 | 0 | none reported | 7,303 | 3,909 | $0.29 |
| audit | `expense_exposure_reviewer` | `session-020` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 166,258 | 4,435,456 | 0 | none reported | 27,438 | 6,324 | $3.87 |
| audit | `expense_exposure_reviewer/expense_quality` | `session-021` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 34,437 | 145,152 | 0 | none reported | 2,084 | 1,060 | $0.12 |
| audit | `scalability_reviewer` | `session-022` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 295,052 | 6,906,880 | 0 | none reported | 29,520 | 4,607 | $5.81 |
| audit | `scalability_reviewer/scalability_quality` | `session-023` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 49,886 | 463,872 | 0 | none reported | 8,438 | 4,892 | $0.29 |
| audit | `compliance_assurance_reviewer` | `session-024` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 177,009 | 5,095,680 | 0 | none reported | 41,345 | 6,842 | $4.67 |
| audit | `compliance_assurance_reviewer/compliance_quality` | `session-025` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 86,391 | 633,344 | 0 | none reported | 9,639 | 6,260 | $0.42 |
| audit | `contributor_vendor_value_reviewer` | `session-026` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 198,085 | 7,090,944 | 0 | none reported | 42,866 | 9,091 | $5.82 |
| audit | `contributor_vendor_value_reviewer/contribution_value_collector` | `session-027` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 75,505 | 1,120,512 | 0 | none reported | 14,661 | 5,467 | $0.55 |
| audit | `contributor_vendor_value_reviewer/contributor_value_quality` | `session-028` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 49,342 | 259,072 | 0 | none reported | 8,583 | 6,279 | $0.25 |
| audit | `maintenance_cost_reviewer` | `session-029` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 170,303 | 5,061,888 | 0 | none reported | 29,351 | 4,850 | $4.26 |
| audit | `maintenance_cost_reviewer/maintenance_quality` | `session-030` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 46,289 | 302,592 | 0 | none reported | 5,478 | 3,121 | $0.22 |
| audit | `maintenance_cost_reviewer/delivery_quality_packet` | `session-031` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 65,210 | 475,392 | 0 | none reported | 7,797 | 2,069 | $0.32 |
| audit | `revenue_risk_reviewer` | `session-032` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 96,247 | 2,036,224 | 0 | none reported | 17,709 | 3,935 | $2.03 |
| audit | `revenue_risk_reviewer/revenue_quality` | `session-033` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 54,448 | 275,200 | 0 | none reported | 4,313 | 1,665 | $0.22 |
| audit | `project_health_reviewer` | `session-034` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 130,309 | 3,305,216 | 0 | none reported | 23,368 | 6,002 | $3.01 |
| audit | `project_health_reviewer/project_health_quality` | `session-035` | `gpt-5.6-terra` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 63,314 | 377,856 | 0 | none reported | 6,643 | 3,851 | $0.28 |
| **audit subtotal** |  |  |  |  | **4,987,428** | **133,793,280** | **0** |  | **653,288** | **157,974** | **$102.24** |
| summary | `Terra audit coordinator` | `session-001` | `gpt-5.6-sol` / OpenAI | standard, declared API-equivalent; short, threshold-derived | 228,968 | 4,422,400 | 0 | none reported | 22,173 | 1,500 | $4.02 |
| **summary subtotal** |  |  |  |  | **228,968** | **4,422,400** | **0** |  | **22,173** | **1,500** | **$4.02** |

Reasoning is an informational subcomponent of output and is never added a second time to billable output. Row and subtotal displays are rounded half up from exact evidence; the total is independently rounded from the exact reconciled total.

## Model-By-Model Cost

| Model/provider | Service tier/context | Rate components or recorded-cost basis | Exact-evidence status | Displayed cost |
|---|---|---|---|---:|
| `gpt-5.6-sol` / OpenAI | standard declared / short derived | $5.00 uncached input; $0.50 cache read; $30.00 output per million | Exact subtotal `102.304694`; all included requests priced | $102.30 |
| `gpt-5.6-terra` / OpenAI | standard declared / short derived | $2.00 uncached input; $0.20 cache read; $12.00 output per million | Exact subtotal `6.9819012`; all included requests priced | $6.98 |
| **Total** |  | Exact reconciled total `109.2865952` | Two passes matched | **$109.29** |

## Reconciliation Status

**Final.** Two independent Terra/high verification passes parsed the same immutable manifest. After deterministic ordering, their complete JSON results matched byte-for-byte: each SHA-256 is `b47b9e19972537cd45978241b8a4a1a48279f48f1075138c1dab520b422ed8c8`. Both reported 38 aggregate rows, 1,457 priced legacy-state requests, 29 unchanged-state duplicates, zero excluded pre-cutoff requests, zero schema/pricing issues, and exact total `109.2865952` USD.

## Limitations

- This is a portable API-equivalent estimate of recorded model requests, not a Codex invoice, subscription charge, or representation of the backend service tier.
- The records did not expose stable provider request IDs. The schema-aware fallback counts each changed `last_token_usage` state once within session, turn, model, tier, and context band, and suppresses consecutive identical echoes. It cannot distinguish two genuinely separate legacy requests with identical usage state.
- The declared `standard` tier and threshold-derived `short` band are pricing assumptions required by the checked-in rate card; they are not provider billing facts.
- No nonzero cache-write input was reported. Tool charges, regional uplift, subscription effects, and non-token charges are not inferred.
- The temporary manifest and verification results remain outside the audit root; only the aliased public receipt is publishable. Cost-calculation requests after the frozen completion marker are excluded.
