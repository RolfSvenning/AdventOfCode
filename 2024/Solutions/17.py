R1, P1 = open("2024/Input/17.txt").read().split("\n\n")
P = [int(x) for x in P1.split(": ")[1].split(",")]
R1 = {l[9]: int(l.split(": ")[1]) for l in R1.split("\n")}
n = len(P)

### <----------------------- PART ONE -----------------------> ###

def combo(op, R):
    match op:
        case 4: return R["A"]
        case 5: return R["B"]
        case 6: return R["C"]
        case _: return op

def f(R, isPartTwo=False):
    output = []
    ip = 0
    while ip < n:
        op = P[ip + 1]

        match P[ip]:
            case 0: R["A"] = R["A"] >> combo(op, R)     
            case 1: R["B"] = R["B"] ^ op                    
            case 2: R["B"] = combo(op, R) % 8                     
            case 3:     
                if R["A"]:                                  
                    ip = op
                    continue
            case 4: R["B"] = R["B"] ^ R["C"]                 
            case 5:   
                if isPartTwo: return combo(op, R) % 8  
                output.append(combo(op, R) % 8)          
            case 6: R["B"] = R["A"] >> combo(op, R)        
            case 7: R["C"] = R["A"] >> combo(op, R)       
    
        ip += 2

    return output
        
print("PART ONE: ", ",".join(str(o) for o in f(R1)))
        

### <----------------------- PART TWO -----------------------> ###

def f2(i, A):
    if i == -1: return A
    target = P[i]

    S = [j for j in range(8) if f({"A": j + 8 * A, "B": 0, "C": 0}, True) == target]
    if not S: return 10**100

    return min(f2(i - 1, 8 * A + s) for s in S)


res = f2(n - 1, 0)
print("PART TWO: ", res)

R1["A"] = res
print(f(R1))





