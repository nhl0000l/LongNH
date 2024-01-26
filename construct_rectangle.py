from math import sqrt

area = int(input("Enter area: "))
arr = []
length = width = area

for i in range(area, int(sqrt(area))-1, -1):
    if area % i == 0:
        length = min(length, i)
        width = area / length

print(f"[{length}, {int(width)}]")

