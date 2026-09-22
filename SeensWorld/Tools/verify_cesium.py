"""Validate saved starter map without exposing Cesium credentials."""
import unreal
levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
assert levels.load_level('/Game/Maps/WorldMap')
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()
geos = [a for a in actors if isinstance(a, unreal.CesiumGeoreference)]
assert len(geos) == 1, 'Expected exactly one georeference'
geo = geos[0]
origin = geo.get_origin_longitude_latitude_height()
assert abs(origin.x - 106.7009) < 0.000001
assert abs(origin.y - 10.7769) < 0.000001
assert abs(origin.z) < 0.001
terrain = next(a for a in actors if isinstance(a, unreal.Cesium3DTileset))
assert terrain.get_editor_property('ion_asset_id') == 1
assert terrain.get_editor_property('georeference') == geo
overlays = terrain.get_components_by_class(unreal.CesiumIonRasterOverlay)
assert len(overlays) == 1 and overlays[0].get_editor_property('ion_asset_id') == 2
assert any(isinstance(a, unreal.CesiumSunSky) for a in actors)
pawn = next(a for a in actors if a.get_actor_label() == 'City Explorer')
assert pawn.get_editor_property('auto_possess_player') == unreal.AutoReceiveInput.PLAYER0
world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()
assert not world.get_world_settings().get_editor_property('enable_world_bounds_checks')
unreal.log('SEENS_VERIFY_PASS: saved HCMC origin, terrain, sun, pawn and world bounds verified')
