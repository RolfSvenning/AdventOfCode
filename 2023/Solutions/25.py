import networkx as nx

input = [l.strip().split(": ") for l in open("2023/Input/25.txt")]
input = [(k, v.split(" ")) for k, v in input]
n = len(input)
G = nx.Graph()

def edges(i): 
    return [(input[i][0], v) for v in input[i][1]]

G.add_edges_from(list(e for i in range(n) for e in edges(i)))
P1, P2 = nx.stoer_wagner(G)[1]
print("PART ONE: ", len(P1) * len(P1))

