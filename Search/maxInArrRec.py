def MaxInArray(list, Max = -float("inf"), indCurr = 0):
    if Max < list[indCurr]:
        Max = list[indCurr]
    if indCurr == len(list)-1:
        return Max
    return MaxInArray(list,Max,indCurr = indCurr+1)
print(MaxInArray([2,3,40,5,6,7]))