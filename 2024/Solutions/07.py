from math import floor, log10

I = [l.strip().split(": ") for l in open("2024/Input/07.txt").readlines()]
I = [(int(v), list(map(int, nums.split(" ")))) for v, nums in I]


### <----------------------- PART ONE -----------------------> ###
def f(v, nums):
    S = set([nums[0]])
    for i in range(1, len(nums)):
        S = set(s + nums[i] for s in S) | set(s * nums[i] for s in S)
        S = set(s for s in S if s <= v)
    return v in S

print("PART ONE: ", sum(v * f(v, nums) for v, nums in I))


### <----------------------- PART TWO -----------------------> ###
def f2(v, nums):
    S = set([nums[0]])
    for i in range(1, len(nums)):
        S = set(s + nums[i] for s in S) | set(s * nums[i] for s in S) | set(s * 10 ** (1 + floor(log10(nums[i]))) + nums[i] for s in S)
        S = set(s for s in S if s <= v)
    return v in S

print("PART TWO: ", sum(v * f2(v, nums) for v, nums in I))







