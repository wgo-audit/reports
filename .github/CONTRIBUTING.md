# Contributing to WGO Reports

This repository is a **core-team showcase**: it publishes reports produced by the
[wgo-audit](https://github.com/wgo-audit/code) engine to demonstrate the tool. It is not a
place for external code contributions. The one recurring task is **adding a generated
report**, covered below.

## Rules

- **Reports are immutable.** Once a report is committed, never edit its contents. A
  re-audit is a **new** folder under a new evidence cutoff.
- **Never commit build junk** — dependency clones, rendered site output, a `tmp/` copy of
  the audited project, or an audited project's `.git/`.
- **Keep each folder self-contained** — `index.md` is always the entrypoint and
  `manifest.json` is always present.
- **Don't hand-edit generated files.** `README.md` (Reports table + badges), each
  `audits/<asset>/README.md`, and `audits/index.json` are produced by
  `scripts/build_index.py`; CI regenerates them and fails if a commit is out of date.

### manifest.json

Every report folder carries a `manifest.json` describing the audit. Minimum fields:

| Field | Purpose |
|---|---|
| `asset` | The audited asset, e.g. `vanityurls.link`. |
| `assetUrl` | Public URL for the asset; used to link its name on the per-asset page. Optional. |
| `evidenceCutoff` | ISO date the evidence was frozen. |
| `label` | Display name for the index, e.g. `Continuity & third-party operability (deep)`. |
| `highlights` | Key takeaways, one string per item — shown as bullets on the per-asset page. |
| `conclusions` | `question: answer` map — powers the per-asset "conclusions over time" matrix. |
| `sources` | List of `{repo, commit}` the audit was pinned to. |
| `generatedAt`, `generator`, `reviewers` | Provenance; fill when known. |

> **Not yet emitted by the engine.** The audit engine does not currently write
> `manifest.json` — it is added when the report is ingested (the script scaffolds one if
> the bundle lacks it). Automating this in the engine is tracked in
> [wgo-audit/code#3](https://github.com/wgo-audit/code/issues/3).

## Layout

Every report is a self-contained bundle at `audits/<asset>/<evidence-cutoff>/`:

```
audits/
└── <asset>/                        # the audited asset name
    └── <evidence-cutoff>/          # date the evidence was frozen (e.g., cutoff)
        ├── index.md                # START HERE — THE REPORT'S ENTRYPOINT
        ├── manifest.json           # machine-readable metadata
        ├── executive-summary.md    # the reconciled assessment and 30–90 day plan
        ├── controls/               # control-by-control analysis of each safeguard
        ├── evidence/               # evidence ledger and supporting packets
        ├── reviewer-reports/       # findings by review discipline
        └── operator-aids/          # how-to guides for a new operator to rebuild, recover, and monitor
```

- **`<asset>`** — one directory per audited asset; it groups every audit of that asset so
  the situation can be compared over time.
- **`<evidence-cutoff>`** — the ISO date the evidence was frozen (the "situation" the report
  describes). Compare along this axis, not the generation date; both are recorded in
  `manifest.json`.

## Adding a report

Always add a report with the script:

```bash
scripts/add-report.sh <bundle-dir-or-zip> --asset <asset> --cutoff <YYYY-MM-DD>
```

For example, ingesting the vanityurls.link bundle:

```bash
scripts/add-report.sh ~/Downloads/_whats-going-on.zip \
  --asset vanityurls.link --cutoff 2026-07-22
```

Review the result and commit the report.

### What the script does

1. Unpacks the bundle (or copies the directory) into a temporary area.
2. Strips cruft — `.DS_Store`, `__MACOSX/`, any `.git/` from the audited project, and any
   `tmp/` clone of the audited source.
3. Places the report verbatim at `audits/<asset>/<evidence-cutoff>/`, refusing to
   overwrite an existing one (reports are immutable). `<evidence-cutoff>` is the ISO date
   the evidence was frozen — not the generation date.
4. Scaffolds `manifest.json` if the bundle didn't include one, leaving `TODO` fields for
   you to fill.
5. Regenerates the index (`scripts/build_index.py`): the README Reports table and badges,
   every per-asset page, and `audits/index.json`.

It stops there without staging anything, and prints the `git` commands to review and
commit.
