from math import floor

arr = input()
list = list(map(str, arr.split(" ")))

def reverseString(arr):
    n = len(arr)
    for i in range(0, floor(n // 2)):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp
    return arr

print(reverseString(list))

