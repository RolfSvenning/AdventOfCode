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
print("coords:", x, y, f)
np.savetxt("2022/Output/22_partOne.out", B1, fmt="%s")

### <----------------------- PART TWO -----------------------> ###
B2 = B.copy()
x,y = 0,np.argwhere(B2[0] == ".")[0][0]

f = 0
B2[x,y] = F[f]
dx, dy = facings[f]
n_tile, m_tile = n // 3, m // 4
assert n_tile == n_tile
w = n_tile

from enum import Enum
class C(Enum):
    W0 = 0
    W1 = w
    W2 = 2 * w
    W3 = 3 * w
    W4 = 4 * w

print("n_tile, m_tile:", n_tile, m_tile)

# def toC(c):
#     if c == 0 * w: return C.W0
#     if c == 1 * w: return C.W1
#     if c == 2 * w: return C.W2
#     if c == 3 * w: return C.W3
#     if c == 4 * w: return C.W4
#     return None

def moveXY_2(x, y, f):
    # w = C.W # <----------- why needed? ------------
    # print("C.W1", C.W1)
    # print(x,y,w)
    xt, yt = x // w, y // w
    dx, dy = facings[f]
    match x + 1, xt, y + 1, yt, f: # <--------------------------------------------DANGER x+1, y+1
        # ------> TILE #ID #POSITION/#DIRECTION <------
        # WHEN ENTERING RIGHT SIDE OF TILE THEN : c * w - 1 (for c in 0,1,2,3)
        # WHEN ENTERING LEFT SIDE OF TILE THEN  : c * w     (for c in 0,1,2,3)
        # WHEN ENTERING TOP SIDE OF TILE THEN   : c * w     (for c in 0,1,2,3)
        # WHEN ENTERING BOTTOM SIDE OF TILE THEN: c * w - 1 (for c in 0,1,2,3)

        # TILE 2 TOP/UP ---> TILE 4 TOP/DOWN
        case 0, _, _, _, 2, 3   :   return (w, y - 2 * w, 1)
        # TILE 4 TOP/UP ---> TILE 2 TOP/DOWN
        case C.W1, _, _, _, 0, 3 :   return (0, y + 2 * w, 1)

        # TILE 2 LEFT/LEFT ---> TILE 5 TOP/DOWN
        case _, 0, C.W2, _, 2:   return (w, w + x, 1)
        # TILE 5 TOP/UP ---> TILE 2 LEFT/RIGHT
        case C.W1, _, 1, _, 3:       return (y - w, 2 * w, 0)

        # TILE 2 RIGHT/RIGHT ---> TILE 11 RIGHT/LEFT
        case _, 0, C.W3, _, 0:   return (2 * w + x, 4 * w - 1, 2)
        # TILE 11 RIGHT/RIGHT ---> TILE 2 RIGHT/LEFT
        case _, 2, C.W4, _, 0:   return (x - 2 * w, 3 * w - 1, 2)

        # TILE 4 LEFT,LEFT ---> TILE 11 BOTTOM/UP
        case _, 1, 0, _, 2:         return (3 * w - 1, 3 * w + (w - (x - w)), 3)
        # TILE 11 BOTTOM,DOWN ---> TILE 4 LEFT/RIGHT
        case C.W3, _, _, 3, 1:   return (0, w + (w - (y - 3 * w)))

        # TILE 4 BOTTOM/DOWN ---> TILE 10 BOTTOM/UP
        case C.W2, _, _, 0, 1:   return (3 * w - 1, 3 * w - 1 - y, 3)
        # TILE 10 BOTTOM/DOWN ---> TILE 4 BOTTOM/UP
        case C.W3, _, _, 2, 1:   return (2 * w - 1, 3 * w - 1 - y, 3)
        
        # TILE 5 BOTTOM/DOWN ---> TILE 10 LEFT/RIGHT
        case C.W2, _, _, 1, 1:   return (2 * w + 2 * w - 1 - y, 2 * w, 0)
        # TILE 10 LEFT/LEFT ---> TILE 5 BOTTOM/UP
        case _, 2, C.W2, _, 2:   return (2 * w - 1, w + 3 * w - 1 - x, 3)

        # TILE 6 RIGHT/RIGHT ---> TILE 11 TOP/DOWN
        case _, 1, C.W3, _, 0:   return (2 * w, 3 * w + 2 * w - 1 - x, 1)
        # TILE 11 TOP/UP ---> TILE 6 RIGHT/LEFT
        case C.W2, _, _, 3, 3:   return (w + 4 * w - 1 - y, 3 * w - 1, 2)

        # facings = [(0,1), (1,0), (0,-1), (-1,0)]
        # F = {0:">", 1:"v", 2:"<", 3:"^"}
        case _:
            assert ((x + dx) % n, (y + dy) % m) == ((x + dx), (y + dy))
            return (x + dx), (y + dy), f

for p in path:
    assert B2[x,y] in ".>v<^"
    if type(p) == int:
        for i in range(p):
            match B2[moveXY_2(x, y, f)[:2]]:
                case "."|">"|"v"|"<"|"^": 
                    x, y, f = moveXY_2(x, y, f)
                    B2[x,y] = F[f]
                case "#": break
                case _  : 
                    print(B2)
                    raise NotImplementedError(p, B2[moveXY_2(x, y, f)[:2]], x, y)
    else:
        match p:
            case "L": f = (f - 1) % 4
            case "R": f = (f + 1) % 4
            case _  : raise NotImplementedError(p)
        dx, dy = facings[f]
        B2[x,y] = F[f]

    # print(p, "\n", B)

    # if r == 30: break

print("PART ONE:", (x + 1) * 1000 + (y + 1) * 4 + f)
print("coords:", x, y, f)
np.savetxt("2022/Output/22_partTwo.out", B2, fmt="%s")