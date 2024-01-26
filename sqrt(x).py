x = int(input())

def sqrt(x) -> int:
    ans = 0
    if x == 0:
        ans = 0
    elif x == 1:
        ans = 1
    else:
        for i in range(x):
            if i * i <= x:
                ans = i
    return ans

print(sqrt(x))