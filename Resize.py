import bpy
import bpy_types
import math

def ResizeEdge(obj : bpy.types.Object, edgeIndex : int, length : float):
    edge = obj.data.edges[edgeIndex]
    v1 = obj.data.vertices[edge.vertices[0]].co
    v2 = obj.data.vertices[edge.vertices[1]].co
    center = (v1 + v2)/2
    v1 = (v1 - center).normalized() * length
    v2 = (v2 - center).normalized() * length
    obj.data.vertices[edge.vertices[0]].co = v1
    obj.data.vertices[edge.vertices[1]].co = v2
ResizeEdge(bpy.context.active_object, 0, 2.0)