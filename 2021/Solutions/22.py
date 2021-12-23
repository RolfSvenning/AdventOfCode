import numpy as np
import re

def part_one():
    coords = [[int(s) + 50 for s in re.findall("[-]*\d+", l)] for l in open("2021/input/22.txt").read().split("\n")]
    on_or_off = [1 if re.match("[a-z]+", l)[0] == "on" else 0 for l in open("2021/input/22.txt").read().split("\n")]

    reactor = np.zeros((101,101,101), dtype=np.int0)
    for cs, switch in zip(coords, on_or_off):
        if min(cs) < 0 or max(cs) > 100:
            continue
        x1, x2, y1, y2, z1, z2 = cs
        reactor[x1:x2+1,y1:y2+1,z1:z2+1] = switch
    
    print("Part one, number of cubes on in small region: ", np.sum(reactor))
    

def part_two():
    cubes = [[int(s) for s in re.findall("[-]*\d+", l)] for l in open("2021/input/22.txt").read().split("\n")]
    on_or_off = [1 if re.match("[a-z]+", l)[0] == "on" else 0 for l in open("2021/input/22.txt").read().split("\n")]
    cubes = [(c,s) for c,s in zip(cubes, on_or_off)]

    def intersects(cubeA,cubeB):
        (Ax1, Ax2, Ay1, Ay2, Az1, Az2), _ = cubeA
        (Bx1, Bx2, By1, By2, Bz1, Bz2), _ = cubeB
        return not(Bx2 < Ax1 or Ax2 < Bx1 or By2 < Ay1 or Ay2 < By1 or Bz2 < Az1 or Az2 < Bz1)
    
    # Note that we assume that the cubes are overlapping! (only case where the function get called)
    def createOverlappingCube(cubeA, cubeB):
        (Ax1, Ax2, Ay1, Ay2, Az1, Az2), _ = cubeA
        (Bx1, Bx2, By1, By2, Bz1, Bz2), Bs = cubeB
        x1 = max(Ax1, Bx1)
        x2 = min(Ax2, Bx2)
        y1 = max(Ay1, By1)
        y2 = min(Ay2, By2)
        z1 = max(Az1, Bz1)
        z2 = min(Az2, Bz2)
        return (x1, x2, y1, y2, z1, z2), -Bs

    #  1  1  -1
    #  1 -1   1
    # -1  1  -1
    # -1 -1   1
    def volume(cube):
        x1, x2, y1, y2, z1, z2 = cube
        return (x2-x1+1) * (y2-y1+1) * (z2-z1+1)

    currentCubes = []
    for cubeA in cubes:
        print(len(currentCubes))
        newCubes = []
        for cubeB in currentCubes:
            if not intersects(cubeA, cubeB):
                continue
            # print("here")
            newCubes.append(createOverlappingCube(cubeA,cubeB)) 
        if cubeA[-1] == 1:
            currentCubes += [cubeA]
        currentCubes += newCubes
        # print(currentCubes)
        # sum = np.sum([s * volume(coords) for coords,s in currentCubes])
        # print("Total sum: ", sum)


    
    print("Len total cubes: ", len(currentCubes), )
    sum = np.sum([s * volume(coords) for coords,s in currentCubes])
    print("Total sum: ", sum)


    


    # insert cubes one at a time.
    # for c in cubes:
    #   for c' in cubes:
    #       if c interset c':
    #           handle cube for overlap by adding new overlap cube
    #           add entire cube

    # XYZs_ = [[cubes[i][j:j+2] for i in range(len(cubes))] for j in [0,2,4]]
    # Xs, Ys, Zs = [sorted([v for pairs in coord for v in pairs]) for coord in XYZs_]




if __name__ == '__main__':
    # part_one()
    part_two()