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
        result = result.replace("  ", " ")
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
    temp = []
    for s in name.split(" "):
        temp.append(s.replace(s[0], s[0].upper()))
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
            obj.data.name = obj.name
        if (len(active.children) == 0):
            tags.pop()


def ChangeNames(objects: []):
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
            if obj in objects:
                obj.name = tag + RemoveTags(obj.name, tags)
                obj.name = RemoveDoubleSpaces(obj.name)
                obj.name = RemoveDotWithAfter(obj.name)
                obj.name = Trim(obj.name)
                obj.name = Capitalize(obj.name)
                obj.data.name = obj.name
        if (len(active.children) == 0):
            tags.pop()


def ChangeNames(prefix: str = None, postfix: int | str = None):
    isPostfixStr = postfix is str
    begin: int
    if isPostfixStr and len(postfix) != 1:
        pass
    elif isPostfixStr:
        begin = int(postfix[0])
    elif postfix is int:
        begin = postfix
    else:
        pass
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
        temp = begin
        for obj in active.objects:
            obj.name = tag + RemoveTags(obj.name, tags)
            obj.name = RemoveDoubleSpaces(obj.name)
            obj.name = RemoveDotWithAfter(obj.name)
            obj.name = Trim(obj.name)
            obj.name = Capitalize(obj.name)
            if isPostfixStr:
                obj.name += " " + chr(temp)
            else:
                obj.name += " " + str(temp)
            if prefix is not None:
                obj.name = prefix + obj.name
            obj.data.name = obj.name
            temp += 1
        if (len(active.children) == 0):
            tags.pop()
