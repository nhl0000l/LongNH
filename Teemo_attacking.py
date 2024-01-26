arr = input()
timeSeries = list(map(int, arr.split( )))
duration = int(input("Enter duration: "))
total = 0

for i in range(len(timeSeries)):
    total += 2
    for j in range(i+1, len(timeSeries)):
        if timeSeries[j] - timeSeries[i] < duration:
            total -= 1

print(total)