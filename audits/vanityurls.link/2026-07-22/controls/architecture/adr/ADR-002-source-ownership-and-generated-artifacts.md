# ADR-002: Source Ownership And Generated Artifacts

- Status: accepted
- Evidence cutoff: July 22, 2026

## Decision Statement

Product-maintained files live under `defaults/` and build/tooling paths, instance choices live under `custom/` and `wrangler.toml`, and `build/`, `src/`, and `functions/` are generated outputs that operators should not edit directly.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | The build copies defaults, overlays custom files, validates configuration, and emits runtime artifacts. | `scripts/build.mjs`; `scripts/lib/build-assets.mjs`; `docs/README.md` | Build was not executed. |
| Runtime/live state | Wrangler points to generated `src/worker.mjs` and `build/`. | `wrangler.toml` | Deployed artifact equivalence is unknown. |
| Rationale | Preserve upgrades while keeping instance changes separate and reviewable. | Source ADRs 0002, 0004, 0018 | Rationale is repository-authored, not independently approved. |
| Approval | Existing source ADRs mark the behavior accepted. | `docs/adr/0002-*`, `0004-*`, `0018-*` | Current maintainer reaffirmation is unknown. |

## Constraints, Options, And Tradeoffs

The overlay model makes an independent instance understandable and upgradable but creates a nontrivial build contract. Editing generated files may appear to work briefly and then be overwritten.

## Impacts And Boundaries

Maintainer onboarding must teach source ownership before code changes. Code Quality must verify build determinism and upgrade checks; Product Value must preserve visible behavior across defaults and overrides.

## Change, Reversal, And Follow-Up

Change only with migration tooling and updated upgrade/detach documentation. A third-party exercise should confirm that a clean checkout can regenerate the expected runtime without creator knowledge.
