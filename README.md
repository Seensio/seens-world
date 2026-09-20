# Seens: Open World (seens-core)

Rebuilding the world, one scene at a time. Seens is an open-source, community-driven 3D sandbox and urban massing platform built in Unreal Engine 5.

## Repository Architecture
To keep version control fast and lightweight, this repository strictly tracks engine logic, Blueprints, C++ code, and configuration files.

**Do not push heavy binary assets (.uasset, .fbx, textures) directly to this Git repository.**
All 3D models, textures, and massive datasets are routed through our [Hugging Face Dataset / Asset Hub].

## Local Setup (Mac Studio / PC)
1. Clone this repository to your fast local SSD.
2. [Instructions for downloading the Hugging Face asset pack will go here]
3. Generate project files and launch in Unreal Engine 5.
