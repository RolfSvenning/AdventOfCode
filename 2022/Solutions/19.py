import re
from functools import cache

input = [[int(d) for d in re.findall("\d+", l)] for l in open("2022/Input/19.txt").readlines()]

def simulateBlueprint(b):
    _, r1Cost1, r2Cost1, r3Cost1, r3Cost2, r4Cost1, r4Cost3 = b
    print(_, r1Cost1, r2Cost1, r3Cost1, r3Cost2, r4Cost1, r4Cost3)

    def newRobotsFromResources(res1, res2, res3, time):
        
        
        for r1 in range((time >= r1Cost1 + 2) * (res1 // r1Cost1) + 1): # <-D-A-N-G-E-R-!-!-!----- # (time >= r1Cost1 + 2) #-------------------------
            
            res1Remaining1 = res1 - r1 * r1Cost1
            for r2 in range((time >= 2) * (res1Remaining1 // r2Cost1) + 1):

                res1Remaining2 = res1Remaining1 - r2 * r2Cost1
                for r3 in range(min(res1Remaining2 // r3Cost1, res2 // r3Cost2) + 1):
                    res2Remaining = res2 - r3 * r3Cost2
                    res1Remaining3 = res1Remaining2 - r3 * r3Cost1

                    # if res2Remaining > 2 * r3Cost2: continue # <-D-A-N-G-E-R-!-!-!------------------------------
                    for r4 in range(min(res1Remaining3 // r4Cost1, res3 // r4Cost3) + 1):
                        res1Remaining4 = res1Remaining3 - r4 * r4Cost1
                        res3Remaining = res3 - r4 * r4Cost3

                        if res1Remaining4 > r1Cost1: continue # <-D-A-N-G-E-R-!-!-!------------------------------
                        if res3Remaining > r4Cost3: continue # <-D-A-N-G-E-R-!-!-!------------------------------
                        yield r4, [r1, r2, r3], [res1Remaining4, res2Remaining, res3Remaining] # geode robots, state

    @cache
    def optimizeFromState(state):
        r1, r2, r3, res1, res2, res3, time = state
        if time == 1: return 0, state 
        if sum([r1, r2, r3]) % 100 == 0: print(state)
        
        bestFound, stateFound = 0, state
        for newGeodes, newRobots, resourcesRemaining in newRobotsFromResources(res1, res2, res3, time):
            r1Added, r2Added, r3Added = newRobots  
            res1NEW, res2NEW, res3NEW = resourcesRemaining  

            newState = (r1 + r1Added, r2 + r2Added, r3 + r3Added, r1 + res1NEW, r2 + res2NEW, r3 + res3NEW, time - 1)

            recFound, recState = optimizeFromState(newState)
            if bestFound < newGeodes * (time - 1) + recFound:
                bestFound = newGeodes * (time - 1) + recFound
                stateFound = recState

        return bestFound, stateFound
    

    maxTime = 24

    for time in range(18, maxTime + 1):
        initState = (1, 0, 0, 0, 0, 0, time)
        print(f"time {time}: {optimizeFromState(initState)}")

    return optimizeFromState((1, 0, 0, 0, 0, 0, maxTime))


# simulateBlueprint(input[0])

for b in input[:]:
    print(f"\n------blueprint: {b}------")
    print(simulateBlueprint(b))

# Notes:
# Maybe not best to spend as much as possible in every round?


# Heuristics:
# 1) only build robot if it has time to pay itself back
# 2) #oreRobots > #clayRobots
# 3) bound on ore needed

