# Contributing a city block

## Claim and prepare

1. Open or claim a GitHub issue for a city/block before starting. Record city ID, block ID, boundary coordinates, assigned contributor, and road connection points. Use stable lowercase IDs such as `ho-chi-minh-city`, `block-001`, and `corner-house`.
2. Record the current Hugging Face dataset commit hash in the issue so collaborators use the same baseline. Download that revision with `sync_assets.sh`.
3. Prepare one asset package under `SeensWorld/Content/RawImports/`. Keep unrelated work out of the package. Every file in it will be uploaded.

Example package:

```text
corner-house/
  README.md
  LICENSE
  building.glb
  textures/
    base-color.png
```

The package README must describe author/attribution, source and redistribution rights, city/block/asset IDs, geographic placement (latitude, longitude, elevation and its datum), orientation, dimensions, triangle count, texture sizes, and dependencies. For Unreal packages, also state engine/plugin versions and exact import/content paths. Include the actual applicable license text in LICENSE; do not assume a model uses the code repository's license.

Use metric scale (1 Unreal unit = 1 cm), a bottom-center footprint pivot at Z=0, FBX/glTF/GLB source geometry, standard PBR textures, and maximum 2048×2048 textures. Triangle counts are reported for review; no universal budget has been established yet. Automated geometry/texture validation is not implemented by these scripts.

## Preview and submit

Run from the repository root, or use absolute paths:

```sh
bash tools/submit_assets.sh SeensWorld/Content/RawImports/corner-house ho-chi-minh-city block-001 corner-house
```

This lists all files and the remote destination without contacting Hugging Face. It rejects missing README/LICENSE files, hidden content, symlinks, and common Unreal project/cache files. Inspect the list before uploading.

Log in with your own Hugging Face account and a token permitted to submit contributions to the dataset. Never add tokens to scripts, issues, or Git:

```sh
hf auth login
bash tools/submit_assets.sh SeensWorld/Content/RawImports/corner-house ho-chi-minh-city block-001 corner-house --submit
```

The upload creates a Hugging Face pull request at `cities/ho-chi-minh-city/blocks/block-001/corner-house`. Add its returned URL to the GitHub block issue. Repository permissions may require maintainer assistance; do not request a shared maintainer token. Re-running creates another review request, so coordinate revisions in the existing discussion. The script does not delete remote files; list obsolete files for maintainers to remove during review.

## Maintainer review and publication

1. Inspect the review diff, attribution/license, package scope, dependencies, mesh scale/pivot, geometry, and texture dimensions. Check that it does not overwrite another contributor's assigned asset ID.
2. Test the proposed dataset revision using `bash tools/sync_assets.sh refs/pr/<number>` in a separate project checkout, preserving existing local assets. Import raw geometry if needed and verify placement, road connections, and appearance in Unreal.
3. Merge the Hugging Face review request once accepted. Record the resulting dataset commit hash and asset path in the GitHub block issue and any associated code/map pull request.
4. Contributors download that published hash. Keep large models and textures inside the ignored asset directories. Review Git's staged file list before every commit; project-owned maps and Blueprints are intentional exceptions, not permission to commit community binaries elsewhere.

The GitHub change and dataset revision form a release pair. A future machine-readable dependency manifest can enforce this pairing; the current workflow records it in the block issue and pull request.
