#!/bin/bash
set -euo pipefail

if [[ $# -gt 1 || ${1:-} == --help ]]; then
  echo 'Usage: bash tools/sync_assets.sh [revision]'
  echo 'Downloads published assets; revision defaults to main. Use a commit hash for reproducibility.'
  [[ ${1:-} == --help ]] && exit 0
  exit 2
fi
command -v hf >/dev/null 2>&1 || { echo 'Missing hf CLI. Install huggingface_hub (see README).' >&2; exit 1; }
root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
destination="$root/SeensWorld/Content/CommunityAssets"
echo "Downloading seensio/seens-assets at ${1:-main} into $destination"
hf download seensio/seens-assets --repo-type dataset --revision "${1:-main}" --local-dir "$destination"
echo 'Download complete. Local files absent from the dataset are not deleted.'
