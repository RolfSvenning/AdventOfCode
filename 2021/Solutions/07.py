import numpy as np


def part_one_and_two():
    positions = np.array([int(s) for s in next(open("2021/input/07.txt")).rstrip("\n").split(",")])
    median = int(np.median(positions))
    totalDistance = sum([abs(p - median) for p in positions])
    print("Part one total fuel: ", totalDistance)

    def dist(a, b):
        return int(((a - b)**2 + (abs(a - b))) / 2)
    meanPos = np.mean(positions)
    # take derivative of cost function d/dc 0.5 * sum_i (x_i - c)^2 |x_i - c| and observe it takes values in xbar +- 0.5
    cs = [int(c) for c in [np.floor(meanPos - 0.5), np.ceil(meanPos - 0.5), np.floor(meanPos + 0.5), np.ceil(meanPos + 0.5)]]
    totalDistance2 = min([sum([dist(p, c) for p in positions]) for c in cs])
    print("Part two total fuel: ", totalDistance2)


if __name__ == '__main__':
    part_one_and_two()