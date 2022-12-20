input = list(int(l) for l in open("2022/Input/20.txt").readlines())
n = len(input)
input1 = [(num, id) for id, num in enumerate(input)]

### <----------------------- PART ONE AND TWO -----------------------> ###
def mix(x, numbers):
    (k, id), i = next(((k, id), i) for i,(k, id) in enumerate(numbers) if id == x)
    j = (i + k) % n # new index
    newInput = numbers[:(j + 1)] + [(k, id)] + numbers[j + 1:]
    return newInput[:i + (j < i)] + newInput[i + 1 + (j < i):]


def performMixing(input, rounds=1):
    # Deal with large numbers once at the beginning. Ensures all are in range [0,n-1].
    input = [(k % (n - 1), id) for k,id in input]
    for _ in range(rounds):
        for i in range(n):
            input = mix(i, input)
    return input
            

part1 = performMixing(input1[:])
zero = [k for k,_ in part1].index(0)
print(f"PART ONE: {sum([input[part1[(zero + i * 1000) % n][1]] for i in range(1,4)])}")


input2 = [(811589153 * k,id) for k,id in input1]
part2 = performMixing(input2, rounds=10)
zero = [k for k,_ in part2].index(0)
print(f"PART TWO: {sum([input2[part2[(zero + i * 1000) % n][1]][0] for i in range(1,4)])}")