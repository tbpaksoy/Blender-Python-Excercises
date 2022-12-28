import bpy
import bpy_types
import mathutils


def GetFaceCenter(obj: bpy.types.Object, faceIndex: int) -> mathutils.Vector:
    vertices = [
        obj.data.vertices[i].co for i in obj.data.polygons[faceIndex].vertices]
    sum = mathutils.Vector()
    for v in vertices:
        sum += v
    return sum / len(vertices)

print(GetFaceCenter(bpy.context.active_object, 0))
