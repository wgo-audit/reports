# API-Equivalent Audit Cost Estimate

**Status: Unreconciled.** Two independent `gpt-5.6-terra` calculations reconcile exactly for the 28 included sessions, producing an included-session subtotal of **$151.49**. This is not a complete audit total because one spawned audit collector lacks the terminal lifecycle event required to establish its frozen cutoff and remains excluded from the immutable manifest. This control is an API-equivalent estimate, not a Codex invoice.

## Pricing Basis And Rate Card

The frozen basis is the checked-in API rate card at `core:references/data/api-rate-card-2026-08-07.json`, dated 2026-08-07, USD, sourced from <https://platform.openai.com/docs/pricing>. All priced requests use the declared API-equivalent `standard` tier and threshold-derived `short` context band; those are reproducible assumptions, not observed backend billing attributes.

The formula is:

```text
uncached input × input rate + cached input × cached-input rate + output × output rate
```

Reasoning is an informational output subcomponent and is not charged again. No cache-write, regional, tool, subscription, or other non-token charge is inferred.

## Frozen Manifest And Exclusions

The public [calculation receipt](cost-calculation.json) preserves the frozen calculation result using audit-local aliases only. Temporary provider manifests and independent pass files are retained outside the public audit. Their source identifiers and storage locators are intentionally not published.

The frozen evidence contains 28 included sessions: the WGO audit root, 16 direct audit descendants, and 11 terminally correlated nested descendants. The source calculation verified each included boundary before the public alias-only receipt was produced.

| Excluded session | Reason |
|---|---|
| `excluded-session-001` (`feature_contribution_collector`) | Spawn provenance and task start exist, but no terminal lifecycle event establishes an immutable audit-task cutoff. Its usage is not guessed. |
| `excluded-session-002` (`cost_coordinator`) | Cost-calculation work begins after the frozen audit cutoff and is correctly outside the audit estimate. |

## Token Totals By Session And Model

| Session / WGO role | Model | Tier / band | Uncached input | Cached input | Output | Reasoning* | Cost |
|---|---|---|---:|---:|---:|---:|---:|
| `session-001` WGO audit coordinator | `gpt-5.6-sol` | standard / short | 2,097,534 | 85,129,728 | 176,728 | 38,616 | $58.35 |
| `session-001` WGO audit coordinator | `gpt-5.6-terra` | standard / short | 495,393 | 8,685,824 | 44,690 | 19,599 | $3.26 |
| `session-002` documentation preparation | `gpt-5.6-sol` | standard / short | 130,866 | 1,654,528 | 22,310 | 3,647 | $2.15 |
| `session-003` GitHub-history collector | `gpt-5.6-sol` | standard / short | 195,005 | 3,063,296 | 17,644 | 5,431 | $3.04 |
| `session-004` architecture reviewer | `gpt-5.6-sol` | standard / short | 203,239 | 9,629,440 | 44,610 | 6,885 | $7.17 |
| `session-025` architecture components | `gpt-5.6-sol` | standard / short | 154,414 | 2,740,736 | 12,136 | 2,376 | $2.51 |
| `session-026` architecture data/jobs | `gpt-5.6-sol` | standard / short | 124,694 | 2,691,072 | 15,812 | 2,281 | $2.44 |
| `session-027` architecture runtime | `gpt-5.6-sol` | standard / short | 119,705 | 2,184,448 | 12,088 | 2,830 | $2.05 |
| `session-028` architecture quality | `gpt-5.6-sol` | standard / short | 40,245 | 297,984 | 2,822 | 588 | $0.43 |
| `session-005` code-quality reviewer | `gpt-5.6-sol` | standard / short | 172,159 | 7,103,744 | 29,297 | 6,947 | $5.29 |
| `session-006` product-value reviewer | `gpt-5.6-sol` | standard / short | 200,865 | 6,378,752 | 40,723 | 4,402 | $5.42 |
| `session-007` security identity | `gpt-5.6-sol` | standard / short | 182,086 | 3,756,288 | 16,276 | 2,833 | $3.28 |
| `session-008` product-value quality | `gpt-5.6-sol` | standard / short | 93,826 | 1,809,664 | 8,565 | 2,729 | $1.63 |
| `session-009` code-quality artifact review | `gpt-5.6-sol` | standard / short | 64,118 | 590,848 | 7,964 | 3,359 | $0.85 |
| `session-010` security edge | `gpt-5.6-sol` | standard / short | 150,924 | 2,057,728 | 16,280 | 3,063 | $2.27 |
| `session-011` security supply chain | `gpt-5.6-sol` | standard / short | 228,053 | 5,447,168 | 23,838 | 6,086 | $4.58 |
| `session-012` security quality | `gpt-5.6-sol` | standard / short | 93,396 | 931,072 | 10,632 | 5,546 | $1.25 |
| `session-013` business-continuity reviewer | `gpt-5.6-sol` | standard / short | 660,856 | 13,344,000 | 46,273 | 8,375 | $11.36 |
| `session-014` expense-exposure reviewer | `gpt-5.6-sol` | standard / short | 221,766 | 6,596,864 | 22,808 | 4,448 | $5.09 |
| `session-015` expense quality | `gpt-5.6-sol` | standard / short | 116,161 | 1,408,768 | 11,053 | 6,350 | $1.62 |
| `session-016` scalability reviewer | `gpt-5.6-sol` | standard / short | 273,972 | 9,376,000 | 31,904 | 6,854 | $7.01 |
| `session-017` contributor/vendor reviewer | `gpt-5.6-sol` | standard / short | 194,709 | 9,223,680 | 36,369 | 6,271 | $6.68 |
| `session-018` maintenance-cost reviewer | `gpt-5.6-sol` | standard / short | 133,886 | 5,406,464 | 29,473 | 5,460 | $4.26 |
| `session-019` maintenance quality | `gpt-5.6-sol` | standard / short | 62,344 | 812,032 | 6,476 | 2,659 | $0.91 |
| `session-020` contributor/vendor quality | `gpt-5.6-sol` | standard / short | 64,230 | 1,069,312 | 8,394 | 2,697 | $1.11 |
| `session-021` revenue-risk reviewer | `gpt-5.6-sol` | standard / short | 129,600 | 3,224,064 | 25,697 | 5,067 | $3.03 |
| `session-022` revenue quality | `gpt-5.6-sol` | standard / short | 100,421 | 1,052,160 | 8,976 | 4,136 | $1.30 |
| `session-023` project-health reviewer | `gpt-5.6-sol` | standard / short | 115,690 | 2,610,688 | 18,748 | 2,780 | $2.45 |
| `session-024` project-health quality | `gpt-5.6-sol` | standard / short | 49,512 | 418,048 | 7,719 | 4,156 | $0.69 |

\* Reasoning is included within output and is shown only for transparency.

## Model-By-Model Cost

| Model | Tier / band | Uncached input | Cached input | Output | Reasoning* | Included-session subtotal |
|---|---|---:|---:|---:|---:|---:|
| `gpt-5.6-sol` | standard / short | 6,374,276 | 190,008,576 | 711,615 | 156,872 | $148.22 |
| `gpt-5.6-terra` | standard / short | 495,393 | 8,685,824 | 44,690 | 19,599 | $3.26 |
| **Included sessions** |  | **6,869,669** | **198,694,400** | **756,305** | **176,471** | **$151.49** |

## Reconciliation Status

The auditor explicitly authorized `gpt-5.6-terra` as the substitute for unavailable Luna verification workers. The two temporary passes were independently recomputed from the same frozen input and were byte-for-byte identical, SHA-256 `1049bb4a9b2ae666e3f350ff5dce270ac81e5b57e7cef5f7e12baa0eda238de2`. Their public, alias-only result is preserved in [the calculation receipt](cost-calculation.json):

- 1,726 accepted request states;
- 55 duplicate zero-usage echoes excluded;
- 0 request, schema, pricing, or hash issues; and
- identical token rows and included-session subtotal.

The status remains **Unreconciled** solely because the excluded `feature_contribution_collector` has no terminal lifecycle cutoff. The reported $151.49 is therefore a reconciled subtotal for the frozen included sessions, not a complete audit total. The exact fractional subtotal remains in the public receipt.

## Limitations

- The original portable recipe was incompatible with full-history fork logs: it counted inherited parent history and repeated cumulative-state echoes, and it validated the last inherited session metadata. The reconciled passes instead use each descendant's task boundary, validate its own metadata, and deduplicate unchanged cumulative request states.
- All 1,726 accepted records lack provider request IDs. Their identities are deterministic hashes of session, active turn, and complete cumulative-usage state; they cannot prove provider-level retry relationships.
- One spawned audit collector is excluded because its terminal lifecycle event is absent. No complete audit total is stated.
- The root cutoff was created when `wgo:cost` was invoked, after earlier audit-related follow-up discussion in the same root session. Those pre-marker root requests are included by the frozen WGO boundary.
- This is an API-equivalent estimate, not a Codex invoice. Declared tier/context assumptions, subscription treatment, backend pricing, regional uplift, tool charges, cache-write charges, and other non-token charges may differ.
