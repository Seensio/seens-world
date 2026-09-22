"""Build the starter map, resuming only an empty map from an interrupted run."""
import unreal
from pathlib import Path

MAP = '/Game/Maps/WorldMap'
unreal.AssetRegistryHelpers.get_asset_registry().scan_paths_synchronous(['/Game', '/CesiumForUnreal'], True)
pawn_class = unreal.load_class(None, '/CesiumForUnreal/DynamicPawn.DynamicPawn_C')
assert pawn_class, 'DynamicPawn unavailable'
levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
if (Path(unreal.Paths.project_content_dir()) / 'Maps/WorldMap.umap').exists():
    assert levels.load_level(MAP), 'Could not load WorldMap'
    existing = actors.get_all_level_actors()
    assert all(a.get_class().get_name() in ('WorldSettings', 'Brush', 'DefaultPhysicsVolume') for a in existing), 'Map contains work; refusing to overwrite it'
else:
    assert levels.new_level(MAP), 'Could not create WorldMap'
world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()
world.get_world_settings().set_editor_property('enable_world_bounds_checks', False)
geo = actors.spawn_actor_from_class(unreal.CesiumGeoreference, unreal.Vector())
geo.set_actor_label('CesiumGeoreference_HoChiMinhCity')
geo.set_editor_property('tags', [unreal.Name('DEFAULT_GEOREFERENCE')])
geo.set_origin_longitude_latitude_height(unreal.Vector(106.7009, 10.7769, 0.0))
sun = actors.spawn_actor_from_class(unreal.CesiumSunSky, unreal.Vector())
sun.set_actor_label('CesiumSunSky')
terrain = actors.spawn_actor_from_class(unreal.Cesium3DTileset, unreal.Vector())
terrain.set_actor_label('Cesium World Terrain')
terrain.set_editor_property('ion_asset_id', 1)
pawn = actors.spawn_actor_from_class(pawn_class, unreal.Vector(0, 0, 150000), unreal.Rotator(pitch=-35, yaw=0, roll=0))
pawn.set_actor_label('City Explorer')
pawn.set_editor_property('auto_possess_player', unreal.AutoReceiveInput.PLAYER0)
unreal.EditorLevelLibrary.set_level_viewport_camera_info(unreal.Vector(0, 0, 150000), unreal.Rotator(pitch=-45, yaw=0, roll=0))
assert levels.save_current_level(), 'WorldMap save failed'
unreal.log('SEENS_SETUP_COMPLETE: WorldMap saved at 10.7769 N, 106.7009 E')
