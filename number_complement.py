import math
decimal = int(input("Enter decimal number: "))

def decimalToFlipBinary(decimal):
    binaryArr = []
    while(decimal > 0):
        binaryArr.append(decimal % 2)
        decimal = decimal // 2
    binaryArr.reverse()

    for i in range(len(binaryArr)):
        if binaryArr[i] == 1:
            binaryArr[i] = 0
        elif binaryArr[i] == 0:
            binaryArr[i] = 1
    return binaryArr

def binaryToDecimal(binaryArr):
    decimal = 0
    for i in range(len(binaryArr)):
        digit = binaryArr.pop()
        if digit == 1:
            decimal = decimal + pow(2, i)
    return decimal


print(decimalToFlipBinary(decimal))
print(binaryToDecimal(decimalToFlipBinary(decimal)))
