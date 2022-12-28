import bpy
import mathutils
import math


def PlaceAlongEdge(obj: bpy.types.Object, edgeIndex: int, objectToPlace: bpy.types.Object, count: int, scale: mathutils.Vector = (1, 1, 1), alongNormal: bool = False):
    edge = obj.data.edges[edgeIndex]
    rv = [obj.data.vertices[v] for v in edge.vertices]
    ptp = [rv[0].co + (rv[1].co - rv[0].co) * (float(i) / float(count - 1))
           for i in range(count)]
    copies = []
    for v in ptp:
        temp = objectToPlace.copy()
        copies.append(temp)
        bpy.context.collection.objects.link(temp)
        temp.location = v
        temp.scale = scale
    if alongNormal:
        dir = (rv[1].co - rv[0].co)
        norm = math.sqrt(dir[0] ** 2 + dir[1] ** 2 + dir[2] ** 2)
        normAngle = [dir[0] / norm, dir[1] / norm, dir[2] / norm]
        for o in copies:
            o.rotation_euler = normAngle


def PlaceAlongEdge(obj: bpy.types.Object, edgeIndex: int, objectToPlace: bpy.types.Object, distance: float, scale: mathutils.Vector = (1, 1, 1), alongNormal: bool = False):
    edge = obj.data.edges[edgeIndex]
    rv = [obj.data.vertices[v] for v in edge.vertices]
    count = int((rv[1].co - rv[0].co).magnitude / distance)
    print(count)
    ptp = [rv[0].co + (rv[1].co - rv[0].co).normalized() * i * distance
           for i in range(count)]
    copies = []
    for v in ptp:
        temp = objectToPlace.copy()
        copies.append(temp)
        bpy.context.collection.objects.link(temp)
        temp.location = v
        temp.scale = scale
    if alongNormal:
        dir = (rv[1].co - rv[0].co)
        norm = math.sqrt(dir[0] ** 2 + dir[1] ** 2 + dir[2] ** 2)
        normAngle = [dir[0] / norm, dir[1] / norm, dir[2] / norm]
        for o in copies:
            o.rotation_euler = normAngle


selected = bpy.context.scene.collection.objects
PlaceAlongEdge(selected[0], 0, selected[1], 1.0, (0.1, 0.1, 0.1), True)