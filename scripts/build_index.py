#!/usr/bin/env python3
"""Regenerate the report index from manifest.json files.

Reads every audits/<asset>/<cutoff>/manifest.json and rewrites, idempotently:
  - the BADGES and REPORTS blocks in README.md (between HTML-comment markers)
  - audits/<asset>/README.md   (per-asset timeline + conclusions-over-time matrix)
  - audits/index.json          (machine-readable catalog)

Run it after adding or editing a report, then commit the result. CI runs the
same script and fails if anything is out of date (see .github/workflows/reindex.yml).

Standard library only — no third-party dependencies.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDITS = ROOT / "audits"
README = ROOT / "README.md"
REPO = "wgo-audit/reports"


def load_reports() -> list[dict]:
    reports = []
    for manifest in sorted(AUDITS.glob("*/*/manifest.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["_dir"] = manifest.parent.relative_to(ROOT).as_posix()
        data["_asset"] = manifest.parent.parent.name
        data["_cutoff"] = manifest.parent.name
        reports.append(data)
    return reports


def esc(value) -> str:
    return str(value).replace("|", "\\|")


def label(report: dict) -> str:
    if report.get("label"):
        return report["label"]
    kind = str(report.get("auditType", "audit")).replace("-", " ")
    depth = report.get("depth")
    return f"{kind} ({depth})" if depth else kind


def group_by_asset(reports: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for report in reports:
        grouped.setdefault(report["_asset"], []).append(report)
    for rs in grouped.values():
        rs.sort(key=lambda r: r["_cutoff"], reverse=True)
    return grouped


def reports_section(reports: list[dict]) -> str:
    if not reports:
        return "_No reports published yet._\n"
    rs = sorted(reports, key=lambda r: r["_cutoff"], reverse=True)
    rs = sorted(rs, key=lambda r: r["_asset"])
    out = ["| Asset | Evidence cutoff | Audit |", "|---|---|---|"]
    for r in rs:
        asset_link = f'[{r["_asset"]}](audits/{r["_asset"]}/README.md)'
        cutoff_link = f'[{r["_cutoff"]}]({r["_dir"]}/index.md)'
        out.append(f'| {asset_link} | {cutoff_link} | {esc(label(r))} |')
    return "\n".join(out).rstrip() + "\n"


def badges_block(reports: list[dict]) -> str:
    # Raw HTML (not markdown, which wouldn't parse next to the banner block),
    # left-aligned, matching the org profile's flat-square + dark-label + teal.
    n = len(reports)
    style = "style=flat-square&labelColor=111827"
    accent = "2DD4BF"
    return (
        f'<a href="#reports"><img alt="Reports" '
        f'src="https://img.shields.io/badge/Reports-{n}-{accent}?{style}"></a>\n'
        f'<a href="https://github.com/{REPO}/commits/main"><img alt="Last commit" '
        f'src="https://img.shields.io/github/last-commit/{REPO}?{style}&color={accent}&label=Last%20commit"></a>\n'
        f'<a href="LICENSE.md"><img alt="License" '
        f'src="https://img.shields.io/github/license/{REPO}?{style}&color={accent}"></a>\n'
    )


def replace_block(text: str, name: str, content: str) -> str:
    start, end = f"<!-- {name}:START -->", f"<!-- {name}:END -->"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if not pattern.search(text):
        raise SystemExit(f"marker <!-- {name} --> not found in README.md")
    return pattern.sub(f"{start}\n{content}{end}", text)


def per_asset_readme(asset: str, rs: list[dict]) -> str:
    asset_url = next((r.get("assetUrl") for r in rs if r.get("assetUrl")), None)
    asset_ref = f"[{asset}]({asset_url})" if asset_url else asset
    out = [
        f"# {asset}",
        "",
        f"Point-in-time audits of {asset_ref}, newest first. Each row is a frozen "
        "snapshot; read across the columns below to see how the situation changes "
        "over time.",
        "",
        "| Evidence cutoff | Audit |",
        "|---|---|",
    ]
    for r in rs:
        link = f'[{r["_cutoff"]}]({r["_cutoff"]}/index.md)'
        out.append(f'| {link} | {esc(label(r))} |')
    out.append("")

    keys: list[str] = []
    for r in rs:
        for key in (r.get("conclusions") or {}):
            if key not in keys:
                keys.append(key)
    highlights = rs[0].get("highlights") or [] if rs else []
    if keys or highlights:
        out.append("## Conclusions over time")
        out.append("")
        for item in highlights:
            out.append(f"- {item}")
        if highlights:
            out.append("")
        if keys:
            out.append("| Question | " + " | ".join(r["_cutoff"] for r in rs) + " |")
            out.append("|" + "---|" * (len(rs) + 1))
            for key in keys:
                cells = [esc(key)]
                for r in rs:
                    cells.append(esc((r.get("conclusions") or {}).get(key, "—")))
                out.append("| " + " | ".join(cells) + " |")
            out.append("")
    return "\n".join(out).rstrip() + "\n"


def index_json(reports: list[dict]) -> dict:
    items = []
    for r in sorted(reports, key=lambda r: (r["_asset"], r["_cutoff"]), reverse=True):
        items.append({
            "asset": r["_asset"],
            "evidenceCutoff": r["_cutoff"],
            "path": r["_dir"],
            "label": label(r),
            "highlights": r.get("highlights", []),
            "generatedAt": r.get("generatedAt"),
        })
    return {"count": len(items), "reports": items}


def main() -> None:
    reports = load_reports()

    text = README.read_text(encoding="utf-8")
    text = replace_block(text, "BADGES", badges_block(reports))
    text = replace_block(text, "REPORTS", reports_section(reports))
    README.write_text(text, encoding="utf-8")

    for asset, rs in group_by_asset(reports).items():
        (AUDITS / asset / "README.md").write_text(
            per_asset_readme(asset, rs), encoding="utf-8"
        )

    (AUDITS / "index.json").write_text(
        json.dumps(index_json(reports), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"indexed {len(reports)} report(s)")


if __name__ == "__main__":
    main()
