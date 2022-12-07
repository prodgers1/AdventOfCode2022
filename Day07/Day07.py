import sys
import math
from copy import deepcopy
from collections import defaultdict
sys.path.append('./')
from adventInput import GetInput
_input = GetInput(7)

class Directory:
    def __init__(self, name, fileSystem):
        self.Items = {}
        self.Cwd = ""
        self.Root = "/"
        self.ParentDirectory = fileSystem
        self.Name = name
        self.Size = 0
    
    def CreateFolder(self, folderName, fileSystem):
        fileSystem.Items[folderName] = Directory(folderName, fileSystem)
    
    def CreateFile(self, fileName, size, fileSystem):
        fileSystem.Items[fileName] = File(fileName, size, fileSystem)
    
    def SetCwd(self, cwd):
        self.Cwd = cwd
        if cwd not in fileSystem.Items:
            return self
        return fileSystem.Items[cwd]
    
    def GetRoot(self, currentCwd):
        while currentCwd.ParentDirectory != None:
            currentCwd = currentCwd.ParentDirectory
        
        return currentCwd

class File:
    def __init__(self, fileName, size, cwd):
        self.Type = "File"
        self.Size = int(size)
        self.ParentDirectory = cwd

class Folder:
    def __init__(self, name, cwd):
        self.Type = "Folder"
        self.Name = name
        self.Size = "" #sum of children
        self.Folders = []
        self.Files = []
        self.ParentDirectory = cwd

fileSystem = Directory('/', None)

i = 0
while i < len(_input):
    line = _input[i]
    if line.startswith('$'):
        if line.startswith('$ cd') and '..' not in line:
            _, _, directoryName = line.split()
            fileSystem = fileSystem.SetCwd(directoryName)
        elif line.startswith('$ cd') and '..' in line:
            fileSystem = fileSystem.ParentDirectory
            
        elif line.startswith('$ ls'):
            #print current directory
            j = i + 1
            while j < len(_input):
                nextLine = _input[j]
                if nextLine.startswith('$'):
                    j -= 1
                    break
                else:
                    if nextLine.startswith('dir'):
                        _, name = nextLine.split()
                        fileSystem.CreateFolder(name, fileSystem)
                    else: #file
                        size, name = nextLine.split()
                        fileSystem.CreateFile(name, size, fileSystem)

                j += 1
            i = j
    i += 1

ans = 0
limit = 100000
directories = []


def recurse(fileSystem):
    global ans
    global directories
    total = 0
    if len(fileSystem.Items) == 0:
        return total
    
    for item in fileSystem.Items:
        if isinstance(fileSystem.Items[item], File):
            total += fileSystem.Items[item].Size
    
    for item in fileSystem.Items:
        if isinstance(fileSystem.Items[item], Directory):
            total += recurse(fileSystem.Items[item])
    directories.append(total)
    fileSystem.Size = total
    if total <= limit:
        ans += total
    return total

fileSystem = fileSystem.GetRoot(fileSystem)
totalSize = recurse(fileSystem)

print(ans)

remaining = 70000000 - totalSize
spaceINeed = 30000000 - remaining

directories.sort()

for directory in directories:
    if directory > spaceINeed:
        print(directory)
        break
