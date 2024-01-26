arr = input()
nums = list(map(int, arr.split(" ")))
target = int(input())

def searchInserPosition(nums,target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return l    

print(searchInserPosition(nums,target))

