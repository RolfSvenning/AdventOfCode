import numpy as np


def part_one():
    fish = np.array([int(s) for s in next(open("2021/input/06.txt")).rstrip("\n").split(",")])
    for _ in range(80):
        newFish = np.sum(fish == 0)
        fish[fish == 0] = 7
        fish[fish > 0] -= 1
        fish = np.concatenate((fish, np.array([8] * newFish)))
    print("Number of fish after 80 days is: ", len(fish))

def part_two():
    fish = np.array([int(s) for s in next(open("2021/input/06.txt")).rstrip("\n").split(",")])
    timers, counts = np.unique(fish, return_counts=True)
    fishCounts = np.zeros(9, dtype=np.int64)
    fishCounts[timers] = counts

    for _ in range(256):
        fishCounts2 = np.zeros(9, dtype=np.int64)
        for c in range(9):
            if c == 6:
                fishCounts2[c] = fishCounts[0] + fishCounts[c + 1]
            elif c == 8:
                fishCounts2[c] = fishCounts[0]
            else:
                fishCounts2[c] = fishCounts[c + 1]
        fishCounts = fishCounts2
    print("Number of fish after 256 days: ", sum(fishCounts))


if __name__ == '__main__':
    part_one()
    part_two()