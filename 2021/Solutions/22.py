import numpy as np
import re

def part_one():
    coords = [[int(s) + 50 for s in re.findall("[-]*\d+", l)] for l in open("2021/input/21.txt").read().split("\n")]
    on_or_off = [1 if re.match("[a-z]+", l)[0] == "on" else 0 for l in open("2021/input/21.txt").read().split("\n")]

    reactor = np.zeros((101,101,101), dtype=np.int0)
    for cs, switch in zip(coords, on_or_off):
        if min(cs) < 0 or max(cs) > 100:
            continue
        x1, x2, y1, y2, z1, z2 = cs
        reactor[x1:x2+1,y1:y2+1,z1:z2+1] = switch
    
    print("Part one, number of cubes on in small region: ", np.sum(reactor))
    

def part_two():
    coords = [[int(s) for s in re.findall("[-]*\d+", l)] for l in open("2021/input/21.txt").read().split("\n")]
    on_or_off = [1 if re.match("[a-z]+", l)[0] == "on" else 0 for l in open("2021/input/21.txt").read().split("\n")]
    
    XYZs_ = [[coords[i][j:j+2] for i in range(len(coords))] for j in [0,2,4]]
    Xs, Ys, Zs = [sorted([v for pairs in coord for v in pairs]) for coord in XYZs_]

    elementaryCubes = []
    for x in Xs:
        print(x)
        for y in Ys:
            for z in Zs:
                # elementaryCubes.append([x,y,z,0])
                pass

    # insert cubes one at a time.
    # for c in cubes:
    #   for c' in cubes:
    #       if c interset c':
    #           handle cube for overlap by adding new overlap cube
    #           add entire cube







    # def splitCubes(As,Bs):
    #     Ax1, Ax2, Ay1, Ay2, Az1, Az2 = As
    #     Bx1, Bx2, By1, By2, Bz1, Bz2 = Bs
    #     if Bx2 < Ax1 or 

if __name__ == '__main__':
    part_two()