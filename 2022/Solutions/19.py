import re
from functools import cache

input = [[int(d) for d in re.findall("\d+", l)] for l in open("2022/Input/19.txt").readlines()]

def simulateBlueprint(b, maxTime):
    _, r1Cost1, r2Cost1, r3Cost1, r3Cost2, r4Cost1, r4Cost3 = b
    r1CostMax = max(r1Cost1, r2Cost1, r3Cost1, r4Cost1)

    def newRobotsFromResources(state):
        r1, r2, r3, _, res1, res2, res3, time, _ = state
        canBuilds = [res1 >= r1Cost1 and time >= r1Cost1 + 2 and r1 <= r1CostMax, 
                     res1 >= r2Cost1 and r2 <= r3Cost2, 
                     res1 >= r3Cost1 and res2 >= r3Cost2, 
                     res1 >= r4Cost1 and res3 >= r4Cost3]
        res1 += r1
        res2 += r2
        res3 += r3

        for i,t in reversed(list(enumerate(canBuilds))):
            if t:
                match (i + 1, t):
                    case 1, True: yield  [0 if j != i else 1 for j in range(4)], [res1 - r1Cost1, res2, res3]
                    case 2, True: yield  [0 if j != i else 1 for j in range(4)], [res1 - r2Cost1, res2, res3]
                    case 3, True: yield  [0 if j != i else 1 for j in range(4)], [res1 - r3Cost1, res2 - r3Cost2, res3]
                    case 4, True: yield  [0 if j != i else 1 for j in range(4)], [res1 - r4Cost1, res2, res3 - r4Cost3]
                    case _: raise NotImplementedError
            yield [0] * 4, [res1, res2, res3] # always try this?

    def upperBound(state):
        r4, time = state[3], state[7]
        return state[8] + r4 * time + ((time) * (time - 1) / 2)

    bestSoFar = [0]

    @cache
    def optimizeFromState(state):
        r1, r2, r3, r4, _, _, _, time, geodes = state
        if time == 1:
            if state[8] + r4 > bestSoFar[0]: bestSoFar[0] = state[8] + r4
            return state[8] + r4 
        else:
            temp = state[8]
            for newRobots, resourcesRemaining in newRobotsFromResources(state):
                if upperBound(state) < bestSoFar[0]: continue

                r1Added, r2Added, r3Added, r4Added = newRobots  
                res1NEW, res2NEW, res3NEW = resourcesRemaining
                if r1 >= r1CostMax: res1NEW = r1CostMax
                if r2 >= r3Cost2:   res2NEW = r3Cost2
                newState = (r1 + r1Added, r2 + r2Added, r3 + r3Added, r4 + r4Added, res1NEW, res2NEW, res3NEW, time - 1, geodes + r4)
                
                temp = max(temp, optimizeFromState(newState))

            return temp
    

    # for time in range(1, maxTime + 1):
    #     initState = (1, 0, 0, 0, 0, 0, 0, time, 0)
    #     print(f"time {time}: {optimizeFromState(initState)}")
    #     print(bestSoFar[0])

    return optimizeFromState((1, 0, 0, 0, 0, 0, 0, maxTime, 0))

maxTime = 24
res = [-1] * len(input)
for i,b in enumerate(input[:]):
    print(f"\n------blueprint: {b}------")
    res[i] = simulateBlueprint(b, maxTime)
    print(res[i])

print("res", res)
print("PART ONE", sum([(i+1) * v for i,v in enumerate(res) if v != None]),"\n")


maxTime = 32
res = [-1] * len(input)
for i,b in enumerate(input[:3]):
    print(f"\n------blueprint: {b}------")
    res[i] = simulateBlueprint(b, maxTime)
    print(res[i])

print("res", res)
print("PART TWO", res[0] * res[1] * res[2])

# Notes:
# Maybe not best to spend as much as possible in every round?


# Heuristics:
# 1) only build robot if it has time to pay itself back
# 2) #oreRobots > #clayRobots
# 3) bound on ore needed

