import math

arr  = input()
nums = list(map(int, arr.split( )))

m = 0
currentMax = 0

for i in nums:
    if i == 1:
        currentMax += 1
        m = max(m, currentMax)
    else:
        currentMax = 0

print(m)
        