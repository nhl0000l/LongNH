x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

def decimalToBinary(decimal):
    binaryArr = []
    while(decimal > 0):
        binaryArr.append(decimal % 2)
        decimal = decimal // 2
    binaryArr.reverse()
    return binaryArr

x = decimalToBinary(x)
y = decimalToBinary(y)

def hammingDistance(x, y):
    distance = 0
    x.reverse()
    y.reverse()
    if len(x) < len(y):
        for i in range(len(y) - len(x)):
            x.append(0)
    elif len(y) < len(x):
        for i in range(len(x) - len(y)):
            y.append(0)
    x.reverse()
    y.reverse()
    for i in range(len(x)):
        if x[i] != y[i]:
            distance += 1
    return distance


print(hammingDistance(x,y))