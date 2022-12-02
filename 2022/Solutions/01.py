# inputAsDigits = "".join(stringToDigit[s] for s in open("2021/input/23.txt").read()).split("\n")
# coords = [[int(s) for s in re.findall("\d", l)] for l in inputAsDigits if len(re.findall("\d", l)) > 0]

allElfes = ("_".join(open("2022/input/01.txt").read().split("\n"))).split("__")
sumPerElf = [sum([int(c) for c in calories.split("_")]) for calories in allElfes]

print(max(sumPerElf))                   # <------------ PART ONE
print(sum(sorted(sumPerElf)[-3::]))     # <------------ PART TWO