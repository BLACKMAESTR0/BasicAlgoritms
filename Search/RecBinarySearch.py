def BinarySearch(list, el, low, high):
    guess = (low + high)//2
    if low > len(list)-1 or high < 0:
        return None
    if list[guess] == el:
        return guess
    if list[guess] < el:
        return BinarySearch(list, el, low = guess+1, high = high)
    if list[guess] > el:
        return BinarySearch(list, el,  low = guess, high = guess - 1)
a = [1,2,3]
print(BinarySearch(a,-1, 0, len(a)-1))