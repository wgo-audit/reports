# PDR-003: Git-Reviewed Link Management

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

Operators manage links, readable slugs, schedules, tags, ownership labels, and source policy in `custom/`; the `lnk` CLI validates write operations and can stage, commit, and push successful changes.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | A terminal workflow covers adding/listing/replacing links, splats, schedules, and policy. | LNK documentation | Usability and failure recovery unobserved. |
| Implementation | CLI and library source implement parsing, precedence, validation, Git actions, and dry-run options. | `scripts/lnk`; `scripts/blocklist-cli.mjs`; build/check source | Commands not run. |
| Runtime/demonstration | Generated registry is the CLI list source and Worker input. | Runtime registry source/docs | Generated instance output not inspected as an executed build. |
| Approval/specialist sign-off | Source ADR 0006 records readable random slugs. | `docs/adr/0006-*` | No operator acceptance study. |

## Constraints, Options, And Tradeoffs

Git-integrated writes improve traceability but make the CLI capable of external pushes; operators need clear previews, clean-worktree expectations, credentials, and rollback literacy.

## Impacts And Boundaries

Contributor onboarding and instance operation share tools but not authority. An independent operator can use the CLI in its own repository; takeover requires access to the existing repository/deploy connection.

## Change, Reversal, And Follow-Up

Retain dry-run/no-replace behavior and treat push semantics as an operational control. OI-004 should include add, replace, schedule, validation failure, and rollback tasks.
