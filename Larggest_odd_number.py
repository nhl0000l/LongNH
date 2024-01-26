n = input()

def oddNumber(n):
    for i in range(len(n)-1, -1, -1):
        if int(n[i]) % 2 != 0:
            return n[:i+1]
    return ""
        
print(oddNumber(n))
