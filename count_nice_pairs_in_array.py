def rev(x):
    ans = 0
    while x > 0:
        ans = ans * 10 + x % 10 
        x = x // 10
    return ans

def countNicePairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + rev(nums[j]) == rev(nums[i]) + nums[j] and i != j:
                count += 1
    MOD = 10 ** 9 + 7
    total = (count/2) % MOD
    return int(total)

arr = input()
nums = list(map(int, arr.split( )))
print(countNicePairs(nums))

