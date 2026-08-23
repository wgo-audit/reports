# Application Security Handoff

## Confirmed Navigation

Use the [report](report.md), [attack-path view](../../controls/application-security/attack-path-and-control-view.md), [dependency/build note](../../controls/application-security/dependency-and-build-input-exploitability.md), and direct [E-043–E-045](../../evidence/evidence-ledger.md#e-043).

## Constraints And Conflicts

Source confirms conditional Sentry disclosure, permissive analytics integrity, a bot credential crossing PR-controlled code, and a Browserless validation/fetch mismatch. No exploit, scanner, tenant, runner, network, registry, or deployment validation ran.

## Material Unknowns

Close OI-015–OI-020 plus linked OI-003/OI-007/OI-013. Storybook is fixed in pinned source; affected deployment and incident closure remain unknown.

## Downstream Use

Cloud Security may use application boundaries but must not infer live control effectiveness. Compliance Assurance may map requirements but must not infer certification. Public GitHub issues, PRs, advisory, release, and discussion were inspected where relevant.
