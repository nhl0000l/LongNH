arr = input()
height = list(map(int, arr.split( )))

def maxArea(height):
    n = len(height)
    max = (n - 1) * min(height[0], height[n - 1])
    l = 0
    r = n - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        if area > max:
            max = area
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1
    return max

print(maxArea(height))

