from functools import reduce


def part_one_and_two():
    lines = [list(line.strip()) for line in open("2021/input/10.txt")]

    sum1 = 0
    incomplete_scores = []
    for l in lines:
        stack = []
        l_corrupted = False
        for c in l:
            # print("stack: ", stack)
            if c in list("([{<"):
                stack.append(c)
            else:
                top = stack.pop()
                match top:
                    case "(": rev_top = ")"
                    case "[": rev_top = "]"
                    case "{": rev_top = "}"
                    case "<": rev_top = ">"
                if rev_top != c:
                    match c:
                        case ")": sum1 += 3
                        case "]": sum1 += 57
                        case "}": sum1 += 1197
                        case ">": sum1 += 25137
                    # l_corrupted = True
                    break
        else: # if not l_corrupted
            def score(c):
                match c:
                        case "(": return 1
                        case "[": return 2
                        case "{": return 3
                        case "<": return 4
            s = reduce(lambda a, c: 5 * a + score(c), stack[::-1], 0)
            incomplete_scores.append(s)
    print("Part one, sum of first illegal characters of corrupted lines is: ", sum1)
    print("Part two, median of incomplete scores", sorted(incomplete_scores)[int(len(incomplete_scores) / 2)])

if __name__ == '__main__':
    part_one_and_two()