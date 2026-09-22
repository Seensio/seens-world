"""Apply the city overview and imagery in the already-open WorldMap."""
import unreal
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()
terrain = next(a for a in actors if isinstance(a, unreal.Cesium3DTileset))
subsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
if not terrain.get_components_by_class(unreal.CesiumIonRasterOverlay):
    handles = subsystem.k2_gather_subobject_data_for_instance(terrain)
    handle, reason = subsystem.add_new_subobject(unreal.AddNewSubobjectParams(parent_handle=handles[0], new_class=unreal.CesiumIonRasterOverlay))
    data = unreal.SubobjectDataBlueprintFunctionLibrary.get_data(handle)
    overlay = unreal.SubobjectDataBlueprintFunctionLibrary.get_object(data)
    assert overlay, str(reason)
    overlay.set_editor_property('ion_asset_id', 2)
    overlay.set_editor_property('material_layer_key', 'Overlay0')
rotation = unreal.Rotator(pitch=-60, yaw=0, roll=0)
editor = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
editor.set_level_viewport_camera_info(unreal.Vector(0, 0, 150000), rotation)
for actor in actors:
    if actor.get_actor_label() == 'City Explorer':
        actor.set_actor_rotation(rotation, False)
assert unreal.get_editor_subsystem(unreal.LevelEditorSubsystem).save_current_level()
unreal.log('SEENS_LIVE_FINISH: city overview and ion imagery configured')
