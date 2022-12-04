import re

with open("2022/Input/04.txt", "r") as f:
    lines = [[int(i) for i in re.split(",|-", l.strip())] for l in f.readlines()]

# Part 1
def contained_in(s1, e1, s2, e2):
    # s1 s2 e2 e1 
    return (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2)

print("Part 1:", sum([contained_in(*l) for l in lines]))

# Part 2
def overlaps(s1, e1, s2, e2):
    # s1----e1 s2----e2
    # s2----e2 s1----e1
    return not (e1 < s2 or e2 < s1)

print("Part 2:", sum([overlaps(*l) for l in lines]))