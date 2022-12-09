import numpy as np

moves = [(t, int(c)) for t,c in [m.split(" ") for m in open("2022/Input/09.txt").read().strip().split("\n")]]
totalMoves = sum([c for _,c in moves])
numberOfKnots = 10

def notAdj(hx, hy, tx, ty):
    return abs(hx - tx) > 1 or abs(hy - ty) > 1

def moveHead(t, hx, hy):
    match t:
        case "R": return hx, hy + 1
        case "L": return hx, hy - 1
        case "D": return hx + 1, hy
        case "U": return hx - 1, hy

def moveTail(hx, hy, tx, ty):
    if hx == tx: # same row 
        if hy > ty: return tx, hy - 1
        else:       return tx, hy + 1
    if hy == ty: # same column
        if hx > tx: return hx - 1, ty
        else:       return hx + 1, ty
    if tx > hx and ty < hy: return tx - 1, ty + 1 #bottom left
    if tx < hx and ty < hy: return tx + 1, ty + 1 #top    left 
    if tx < hx and ty > hy: return tx + 1, ty - 1 #top    right 
    if tx > hx and ty > hy: return tx - 1, ty - 1 #bottom right 

def partOneAndTwo():
    b1 = np.empty(totalMoves**2).reshape((totalMoves,totalMoves))
    b2 = np.empty(totalMoves**2).reshape((totalMoves,totalMoves))
    knots = [(0,0)] * numberOfKnots
    b1[knots[ 1]] = -1
    b2[knots[-1]] = -2
    for t,c in moves:
        for _ in range(c):
            knots[0] = moveHead(t, *knots[0])
            for i in range(1, len(knots)):
                if notAdj(*knots[i], *knots[i-1]):
                    knots[i] = moveTail(*knots[i-1], *knots[i])
                else: break # no later knots will move if this one doesn't
            b1[knots[ 1]] = -1
            b2[knots[-1]] = -2
    return b1, b2            

b1, b2 = partOneAndTwo()
print("PART ONE:", np.sum(b1 == -1), "\nPART TWO:", np.sum(b2 == -2))