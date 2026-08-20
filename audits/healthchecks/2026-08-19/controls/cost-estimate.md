# API-Equivalent Audit Cost Estimate

| Field | Value |
|---|---|
| Coverage | audit |
| Reconciliation status | Final |
| Rate-card/basis date | 2026-08-07 |
| Currency | USD |
| Pricing basis | OpenAI API-equivalent estimate; not a Codex or OpenAI invoice |

## Pricing Basis And Dated Data

The frozen basis is the checked-in OpenAI API rate card at
`references/data/api-rate-card-2026-08-07.json`, sourced from
https://platform.openai.com/docs/pricing and denominated in USD per one million
tokens. The recorded sessions do not return a service tier, so the manifest's
declared standard API-equivalent tier applies. All request inputs are at or
below the 272,000-token threshold and therefore use the short-context band.

The exact formula is `uncached input × input rate + cached input × cached-input
rate + output × output rate`. Reasoning is reported as an informational output
subcomponent and is not added again. The exact reconciled result is
`$103.0189036`; the independently rounded display total is **$103.02**.

## Frozen Manifest And Exclusions

The public alias-only [calculation receipt](cost-calculation.json) records the
temporary input digest, pass count, byte-identical pass-result digest, exact
aliased rows, and exact total. Provider-native manifests and pass files remain
outside the audit as temporary troubleshooting data.

The repaired manifest includes the root plus all 31 provenance-linked audit
descendants and excludes only post-cutoff cost-calculation work.

### Phase Boundaries

| Phase | Session | Marker and record boundary | Included or excluded |
|---|---|---|---|
| onboarding | `session-001` | `WGO_PHASE_ONBOARDING_START`, manifest line 92 | Included |
| audit | `session-001` | `WGO_PHASE_AUDIT_START`, manifest line 523 | Included |
| summary | `session-001` | `WGO_PHASE_SUMMARY_START`, manifest line 2958 | Included |
| cost-estimation | `session-001` | `WGO_AUDIT_COMPLETE_COST_PHASE_STARTS`, frozen response cutoff line 3065 | Excluded after cutoff |

### Session And Request Exclusions

| Session/request | Phase | Rationale |
|---|---|---|
| `root/cost_closeout` (`excluded-session-001`) | cost-estimation | Spawned after the frozen audit cutoff; calculation requests are excluded. |
| Pass A, pass B, and this repair closeout | cost-estimation | Calculation work occurred after the frozen root cutoff and is not part of audit coverage. |

## Token Totals By Session And Model

| Phase | WGO role/task | Session | Model/provider | Service tier/basis | Uncached/new input | Cache read | Cache write | Cache-write detail | Output | Reasoning (informational) | Cost |
|---|---|---|---|---|---:|---:|---:|---|---:|---:|---:|
| unattributed | `WGO audit coordinator` | `session-001` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 39,199 | 289,792 | 0 | none observed | 4,244 | 1,572 | $0.47 |
| **unattributed subtotal** |  |  |  |  | **39,199** | **289,792** | **0** | none observed | **4,244** | **1,572** | **$0.47** |
| onboarding | `WGO audit coordinator` | `session-001` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 132,323 | 4,774,400 | 0 | none observed | 29,346 | 10,501 | $3.93 |
| onboarding | `root/wgo_documentation_catalog` | `session-015` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 11,647 | 307,200 | 0 | none observed | 869 | 309 | $0.10 |
| **onboarding subtotal** |  |  |  |  | **143,970** | **5,081,600** | **0** | none observed | **30,215** | **10,810** | **$4.02** |
| audit | `WGO audit coordinator` | `session-001` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 542,744 | 63,208,960 | 0 | none observed | 98,605 | 14,218 | $37.28 |
| audit | `root/architecture_review` | `session-002` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 195,189 | 7,016,448 | 0 | none observed | 43,097 | 7,670 | $5.78 |
| audit | `root/architecture_review/component_topology` | `session-017` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 126,881 | 1,420,544 | 0 | none observed | 8,290 | 1,326 | $0.64 |
| audit | `root/architecture_review/data_jobs` | `session-018` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 116,276 | 1,089,792 | 0 | none observed | 7,423 | 1,194 | $0.54 |
| audit | `root/architecture_review/architecture_quality` | `session-016` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 12,935 | 108,288 | 0 | none observed | 3,230 | 1,129 | $0.09 |
| audit | `root/code_quality_review` | `session-004` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 10,779 | 1,372,416 | 0 | none observed | 4,411 | 1,460 | $0.87 |
| audit | `root/code_quality_review/code_quality_artifact_review` | `session-021` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 35,992 | 337,920 | 0 | none observed | 5,818 | 3,120 | $0.21 |
| audit | `root/product_value_review` | `session-010` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 193,934 | 6,643,968 | 0 | none observed | 49,230 | 3,796 | $5.77 |
| audit | `root/product_value_review/product_value_quality` | `session-025` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 51,375 | 285,440 | 0 | none observed | 5,703 | 2,782 | $0.23 |
| audit | `root/security_privacy_review` | `session-014` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 356,209 | 7,252,224 | 0 | none observed | 52,548 | 7,355 | $6.98 |
| audit | `root/security_privacy_review/identity_boundaries` | `session-031` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 186,120 | 2,549,504 | 0 | none observed | 10,415 | 3,636 | $1.01 |
| audit | `root/security_privacy_review/edge_runtime` | `session-030` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 75,678 | 1,063,424 | 0 | none observed | 6,842 | 2,271 | $0.45 |
| audit | `root/security_privacy_review/security_quality` | `session-032` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 51,612 | 285,696 | 0 | none observed | 3,464 | 1,470 | $0.20 |
| audit | `root/business_continuity_review` | `session-003` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 156,286 | 5,418,496 | 0 | none observed | 34,636 | 4,680 | $4.53 |
| audit | `root/business_continuity_review/recovery_dataops_alerting` | `session-020` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 83,211 | 766,464 | 0 | none observed | 6,621 | 1,893 | $0.40 |
| audit | `root/business_continuity_review/business_continuity_quality` | `session-019` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 46,298 | 265,728 | 0 | none observed | 5,159 | 2,287 | $0.21 |
| audit | `root/scalability_review` | `session-013` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 221,890 | 13,721,344 | 0 | none observed | 44,560 | 8,548 | $9.31 |
| audit | `root/scalability_review/scalability_quality` | `session-029` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 57,228 | 459,264 | 0 | none observed | 9,183 | 5,235 | $0.79 |
| audit | `root/expense_exposure_review` | `session-007` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 124,845 | 7,982,592 | 0 | none observed | 30,537 | 8,272 | $5.53 |
| audit | `root/expense_exposure_review/vendor_commercial_collector` | `session-024` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 60,536 | 388,608 | 0 | none observed | 4,543 | 862 | $0.25 |
| audit | `root/expense_exposure_review/expense_quality` | `session-023` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 25,820 | 125,952 | 0 | none observed | 3,097 | 1,398 | $0.11 |
| audit | `root/contributor_vendor_value_review` | `session-006` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 14,099 | 1,392,128 | 0 | none observed | 5,707 | 713 | $0.94 |
| audit | `root/maintenance_cost_review` | `session-009` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 13,654 | 941,056 | 0 | none observed | 3,880 | 1,153 | $0.66 |
| audit | `root/contributor_vendor_value_review/feature_contribution_collector` | `session-022` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 136,466 | 3,343,872 | 0 | none observed | 20,572 | 6,506 | $2.97 |
| audit | `root/contributor_value_quality` | `session-005` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 55,995 | 230,912 | 0 | none observed | 2,190 | 636 | $0.18 |
| audit | `root/maintenance_cost_quality` | `session-008` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 33,885 | 461,312 | 0 | none observed | 4,222 | 1,396 | $0.21 |
| audit | `root/revenue_risk_review` | `session-012` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 147,637 | 3,917,312 | 0 | none observed | 25,759 | 3,278 | $3.47 |
| audit | `root/revenue_risk_review/quality_review` | `session-028` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 78,083 | 181,760 | 0 | none observed | 3,504 | 1,496 | $0.23 |
| audit | `root/project_health_review` | `session-011` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 164,487 | 6,803,968 | 0 | none observed | 32,694 | 6,859 | $5.21 |
| audit | `root/project_health_review/github_history_collector` | `session-027` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 88,591 | 795,392 | 0 | none observed | 12,561 | 4,594 | $0.49 |
| audit | `root/project_health_review/artifact_quality` | `session-026` | `gpt-5.6-terra` | `standard` / `short` (declared/derived) | 92,013 | 755,712 | 0 | none observed | 7,003 | 2,407 | $0.42 |
| **audit subtotal** |  |  |  |  | **3,556,748** | **140,586,496** | **0** | none observed | **555,504** | **113,640** | **$95.94** |
| summary | `WGO audit coordinator` | `session-001` | `gpt-5.6-sol` | `standard` / `short` (declared/derived) | 159,377 | 2,762,240 | 0 | none observed | 13,513 | 1,613 | $2.58 |
| **summary subtotal** |  |  |  |  | **159,377** | **2,762,240** | **0** | none observed | **13,513** | **1,613** | **$2.58** |

Reasoning tokens are already included in output and are not billed twice. Exact
row costs and request identities remain in the linked pass evidence; positive
row values below half a cent can display as `$0.00` here.

## Model-By-Model Cost

| Model/provider | Service tier/context | Rate components or recorded-cost basis | Exact-evidence status | Displayed cost |
|---|---|---|---|---:|
| `gpt-5.6-sol` | `standard` / `short` | input $5.00, cached input $0.50, output $30.00 per million | `97.057630` exact; priced | $97.06 |
| `gpt-5.6-terra` | `standard` / `short` | input $2.00, cached input $0.20, output $12.00 per million | `5.9612736` exact; priced | $5.96 |
| **Total** | standard / short | Exact total rounded directly, not from displayed rows | `103.0189036` exact | **$103.02** |

## Reconciliation Status

**Final.** Pass A and pass B independently produced byte-identical 35-row
results with zero calculation issues. They attribute the root and all 31 audit
descendants, suppress the same 41 unchanged legacy usage echoes, and reconcile
an exact total of `$103.0189036`. The original failure was an adapter defect:
current Codex child lifecycle records correlate on `turn_id`, and current child
`session_meta.payload.id` identifies the child while `payload.session_id` may
retain the forked root.

## Limitations

This is an API-equivalent estimate, not a Codex subscription or OpenAI invoice.
The 1,381 counted usage states lack stable provider request IDs and therefore use
the disclosed `legacy-state:<session>:<turn>:<line>` identity fallback. That
fallback suppresses consecutive identical echoes but cannot distinguish two
genuinely separate consecutive requests with identical usage. Service tier is a
declared standard API-equivalent basis, context band is threshold-derived, and
provider billing differences, subscription economics, regional uplift, tool
charges, and other non-token charges are not represented. No cache-write tokens
were observed in included request records. Cost-calculation requests are excluded.
