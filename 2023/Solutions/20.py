from math import lcm

ls = [(t, ds.split(", ")) for t, ds in [l.strip().split(" -> ") for l in open("2023/input/20.txt").readlines()]]

### <----------------------- PART ONE & TWO -----------------------> ###
class Module:
    def __init__(self, name, ds):
        self.ds = ds
        self.t = name[0]
        self.id = name[1:]
        match self.t:
            case "%": self.state = 0
            case "&": self.state = {}
            case _: 
                if name == "broadcaster" or name == "rx": 
                    self.state = name
                    self.id = name
                else: self.state = None

    def receive(self, p, s):
        match self.t:
            case "b": return [(p, self.id, d) for d in self.ds]
            case "%": 
                if p: return []
                else: 
                    self.state ^= 1
                    return [(self.state, self.id, d) for d in self.ds]
            case "&": 
                self.state[s] = p
                notAllHigh = int(not all(self.state.values()))
                return [(notAllHigh, self.id, d) for d in self.ds]

def roundsToTarget(target, partTwo=True):
    lows = 0
    highs = 0
    ms = {m.id: m for m in [Module(*l) for l in ls] if m.state != None}
    for id, m in ms.items():
        for d in m.ds:
            if d in ms.keys() and ms[d].t == "&": ms[d].state[id] = 0
    i = 0
    while 1:
        ps = [(0, "button", "broadcaster")]
        i = i + 1
        for (t, s, d) in ps:
            lows  += t == 0
            highs += t == 1
            if partTwo and s == target and t == 1: return i
            if d not in ms.keys(): continue
            for p_ in ms[d].receive(t, s):
                ps.append(p_)
        if not partTwo and i == 1000: return lows * highs


print("PART ONE: ", roundsToTarget("-1", partTwo=False))
print("PART TWO: ", lcm(*[roundsToTarget(t) for t in ["xj", "qs", "kz", "km"]]))
