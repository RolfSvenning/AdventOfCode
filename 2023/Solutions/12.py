from functools import cache

ls = [l.strip().split(" ") for l in open("2023/input/12.txt")]
ls = [(l[0], tuple(map(int,l[1].split(",")))) for l in ls]

### <----------------------- PART ONE & TWO -----------------------> ###
def partOne(partTwo=False):
    res = 0
    for s, p in ls:
        if partTwo:
            s = "?".join([s] * 5)
            p = p * 5
        n, m = len(s), len(p)

        @cache
        def solve(i, j):
            if i == n:   return j == m
            if j == m:   return all("#" != c for c in s[i:])
            if (sj:=s[i]) == ".": return solve(i + 1, j)
            else:
                if i + (pj:=p[j]) > n: return 0
                if i + pj == n: return "." not in s[i : i + pj] and j + 1 == m
                putBlock = solve(i + pj + 1, j + 1) if "." not in s[i : i + pj] and s[i + pj] in ".?" else 0
                return putBlock + (solve(i + 1, j) if sj == "?" else 0)
        res += solve(0, 0)
    return res

print("PART ONE: ", partOne())
print("PART TWO: ", partOne(True))
