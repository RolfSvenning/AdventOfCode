import numpy as np


def part_one_and_two():
    input2 = [[int(s) for s in line.rstrip("\n").replace(" -> ", ",").split(",")] for line in open("2021/input/05.txt") if line != "\n"]
    
    # PART ONE -------------------------------------------------------
    input1 = [l for l in input2 if l[0] == l[2] or l[1] == l[3]] # only keep horisontal or vertical lines for this part
    I = np.array(input1)
    maxVals = I.max(axis=0)
    rows, columns = max(maxVals[0], maxVals[2]) + 1, max(maxVals[1], maxVals[3]) + 1
    V = np.zeros((rows, columns)) # V is matrix of locations of vents
    
    for (x1, y1, x2, y2) in input1:
        if x1 == x2 and y1 != y2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                V[x1, y] += 1

        if x1 != x2 and y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                V[x, y1] += 1

    print("PART ONE: ", np.sum(V >= 2))

    # PART TWO -------------------------------------------------------
    I = np.array(input2)
    maxVals = I.max(axis=0)
    rows, columns = max(maxVals[0], maxVals[2]) + 1, max(maxVals[1], maxVals[3]) + 1
    V = np.zeros((rows, columns)) # V is matrix of locations of vents
    
    for (x1, y1, x2, y2) in input2:
        if x1 == x2 and y1 != y2: # horisontal
            for y in range(min(y1, y2), max(y1, y2) + 1):
                V[x1, y] += 1

        if x1 != x2 and y1 == y2: # vertical
            for x in range(min(x1, x2), max(x1, x2) + 1):
                V[x, y1] += 1
        
        if x1 != x2 and y1 != y2: # diagonal
            def myToList(a,b):
                if a < b:
                    return list(range(a, b + 1))
                else:
                    return list(range(b, a + 1))[::-1] # reverses the list, eq. to [-1:-(n+1):-1]
            
            xs, ys = myToList(x1, x2), myToList(y1, y2)
            for x,y in zip(xs, ys):
                V[x,y] += 1

    print("PART TWO: ", np.sum(V >= 2))

if __name__ == "__main__":
    part_one_and_two()