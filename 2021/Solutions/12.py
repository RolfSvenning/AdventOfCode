from collections import defaultdict


def part_one_and_two():
    edgeList = [[x for x in line.strip().split("-")] for line in open("2021/input/12.txt")]
    V = set() #visitedSet
    A = defaultdict(list) #adjacencyRepresentation
    for u,v in edgeList:
        A[u].append(v)
        A[v].append(u)
    count1 = dfs("start", A, V, False)
    print("Part one, number of paths visiting small caves once: ", count1)
    count2 = dfs("start", A, V, True)
    print("Part one, number of paths where a one small cave can be visited twice: ", count2)


def dfs(u, A, V, freePass):
    if u == "end":
        return 1
    if u.islower():
        V.add(u)

    count = 0
    for v in A[u]:
        if v not in V:
            count += dfs(v, A, V.copy(), freePass)
        elif freePass and v != "start":
            count += dfs(v, A, V.copy(), False)
    return count


if __name__ == '__main__':
    part_one_and_two()