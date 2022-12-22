import numpy as np
import re

# PARSING INPUT ...
B,path = open("2022/Input/22.txt").read().split("\n\n")
path = [int(p) if str.isdigit(p) else p for p in re.findall("\d+|[A-Z]", path)]
B = B.split("\n")
n = max([len(r) for r in B])
B = [r if len(r) == n else r + " " * (n - len(r)) for  r in B]
B = np.array([list(l) for l in B])
B[B == " "] = "O"
B1 = B.copy()
n,m = np.shape(B1)
# print("n", n)
# print(B,path)
print("n,m:",n,m)

### <----------------------- PART ONE -----------------------> ###
x,y = 0,np.argwhere(B1[0] == ".")[0][0]

facings = [(0,1), (1,0), (0,-1), (-1,0)]
F = {0:">", 1:"v", 2:"<", 3:"^"}
f = 0
B1[x,y] = F[f]
dx, dy = facings[f]

def moveXY(x, y, f):
    dx, dy = facings[f]
    return (x + dx) % n, (y + dy) % m

for r, p in enumerate(path):
    assert B1[x,y] in ".>v<^"
    if type(p) == int:
        for i in range(p):
            match B1[moveXY(x, y, f)]:
                case "."|">"|"v"|"<"|"^": 
                    x,y = moveXY(x, y, f)
                    B1[x,y] = F[f % 4]
                case "#": break
                case "O":
                    x_, y_ = x,y
                    while(B1[moveXY(x_, y_, f)] == "O"):
                        x_,y_ = moveXY(x_, y_, f)
                        match B1[moveXY(x_, y_, f)]:
                            case "#": break
                            case "."|">"|"v"|"<"|"^": 
                                x,y = moveXY(x_, y_, f)
                                B1[x,y] = F[f]
                case _  : raise NotImplementedError(p)
    else:
        match p:
            case "L": f = (f - 1) % 4
            case "R": f = (f + 1) % 4
            case _  : raise NotImplementedError(p)
        dx, dy = facings[f]
        B1[x,y] = F[f]

    # print(p, "\n", B)

    # if r == 30: break

print("PART ONE:", (x + 1) * 1000 + (y + 1) * 4 + f)
# print("coords:", x, y, f)
np.savetxt("2022/Output/22_partOne.out", B1, fmt="%s")

### <----------------------- PART TWO -----------------------> ###
B2 = B.copy()


if len(path) > 100: # NOT TEST INPUT, HAVE TO TRANSFORM...
    n_t = n // 4 # My input is 4 tiles high
    tiles = [B2[(i // 3) * n_t:((i // 3) + 1) * n_t, (i % 3) * n_t: ((i % 3) + 1) * n_t] for i in range(12)]
    for t in tiles:
        assert np.shape(t) == (50,50)

    B2row1 = np.hstack([tiles[0], tiles[0], tiles[1], tiles[0]])
    B2row2 = np.hstack([np.rot90(tiles[9], -1), np.rot90(tiles[6], -1), tiles[4], tiles[0]])
    B2row3 = np.hstack([tiles[0], tiles[0], tiles[7], np.rot90(tiles[2], 2)])
    rows = [B2row1, B2row2, B2row3]
    
    for r in rows:
        assert np.shape(r) == (50,200), np.shape(r)
    B2 = np.vstack(rows)

    assert np.shape(B2) == (150, 200)

# np.savetxt("2022/Output/22_partTwo.out", B2, fmt="%s")
x,y = 0,np.argwhere(B2[0] == ".")[0][0]

f = 0
B2[x,y] = F[f]
dx, dy = facings[f]

n,m = np.shape(B2)

n_tile, m_tile = n // 3, m // 4
assert n_tile == n_tile
w = n_tile

from enum import Enum
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

# print("n_tile, m_tile:", n_tile, m_tile)

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
    return None

def moveXY_2(x, y, f):
    # w = C.W # <----------- why needed? ------------
    # print("C.W1", C.W1)
    # print(x,y,w)
    xt, yt = x // w, y // w
    dx, dy = facings[f]
    # print("matching:", toC(x), xt, toC(y), yt, f)
    match toC(x), xt, toC(y), yt, f: # <--------------------------------------------DANGER x+1, y+1
        # ------> TILE #ID #POSITION/#DIRECTION <------
        # WHEN ENTERING RIGHT SIDE OF TILE THEN : c * w - 1 (for c in 0,1,2,3)
        # WHEN ENTERING LEFT SIDE OF TILE THEN  : c * w     (for c in 0,1,2,3)
        # WHEN ENTERING TOP SIDE OF TILE THEN   : c * w     (for c in 0,1,2,3)
        # WHEN ENTERING BOTTOM SIDE OF TILE THEN: c * w - 1 (for c in 0,1,2,3)

        # TOP MATCH C.W
        # BOTTOM MATCH C.W_M
        # LEFT MATCH C.W
        # RIGHT MATCH C.W_M

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

        # facings = [(0,1), (1,0), (0,-1), (-1,0)]
        # F = {0:">", 1:"v", 2:"<", 3:"^"}
        case _:
            # print("all matching:", toC(x), xt, toC(y), yt, f)
            assert ((x + dx) % n, (y + dy) % m) == ((x + dx), (y + dy))
            return (x + dx), (y + dy), f

# print("move was:", print(moveXY_2(4, 6, 3)))
# assert moveXY_2(4, 6, 3) == (2, 8, 0), moveXY_2(4, 6, 3)

for i,p in enumerate(path):
    assert B2[x,y] in ".>v<^", (B2[x,y],i, p)
    if type(p) == int:
        for i in range(p):
            match B2[moveXY_2(x, y, f)[:2]]:
                case "."|">"|"v"|"<"|"^": 
                    x, y, f = moveXY_2(x, y, f)
                    B2[x,y] = F[f]
                case "#": break
                case _  : raise NotImplementedError(p, B2[moveXY_2(x, y, f)[:2]], moveXY_2(x, y, f)[:2], x, y)
    else:
        match p:
            case "L": f = (f - 1) % 4
            case "R": f = (f + 1) % 4
            case _  : raise NotImplementedError(p)
        dx, dy = facings[f]
        B2[x,y] = F[f]

    # print(p, "\n", B)

    # if r == 30: break

print("PART TWO:", (x + 1) * 1000 + (y - 50 + 1) * 4 + f)
print("coords:", x, y, f)
np.savetxt("2022/Output/22_partTwo.out", B2, fmt="%s")

assert 1 == 0, "MOVE COORDS BACK TO ORIGINAL.... -50 in PART TWO is now hardcoded"
# 64519 too low

# 78491

# 85315 too high
# 144457 too high
