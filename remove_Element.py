arr = input()
nums = list(map(int,arr.split(" ")))
val = int(input())

def removeElement(list,val):
    list0 = []
    for i in list:
        if i != val:
            list0.append(i)
    return list0

print(len(removeElement(nums,val)))
print("nums= " + str(removeElement(nums,val)))
