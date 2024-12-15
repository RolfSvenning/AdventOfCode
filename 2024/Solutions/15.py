from copy import deepcopy

I, S = open("2024/Input/15.txt").read().split("\n\n")
S = "".join(l for l in S.split("\n"))
I = [list(l.strip()) for l in I.split("\n")]
for i in range(len(I)):
    if "@" in I[i]:
        Px, Py = (i, I[i].index("@"))
n, m = len(I), len(I[0])

### <----------------------- PART ONE -----------------------> ###

# def printI(I):
#     print("\n".join("".join(l) for l in I))

def dir(s):
    match s:
        case "<": return ( 0, -1)
        case ">": return ( 0,  1)
        case "v": return ( 1,  0)
        case "^": return (-1,  0)

def part1(I, Px, Py):
    I = deepcopy(I)
    for i, s in enumerate(S):
        dx, dy = dir(s)
        Qx, Qy = Px + dx, Py + dy
        match I[Qx][Qy]:
            case ".": 
                I[Px][Py], I[Qx][Qy] = I[Qx][Qy], I[Px][Py]
                Px, Py = Qx, Qy
            case "#": continue
            case "O": 
                for i in range(1, max(n, m)):
                    match I[Qx + i * dx][Qy + i * dy]:
                        case ".": 
                            I[Qx + i * dx][Qy + i * dy], I[Qx][Qy] = I[Qx][Qy], I[Qx + i * dx][Qy + i * dy]
                            I[Px][Py], I[Qx][Qy] = I[Qx][Qy], I[Px][Py]
                            Px, Py = Qx, Qy
                            break
                        case "#": break
                        case "O": continue
    return I

def score(I, char):
    return sum(100 * i + j for i in range(n) for j in range(len(I[0])) if I[i][j] == char)

print("PART ONE: ", score(part1(I, Px, Py), "O"))
            

### <----------------------- PART TWO -----------------------> ###

def wideMap(I):
    return [list("".join([(2 * x if x != "O" else "[]") if x != "@" else "@." for x in l])) for l in I]

def part2(I, Px, Py):
    I = wideMap(I)
    for i, s in enumerate(S):
        dx, dy = dir(s)
        Qx, Qy = Px + dx, Py + dy
        match I[Qx][Qy]:
            case ".": 
                I[Px][Py], I[Qx][Qy] = I[Qx][Qy], I[Px][Py]
                Px, Py = Qx, Qy
            case "#": continue
            case   _:
                # inital frontier F
                Fs = [[(Px, Py)]]

                for i in range(2 * max(n, m)):
                    # find next frontier
                    F2 = set()
                    for Fx, Fy in Fs[i]:
                        match I[Fx + dx][Fy + dy]:
                            case ".": continue
                            case "#": break
                            case   _: 
                                F2 |= set([(Fx + dx, Fy + dy)])
                                if dx != 0:
                                    F2 |= set([(Fx + dx, Fy + dy + (1 if I[Fx + dx][Fy + dy] == "[" else -1))])
                    else:
                        # no more frontiers (and not blocked) => shift all frontiers and move the robot
                        if not F2: 
                            for F in reversed(Fs[1:]):
                                for Fx, Fy in F:
                                    I[Fx][Fy], I[Fx + dx][Fy + dy] = I[Fx + dx][Fy + dy], I[Fx][Fy]
                            I[Px][Py], I[Qx][Qy] = I[Qx][Qy], I[Px][Py]
                            Px, Py = Qx, Qy
                            break
                        
                        # go to next frontier
                        Fs.append(F2)
                        continue

                    break # found border
    return I

print("PART TWO: ", score(part2(I, Px, 2 * Py), "["))
