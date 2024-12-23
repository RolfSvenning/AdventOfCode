from collections import defaultdict

E = set([tuple(l.strip().split("-")) for l in open("2024/Input/23.txt").readlines()])

### <----------------------- PART ONE -----------------------> ###

AL = defaultdict(lambda: set())
for u, v in E:
    AL[u].add(v)
    AL[v].add(u)

def f(u, v):
    return set(tuple(sorted([u, v, x])) for x in AL[u] & AL[v]) # optimize by intersecting smallest with largest

print("PART ONE: ", len(set().union(*[f(*e) for e in E if "t" in "".join(x[0] for x in e)])))

### <----------------------- PART TWO -----------------------> ###

Ts = set().union(*[f(*e) for e in E])

P = defaultdict(int)
for t in Ts:
    for x in t:
        P[x] += 1

print("PART TWO: ", len([x for x, p in P.items() if p == max(P.values())]))




            

# import networkx as nx
# import matplotlib.pyplot as plt


# def f3(t):
#     for x in t:
#         for y in t:
#             if x == y: continue
#             yield tuple(sorted((x, y)))


# # Create a graph object
# G = nx.Graph()

# E2 =  set.union(*[set(e for e in f3(t)) for t in Ts])
# # Add edges to the graph
# G.add_edges_from(set([e for e in E if e in E2]))

# # Draw the graph
# plt.figure(figsize=(8, 6))
# nx.draw(G)
# plt.title("Graph Visualization")
# plt.show()
