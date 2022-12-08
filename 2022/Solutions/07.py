import re

cs = [c.strip() for c in open("2022/Input/07.txt").read().strip().split("$") if c != '']

print(cs[0:3])

class Dir:
    def __init__(self, parent):
        self.parent = parent
        self.files = []
        self.subdirectories = {}
        self.checked = False
        self.size = 0
main=Dir(parent=None) 

currentDirectory = main
for command in cs:
    match re.split(" |\n", command, 1):
        case "cd",  "..": 
            currentDirectory = currentDirectory.parent # print("cd ..")
        case "cd", "/"  : 
            currentDirectory = main 
            print("cd /")
        case "cd",  dir_name: 
            print("name: ", dir_name)
            if dir_name in currentDirectory.subdirectories:
                currentDirectory = currentDirectory.subdirectories[dir_name]
            else: raise NotImplementedError #subdirectory doesn't exist, should never happen
        case "ls", contents: 
            print("ls")
            if len(currentDirectory.files) + len(currentDirectory.subdirectories) == 0:
                for c in contents.split("\n"):
                    match c.split(" "):
                        case "dir", dir_name: 
                            currentDirectory.subdirectories[dir_name] =  Dir(parent=currentDirectory) 
                            print("dir", dir_name)
                        case size, file_name: 
                            currentDirectory.files.append((int(size), file_name)) #converts size from string to int
                            print(size, file_name)
                        case _: raise NotImplementedError #should never happen
            else: pass #already used 'ls' here before
        case other: raise NotImplementedError #should never happen

total = 0

def sizeOfDir(dir):
    total += 1
    if not dir.checked:
        dir.size = sum([s for s,_ in dir.files] + [sizeOfDir(d) for d in dir.subdirectories.values()])
        dir.checked = True
        return dir.size
    else: return dir.size

def sumOfSmallDirectories(dir: Dir, maxSize):
    dirSize = sizeOfDir(dir)
    return dirSize * (dirSize <= maxSize) + sum([sumOfSmallDirectories(d, maxSize) for d in dir.subdirectories.values()])


print("res: ", sumOfSmallDirectories(main, 100000))

#print(sizeOfDir(main.subdirectories["d"]))