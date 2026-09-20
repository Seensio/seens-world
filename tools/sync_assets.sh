#!/bin/bash
echo "Syncing 3D assets from Hugging Face (seensio/seens-assets)..."
huggingface-cli download seensio/seens-assets \
  --repo-type dataset \
  --local-dir ./SeensWorld/Content/CommunityAssets
echo "Sync complete!"