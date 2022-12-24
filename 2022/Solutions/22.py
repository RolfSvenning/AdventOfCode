import numpy as np
import re
from enum import Enum

# PARSING INPUT ...
B,path = open("2022/Input/22.txt").read().split("\n\n")
path = [int(p) if str.isdigit(p) else p for p in re.findall("\d+|[A-Z]", path)]
B = B.split("\n")
n = max([len(r) for r in B])
B = [r if len(r) == n else r + " " * (n - len(r)) for  r in B]
B = np.array([list(l) for l in B])
B[B == " "] = "O"
B1 = B.copy()
n, m = np.shape(B1)


### <----------------------- PART ONE -----------------------> ###
facings = [(0,1), (1,0), (0,-1), (-1,0)]
F = {0:">", 1:"v", 2:"<", 3:"^"}

def moveP1(x, y, f):
    dx, dy = facings[f]
    return (x + dx) % n, (y + dy) % m, f

def partOneAndTwo(B, move):
    x,y = 0,np.argwhere(B[0] == ".")[0][0]
    F = {0:">", 1:"v", 2:"<", 3:"^"}
    f = 0
    B[x,y] = F[f]

    for p in path:
        if type(p) == int:
            for _ in range(p):
                match B[move(x, y, f)[:2]]:
                    case "."|">"|"v"|"<"|"^": 
                        x,y,f = move(x, y, f)
                        B[x,y] = F[f % 4]
                    case "#": break
                    case "O": # only needed for part 1
                        x_, y_ = x,y
                        while(B[move(x_, y_, f)[:2]] == "O"):
                            x_,y_,f = move(x_, y_, f)
                            match B[move(x_, y_, f)[:2]]:
                                case "#": break
                                case "."|">"|"v"|"<"|"^": 
                                    x,y,f = move(x_, y_, f)
                                    B[x,y] = F[f]
        else:
            match p:
                case "L": f = (f - 1) % 4
                case "R": f = (f + 1) % 4
            B[x,y] = F[f]
    return x,y,f

x,y,f = partOneAndTwo(B1, moveP1)

print("PART ONE:", (x + 1) * 1000 + (y + 1) * 4 + f)
# print("coords:", x, y, f)
np.savetxt("2022/Output/22_partOne.out", B1, fmt="%s")


### <----------------------- PART TWO -----------------------> ###
def convertInputToTestShape(B):
    n = np.shape(B)[0]
    n_t = n // 4 # My input is 4 tiles high
    tiles = [B[(i // 3) * n_t:((i // 3) + 1) * n_t, (i % 3) * n_t: ((i % 3) + 1) * n_t] for i in range(12)]

    B2row1 = np.hstack([tiles[0], tiles[0], tiles[1], tiles[0]])
    B2row2 = np.hstack([np.rot90(tiles[9], -1), np.rot90(tiles[6], -1), tiles[4], tiles[0]])
    B2row3 = np.hstack([tiles[0], tiles[0], tiles[7], np.rot90(tiles[2], 2)])
    rows = [B2row1, B2row2, B2row3]

    return np.vstack(rows)

B2 = convertInputToTestShape(B)
w = np.shape(B2)[0] // 3

class C(Enum):
    W0 = 0
    W1M = w - 1
    W1 = w
    W2M = 2 * w - 1
    W2 = 2 * w
    W3M = 3 * w - 1
    W3 = 3 * w
    W4M = 4 * w - 1
    W4 = 4 * w

def toC(c):
    if c == 0 * w:      return C.W0
    if c == 1 * w - 1:  return C.W1M
    if c == 1 * w:      return C.W1
    if c == 2 * w - 1:  return C.W2M
    if c == 2 * w:      return C.W2
    if c == 3 * w - 1:  return C.W3M
    if c == 3 * w:      return C.W3
    if c == 4 * w - 1:  return C.W4M
    if c == 4 * w:      return C.W4

def moveXY_2(x, y, f):
    xt, yt = x // w, y // w
    dx, dy = facings[f]
    match toC(x), xt, toC(y), yt, f: 
        # TILE 2 TOP/UP ---> TILE 4 TOP/DOWN
        case C.W0, _,  _, 2, 3:     return (w, 3 * w - 1 - y, 1)
        # TILE 4 TOP/UP ---> TILE 2 TOP/DOWN
        case C.W1, _, _, 0, 3:      return (0, 2 * w + w - 1 - y, 1)

        # TILE 2 LEFT/LEFT ---> TILE 5 TOP/DOWN
        case _, 0, C.W2, _, 2:      return (w, w + x, 1)
        # TILE 5 TOP/UP ---> TILE 2 LEFT/RIGHT
        case C.W1, _, _, 1, 3:      return (y - w, 2 * w, 0)

        # TILE 2 RIGHT/RIGHT ---> TILE 11 RIGHT/LEFT
        case _, 0, C.W3M, _, 0:     return (2 * w + w - 1 - x, 4 * w - 1, 2)
        # TILE 11 RIGHT/RIGHT ---> TILE 2 RIGHT/LEFT
        case _, 2, C.W4M, _, 0:     return (3 * w - 1 - x, 3 * w - 1, 2)

        # TILE 4 LEFT,LEFT ---> TILE 11 BOTTOM/UP
        case _, 1, C.W0, _, 2:      return (3 * w - 1, 3 * w + 2 * w - 1 - x, 3)
        # TILE 11 BOTTOM,DOWN ---> TILE 4 LEFT/RIGHT
        case C.W3M, _, _, 3, 1:     return (w + (4 * w - 1 - y), 0, 0)

        # TILE 4 BOTTOM/DOWN ---> TILE 10 BOTTOM/UP
        case C.W2M, _, _, 0, 1:     return (3 * w - 1, 3 * w - 1 - y, 3)
        # TILE 10 BOTTOM/DOWN ---> TILE 4 BOTTOM/UP
        case C.W3M, _, _, 2, 1:     return (2 * w - 1, 3 * w - 1 - y, 3)
        
        # TILE 5 BOTTOM/DOWN ---> TILE 10 LEFT/RIGHT
        case C.W2M, _, _, 1, 1:     return (2 * w + 2 * w - 1 - y, 2 * w, 0)
        # TILE 10 LEFT/LEFT ---> TILE 5 BOTTOM/UP
        case _, 2, C.W2, _, 2:      return (2 * w - 1, w + 3 * w - 1 - x, 3)

        # TILE 6 RIGHT/RIGHT ---> TILE 11 TOP/DOWN
        case _, 1, C.W3M, _, 0:     return (2 * w, 3 * w + 2 * w - 1 - x, 1)
        # TILE 11 TOP/UP ---> TILE 6 RIGHT/LEFT
        case C.W2, _, _, 3, 3:      return (w + 4 * w - 1 - y, 3 * w - 1, 2)

        # NORMAL MOVE BETWEEN ADJACENT TILES
        case _:                     return (x + dx), (y + dy), f

x, y, f = partOneAndTwo(B2, moveXY_2)
print("PART TWO:", (x + 1) * 1000 + (y - 50 + 1) * 4 + f)
# MOVE COORDS BACK TO ORIGINAL.... -50 in PART TWO is now hardcoded based on where I end up for my input
