#!/bin/bash
set -euo pipefail

usage() {
  echo 'Usage: bash tools/submit_assets.sh <package-directory> <city-id> <block-id> <asset-id> [--submit]'
  echo 'Previews by default. --submit uploads a new Hugging Face review request.'
}
if [[ ${1:-} == --help ]]; then usage; exit 0; fi
if [[ $# -lt 4 || $# -gt 5 ]]; then usage >&2; exit 2; fi
if [[ $# -eq 5 && $5 != --submit ]]; then usage >&2; exit 2; fi
for id in "$2" "$3" "$4"; do
  [[ $id =~ ^[a-z0-9][a-z0-9_-]*$ ]] || { echo 'IDs must use lowercase letters, digits, underscores or hyphens.' >&2; exit 2; }
done
[[ -d $1 ]] || { echo 'Package directory does not exist.' >&2; exit 2; }
package="$(cd "$1" && pwd)"
[[ -s "$package/README.md" && -s "$package/LICENSE" ]] || {
  echo 'Package must contain a nonempty README.md and LICENSE. See CONTRIBUTING.md.' >&2; exit 2;
}
# Upload a deliberately prepared package, never a project tree or hidden cache.
bad="$(find "$package" \( -type l -o -name '.*' -o -name '*.uproject' -o -name Binaries -o -name Intermediate -o -name Saved -o -name DerivedDataCache \) -print)"
[[ -z $bad ]] || { printf 'Remove symlinks, hidden files, or project/cache content before submitting:\n%s\n' "$bad" >&2; exit 2; }
target="cities/$2/blocks/$3/$4"
printf 'Dataset: seensio/seens-assets\nSource: %s\nDestination: %s\nFiles:\n' "$package" "$target"
find "$package" -type f -print
if [[ ${5:-} != --submit ]]; then
  echo 'Preview only. Review all files, then repeat with --submit to open a review request.'
  exit 0
fi
command -v hf >/dev/null 2>&1 || { echo 'Missing hf CLI. Install huggingface_hub (see README).' >&2; exit 1; }
hf upload seensio/seens-assets "$package" "$target" --repo-type dataset --create-pr \
  --commit-message "Submit $2 / $3 / $4"
echo 'Submission complete. Use the review URL above; a maintainer must approve and merge it.'
