import re

def part_one_and_two():
    As = re.findall("add x [-]*\d+", open("2021/input/24.txt").read())
    As = [(i,re.search("[-]*\d+", s)[0]) for i,s in enumerate(As)]
    Bs = re.findall("add y w\nadd y \d+", open("2021/input/24.txt").read())
    Bs = [(i,re.search("\d+", s)[0]) for i,s in enumerate(Bs)]

    As_ = [(i,"a",int(a)) for (i,a) in As if int(a) < 0]
    Bs_ = [(j,"b",int(b)) for ((_,a),(j,b)) in zip(As,Bs) if int(a) > 0]
    ABs_ = sorted(As_ + Bs_, key=lambda x: x[0])

    Ws_min, Ws_max = [0]*14, [0]*14
    stack = []
    for (j,type, val) in ABs_:
        if type == "b":
            stack.append((j,type, val))
        elif type == "a":
            (i,_,valB) = stack.pop()
            if (valB + val) >= 0:
                Ws_min[j] = 1 + (valB + val)
                Ws_min[i] = 1
                Ws_max[j] = 9
                Ws_max[i] = 9 - (valB + val)
            else:
                Ws_min[j] = 1
                Ws_min[i] = 1 - (valB + val)
                Ws_max[j] = 9 + (valB + val)
                Ws_max[i] = 9
        # print("stack: ", stack)
    print("Part one, largest valid model number:  ", "".join([str(s) for s in Ws_max]))
    print("Part two, smallest valid model number: ", "".join([str(s) for s in Ws_min]))


if __name__ == '__main__':
    part_one_and_two()

# -------------------------------------------------------------------------------
# | NO NEED TO EVALUATE THE PROGRAM AT ALL, DIRECTLY CALCULATE THE MODEL NUMBER |
# -------------------------------------------------------------------------------
#
# def evalInput():
#     Is = [l.split(" ") for l in open("2021/input/24.txt").read().split("\n")]
#     numbersInInput = re.findall("[-]*\d+", open("2021/input/24.txt").read())
#     env = {"x": 0, "y": 0, "z": 0, "w": 0}
#     for n in numbersInInput:
#         env[n] = int(n)
#
#     def evalprogram(input):
#         env["x"] = 0
#         env["y"] = 0
#         env["z"] = 0
#         env["w"] = 0
#         nextInput = 0
#         for I in Is:
#             match I[0]:
#                 case "inp": 
#                     env[I[1]] = input[nextInput]
#                     nextInput += 1
#                 case "add": env[I[1]] += env[I[2]]
#                 case "mul": env[I[1]] *= env[I[2]]
#                 case "div": env[I[1]] //= env[I[2]]
#                 case "mod": env[I[1]] %= env[I[2]]
#                 case "eql": env[I[1]] = int(env[I[1]] == env[I[2]])
#                 case _: raise NotImplemented
#         return env
#
#     env = evalprogram([int(s) for s in str(n)])
#     print("env: ", env)