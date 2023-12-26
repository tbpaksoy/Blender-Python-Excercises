import bpy
import mathutils
from enum import Enum
import bmesh


class ClosingType(Enum):
    Distance = 0
    Ratio = 1


def GetFaceCenter(obj: bpy.types.Object, faceIndex: int) -> mathutils.Vector:
    vertices = [
        obj.data.vertices[i].co for i in obj.data.polygons[faceIndex].vertices]
    sum = mathutils.Vector()
    for v in vertices:
        sum += v
    return sum / len(vertices)


def GetCloserPoints(points: [], toClose: mathutils.Vector | bpy.types.MeshVertex, value: float, closingType) -> []:
    if closingType != ClosingType.Distance and closingType != ClosingType.Ratio:
        pass
    if not all([isinstance(i, mathutils.Vector) for i in points]):
        pass
    if toClose is bpy.types.MeshVertex:
        toClose = toClose.co
    result = []
    match(closingType):
        case ClosingType.Distance:
            for p in points:
                direction = (toClose - p).normalized()
                result.append(direction * value)
        case ClosingType.Ratio:
            for p in points:
                way = toClose - p
                result.append(p + way * value)
    return result


def DivideMultipleEdges(edges: [], divisions: int) -> []:
    if not all(isinstance(i, bpy.types.MeshEdge | bmesh.types.BMEdge) for i in edges):
        pass
    result = []
    lengths = [(l.vertices[0] - l.vertices[1]).length for l in edges]
    length = sum(lengths)
    step = length / divisions
    for i in range(0.0, length, step):
        temp = step
        result.append(mathutils.Vector())
        while temp > 0:
            attempted = min(lengths[0], temp)
            result[len(result) - 1] = edges.vertices[0] + \
                edges.vertices[1] * (attempted / lengths[0])
            lengths[0] -= attempted
            if lengths[0] == 0:
                lengths.remove(lengths[0])
                edges.remove(edges[0])
    return result


for obj in bpy.context.objects_in_mode:
    bm = bmesh.new()
    bm.from_mesh(obj.to_mesh())
    edges = [obj.to_mesh().edges[e.index]
             for e in bm.select_history if isinstance(e, bmesh.types.BMEdge)]
    print(len(edges))
