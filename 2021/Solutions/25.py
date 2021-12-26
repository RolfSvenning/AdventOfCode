import numpy as np

def part_one_and_two():
    input = open("2021/input/25.txt").read().replace(".","0").replace(">","1").replace("v","2").split("\n")
    seaFloor = np.array([[int(s) for s in row] for row in input])
    n,d = np.shape(seaFloor)
    r = 0
    changeDetected = True
    while changeDetected:
        changeDetected = False
        r = r + 1
        seaFloorNext = np.zeros_like(seaFloor)
        # MAKE ALL POSSIBLE MOVES TO THE RIGHT
        for i,j in [(i,j) for i in range(n) for j in range(d)]:
            match seaFloor[i,j]:
                case 1: # >
                    nextPos = i,(j + 1) % d
                    if seaFloor[nextPos] == 0:
                        seaFloorNext[nextPos] = 1
                        changeDetected = True
                    else:
                        seaFloorNext[i,j] = 1
                case _: continue

        # MAKE ALL POSSIBLE MOVES DOWNWARDS
        for i,j in [(i,j) for i in range(n) for j in range(d)]:
            match seaFloor[i,j]:
                case 2: # v
                    nextPos = (i + 1) % n,j
                    if seaFloorNext[nextPos] == 0 and seaFloor[nextPos] != 2:
                        changeDetected = True
                        seaFloorNext[nextPos] = 2
                    else:
                        seaFloorNext[i,j] = 2
                case _: continue 
        seaFloor = seaFloorNext.copy()
    
    print("Part one, first round with no movement is: ", r)


if __name__ == '__main__':
    part_one_and_two()