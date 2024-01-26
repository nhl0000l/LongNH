arr = input("Enter flowerbed: ")
flowerbed = list(map(int, arr.split( )))
n = int(input("Enter number of new flower: "))

def checkFlower(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
    if n == 0:
        return True
    else:
        return False

print(checkFlower(flowerbed, n))