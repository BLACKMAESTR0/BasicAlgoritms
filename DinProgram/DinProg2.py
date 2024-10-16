

# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ
# НЕ РАБОТАЕТ


with open("DinProg2") as f:
    a=f.read().strip()
a=a.split("\n")

name = [x.split()[0] for x in a]
time = list(map(float,[x.split()[1] for x in a]))
mark = list(map(float,[x.split()[2] for x in a]))
MaxTime = 100
key = list(set(time))
key.sort()
key = [0] + key
nameOfDost = {x: "" for x in key}
maxMarkBasedOnTime = {x: 0 for x in key}
for i in range(len(name)):
    currNames = nameOfDost.copy()
    currMax = maxMarkBasedOnTime.copy()
    newMaxBasedOnTime = maxMarkBasedOnTime.copy()
    newNameOfDost = nameOfDost.copy()
    for z in maxMarkBasedOnTime:
        if z >= time[i]:
            if z-time[i] in currMax:
                if maxMarkBasedOnTime[z] < mark[i] + currMax[z-time[i]]:
                    maxMarkBasedOnTime[z] = mark[i] + currMax[z-time[i]]
                    nameOfDost[z] = name[i] + currNames[z-time[i]]
                    for k in currMax:
                        if k+z not in maxMarkBasedOnTime and k!=z:
                            newMaxBasedOnTime[k+z] = maxMarkBasedOnTime[k] + maxMarkBasedOnTime[z]
                            newNameOfDost[k+z] = nameOfDost[k] + nameOfDost[z]
            else:
                maxMarkBasedOnTime[z] = mark[i] + currMax[int(z - time[i])]
                nameOfDost[z] = name[i] + currNames[int(z - time[i])]
                for k in currMax:
                    if k + z not in maxMarkBasedOnTime and k != z:
                        newMaxBasedOnTime[k + z] = maxMarkBasedOnTime[k] + maxMarkBasedOnTime[z]
    maxMarkBasedOnTime = newMaxBasedOnTime.copy()
print(maxMarkBasedOnTime)