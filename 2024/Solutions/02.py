R = list(list(map(int, l.split(" "))) for l in open("2024/input/02.txt").readlines())

def isSafe(r): 
    if not (r == sorted(r) or r == sorted(r)[::-1]):
        return False
    for i in range(len(r)):
        if i != 0:
            if not abs(r[i - 1] - r[i]) in [1, 2, 3]: return False
        if i != len(r) - 1:
            if not abs(r[i + 1] - r[i]) in [1, 2, 3]: return False
    return True     


print("PART ONE: ", sum(1 for r in R if isSafe(r))) 

def isSafe2(r): 
    for i in range(len(r) + 1):
        if isSafe(r[:i - 1] + r[i:]): return True
    return False

print("PART TWO: ", sum(1 for r in R if isSafe2(r))) 
