arr = input()
digits = list(map(int,arr.split(" ")))

def plusOne(digits):
    digits0 = []
    s = 0
    for i in digits:
        s = s * 10 + i
    s += 1
    while s > 0:
        digits0.append(s % 10)
        s = s // 10
    digits0.reverse()
    return digits0

print(plusOne(digits))
