with open("DinProg") as f:
    a=f.read()
a=a.split("\n")

name = [x.split()[0] for x in a]
cost = list(map(float,[x.split()[1] for x in a]))
weight = list(map(float,[x.split()[2] for x in a]))
weightOfTheBag = 4
tableOfMax = {x: 0 for x in range(weightOfTheBag+1)}
tableOfNames = {x: [] for x in range(weightOfTheBag+1)}
for i in range(len(a)):
    currArr = tableOfMax.copy()
    currArrNames = tableOfNames.copy()
    for z in range(1, len(tableOfMax)):
        if z >= weight[i]:
            if currArr[z] < cost[i]+currArr[z-weight[i]]:
                tableOfMax[z] = cost[i]+currArr[z-weight[i]]
                tableOfNames[z] = [name[i]] + currArrNames[z-weight[i]]
print(tableOfMax)
print(tableOfNames[4])