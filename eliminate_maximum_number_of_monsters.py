arr1 = input("Enter dist: ")
dist = list(map(int, arr1.split( )))
arr2 = input("Enter speed: ")
speed = list(map(int, arr2.split()))

n = len(dist)
if n == 1:
    print("1")
else:
    for i in range(n):
        dist[i] = dist[i] / speed[i]

    dist.sort()
    count = 1
    alive = True
    start = 1

    while alive and start <= n:
        for i in range(start, n):
            dist[i] = dist[i] - float(1)
        print(dist)
        if dist[start] > 0:
            count += 1
            start += 1
        else:
            alive = False

    print(count)
