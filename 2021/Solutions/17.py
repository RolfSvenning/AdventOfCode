import re
import matplotlib.pyplot as plt
from numpy import ceil, sqrt, NINF, zeros, shape

def part_one_and_two():
    i = re.split("[ ,.=]+", open("2021/input/17.txt").readline().strip())
    print(i)
    Tx1, Tx2, Ty1, Ty2 = [int(s) for s in [i[3], i[4], i[6], i[7]]]

    assert 0 < Tx1 and Ty1 < 0 # TARGET IS STRICTLY TO THE RIGHT AND DOWN
    x1 = int(ceil(0.5*(sqrt(8 * Tx1 + 1) - 1)))

    yMax = NINF
    nrGoodInitVels = 0
    bestVX, bestVY = 0,0
    for vx_ in range(x1, Tx2+1):
        for vy_ in range(Ty1,-Ty1):
            vx = vx_
            vy = vy_
            x = y = 0
            yBest = NINF
            while(x <= Tx2 and y > Ty2): #SHOOTING
                x += vx
                y += vy
                if vx > 0:
                    vx -= 1
                vy -= 1
                yBest = max(yBest, y)
                if Tx1 <= x <= Tx2 and Ty1 <= y <= Ty2: # IN TARGET
                    nrGoodInitVels += 1
                    if yBest > yMax:
                        yMax = yBest
                        bestVX, bestVY = vx_, vy_
    print("Part one, max height reached is: ", yMax)
    print("Part two, number of good initial velocities: ", nrGoodInitVels)
    print("Best initial velocity:", bestVX, bestVY)
    shootAndPlot(bestVX, bestVY, Tx1, Tx2, Ty1, Ty2)


# PLOTTING FUNCTION -----------------------------------------------------------------------------------------
def shootAndPlot(vx, vy, Tx1, Tx2, Ty1, Ty2):
    x = y = 0
    positions = [(0,0)]
    while(x <= Tx2 and y > Ty2): #SHOOTING
        x += vx
        y += vy
        
        if vx > 0:
            vx -= 1
        vy -= 1
        positions.append((x,y))
        if Tx1 <= x <= Tx2 and Ty1 <= y <= Ty2: # IN TARGET
            break
    positions = [(x, y - Ty1) for x,y in positions]
    plt.scatter([x for x,_ in positions], [y for _,y in positions], color='black')
    plt.scatter(positions[0][0], positions[0][1], color='green')
    plt.scatter(positions[-1][0], positions[-1][1], color='red')
    plt.show()
# PLOTTING FUNCTION -----------------------------------------------------------------------------------------

if __name__ == '__main__':
    part_one_and_two()