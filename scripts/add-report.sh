#!/usr/bin/env bash
# Add a generated report bundle to the showcase.
#
# Usage:
#   scripts/add-report.sh <bundle-dir|bundle.zip> [--asset <asset>] [--cutoff <YYYY-MM-DD>]
#
# What it does:
#   1. Unpacks/copies the bundle to a temp area and strips cruft
#      (.DS_Store, __MACOSX, nested .git, tmp/ clones of the audited project).
#   2. Reads --asset / --cutoff, falling back to the bundle's schema 1.0.0
#      manifest.json.
#   3. Copies the bundle to audits/<asset>/<cutoff>/ (refuses to overwrite —
#      reports are immutable).
#   4. Scaffolds manifest.json if the bundle didn't include one.
#   5. Regenerates the index (scripts/build_index.py).
#
# Then review the result and commit it yourself.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUNDLE=""; ASSET=""; CUTOFF=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --asset)  ASSET="${2:?}";  shift 2 ;;
    --cutoff) CUTOFF="${2:?}"; shift 2 ;;
    -h|--help) sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*) echo "unknown flag: $1" >&2; exit 2 ;;
    *) BUNDLE="$1"; shift ;;
  esac
done

[[ -n "$BUNDLE" ]] || { echo "error: bundle path required (see --help)" >&2; exit 2; }
[[ -e "$BUNDLE" ]] || { echo "error: no such bundle: $BUNDLE" >&2; exit 2; }

work="$(mktemp -d)"; trap 'rm -rf "$work"' EXIT
if [[ "$BUNDLE" == *.zip ]]; then
  unzip -q "$BUNDLE" -d "$work/src"
else
  mkdir -p "$work/src"; cp -R "$BUNDLE" "$work/src/"
fi
src="$work/src"

# Strip cruft before locating the report root.
find "$src" -name .DS_Store -delete
find "$src" -type d \( -name __MACOSX -o -name .git -o -name tmp \) -prune -exec rm -rf {} +

# The report root is the shallowest directory containing index.md.
bdir=""; best=9999
while IFS= read -r -d '' f; do
  depth="$(awk -F/ '{print NF}' <<<"$f")"
  if (( depth < best )); then best="$depth"; bdir="$(dirname "$f")"; fi
done < <(find "$src" -name index.md -print0)
[[ -n "$bdir" ]] || { echo "error: no index.md found in bundle" >&2; exit 1; }

mani="$bdir/manifest.json"
if [[ -f "$mani" ]] && command -v jq >/dev/null 2>&1; then
  [[ -n "$ASSET"  ]] || ASSET="$(jq -r '.subject.id // .asset // empty' "$mani")"
  [[ -n "$CUTOFF" ]] || CUTOFF="$(jq -r '.evidence.cutoff // .evidenceCutoff // empty' "$mani")"
fi
[[ -n "$ASSET" && -n "$CUTOFF" ]] || {
  echo "error: --asset and --cutoff are required (or set them in the bundle's manifest.json)" >&2
  exit 2
}
[[ "$CUTOFF" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || {
  echo "error: --cutoff must be an ISO date (YYYY-MM-DD), got: $CUTOFF" >&2; exit 2; }

dest="$ROOT/audits/$ASSET/$CUTOFF"
[[ ! -e "$dest" ]] || { echo "error: $dest already exists — reports are immutable" >&2; exit 1; }
mkdir -p "$dest"
cp -R "$bdir"/. "$dest"/

if [[ ! -f "$dest/manifest.json" ]]; then
  cat > "$dest/manifest.json" <<JSON
{
  "\$schema": "https://wgo-audit.com/schemas/manifest/1.0.0.json",
  "schemaVersion": "1.0.0",
  "report": {
    "id": "TODO-stable-report-id",
    "title": "TODO report title",
    "generatedAt": null,
    "language": "en",
    "entrypoint": "index.md",
    "headline": {
      "rating": "TODO",
      "statement": "TODO one-line evidence-supported conclusion"
    }
  },
  "subject": {
    "id": "$ASSET",
    "name": "TODO subject name",
    "kind": "software-project",
    "description": null,
    "canonicalUrl": null
  },
  "audit": {
    "type": "TODO-audit-type",
    "mode": "unknown",
    "depth": "custom"
  },
  "businessConcerns": [],
  "evidence": {
    "cutoff": "$CUTOFF",
    "sources": [],
    "accessBoundary": {
      "level": "unknown",
      "included": [],
      "excluded": []
    }
  },
  "execution": {
    "generator": {
      "name": "wgo-audit",
      "repository": "wgo-audit/code",
      "version": null,
      "commit": null
    },
    "reviewers": []
  },
  "relationships": {
    "previousAudit": null,
    "baseline": null,
    "comparesTo": [],
    "supersedes": null
  }
}
JSON
  echo "note: scaffolded manifest.json — fill in the TODO fields, then re-run build_index.py"
fi

python3 "$ROOT/scripts/build_index.py"

echo
echo "Added audits/$ASSET/$CUTOFF"
echo "Review it, then:  git add -A && git commit -m \"Add $ASSET $CUTOFF audit\""
