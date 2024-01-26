s = str(input())

def lengthOfLastWord(s):
    s = s.rstrip()
    r = len(s)-1
    l = 0
    while s[r] != " ":
        l += 1
        r -= 1
    return l

print(lengthOfLastWord(s))