import re
from collections import namedtuple

input = [(l[0], int(l[1]), set(l[2:])) for l in [re.findall("\d+|[A-Z][A-Z]+", l) for l in open("2022/Input/16.txt").readlines()]]

# print(input)
Node = namedtuple('Node', 'rate adj')
G = {u:[int(rate), adj] for u, rate, adj in input}
# print(G)

def skipNode(u):
    S = set()
    for v in G[u][1]:
        S.add(v)
    for v in G[u][1]:
        G[v][1] |= S
        G[v][1].remove(u)

for u in G.keys():
    if G[u][0] == 0: 
        skipNode(u)
G = {u:node for u,node in G.items() if node[0] != 0}


print("final:", G)
