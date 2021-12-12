import numpy as np


def part_one_and_two():
    energyLevels = np.array([[int(x) for x in list(line.strip())] for line in open("2021/input/11.txt")])
    n, d = np.shape(energyLevels)
    sumFlashes = 0
    r = 0
    while(True):
        r += 1
        energyLevels += 1
        while len(flashIndices := list(zip(np.where(energyLevels == 10)[0], np.where(energyLevels == 10)[1]))) > 0:
            sumFlashes += len(flashIndices)
            for x, y in flashIndices:
                energyLevels[x,y] += 1
                for i in range(max(0,x - 1), min(n, x + 2)):
                    for j in range(max(0,y - 1), min(d, y + 2)):
                        if energyLevels[i,j] < 10:
                            energyLevels[i,j] += 1 
        energyLevels[energyLevels == 11] = 0
        if np.sum(energyLevels == 0) == n*d:
            break
        
    print("Part one, total number of flashes in 100 steps: ", sumFlashes)
    print("Part two, first round when all flashes is: ", r)

if __name__ == '__main__':
    part_one_and_two()