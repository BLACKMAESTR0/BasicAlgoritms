def FindMin(list: list):
    minInd = 0
    minEl = list[0]
    for i in range(len(list)):
        if list[i] < minEl:
            minEl = list[i]
            minInd = i
    return minInd
def SortVblborom(list: list):
    newArr = []
    for i in range(len(list)):
        indMin = FindMin(list)
        newArr.append(list.pop(indMin))
    return newArr
print(SortVblborom([3,4,1,22,3,55,63,-1]))
if not(None is None):
    print(1)
else:
    print(2)