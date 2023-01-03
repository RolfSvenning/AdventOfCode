input = [l.strip() for l in open("2022/Input/25.txt").readlines()]


def toDecimal(ds):
    sum = 0
    for i, d in enumerate(reversed(ds)):
        match d:
            case "=": sum += -2 * (5**i)
            case "-": sum += -1 * (5**i)
            case "0": sum +=  0 * (5**i)
            case "1": sum +=  1 * (5**i)
            case "2": sum +=  2 * (5**i)
    return sum

def closerToA(ds, a, b):
    assert ds - a >= 0 and b - ds >= 0
    return 1 if ds - a < b - ds else 0

def enc(d, isPositive):
    match d:
        case 0: return "0"
        case 1: return "1" if isPositive else "-"
        case 2: return "2" if isPositive else "="

def toSNAFU(ds, isPositive):
    if ds == 0: return []

    res = 0
    for i in range(ds + 1): # refactor next()
        res += 2 * 5**i
        if res >= ds: break

    g1 = 5**i
    g2 = 2 * 5**i
    
    if ds <= g1: 
        return [(i, enc(1, isPositive))] + toSNAFU(g1 - ds, not isPositive)
    if g1 < ds <= g2:
        if closerToA(ds, g1, g2): return [(i, enc(1, isPositive))] + toSNAFU(ds - g1, isPositive)
        else: return [(i, enc(2, isPositive))] + toSNAFU(g2 - ds, not isPositive)
    if g2 < ds < res + 1:
        return [(i, enc(2, isPositive))] + toSNAFU(ds - g2, isPositive)


def dec(ls):
    l = ["0"] * (ls[0][0] + 1)
    for i,s in ls:
        l[i] = s
    return "".join(reversed(l))


print("PART ONE:", dec(toSNAFU(sum([toDecimal(ds) for ds in input]), True)))