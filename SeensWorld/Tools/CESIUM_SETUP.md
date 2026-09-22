# Ho Chi Minh City starter map

Open `/Game/Maps/WorldMap` in Unreal. This is the editor startup and game default map.

- Origin: longitude 106.7009, latitude 10.7769, ellipsoid height 0 metres.
- Cesium World Terrain: ion asset 1, using the developer's project default token.
- Cesium SunSky and globe-aware DynamicPawn, initially 1,500 metres above the origin.
- World bounds checks disabled for globe navigation.

The origin is a starting reference near central District 1, not a surveyed building position. Terrain elevations determine ground level; the origin height is not a claim about local ground elevation.

## Local connection

In Window > Cesium, connect your ion account. Select Token and create or select a project default token with access to Cesium World Terrain. Save the settings asset and reopen WorldMap. Account login and the project streaming token are separate steps.

`Content/CesiumSettings/` is intentionally ignored because it can contain a developer's token. Each contributor must configure their own token. Never place token strings in map actors or tracked configuration files.

The map includes Cesium World Terrain with Bing aerial imagery (ion asset 2). Terrain and imagery were verified in the live editor over Ho Chi Minh City. OSM buildings, editable roads, and community blocks have not been added yet.

The current editing view uses noon in UTC+7 and a reduced sunlight intensity of 10 lux for the initial exposure setup; this is not a physically calibrated lighting baseline.

After creating a new starter map, run `finish_live_cesium.py` inside the open WorldMap to add imagery and save a downward overview camera. Each developer needs token access to both ion assets 1 and 2.

## Scripts

`setup_cesium.py` builds the starter map and only resumes an empty map from an interrupted run. It refuses to overwrite a populated map. `verify_cesium.py` checks persisted actors and geographic settings; it does not certify streaming credentials or rendered appearance.

Run scripts through Unreal's Python scripting commandlet with PythonScriptPlugin and EditorScriptingUtilities enabled. Use the main UnrealEditor app executable on this Mac; the separate UnrealEditor-Cmd executable failed to load CesiumRuntime. Run from the SeensWorld repository and keep logs under Saved/Logs.
