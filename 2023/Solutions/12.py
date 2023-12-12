ls = [l.strip().split(" ") for l in open("2023/input/12.txt")]
ls = [(l[0], tuple(map(int,l[1].split(",")))) for l in ls]
# print(ls)


def partOne():
    for i in range(len(ls)):
        s, p = ls[i]
        n, m = len(s), len(p)
        print(s, p, n, m)
        def solve(i, j):
            if j == m: return all("#" != c for c in s[i:])
            return 1
        break

partOne()