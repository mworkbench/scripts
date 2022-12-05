import sys
import os

if len(sys.argv) < 2:
    print("Usage: script prefix")
    exit()

THIS_SCRIPT = sys.argv[0]
PREFIX = sys.argv[1]

FILES_IN_CURRENT = os.listdir(".")
NEW_FILES_IN_CURRENT = []


def ignoreFile(f, aPrefix):
    if f.startswith("."):
        return True
    if f.lower() == THIS_SCRIPT.lower():
        return True
    if f.lower().startswith(aPrefix.lower()):
        return True
    return False


def existsSameName(af, aFiles):
    for f in aFiles:
        if af.lower() == f.lower():
            return True
    return False


def repeatStr(aCount, aS):
    s = ''
    for i in range(aCount):
        s = s + aS
    return s


def newName(af, aPreFix, aFiles, aFiles2, aMaxDepth):
    baseName, extName = os.path.splitext(af)

    depth = 0
    while True:
        alt = aPreFix + '-' + baseName + repeatStr(depth, '-b') + extName

        if depth > aMaxDepth:
            return (False, 'cannot make new filename')

        if existsSameName(alt, aFiles) or existsSameName(alt, aFiles2):
            depth = depth + 1
        else:
            return (True, alt)


for f in FILES_IN_CURRENT:
    if ignoreFile(f, PREFIX):
        print("IGNORE FILE : ***** ", f, "*******")
        continue

    status, name = newName(f, PREFIX, FILES_IN_CURRENT,
                           NEW_FILES_IN_CURRENT, 4)

    if not status:
        print("CANNOT RENAME : ", f, name)
        exit()

    print("TRY TO RENAME: FROM: ", f, " TO ", name)
    os.rename(f, name)
    NEW_FILES_IN_CURRENT.append(name)

# print(FILES_IN_CURRENT)
# print(NEW_FILES_IN_CURRENT)
