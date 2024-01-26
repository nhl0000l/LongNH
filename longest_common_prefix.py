arr = input()
strs = list(map(str,arr.split(' ')))

def longestCommonPrefix(strs):
    base = strs[0]
    for i in range(len(base)):
        for j in strs[1:]:
            if ( i == len(j) or j[i] != base[i]):
                return base[0:i]
    return base

print(longestCommonPrefix(strs))