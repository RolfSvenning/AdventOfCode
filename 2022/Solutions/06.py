signal = open("2022/Input/06.txt").read().strip()

### <---------------- PART ONE ----------------> ###
for i in range(0, len(signal) - 3):
    if len(set(signal[i:i + 4])) >= 4: break
print(i + 4)

### <---------------- PART TWO ----------------> ###
for i in range(i, len(signal) - 13):
    if len(set(signal[i:i + 14])) >= 14: break
print(i + 14)