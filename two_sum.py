n = int(input("nhap so tu nhien: "))

a = []

for i in range(n):
    a.append(int(input("nhap so thu %d: " % (i+1))))

sum = int(input("nhap tong: "))

for i in range(n-1):
    for j in range(i+1,n-1):
        if (i != j and a[i] + a[j] == sum):
            print(i,j)
            


