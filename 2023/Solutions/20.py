ls = [(t, ds.split(", ")) for t, ds in [l.strip().split(" -> ") for l in open("2023/input/20.txt").readlines()]]

# print("ls: ", ls)

class Module:
    def __init__(self, name, ds):
        self.ds = ds
        self.t = name[0]
        self.id = name[1:]
        match self.t:
            case "%": self.state = 0
            case "&": self.state = {}
            case _: 
                if name == "broadcaster": 
                    self.state = "broadcaster"
                    self.id = name
                elif name == "rx":
                    self.state = "rx"
                    self.id = name
                else: self.state = None

    def receive(self, p, source, destination): # p: pulse, s: source, d: destination
        assert self.id == destination
        match self.t:
            case "b": return [(p, self.id, d) for d in self.ds]
            case "%": 
                if p: return []
                else: 
                    self.state ^= 1
                    return [(self.state, self.id, d) for d in self.ds]
            case "&": 
                self.state[source] = p
                
                notAllHigh = int(not all(self.state.values()))
                # print(self.state, notAllHigh)
                return [(notAllHigh, self.id, d) for d in self.ds]
    
            
    def __repr__(self):
        return "Module t id state ds: " + str(self.t) + " " + str(self.id) + " " + str(self.state) + " " + str(self.ds)
            
ms = {m.id: m for m in [Module(*l) for l in ls] if m.state != None}

for id, m in ms.items():
    for d in m.ds:
        if d in ms.keys() and ms[d].t == "&": ms[d].state[id] = 0

rounds = 1000
# print("ms:")
# for m in ms.items():
#     print(m)
#     pass


allPulses = []
for i in range(rounds):
    pulses = [(0, "button", "broadcaster")]
    for (t, s, d) in pulses:
        if d not in ms.keys(): continue
        for p_ in ms[d].receive(t, s, d):
            pulses.append(p_)
    allPulses.append(pulses)
# print("allPulses: ", allPulses)
lows  = sum(sum(p == 0 for p, _, _ in ps) for ps in allPulses)
highs = sum(sum(p == 1 for p, _, _ in ps) for ps in allPulses)
print(lows, highs)
print("PART ONE: ", lows * highs)

# PART TWO
ms2 = {m.id: m for m in [Module(*l) for l in ls] if m.state != None}
# ms2["rx"] = Module("rx", [])

# print("ms:")
# for m in ms2.items():
#     print(m)
#     pass

print("part 2")
i = 0
rxGotLow = False
while i < 10000:
    print("round: ", i, rxGotLow)
    pulses = [(0, "button", "broadcaster")]
    i = i + 1
    for (t, s, d) in pulses:
        if d == "jm" and t == 0:
            print(i, (t, s, d)) 
            print("DONE")
            rxGotLow = True
            break
        if d not in ms2.keys(): continue
        for p_ in ms2[d].receive(t, s, d):
            # if p_ == "DONE": print("HEHRHARE")
            for p_ in ms[d].receive(t, s, d):
                pulses.append(p_)
    # print("pulses: ", len(pulses))
    if rxGotLow: break

#too low 1000000





