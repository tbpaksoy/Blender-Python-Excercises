import bpy


def AddVertexGroups(object: bpy.types.Object, armature: bpy.types.Armature, clearOld: bool):
    if clearOld:
        object.vertex_groups.clear()
    bones = bpy.data.armatures[armature.name].bones
    for bone in bones:
        object.vertex_groups.new(name=bone.name)


def AddVertexGroups(object: bpy.types.Object, names: [], clearOld: bool):
    if clearOld:
        object.vertex_groups.clear()
    for name in names:
        try:
            object.vertex_groups.new(name=name)
        except:
            print("Vertex group already exists.")
