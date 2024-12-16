import re

def f(s):
    I = list([list(map(int, re.findall(r'\d+', l))) for l in re.findall(r'mul\(\d{1,3},\d{1,3}\)', s)])
    return sum(a * b for a, b in I)


print("PART ONE: ", f(open("2024/input/03.txt").read())) 

DOs = [s.split("don't()")[0] for s in open("2024/input/03.txt").read().split("do()")]

print("PART TWO: ", sum(f(s) for s in DOs)) 
