x = int(input())

def isPalindrome(x):
    a = str(x)
    n = len(a)
    i = 0
    for i in range(0,n-1-i):
        if a[i] != a[n-1-i]:
            return False
        else:
            return True

print(isPalindrome(x))
