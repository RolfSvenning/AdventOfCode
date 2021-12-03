from collections import deque

def read_input(file_name):
    for row in open(file_name, "r"):
        yield int(row)

def part_one():
    input = read_input("2021/Input/01.txt")

    last = next(input)
    number_of_increases = 0 
    for curr in input:
        if curr > last:
            number_of_increases += 1
        last = curr

    print("Number of increases is: ", number_of_increases)

def part_two():
    input = read_input("2021/Input/01.txt")

    # Creates sliding window of size 3
    d = deque([next(input), next(input), next(input)])
    lastSum = sum(d)
    number_of_increases = 0 
    for curr in input:
        d.popleft()
        d.append(curr)
        currSum = sum(d)
        if currSum > lastSum:
            number_of_increases += 1
        lastSum = currSum

    print("Number of increases is: ", number_of_increases)
    

def shorter_solution():
    n = list(map(int, read_input("2021/Input/01.txt")))
    print(sum(a < b for a, b in zip(n, n[1:])))
    print(sum(a < b for a, b in zip(n, n[3:])))  # n[1:] and n[2:] would be repeated on both sides of the comparison statement

if __name__ == "__main__":
    part_one()
    part_two()
    shorter_solution()
    