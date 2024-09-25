import bpy
import math
import json
import os

def exportKeyframesJson(action_name):
    keyframes = {}
    action = bpy.data.actions[action_name]
    fileDir = os.path.dirname(bpy.data.filepath)
    
    if action is not None and action is not None:
        for fcu in action.fcurves:
            transformType = fcu.data_path + str(fcu.array_index)
            keyframes[transformType] = {}
            for keyframe in fcu.keyframe_points:
                keyframes[transformType][math.ceil(keyframe.co[0])] = keyframe.co[1]
    
    with open(fileDir + '/keyframes.json', 'w') as f:
        json.dump(keyframes, f, indent=2)
    
    return keyframes


selectedObj = bpy.context.selected_objects

# material node action
print(exportKeyframesJson(selectedObj[0].data.materials[0].node_tree.animation_data.action.name))

# object action
#print(exportKeyframesJson(selectedObj[0].animation_data.action.name))