import re

cs = [c.strip() for c in open("2022/Input/07.txt").read().strip().split("$") if c != '']

### <---------------- PART ONE ----------------> ###
class Dir:
    def __init__(self, name, parent):
        self.parent = parent
        self.subDirs = {}
        self.files = []
        self.size = 0
        self.name = name

    def __str__(self):
        return f"({self.name},{self.size})"

main=Dir(name = "/", parent=None) 

currDir = main
for command in cs:
    match re.split(" |\n", command, 1):
        case "cd",  "..":       currDir = currDir.parent
        case "cd", "/"  :       currDir = main
        case "cd",  name:   currDir = currDir.subDirs[name]
        case "ls", contents: 
            assert len(currDir.files) + len(currDir.subDirs) == 0 # 'ls' used once pr. directory
            for c in contents.split("\n"):
                match c.split(" "):
                    case "dir", name: 
                        currDir.subDirs[name] =  Dir(name=name, parent=currDir) 
                    case size, file_name: 
                        currDir.files += [(int(size), file_name)] #converts size from string to int

def calcSizeOfDirs(dir: Dir):
    dir.size = sum([s for s,_ in dir.files] + [calcSizeOfDirs(d) for d in dir.subDirs.values()])
    return dir.size

maxSize = 100000

def sumOfSmallDirs(dir: Dir):
    return dir.size * (dir.size <= maxSize) + sum([sumOfSmallDirs(d) for d in dir.subDirs.values()])

calcSizeOfDirs(main)
print("---PART ONE---:", sumOfSmallDirs(main))


### <---------------- PART TWO ----------------> ###
diskSpace, ususedSpaceRequired = 70000000, 30000000

def largeEnough(dir): 
    return (diskSpace - main.size + dir.size) >= ususedSpaceRequired

def smallestDir(dir: Dir):
    subDirs = [smallestDir(d) for d in dir.subDirs.values()] + [main] #[main] added so nonempty list for 'min'
    return min(subDirs + ([dir] if largeEnough(dir) else []), key = lambda d: d.size) 

d = smallestDir(main)
print("---PART TWO---:", d.size)
print(f"deleting directory {d} yields unused space: {diskSpace - main.size + d.size}")