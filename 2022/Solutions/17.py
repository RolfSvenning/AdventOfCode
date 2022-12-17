import numpy as np

jets = open("2022/Input/17.txt").read().strip()

# <---------------- ADD TYPES TO NP ARRAY (ONLY 1 BIT NEEDED)

s0 = np.array([1,1,1,1]).reshape((1,4))

s1 = np.array([[0,1,0], 
               [1,1,1], 
               [0,1,0]])

s2 = np.array([[0,0,1], 
               [0,0,1], 
               [1,1,1]])

s3 = np.array([[1], 
               [1], 
               [1], 
               [1]])

s4 = np.array([[1,1], 
               [1,1]])

shapes = [s0, s1, s2, s3, s4]


# def printBoardAndShape(B, s, sX, sY):
#     B_ = B.copy()
#     n,m = np.shape(s)
#     B_[sX - n : sX, sY: sY + m] -= s
#     print(B_, "\n")


def simulate(rocksCount, partTwo=False):
    foundCycle = not partTwo
    B = np.array([[1,0,0,0,0,0,0,0,1]] * 7 + [[1] * 9])
    D = {"<": -1, ">": 1}
    H = {} # heights at time i
    S = {} # state -> # buildings placed

    rockPos = np.shape(B)[0] - 1
    sX = rockPos - 3
    sY = 3

    i = 0
    j = -1
    while True:
        j += 1
        jet = jets[j % len(jets)]
        s = shapes[i % 5]
        n, m = np.shape(s)

        # MOVE JET
        sY += D[jet]
        if ((B[sX - n : sX, sY: sY + m] + s) > 1).any(): 
            sY -= D[jet]

        # MOVE DOWN
        sX += 1
        if ((B[sX - n : sX, sY: sY + m] + s) > 1).any():
            # PLACE SHAPE
            sX -= 1
            B[sX - n : sX, sY: sY + m] += s
            i += 1

            # PREPARE FOR NEXT SHAPE
            if (deltaRockPos := rockPos - min(rockPos, sX - n)) != 0:
                B = np.vstack((np.array([[1,0,0,0,0,0,0,0,1]] * deltaRockPos), B))
            sX = rockPos - 3
            sY = 3

            # CYCLE DETECTION FOR PART TWO
            if not foundCycle:
                H[i] = np.shape(B)[0] - 7 - 1
                # State should technically be BFS from top of board to get entire boundary... but this is good enough
                state = tuple([np.where(B[:,index] == 1)[0][0] for index in range(1, 1 + 7)] + [i % 5, j % len(jets)])
                if state in S:
                    last_i = S[state]
                    cycleLen = i - last_i
                    cycleCount = (rocksCount - i) // cycleLen
                    cyclesHeight = cycleCount * (H[i] - H[last_i])
                    i += cycleLen * cycleCount
                    foundCycle = True
                S[state] = i

            if i == rocksCount: break

    return (np.shape(B)[0] - 7 - 1) + (0 if not partTwo or not foundCycle else cyclesHeight)       


print("PART ONE:", simulate(2022))
print("PART TWO:", simulate(1000000000000, partTwo=True))
