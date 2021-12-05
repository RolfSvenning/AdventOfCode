def part_one():
    input = [line.rstrip("\n") for line in open("2021/input/03.txt")]
    nrOfBits = len(input[0])
    n = len(input)

    sums = [0] * nrOfBits
    for l in input:
        for i in range(nrOfBits):
            sums[i] += int(l[i])
    gamma_rate = "".join([str(int(s >= n/2)) for s in sums])
    epsilon_rate = "".join([str(int(s < n/2)) for s in sums])

    print("Gamma rate:  ", gamma_rate)
    print("Epsilon rate ", epsilon_rate)
    print("Product of the rates in decimal: ", int(gamma_rate, 2) * int(epsilon_rate, 2))


def part_two():
    input = [line.rstrip("\n") for line in open("2021/input/03.txt")]
    input2 = input
    nrOfBits = len(input[0])
    
    for i in range(nrOfBits):
        n = len(input)
        if n == 1:
            break
        sum = 0
        for bits in input:
            sum += int(bits[i])
        most_common = int(sum >= n / 2)
        input = [bits for bits in input if int(bits[i]) == most_common]
    oxygen_generator_rating = input[0]
    print("oxygen_generator_rating: ", oxygen_generator_rating)

    for i in range(nrOfBits):
        n = len(input2)
        if n == 1:
            break
        sum = 0
        for bits in input2:
            sum += int(bits[i])
        least_common = int(sum < n / 2)
        input2 = [bits for bits in input2 if int(bits[i]) == least_common]
    c02_scrubber_rating = input2[0]
    print("c02_scrubber_rating: ", c02_scrubber_rating)
    print("Product of the ratings in decimal: ", int(oxygen_generator_rating, 2) * int(c02_scrubber_rating, 2))

        
if __name__ == "__main__":
    print("PART ONE ------------------------------------------")
    part_one()
    print("\nPART TWO ------------------------------------------")
    part_two()