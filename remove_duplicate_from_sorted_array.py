arr = input()
list = list(map(int, arr.split(" ")))

def removeDuplicate(list):
    replace = 1
    for i in range(1,len(list)):
        if list[i-1] != list[i]:
            list[replace] = list[i]
            replace += 1
    return replace

print(removeDuplicate(list))
        