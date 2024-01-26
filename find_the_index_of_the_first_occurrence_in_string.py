haystack = str(input())
needle = str(input())

def findTheIndex(haystack,needle):
    x = haystack.find(needle)
    return x

print(findTheIndex(haystack,needle))
