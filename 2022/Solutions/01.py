allElfes = ("_".join(open("2022/input/01.txt").read().strip().split("\n"))).split("__")
sumPerElf = [sum([int(c) for c in calories.split("_")]) for calories in allElfes]

print(max(sumPerElf))                   # <------------ PART ONE
print(sum(sorted(sumPerElf)[-3::]))     # <------------ PART TWO