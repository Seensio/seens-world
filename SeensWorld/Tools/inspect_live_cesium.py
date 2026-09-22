import unreal
from pathlib import Path
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()
terrain = next(a for a in actors if isinstance(a, unreal.Cesium3DTileset))
methods = [n for n in dir(terrain) if 'component' in n]
Path(unreal.Paths.project_saved_dir(), 'cesium_live_inspection.txt').write_text('\n'.join(methods))
unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).set_level_viewport_camera_info(unreal.Vector(0, 0, 150000), unreal.Rotator(pitch=-60, yaw=0, roll=0))
unreal.log('SEENS_LIVE_CAMERA_SET')
