import re 
from functools import cmp_to_key


ls = [l.strip().split(" ") for l in open("2023/input/07.txt")]
V = {k : int(v) for k, v in ls}
C = list(V.keys())


def typeOfCard(card):
    cN = len(set(card))
    countOfEach = [len(re.findall(c, card)) for c in set(card)]
    CMax = max(countOfEach)

    match cN:
        # all cards are different => high card
        case 5: return 0
        # 3 unique, 2 equal => 1 pair
        case 4: return 1
        # two pair, or 3 equal
        case 3: return 2 if CMax == 2 else 3
        # 4 equal or full house
        case 2: return 4 if CMax == 3 else 5
        # 5 equal
        case 1: return 6

        case _: raise NotImplemented

types = [typeOfCard(C[i]) for i in range(len(C))]

nums = [(str(i), j) for i, j in zip(range(9, 1, -1), range(8, 0, -1))]
chars = [("A", 13), ("K", 12), ("Q", 11), ("J", 10), ("T", 9)]
S = {k:v for k,v in chars + nums}

def tie(a, b, S):
    for ai, bi in zip(a,b):
        if S[ai] < S[bi]: return -1
        if S[ai] > S[bi]: return 1
    
    raise NotImplemented    

def cmp(a, b):
    if typeOfCard(a) == typeOfCard(b): return tie(a, b, S)
    return -1 if typeOfCard(a) < typeOfCard(b) else 1

sortedCards1 = sorted(C, key=cmp_to_key(cmp))
print(sortedCards1)

print("PART ONE: ", sum(V[c] * (i + 1) for i, c in enumerate(sortedCards1)))

FIX = {k: v for k, v in zip(range(5), ["z", "x", "c", "v", "b"])}
def jokerType(a):
    
    aMinusJ = "".join(ai if ai != "J" else FIX[i] for i, ai in enumerate(a) )
    
    match len(re.findall("J", a)):
        case 0: raise NotImplemented
        case 1:
            match typeOfCard(aMinusJ):
                case 0: return 1
                case 1: return 3
                case 2: return 4
                case 3: return 5
                case 5: return 6
                case _: 
                    # print(a)
                    # print(aMinusJ)
                    # print(typeOfCard(aMinusJ)) 
                    raise NotImplemented
        case 2: 
            match typeOfCard(aMinusJ):
                case 0: return 3
                case 1: return 5
                case 2: raise NotImplemented
                case 3: return 6
                case 4: return NotImplemented
                case 5: raise NotImplemented
                case _: return 6
        case 3:
            match typeOfCard(aMinusJ):
                case 0: return 5
                case 1: return 6
                case 2: raise NotImplemented
                case 3: raise NotImplemented
                case 4: raise NotImplemented
                case 5: raise NotImplemented
                case 6: raise NotImplemented
                case _: raise NotImplemented
        case 4: return 6
        case 5: return 6    
        case _: raise NotImplemented



nums = [(str(i), j) for i, j in zip(range(9, 1, -1), range(9, 1, -1))]
chars = [("A", 13), ("K", 12), ("Q", 11), ("T", 10)]
S2 = {k:v for k,v in chars + nums + [("J", 1)]}

def cmp2(a, b):
    if "J" in a:
        if "J" not in b:
            return 1
    else:
        if "J" in b:
            return -1

    at = jokerType(a) if "J" in a else typeOfCard(a)
    bt = jokerType(b) if "J" in b else typeOfCard(b)
    if at == bt: return tie(a, b, S2)
    return -1 if at < bt else 1


sortedCards2 = sorted(C, key=cmp_to_key(cmp2))
print("PART TWO")
# print(sortedCards2)
# print(tie("32A45", "A2345", S2))

print(sum(V[c] * (i + 1) for i, c in enumerate(sortedCards2)))
# print(C)
print([(c, jokerType(c) if "J" in c else typeOfCard(c)) for c in sortedCards2])


assert(len(C) == len(set(C)))
for i, c in enumerate(C):
    if "J" in c: 
        assert(jokerType(c) >= typeOfCard(c))
        for i in range(5):
            assert jokerType(c) == jokerType(c[i:5] + c[0:i])
    else:
        for i in range(5):
            assert typeOfCard(c) == typeOfCard(c[i:5] + c[0:i])


# try: 251092133