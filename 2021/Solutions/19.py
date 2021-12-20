import re
from numpy import array, column_stack, sign


def part_one_and_two():
    scanners = [array([eval(s) for s in l.split()]) for l in re.split('--- scanner [\d]+ ---\n', open("2021/input/19.txt").read())[1:]]
    n = len(scanners)
    scannerPositions = []
    finished = [True] + [False] * (n-1)
    threeDists = threeDistances(scanners)
    usefulPairs = [(i,j) for i in range(n) for j in range(n) if len(threeDists[i] & threeDists[j]) >= 220 and i != j] # n choose 3 = 220
    Total = arrToSet(scanners[0])
    for _ in range(n):
        foundOne = False
        for i,j in [(i,j) for i,j in usefulPairs if finished[i] and not finished[j]]:
            if foundOne:
                    break
            print("threeDistOverlap: ", len(threeDists[i] & threeDists[j]))
            print("i,j: ", i,j)
            D = scanners[i]
            for D_min in D:
                if foundOne:
                    break 
                for N in rotate(scanners[j]):
                    if foundOne:
                        break
                    for N_min in N:
                        if foundOne:
                            break
                        N_ = N + (scannerPos := (D_min - N_min))
                        D_Set, N_Set = arrToSet(D), arrToSet(N_)
                        if len(D_Set & N_Set) >= 12:
                            Total = Total | N_Set
                            finished[j] = True
                            scanners[j] = N_
                            foundOne = True
                            scannerPositions.append((j,scannerPos, len(Total)))
                            print("update: (overlap,i,j,p,size): ", (len(D_Set & N_Set), i,j,scannerPos, len(Total)))
    print("Scanner positions (i,p,foundBeacons):")
    for p in scannerPositions:
        print(p)
    print("Part one, number of beacons found!: ", len(Total))
    print("Part two, max manhatten distance between found scanners: ", maxDistBetweenScanners(scannerPositions))

def maxDistBetweenScanners(s):
    n = len(s)
    maxDist = 0
    for i,j in [(i,j) for i in range(n) for j in range(n)]:
        maxDist = max(maxDist, sum(abs(s[i][1] - s[j][1])))
    return maxDist

def rotate(A):
    # CAN EASILY BE REFACTORED TO SIX CHOICES FOR FIRST AXIS AND THEN 4 CHOICES FOR SECOND. THIRD AXIS DETERMINED BY FIRST TWO. TOTAL 24.
    A = array(A)
    coords = []
    for locs in [[1,2,3], [3,1,2], [2,3,1], [-2,-1,-3], [-3,-2,-1], [-1,-3,-2]]:
        # Keeps z in place and move x to y and y to opposite of where x was (corresponds to one 90 degree rotation around z)
        for _ in range(4):
            locs_ = [0]*3
            abss = [abs(v) for v in locs]
            signs = [sign(v) for v in locs]
            xLoc = abss.index(1)
            yLoc = abss.index(2)
            zLoc = abss.index(3)
            # Rotate 90 degrees around z
            locs_[yLoc] = 1 * signs[yLoc] # x -> y
            locs_[xLoc] = -2 * signs[xLoc] # y -> -x
            locs_[zLoc] = locs[zLoc] # z -> z
            locs = locs_.copy()
            coords.append(column_stack((signs[0] * A[:,abss[0] - 1], signs[1] * A[:,abss[1] - 1], signs[2] * A[:,abss[2] - 1])))
    return coords

def threeDistances(scanners):
    def dist(a,b):
        return sum((a-b)**2)
    l = []
    for s in scanners:
        n = len(s)
        ds = set()
        for i,j,k in [(i,j,k) for i in range(n) for j in range(n) for k in range(n) if i != j and i != k and j != k]:
            a,b,c = s[i], s[j], s[k]
            d = dist(a,b) + dist(a,c) + dist(b,c)
            ds.add(d)
        l.append(ds)
    return l

def arrToSet(A):
    return set([re.sub("\[,","[",re.sub("[ ]+",",","".join(str(x)))) for x in A])

def setToArray(aSet):
    return array([eval(s) for s in aSet])


if __name__ == '__main__':
    part_one_and_two()