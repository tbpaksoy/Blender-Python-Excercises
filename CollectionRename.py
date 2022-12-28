import bpy
import re


def RemoveTags(name: str, tags: list) -> str:
    result = name
    for tag in tags:
        result = re.sub(tag, "", result, 1)
    return result


def RemoveDoubleSpaces(name: str) -> str:
    result = name
    while "  " in result:
        name = name.replace("  ", " ")
    return result


def RemoveDotWithAfter(name: str) -> str:
    result = name
    while "." in result:
        result = result[0:-1]
    return result


def Trim(name: str) -> str:
    result = name
    while result.startswith(" "):
        result = result[1:0]
    while result.endswith(" "):
        result = result[0:-1]
    return result


def Capitalize(name: str) -> str:
    temp = name.split(" ")
    for s in temp:
        s[0] = s[0].upper()
    return " ".join(temp)


def ChangeNames():
    collections = []
    tags = []
    for collection in bpy.context.scene.collection.children:
        collections.append(collection)
    while len(collections) > 0:
        active = collections.pop()
        tags.append(active.name)
        for collection in active.children:
            collections.append(collection)
        tag = ""
        for t in tags:
            tag += t + " "
        for obj in active.objects:
            obj.name = tag + RemoveTags(obj.name, tags)
            obj.name = RemoveDoubleSpaces(obj.name)
            obj.name = RemoveDotWithAfter(obj.name)
            obj.name = Trim(obj.name)
            obj.name = Capitalize(obj.name)
        if (len(active.children) == 0):
            tags.pop()


ChangeNames()