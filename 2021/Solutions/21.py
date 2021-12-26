import numpy as np
from functools import cache


def part_one():
    positions = [int(l[-1]) for l in open("2021/input/21.txt").read().split("\n")]
    scores = np.array([0,0])
    die, sides, trackSize, goal = 1, 100, 10, 1000
    for i in range(goal):
        rolls = [((d - 1) % sides) + 1 for d in (die + np.array([0,1,2]))]
        positions[i % 2] = ((positions[i % 2] + sum(rolls) - 1) % trackSize) + 1
        scores[i % 2] += positions[i % 2]
        die = (die + 3) % sides
        if (scores >= goal).any():
            print("Part one, number of rolls time losers score: ", (i+1)*3 * np.min(scores))
            break

def part_two():
    p1,p2 = [int(l[-1]) for l in open("2021/input/21.txt").read().split("\n")]
    trackSize, goal  = 10, 21
    sums,counts = np.unique([sum([r1,r2,r3]) for r1 in [1,2,3] for r2 in [1,2,3] for r3 in [1,2,3]], return_counts=True)
    
    @cache
    def winsFromPosition(state):
        p1, p2, s1, s2, turn = state # positions, scores, next player turn
        if s1 >= goal or s2 >= goal:
            return np.array([s1 > s2, s2 > s1])
        wins = np.array([0,0],dtype='int64')
        turn_ = turn^1
        for s,c in zip(sums,counts):
            if turn == 0:
                p1_ = ((p1 + s - 1) % trackSize) + 1
                s1_ = s1 + p1_
                wins += c * winsFromPosition(tuple([p1_, p2, s1_, s2, turn_]))
            else:
                assert turn == 1
                p2_ = ((p2 + s - 1) % trackSize) + 1
                s2_ = s2 + p2_
                wins += c * winsFromPosition(tuple([p1, p2_, s1, s2_, turn_]))
        return wins
        
    wins = winsFromPosition(tuple([p1, p2, 0, 0, 0]))
    print("Part two, number of unierses where the most winning player: ", max(wins))

if __name__ == '__main__':
    part_one()
    part_two()