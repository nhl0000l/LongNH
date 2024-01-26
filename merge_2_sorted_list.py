arr1 = input()
list1 = list(map(int,arr1.split(" ")))
arr2 = input()
list2 = list(map(int,arr2.split(" ")))


def mergeList(list1,list2):
    list1.extend(list2)
    list1.sort()
    # for i in range(len(list1)):
    #     for j in range(i+1,len(list1)):
    #         if list1[i] > list1[j]:
    #             temp = list1[i]
    #             list1[i] = list1[j]
    #             list1[j] =temp
    return list1

print(mergeList(list1,list2))
