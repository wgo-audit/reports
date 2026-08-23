# Supply-Chain And Tooling Results

## Evidence Boundary

This source-bounded view covers `primary-code` at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, targeted public GitHub history effective by the 2026-08-22 22:08:28 EDT cutoff, and read-only tool checks performed after the cutoff ([E-040](../../evidence/evidence-ledger.md#e-040)–[E-042](../../evidence/evidence-ledger.md#e-042)). It does not establish private repository settings, scanner service results, registry controls, deployment, or runtime effectiveness. No package was installed or restored, no lockfile changed, and no dependency metadata was submitted externally.

## Evidence Dimensions Used

| Dimension | Position |
|---|---|
| Implementation | Present: workflows, Dependabot, lockfiles, Dockerfile, and release source. |
| History/rationale | Present: public PR #6186 and #6344, release `v3.2.1`, and GHSA records. |
| Observed operation | Partial: cutoff-bounded hosted records; private scan output, registry verification, and deployed artifact identity are unknown. |
| Ownership/approval | Partial: public review/merge metadata exists; internal security/release authority is unknown. |
| Specialist evidence | Unknown: Application Security, Cloud Security, and Compliance Assurance have not completed. |

## Current Source-Bounded Position

### Dependency And Build Controls

| Control | Source-bounded result | Limit or route |
|---|---|---|
| Dependency locks | `mix.lock` and three npm lockfiles are present; npm locks contain integrity fields. | Lock presence does not establish vulnerability status or reproducibility across every install script. |
| Automated updates | Dependabot schedules daily Mix, Docker, assets-npm, and tracker-npm checks and weekly Actions checks, with a seven-day cooldown. | `e2e/package-lock.json` has no matching version-update directory. Security-alert behavior/settings are not public; obtain proof through [OI-018](../open-items.md#oi-018). |
| Workflow actions | All 73 inspected `uses:` entries are pinned to 40-character commits. PR #6186 records the change. | Pinning reduces tag-movement risk but does not prove upstream review or runner isolation. |
| Container inputs | All three Dockerfile base stages are digest-pinned and runtime uses UID 999. | Alpine/Hex/npm content still resolves during builds; registry policy and rebuilt-image identity are unknown. |
| PR credential boundary | The tracker PR workflow checks out the PR head with `PLAUSIBLE_BOT_GITHUB_TOKEN`, retains credentials by default, then executes PR-controlled npm/compiler code. | Fork secrets may be withheld, but PAT scope and internal branch authority are unknown. Remove the reusable credential from this boundary through [OI-017](../open-items.md#oi-017); Application Security owns exploitability and Cloud Security owns repository/runner effectiveness. |
| NPM publication | The merged-PR workflow grants `id-token: write` and runs `npm publish` on a GitHub-hosted runner, consistent with its trusted-publishing comment. | It also uses the bot PAT for checkout/push; npm provenance and effective publisher settings were not observed. |

### Trust Anchors And Consuming Verifiers

| Produced or consumed anchor | Producer | Consuming verifier or consumer located | Verdict |
|---|---|---|---|
| Base-image SHA-256 digests | Upstream registries; fixed in `Dockerfile` | Docker build resolves `FROM ...@sha256:`. | `verified` for source consumption; registry/runtime identity unknown. |
| Per-platform image digests | `docker/build-push-action` output declaration | Workflow source wires digest artifacts through download into `docker buildx imagetools create` and declares manifest inspection. | `verified` only as source-visible producer-to-consumer wiring; no hosted run, produced manifest, signature verification, or deployed consumer was established. |
| npm integrity values | npm lockfile generation | npm install consumes package locks in visible workflows/builds. | `verified` as an integrity input; vulnerability status unknown. |
| Signature, SBOM, or provenance attestation | No producer found in the approved source set. | No consumer/verifier was locatable. | `finding`: no public source-visible chain; continue through [OI-003](../open-items.md#oi-003), without inferring absence in private delivery systems. |

### Scanner And Read-Only Check Results

Working directory for every command was `primary-code`. Installation/restoration authorization was **not granted**.

| Command/check | Intended coverage | Outcome | Bounded conclusion |
|---|---|---|---|
| `command -v osv-scanner gitleaks scorecard trivy semgrep` | Selected security-tool availability | 0 available; 5 unavailable | Five of five requested binaries were unavailable; no scanner result was produced. Absence is limited to this audit environment. |
| `npm --version` | Available npm client | `11.7.0` | Tool presence only. `npm audit` was not run because it would use a current post-cutoff service and submit dependency metadata externally. |
| Workflow `uses:` qualifier check | Action pin coverage | 73 passed; 0 failed; 0 errors; 0 skipped | All references used a 40-character commit; action contents were not validated. |
| Lockfile/Dependabot inventory | Declared package surfaces | Three npm locks plus `mix.lock`; five Dependabot entries | The `/e2e` npm version-update surface is not declared. Live security-alert state is unknown. |

No dependency, secret, image, or code scanner executed. Requested scanner binaries available: **0/5; unavailable: 5/5**. Separately, the source inventories completed with **73/73 action references commit-qualified** and three npm lockfiles/five Dependabot entries inventoried. SBOM and provenance were inspected as source-production/consumption questions, not treated as scans. No exploit attempt, load test, restore, install, or external submission was performed ([E-042](../../evidence/evidence-ledger.md#e-042)).

### Cutoff-Bounded Security Response

GHSA-mhcv-h7gf-57cf describes unauthenticated RCE in Community Edition versions 3.0 through 3.2.0 via Storybook. PR #6344 removed Storybook on 2026-05-12 after review and passing checks; release `v3.2.1` published the removal on 2026-05-15; the project advisory followed on 2026-06-03. The pinned source contains neither route nor dependency. This is strong public remediation evidence, but not proof every deployment upgraded, incident review occurred, or Cloud runs the fixed image ([E-041](../../evidence/evidence-ledger.md#e-041), [OI-003](../open-items.md#oi-003)).

## Material Unknowns And Closure Routes

- Obtain cutoff-valid vulnerability/dependency/secret scan definitions, coverage, results, triage, and exceptions; reconcile the public scan claim through [OI-018](../open-items.md#oi-018).
- Remove or constrain the bot credential at the PR-controlled execution boundary, prove its scope, and review history through [OI-017](../open-items.md#oi-017).
- Establish signed provenance/SBOM policy, registry verification, promotion, and live-image identity through [OI-003](../open-items.md#oi-003). Application Security owns dependency/source exploitability; Cloud Security owns repository, runner, registry, and deployment effectiveness.
