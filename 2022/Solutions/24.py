input = [l.strip() for l in open("2022/Input/24.txt").readlines()]

n, m = len(input) - 2, len(input[0]) - 2
start, startGoal, end, endGoal = (-1, 0), (0, 0), (n, m - 1), (n - 1, m - 1) 
S = set([(x - 1, y - 1, input[x][y]) for x,y in [(x + 1, y + 1) for x in range(n) for y in range(m)] if input[x][y] in "<>^v"])


def updateState(S):
    def updateBlizzard(b):
        x, y, d = b
        match d:
            case ">": return (x, (y + 1) % m, d)
            case "<": return (x, (y - 1) % m, d)
            case "v": return ((x + 1) % n, y, d)
            case "^": return ((x - 1) % n, y, d)
    return set([updateBlizzard(b) for b in S])


states = [S]
for i in range(n * m):
    S = updateState(S)
    if S in states: break
    states.append(S)
states = [[(x,y) for x,y,_ in states[i]] for i in range(len(states))]


def printState(S):
    ls = [["."] * m for _ in range(n)]
    for x,y,d in S:
        ls[x][y] = d
    print("".join(["".join(l) + "\n" for l in ls]))


def adjMoves(p_s):
    p,s = p_s
    x,y = p
    currP = [(p, s + 1)] if p not in states[((s + 1) % len(states))] else []
    return currP + [(p_, s + 1) for p_ in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)] 
                    if p_ not in states[(s + 1) % len(states)] and 0 <= p_[0] < n and 0 <= p_[1] < m]


def BFS(start_time, end):
    Q = [start_time]
    visited = {start_time}
    for p, ps in Q:
        if p == end: break
        for q, qs in adjMoves((p, ps)):
            if (q, qs % len(states)) in visited: continue
            visited.add((q, qs % len(states)))
            Q.append((q, qs))
    return (ps + 1)


t1 = BFS((start, 0), endGoal)
print("PART ONE:", t1)
t2 = BFS((end, t1 + 1), startGoal)
t3 = BFS((start, t2 + 1), endGoal)
print(t1, t2, t3, "\nPART TWO:", t3)