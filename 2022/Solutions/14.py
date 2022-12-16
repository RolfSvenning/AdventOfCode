import numpy as np

def buildA(xs, ys, rock_paths):
    xmin, xmax = min(xs), max(xs)
    xrange = xmax - xmin
    ymin, ymax = min(ys), max(ys)
    yrange = ymax - ymin
    A = np.full((yrange + 1, xrange + 1), ".")

    for path in rock_paths:
        x1, y1 = path[0]
        for x3,y3 in path[1:]:
            if x1 == x3:
                for y2 in range(min(y1, y3) - ymin, max(y1, y3) - ymin + 1):
                    A[y2, x1 - xmin] = "#"
            else:
                for x2 in range(min(x1, x3) - xmin, max(x1, x3) - xmin + 1):
                    A[y1 - ymin, x2] = "#"
            x1, y1 = x3, y3
    return A, xmin, ymin, xrange, yrange


def printA(A):
    n, _ = np.shape(A)
    strA = "".join(["".join(A[i,:]) + "\n" for i in range(n)])
    print(strA)


def returnMove(A, x, y, xrange, yrange):
    def outOfBound(y, x):
        if not 0 <= x <= xrange or not 0 <= y <= yrange: return -2, -2
        return y, x

    if y + 1 > yrange or A[y + 1, x]     == ".": return outOfBound(y + 1, x)
    if x - 1 < 0      or A[y + 1, x - 1] == ".": return outOfBound(y + 1, x - 1)
    if x + 1 > xrange or A[y + 1, x + 1] == ".": return outOfBound(y + 1, x + 1)
    return -1, -1


def sendOneSandFrom(A, x, y, xrange, yrange, c="o"):
    A[y, x] = c
    while True:
        y_, x_ = returnMove(A, x, y, xrange, yrange)
        if (y_, x_) != (-1, -1) and (y_, x_) != (-2, -2):
            if c == "o": A[y, x] = "."
            y, x = (y_, x_)
            A[y, x] = c
        elif (y_, x_) == (-1, -1): 
            return False
        elif (y_, x_) == (-2, -2): 
            if c == "o": A[y, x] = "."
            return True


def partOneAndTwo(xs, ys, rock_parths, partTwo=False):
    A, xmin, ymin, xrange, yrange = buildA(xs, ys, rock_parths)
    for i in range(300000):
        x, y = 500 - xmin, 0 - ymin
        sandFallingBelow = sendOneSandFrom(A, x, y, xrange, yrange)

        if not partTwo and sandFallingBelow: 
            sendOneSandFrom(A, x, y, xrange, yrange, "~") # trace path where it falls out
            np.savetxt("2022/Output/14_partOne.out", A, fmt="%s")
            print("PART ONE:", i)
            break
        elif partTwo and A[y, x] == "o":
            np.savetxt("2022/Output/14_partTwo.out", A, fmt="%s")
            print("PART TWO:", i + 1)
            break
        # if not partTwo: 
        #     print(i)
        #     printA(A)

rock_paths1 = [[[int(c) for c in xy.split(",")] for xy in l.strip().split(" -> ")] for l in open("2022/Input/14.txt").readlines()]
xs1 = [x for path in rock_paths1 for x,_ in path] + [500]
ys1 = [y for path in rock_paths1 for _,y in path] + [0]

partOneAndTwo(xs1, ys1, rock_paths1)

ymax = max(ys1)
rock_paths2 = rock_paths1 + [[[500 - (ymax + 30), ymax + 2], [500 + (ymax + 30), ymax + 2]]]
xs2 = xs1 + [500, 500 - (ymax + 30), 500 + (ymax + 30)]
ys2 = ys1 + [0, ymax + 2]

partOneAndTwo(xs2, ys2, rock_paths2, partTwo=True)