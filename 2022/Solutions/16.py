from functools import cache
import re

input = [[l[0], int(l[1]), set(l[2:])] for l in [re.findall("\d+|[A-Z][A-Z]+", l) for l in open("2022/Input/16.txt").readlines()]]

class Vertex:
  def __init__(self, id, rate, edges):
    self.id = id
    self.rate = rate
    self.edges = edges

  def __repr__(self):
    return f"({self.rate}, {self.edges})"

G = {u:Vertex(u, rate, adj) for u, rate, adj in input}
print("G1", G)

def BFS(u):
    visited = [u]
    D = {(u,u):0}
    Q = [u]

    def BFS_visit(v):
        for w in G[v].edges:
            if w in visited: continue
            D[(u,w)] = D[(u,v)] + 1
            Q.append(w)
            visited.append(w)

    for v in Q:
        BFS_visit(v)

    return D

# print("BFS", BFS("A"))
D = {k:v for u in G.keys() for k,v in BFS(u).items()}
# print("D", D)

def skipNode(u):
    for v in G[u].edges:
        G[v].edges |= G[u].edges
        G[v].edges -= set([u,v])

for u in G.keys():
    if G[u].rate == 0 and u != "AA": skipNode(u)

G = {u:node for u,node in G.items() if node.rate != 0 or u == "AA"}
print("G2", G)

@cache
def releasePressure(u, time, opened):
    # print(opened)
    if time <= 0: return 0

    res = [0] * (len(G[u].edges) + 1)
    # print("time", time)
    if u not in opened:
        res[0] = releasePressure(u, time - 1, opened | set([u])) + (time - 1) * G[u].rate # <------------------------------ time - 1

    for i, v in enumerate(G[u].edges):
        assert D[(u,v)] != 0
        # print(i, u, v)
        res[i + 1] = releasePressure(v, time - D[(u,v)], opened)
    # print("res:", res)
    return max(res)

p1 = releasePressure("AA", 30, frozenset()) # <------------------------------ 29 and start

print(p1)