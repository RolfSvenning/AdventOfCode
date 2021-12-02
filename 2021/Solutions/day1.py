from collections import deque


def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield int(row)

def part_one():
    input = csv_reader("2021\InputOutput\day1_input.txt")
    output = open("2021\InputOutput\day1_output_partA.txt", "w")

    last = next(input)
    output.write(f"{last} (N/A - no previous measurement)\n")
    number_of_increases = 0 
    for curr in input:
        if curr > last:
            number_of_increases += 1
            output.write(f"{curr} (increased)\n")
        else:
            output.write(f"{curr} (decreased)\n")
        last = curr

    print("Number of increases is: ", number_of_increases)

def part_two():
    input = csv_reader("2021\InputOutput\day1_input.txt")
    output = open("2021\InputOutput\day1_output_partB.txt", "w")

    d = deque([next(input), next(input), next(input)])
    lastSum = sum(d)
    output.write(f"{sum(d)} (N/A - no previous measurement)\n")
    number_of_increases = 0 
    for curr in input:
        d.popleft()
        d.append(curr)
        currSum = sum(d)
        if currSum > lastSum:
            number_of_increases += 1
            output.write(f"{currSum} (increased)\n")
        else:
            output.write(f"{currSum} (decreased)\n")
        lastSum = currSum

    print("Number of increases is: ", number_of_increases)
    

def shorter_solution():
    n = list(map(int, csv_reader("2021\InputOutput\day1_input.txt")))
    print(sum(a < b for a, b in zip(n, n[1:])))
    print(sum(a < b for a, b in zip(n, n[3:])))  # n[1:] and n[2:] would be repeated on both sides of the comparison statement

if __name__ == "__main__":
    part_one()
    part_two()
    shorter_solution()