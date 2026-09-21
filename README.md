# SeensWorld (seens.io)

Rebuilding the world, one scene at a time. An open-source Earth-building project in Unreal Engine: contributors adopt city blocks and replace placeholder buildings with local detail.

## Code and assets

- Git stores code, configuration, documentation, automation, and project-owned maps/Blueprints.
- [Hugging Face asset dataset](https://huggingface.co/datasets/seensio/seens-assets) stores community models, textures, and community Unreal asset packages.
- `SeensWorld/Content/CommunityAssets/` is the ignored download destination. `SeensWorld/Content/RawImports/` is ignored staging space for submissions.

Folder placement determines Git exclusion. Large assets elsewhere are **not** automatically blocked. Maps and Blueprints are binary too: keep these intentional and small; review a separate Git LFS policy before scaling their use.

## Setup

Install Unreal Engine and a compatible Cesium for Unreal plugin. The project currently declares UE 5.8; engine/plugin compatibility must be verified on your machine.

Install the Hugging Face CLI in an isolated environment (requires Python 3 and pip):

```sh
python3 -m venv ~/.venvs/seens-assets
source ~/.venvs/seens-assets/bin/activate
python -m pip install --upgrade huggingface_hub
hf --help
```

From the repository root:

```sh
bash tools/sync_assets.sh
```

You can invoke the script by absolute path from any directory. Public dataset downloads normally require no login. For reproducible work, pass the dataset commit hash recorded in the block's task:

```sh
bash tools/sync_assets.sh <dataset-commit-hash>
```

This downloads and updates files; it does not remove stale files. Save local work separately before downloading, because matching paths may be replaced. Use a clean asset folder when testing an exact release. No automatic schedule is installed.

Open `SeensWorld/SeensWorld.uproject`. Raw FBX/glTF/GLB files still need importing in Unreal; downloading them does not create Unreal assets. For packaged `.uasset` content, preserve its documented `/Game/CommunityAssets/...` paths and use the matching engine version.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for block ownership, package standards, preview/submission commands, and maintainer review.

Scripts use the [official Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/en/guides/cli). Downloads fail with a nonzero exit status when the CLI fails. Submissions always create a review request instead of committing directly to the published branch.
