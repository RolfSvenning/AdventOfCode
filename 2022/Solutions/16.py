from functools import cache
import re
import time


input = [[l[0], int(l[1]), set(l[2:])] for l in [re.findall("\d+|[A-Z][A-Z]+", l) for l in open("2022/Input/16.txt").readlines()]]

### <--------- Compressing graph G and creating distance dictionary D ---------> ###
class Vertex:
  def __init__(self, id, rate, edges):
    self.id = id
    self.rate = rate
    self.edges = edges

  def __repr__(self):
    return f'({self.id}, {self.edges})'

G1 = {u:Vertex(u, rate, adj) for u, rate, adj in input}

def BFS(u):
    visited = [u]
    D = {(u,u):0}
    Q = [u]
    def BFS_visit(v):
        for w in G1[v].edges:
            if w in visited: continue
            D[(u,w)] = D[(u,v)] + 1
            Q.append(w)
            visited.append(w)
    for v in Q:
        BFS_visit(v)
    return D


def skipNode(u):
    for v in G1[u].edges:
        G1[v].edges |= G1[u].edges
        G1[v].edges -= set([u,v])


D = {k:v for u in G1.keys() for k,v in BFS(u).items()}
for u in G1.keys():
    if G1[u].rate == 0 and u != "AA": skipNode(u)
edgesA = G1["AA"].edges
skipNode("AA")
G = {u:node for u,node in G1.items() if node.rate != 0 or u == "AA"}
D = {k:v for k,v in D.items() if k[0] in G and k[1] in G}

print(f"15 largest distances: {sorted(D.values())[-15:]}\nGraph input size: {len(G1)}\nCompressed graph size: {len(G)}\n")

### <----------------------- PART ONE & TWO -----------------------> ###
@cache
def releasePressure2(us, times, opened):
    # both done, 2nd check reduces time by factor 2.  !<----------- DANGER !!!!!! ------------ SET TO MAX DIST = 16, but 4 is enough for input
    if (max(times) <= 0 or abs(times[0] - times[1]) > 4) and times[1] != -1: return 0 
    
    bestSoFar = 0
    for i, (u, time) in enumerate(list(zip(us, times))):
        if time <= 0: continue
        times2 = [0,0]
        i_ = (i + 1) % 2
        times2[i_] = times[i_]
        
        for v in set(G.keys()) - set(opened):
            if (timeLeftFromV := time - D[(u,v)] - 1) <= 0: continue # no point in going
            us2 = [0,0]
            us2[i], us2[i_] = v, us[i_]
            times2[i] = timeLeftFromV
            bestSoFar = max(bestSoFar, releasePressure2(tuple(us2), tuple(times2), opened | set([v])) + timeLeftFromV * G[v].rate)

    return bestSoFar


t0 = time.time()
print("PART ONE:", releasePressure2(tuple(["AA", "AA"]), tuple([30, -1]), frozenset(["AA"])))
print("PART TWO:", releasePressure2(tuple(["AA", "AA"]), tuple([26, 26]), frozenset(["AA"])))
t1 = time.time()

print("\nTime in seconds:", round(t1 - t0, 6))





### <----------------------- PART ONE -----------------------> ###
# @cache
# def releasePressure(u, time, opened):
#     if time <= 0: return 0
#     bestSoFar = 0
    
#     for v in set(G.keys()) - set(opened):
#         if (timeLeftFromV := time - D[(u,v)] - 1) <= 0: continue # no point in going
#         bestSoFar = max(bestSoFar, releasePressure(v, timeLeftFromV, opened | set([v])) + timeLeftFromV * G[v].rate)
    
#     return bestSoFar
# print("PART ONE:", releasePressure("AA", 30, frozenset(["AA"])))