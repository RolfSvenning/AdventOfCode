rounds = open("2022/input/02.txt").read().strip().split("\n")

### <---------------- PART ONE ----------------> ###
D1 = {
    "A X": 3 + 1, 
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1, 
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1, 
    "C Y": 0 + 2,
    "C Z": 3 + 3
    }
print(sum([D1[r] for r in rounds]))

### <---------------- PART TWO ----------------> ###
D2 = {
    "A X": 0 + 3, 
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1, 
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2, 
    "C Y": 3 + 3,
    "C Z": 6 + 1
    }
print(sum([D2[r] for r in rounds]))