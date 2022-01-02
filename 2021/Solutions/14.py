import collections

def part_one_and_two():
    polymer, rules = open("2021/input/14.txt").read().split("\n\n")
    rules = [x.split(" -> ") for x in rules.split("\n")]
    rulesMap = {}
    for l,r in rules:
        rulesMap[l] = r
    
    countsPairs = collections.defaultdict(int)
    counts = collections.defaultdict(int)    

    for a,b in zip(polymer,polymer[1:]):
        countsPairs[a + b] += 1
        counts[a] += 1
    counts[polymer[-1]] += 1
    
    for i in range(40):
        nextCount = collections.defaultdict(int)
        for a,b in [(k[0], k[1]) for k in countsPairs.keys()]:
            nextCount[a + rulesMap[a + b]] += max(countsPairs[a + b], 1)
            nextCount[rulesMap[a + b] + b] += max(countsPairs[a + b], 1)
            counts[rulesMap[a + b]] += max(countsPairs[a + b], 1)
        countsPairs = nextCount.copy()
        if i == 9:
            print("Part one, difference between most and least common: ", max(counts.values()) - min(counts.values()))
    print("Part two, difference between most and least common: ", max(counts.values()) - min(counts.values()))

# def naive_part_one():
#     polymer, rules = open("2021/input/14.txt").read().split("\n\n")
#     rules = [x.split(" -> ") for x in rules.split("\n")]
#     rulesMap = {}
#     for l,r in rules:
#         rulesMap[l] = r
    
#     for _ in range(10):
#         currPolymer = ""
#         for a,b in zip(polymer,polymer[1:]):
#             currPolymer += a + rulesMap[a + b]
#         currPolymer += polymer[-1]
#         polymer = currPolymer

#     C = collections.Counter(polymer)
#     print(polymer)
#     print("Part one, difference in frequence between most common and least common element in final string is: ", 
#            C.most_common()[0][1] - C.most_common()[-1][1])
           
if __name__ == '__main__':
    part_one_and_two()
    # naive_part_one()