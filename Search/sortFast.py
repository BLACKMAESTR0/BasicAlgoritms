import time
import sys
import random
import matplotlib.pyplot as plt
sys.setrecursionlimit(99999)
def quickSort1(array): # Быстрая сортировка с опорным элементом с индексом 0
    op = 0
    if len(array) < 2:
        return array
    else:
        OpEl = array[op]
        LessOpArr = [x for x in array[1:] if x <= array[op]] # Опорный элемент с нулевым индексом => начинаем поиск меньших с индекса 1, чтобы опорный элемент не повторился
        MoreOpArr = [x for x in array if x > array[op]]
        return quickSort1(LessOpArr) + [array[op]] + quickSort1(MoreOpArr)

def quickSort2(array): # Быстрая сортировка с опорным элементом с индексом len(array)//2
    op = len(array)//2
    if len(array) < 2:
        return array
    else:
        OpEl = array[op]
        LessOpArr = [x for x in array[:op]+array[op+1:] if x <= array[op]] # Опорный элемент с нулевым индексом => начинаем поиск меньших с индекса 1, чтобы опорный элемент не повторился
        MoreOpArr = [x for x in array if x > array[op]]
        return quickSort1(LessOpArr) + [array[op]] + quickSort1(MoreOpArr)
arrayOfFastWithZeroOrLen = [0,0]
for _ in range(1000):
    a = [random.randint(1,100000) for x in range(10**3)]
    s = time.time()
    q = (time.time())
    quickSort1(a)
    z = (time.time()) - q
    q = (time.time())
    quickSort2(a)
    b = (time.time()) - q
    if z < b:
        arrayOfFastWithZeroOrLen[0] += 1
    else:
        arrayOfFastWithZeroOrLen[1] += 1
plt.bar(["Опорный 0", "Опорный len(arr)//2"], arrayOfFastWithZeroOrLen)
plt.title('Сравнение опорного 0 и len(arr)//2. (Числа - количества, когда одно превосходит второе)')
plt.show()