import re
from functools import cmp_to_key

packet_pairs = [eval("[" + re.sub("\n", ",", pair) + "]") for pair in open("2022/Input/13.txt").read().strip().split("\n\n")]

### <----------------------- PART ONE -----------------------> ###
def orderOfPair(ps, qs):
    match ps, qs:
        case int(), int(): 
            if ps > qs: return  1 # in order
            if ps < qs: return -1 # not in order
            if ps == qs: return 2 # keep checking
        case list(), list(): 
            res = 2
            for p,q in zip(ps, qs):
                res = orderOfPair(p, q)
                if res != 2: return res
            return orderOfPair(len(ps), len(qs))
        case list(), int(): return orderOfPair(ps, [qs])
        case int(), list(): return orderOfPair([ps], qs)

res = []
for i, pair in enumerate(packet_pairs):
    res.append((orderOfPair(*pair) - 1) * (i + 1) / -2) # filters away those not in order
print(f"PART ONE {sum(res)}")

### -----------------------> PART TWO -----------------------> ###
sort_packet_pairs = sorted([[[2]]] + [[[6]]] + [packet for pair in packet_pairs for packet in pair], key=cmp_to_key(lambda x,y: orderOfPair(x,y)))
print(f"PART TWO: {(1 + sort_packet_pairs.index([[2]])) * (1 + sort_packet_pairs.index([[6]]))}")