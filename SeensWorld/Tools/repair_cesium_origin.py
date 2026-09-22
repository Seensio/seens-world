"""Consolidate the starter map onto one explicit Ho Chi Minh City origin."""
import unreal

levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
assert levels.load_level('/Game/Maps/WorldMap')
all_actors = actors.get_all_level_actors()
geos = [a for a in all_actors if isinstance(a, unreal.CesiumGeoreference)]
geo = next(a for a in geos if a.get_actor_label() == 'CesiumGeoreference_HoChiMinhCity')
geo.set_editor_property('tags', [unreal.Name('DEFAULT_GEOREFERENCE')])
geo.set_origin_longitude_latitude_height(unreal.Vector(106.7009, 10.7769, 0))
for actor in all_actors:
    if isinstance(actor, unreal.Cesium3DTileset):
        actor.set_editor_property('georeference', geo)
    for anchor in actor.get_components_by_class(unreal.CesiumGlobeAnchorComponent):
        anchor.set_editor_property('georeference', geo)
    if isinstance(actor, unreal.CesiumSunSky):
        actor.set_actor_location(unreal.Vector(), False, False)
        actor.set_editor_property('time_zone', 7.0)
        actor.set_editor_property('solar_time', 12.0)
        actor.update_sun()
        actor.get_editor_property('directional_light').set_editor_property('intensity', 10.0)
    if actor.get_actor_label() == 'City Explorer':
        actor.set_actor_location(unreal.Vector(0, 0, 150000), False, False)
        actor.set_actor_rotation(unreal.Rotator(pitch=-45, yaw=0, roll=0), False)
for duplicate in geos:
    if duplicate != geo:
        actors.destroy_actor(duplicate)
unreal.EditorLevelLibrary.set_level_viewport_camera_info(unreal.Vector(0, 0, 150000), unreal.Rotator(pitch=-45, yaw=0, roll=0))
assert levels.save_current_level()
assert len([a for a in actors.get_all_level_actors() if isinstance(a, unreal.CesiumGeoreference)]) == 1
unreal.log('SEENS_ORIGIN_REPAIRED: one HCMC origin; explicit actor references; Vietnam noon lighting')
