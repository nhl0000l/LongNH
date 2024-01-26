n = int(input())

def isPower(n):
    if n <= 0:
        return False
    else:
        while n >= 4:
            temp = n % 4
            if temp != 0:
                return False
            else:
                n = n // 4
        return True


print(isPower(n))


