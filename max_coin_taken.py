def maxCoin(piles):
    n = len(piles)
    i = 0
    maxArr = []
    minArr = []
    result = []
    while i < n // 3:
        maxArr.append(max(piles))
        piles.remove(max(piles))
        minArr.append(min(piles))
        piles.remove(min(piles))
        result.append(max(piles))
        piles.remove(max(piles))
        i += 1
    return result

arr = input()
piles = list(map(int, arr.split()))
print(maxCoin(piles))
