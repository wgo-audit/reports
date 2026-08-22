# API-Equivalent Audit And Operationalization Cost Estimate

| Field | Value |
|---|---|
| Coverage | audit-and-operationalization |
| Reconciliation status | Final |
| Rate-card/basis date | 2026-08-07 |
| Currency | USD |
| Pricing basis | OpenAI API-equivalent token estimate; not a Codex invoice |

## Pricing Basis And Dated Data

The estimate uses the checked-in 2026-08-07 [OpenAI API pricing](https://platform.openai.com/docs/pricing) rate card in USD per one million tokens. The exact formula is `uncached input × input rate + cached input × cached-input rate + output × output rate`. Reasoning tokens are already an informational subcomponent of output and are not charged again.

The rollout records did not return a service tier, so every row uses the frozen `standard` API-equivalent basis; this does not identify Codex's actual backend tier. Every counted request was at or below the 272,000-input-token threshold and therefore uses the threshold-derived `short` context band. No geography or regional uplift is inferred. Exact decimals are preserved in the [public calculation receipt](cost-calculation.json); monetary values below are rounded half up independently.

## Frozen Manifest And Exclusions

The refreshed frozen input is represented publicly as `temporary-input-002` with SHA-256 `d2fce62922a9512b646640d7229352186c8e6e9bd5d3c9562ba7cdb983f6360c`. It contains 29 included sessions and extends the audit-only root through the explicit operationalization-complete marker. The prior [audit-only receipt](cost-calculation-audit-only.json) is preserved unchanged at exact total `84.9074346` USD. The refreshed public [receipt](cost-calculation.json) contains aliased session rows, prefix digests, exact token/cost rows, rate-card evidence, two-pass digests, and reconciliation results. Provider-native files and identifiers remain only under `tmp_debug/wgo-cost/` and are excluded from public audit artifacts.

### Phase Boundaries

| Phase | Session | Marker and record boundary | Included or excluded |
|---|---|---|---|
| unattributed | session-001 | Before onboarding marker at record 37 | Included |
| onboarding | session-001 | `WGO_PHASE_ONBOARDING_START` at record 37 | Included after marker |
| audit | session-001 | `WGO_PHASE_AUDIT_START` at record 439 | Included after marker |
| summary | session-001 | `WGO_PHASE_SUMMARY_START` at record 1864 | Included after marker |
| cost-estimation | session-001 | `WGO_AUDIT_COMPLETE_COST_PHASE_STARTS` at record 1949 | Excluded after marker |
| operationalization | session-001 | `WGO_PHASE_OPERATIONALIZATION_START` at record 2255 | Included after marker |
| cost-estimation | session-001 | `WGO_OPERATIONALIZATION_COMPLETE_COST_PHASE_STARTS` at record 2365 | Excluded; refreshed cutoff |

### Included Session Manifest

| Session | WGO role/task | Parent | Phase | Terminal boundary | Prefix SHA-256 |
|---|---|---|---|---|---|
| session-001 | Audit coordinator | none | from-markers | root cutoff at record 2365 | `c51f619ac5c9964978048e55bfa39dc54b1520ff9363fe1b290cd59f0cd9b8bd` |
| session-002 | Documentation catalog preparation | session-001 | onboarding | completed at record 93 | `0d48ceec1245c6872849d4ddcee2531b730ce511ffec6d7236ce4d930db0e327` |
| session-003 | Architecture reviewer | session-001 | audit | completed at record 515 | `bf4a09f1a07f51f56c989dff7d60614b43356f74b36eb5bea6f6105d05f3eefe` |
| session-004 | Code Quality reviewer | session-001 | audit | completed at record 708 | `c9a1c6871e00bc0b642a4917ca8c0fff81c0d8c71376afb0e84265b398b944a7` |
| session-005 | Product Value reviewer | session-001 | audit | completed at record 726 | `36efd1bf0c307c64892521e5be834b6c7d33fcd2559e8e8f0e94b569815a725b` |
| session-006 | Security and Privacy reviewer | session-001 | audit | completed at record 805 | `9520fcd37dedf6d587091236d3b27f2d9850a54eac9e4eb0b867b64fac42849a` |
| session-007 | Application Security reviewer | session-001 | audit | completed at record 836 | `a698c2b5ea14fd3b9bca3f6b99e1ac15bd6e4eedd4fd8345239d4a8b9c68369c` |
| session-008 | Business Continuity reviewer | session-001 | audit | completed at record 805 | `0df48808cec234233debf3a691c731b5f5f846007554d901f6b14d06f6fa6b5b` |
| session-009 | Cloud Security reviewer | session-001 | audit | completed at record 781 | `2aea850adc8e12204c33f3fbb9feda9adc064cfcfd7b65f0bc2611a4af8746b7` |
| session-010 | Expense Exposure reviewer | session-001 | audit | completed at record 843 | `d4b42907809f30b7baa68e4fb04cd1122a34ef57e62df3a7818f2b232001436c` |
| session-011 | Scalability reviewer | session-001 | audit | completed at record 847 | `83dce7bf1f5fb212ba6fd70eb70c9428addf52cf2bdd3dd400938a89fe15347e` |
| session-012 | Maintenance Cost reviewer | session-001 | audit | completed at record 798 | `b97fa92d466ae7637355ecd11ed228db7e7dffb717440bfdc741195cff9b5544` |
| session-013 | Contributor and Vendor Value reviewer | session-001 | audit | completed at record 979 | `8976f1088c064c1b58663bc9fff2b219039fbc35247e9f93e254cb0bc0be404e` |
| session-014 | Architecture artifact quality review | session-003 | audit | completed at record 99 | `bf67cbccdd3b14f4d6e2487a7cf2edab30aeddbb6848afbc0e5734565e4019ed` |
| session-015 | CI gate evidence collector | session-004 | audit | completed at record 82 | `a92d22f2e8b2bb8e59f39f7a3a96cc54299be68d8e56b0f4593a83008f60625f` |
| session-016 | Runtime and build quality evidence collector | session-004 | audit | completed at record 66 | `dc53a704a9116cdf4ee9cc6556b92cc5c3c7254f567d4dcc2754428d57c7903b` |
| session-017 | Code Quality artifact quality review | session-004 | audit | completed at record 69 | `6c6555c8e28c498ea675c99a7dafa2b69e14505d73f5d7e8e4a9bdba0196e54e` |
| session-018 | Product Value artifact quality review | session-005 | audit | completed at record 89 | `c81298372716c22b28780e8e144958b740955fccc1783409aa41a77220d1fff3` |
| session-019 | Security and Privacy artifact quality review | session-006 | audit | completed at record 270 | `e432dd17c61de2929da18d6961448c60ff68d8560ce7cf9c3bcdf5ad11ef7ef4` |
| session-020 | Application Security artifact quality review | session-007 | audit | completed at record 67 | `2d8cec6083b4a9f2375a74181f6a6bea5b610cd15db42955955f756e12d0d160` |
| session-021 | Recovery and data-operations evidence collector | session-008 | audit | completed at record 96 | `5b7e2c58e2eec984d7106ec204f5c1cadb6d5a3c1d9f89a7dce5bff9d6babdd5` |
| session-022 | Business Continuity artifact quality review | session-008 | audit | completed at record 57 | `c434426176f919225a842d7e44ecc95aab52fe248c8f2856ebc339b013e81113` |
| session-023 | Cloud Security artifact quality review | session-009 | audit | completed at record 55 | `e91aa96dfdbe9886aec7e6cfd30e7b9480e67111ab25c4c37e2d8c829c5080c3` |
| session-024 | Vendor and commercial evidence collector | session-010 | audit | completed at record 724 | `980f4847ac10d73a4db1217a5ec494c2bb4f48b4f48261c4c4d0caf63561448e` |
| session-025 | Expense Exposure artifact quality review | session-010 | audit | completed at record 732 | `656130d22c1709b5631eb83eb3b97c1bf229546ea928f2ce76b24629d50b675f` |
| session-026 | Scalability artifact quality review | session-011 | audit | completed at record 72 | `ed46f3eb1753e74e24c0103224bc48c1deef1fb1c9a8634d9eb230733135c378` |
| session-027 | Maintenance Cost artifact quality review | session-012 | audit | completed at record 82 | `433ab21464ae283c4e6a2b099b82243f1ce6d4e0aff1e1703f658fed0fb3057c` |
| session-028 | Feature contribution evidence collector | session-013 | audit | completed at record 125 | `1c3e98983ab37d2858c999f3fd40ccac5edc713ada1081fced8bbeeedc4de70d` |
| session-029 | Contributor and Vendor Value artifact quality review | session-013 | audit | completed at record 129 | `537b46427197e8842395f28cf953ac78cf987cf58639b393641c72e1ced4b7cf` |

### Session And Request Exclusions

| Session/request | Phase | Rationale |
|---|---|---|
| excluded-session-001 | cost-estimation | Earlier audit-only cost verification pass A; calculation work is outside audit-and-operationalization coverage. |
| excluded-session-002 | cost-estimation | Earlier audit-only cost verification pass B; calculation work is outside audit-and-operationalization coverage. |
| 53 in-prefix requests | cost-estimation | Requests between the audit-only cost marker and operationalization marker are excluded by frozen phase policy. |

The included session set is the recursively recorded WGO task tree, not a date-, directory-, workspace-, or model-based selection. Refreshed calculation requests occur after the root cutoff and are outside the manifest.

## Token Totals By Session And Model

| Phase | WGO role/task | Session | Model/provider | Service tier/basis | Uncached/new input | Cache read | Cache write | Output | Reasoning (informational) | Requests | Cost |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| audit | Audit coordinator | session-001 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 435,458 | 33,624,832 | 0 | 39,075 | 9,625 | 270 | $20.16 |
| audit | Architecture reviewer | session-003 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 192,285 | 5,551,616 | 0 | 26,775 | 3,577 | 46 | $4.54 |
| audit | Architecture artifact quality review | session-014 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 63,416 | 338,176 | 0 | 8,032 | 4,976 | 11 | $0.29 |
| audit | Code Quality reviewer | session-004 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 235,707 | 8,550,144 | 0 | 36,165 | 8,152 | 65 | $6.54 |
| audit | CI gate evidence collector | session-015 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 92,862 | 402,688 | 0 | 7,827 | 2,916 | 11 | $0.36 |
| audit | Runtime and build quality evidence collector | session-016 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 90,867 | 548,096 | 0 | 9,817 | 2,185 | 11 | $0.41 |
| audit | Code Quality artifact quality review | session-017 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 66,814 | 396,032 | 0 | 5,589 | 2,928 | 9 | $0.28 |
| audit | Product Value reviewer | session-005 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 309,022 | 6,327,296 | 0 | 34,312 | 5,718 | 61 | $5.74 |
| audit | Product Value artifact quality review | session-018 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 63,646 | 487,424 | 0 | 7,070 | 2,930 | 12 | $0.31 |
| audit | Security and Privacy reviewer | session-006 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 285,083 | 7,041,024 | 0 | 31,640 | 6,261 | 65 | $5.90 |
| audit | Security and Privacy artifact quality review | session-019 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 59,060 | 239,104 | 0 | 3,361 | 1,358 | 6 | $0.21 |
| audit | Application Security reviewer | session-007 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 272,093 | 6,917,632 | 0 | 23,734 | 4,941 | 67 | $5.53 |
| audit | Application Security artifact quality review | session-020 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 65,587 | 279,296 | 0 | 5,222 | 2,571 | 9 | $0.25 |
| audit | Business Continuity reviewer | session-008 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 210,259 | 7,153,664 | 0 | 28,939 | 5,032 | 52 | $5.50 |
| audit | Recovery and data-operations evidence collector | session-021 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 83,611 | 1,064,448 | 0 | 7,210 | 1,256 | 18 | $0.47 |
| audit | Business Continuity artifact quality review | session-022 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 52,237 | 396,800 | 0 | 2,561 | 1,115 | 10 | $0.21 |
| audit | Cloud Security reviewer | session-009 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 174,943 | 4,872,960 | 0 | 23,203 | 4,359 | 41 | $4.01 |
| audit | Cloud Security artifact quality review | session-023 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 24,870 | 120,576 | 0 | 3,388 | 2,263 | 5 | $0.11 |
| audit | Expense Exposure reviewer | session-010 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 166,708 | 4,792,832 | 0 | 24,976 | 5,942 | 42 | $3.98 |
| audit | Vendor and commercial evidence collector | session-024 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 122,301 | 1,458,688 | 0 | 7,719 | 2,578 | 18 | $0.63 |
| audit | Expense Exposure artifact quality review | session-025 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 47,937 | 354,560 | 0 | 4,585 | 2,409 | 7 | $0.22 |
| audit | Scalability reviewer | session-011 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 195,681 | 4,852,992 | 0 | 24,037 | 4,560 | 39 | $4.13 |
| audit | Scalability artifact quality review | session-026 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 65,756 | 413,952 | 0 | 4,052 | 1,736 | 11 | $0.26 |
| audit | Maintenance Cost reviewer | session-012 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 146,463 | 2,073,856 | 0 | 21,324 | 3,624 | 23 | $2.41 |
| audit | Maintenance Cost artifact quality review | session-027 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 55,508 | 414,976 | 0 | 6,002 | 2,936 | 11 | $0.27 |
| audit | Contributor and Vendor Value reviewer | session-013 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 211,190 | 7,161,856 | 0 | 33,157 | 8,556 | 52 | $5.63 |
| audit | Feature contribution evidence collector | session-028 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 89,972 | 964,864 | 0 | 14,500 | 5,907 | 19 | $0.55 |
| audit | Contributor and Vendor Value artifact quality review | session-029 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 114,989 | 1,223,424 | 0 | 8,577 | 4,299 | 21 | $0.58 |
| **audit subtotal** |  |  |  |  | **3,994,325** | **108,023,808** | **0** | **452,849** | **114,710** | **1,012** | **$79.46** |
| onboarding | Audit coordinator | session-001 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 227,833 | 2,838,784 | 0 | 20,904 | 6,850 | 59 | $3.19 |
| onboarding | Documentation catalog preparation | session-002 | gpt-5.6-terra / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 46,471 | 440,064 | 0 | 12,126 | 3,163 | 13 | $0.33 |
| **onboarding subtotal** |  |  |  |  | **274,304** | **3,278,848** | **0** | **33,030** | **10,013** | **72** | **$3.51** |
| operationalization | Audit coordinator | session-001 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 144,899 | 2,298,368 | 0 | 15,269 | 2,462 | 22 | $2.33 |
| **operationalization subtotal** |  |  |  |  | **144,899** | **2,298,368** | **0** | **15,269** | **2,462** | **22** | **$2.33** |
| summary | Audit coordinator | session-001 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 87,523 | 1,761,792 | 0 | 13,492 | 1,250 | 18 | $1.72 |
| **summary subtotal** |  |  |  |  | **87,523** | **1,761,792** | **0** | **13,492** | **1,250** | **18** | **$1.72** |
| unattributed | Audit coordinator | session-001 | gpt-5.6-sol / OpenAI | standard (declared API-equivalent); short (threshold-derived) | 26,259 | 86,784 | 0 | 1,226 | 292 | 5 | $0.21 |
| **unattributed subtotal** |  |  |  |  | **26,259** | **86,784** | **0** | **1,226** | **292** | **5** | **$0.21** |

Codex reports reasoning within output. The reasoning column is informational and is never added a second time. All included requests reported zero cache-write tokens.

## Model-By-Model Cost

| Model/provider | Service tier/context | Rate components or recorded-cost basis | Exact-evidence status | Displayed cost |
|---|---|---|---|---:|
| gpt-5.6-sol / OpenAI | standard declared; short derived | input $5.00/M; cached input $0.50/M; output $30.00/M | Priced; exact decimal in receipt | $81.51 |
| gpt-5.6-terra / OpenAI | standard declared; short derived | input $2.00/M; cached input $0.20/M; output $12.00/M | Priced; exact decimal in receipt | $5.73 |
| **Total** |  | Exact reconciled total `87.2391836` USD, rounded directly | Final | **$87.24** |

The operationalization increment is exactly `2.331749` USD; it is the difference between the refreshed total and the preserved audit-only total, with both exact values calculated before rounding.

## Reconciliation Status

**Final.** Two independent Terra/high passes over the same immutable refreshed manifest were byte-identical and produced 33 session/model/phase rows, zero calculation issues, and the exact total `87.2391836` USD. Both pass-result SHA-256 values are `32f32e50df6ee6e764342280f2fb5a7f51c264ae1f7c94eceb283d6339dd2fd6`. The prescribed fallback suppressed 21 consecutive unchanged legacy-state echoes.

No included session, event, usage field, or pricing input is disputed. The 53 excluded root-prefix requests are explicitly attributed to the earlier cost-estimation phase. The earlier audit-only calculation and its input digest remain preserved for traceability.

## Limitations

- This is an API-equivalent estimate of recorded model requests, not a Codex invoice, subscription charge, or statement of OpenAI's actual backend service tier.
- The inspected schema exposed no stable provider request IDs for 1,129 counted usage states. The required deterministic legacy-state fallback counts changed per-turn states and suppresses consecutive identical echoes, but cannot distinguish two genuinely separate requests with identical usage state.
- `standard` is the declared API-equivalent tier because no returned tier was present. `short` is derived per request from the recorded input-token threshold, not from an observed billing band.
- Token pricing excludes subscription allocation, tool charges, taxes, regional-processing uplift, and other non-token amounts. No rate is inferred for those items.
- All observed included cache-write tokens were zero. Reasoning tokens are part of output and are shown but not double-counted.
- Unattributed requests before the onboarding marker are included by frozen phase policy rather than assigned from timestamps or command text.
- The exact total and rows are in the public receipt. Displayed monetary values are rounded half up independently, so displayed rows must not be summed to reproduce the exact total.
- The refreshed root cutoff precedes this calculation; every refreshed manifest-verification, reconciliation, and report-writing request is excluded.
