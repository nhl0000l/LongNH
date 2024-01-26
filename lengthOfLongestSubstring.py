s = input()

def lengthOfLongestSubstring(s):
    ans = 0
    x = list(s)
    for i in range(len(x)):
        n = []
        n.append(x[i])
        for j in range(i+1, len(x)):
            if x[j]  in n:
                break
            else:
                n.append(x[j])
            if ans < len(x):
                ans = len(x)
    return ans          
    
print(lengthOfLongestSubstring(s))