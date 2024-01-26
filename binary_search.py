arr = input("Enter array: ")
list = list(map(int, arr.split(" ")))
value = int(input("Enter value: "))

def binarySearch(list, value):
    low = int(list[0])
    high = int(len(list) - 1)
    
    while low <= high:
        mid = (low + high) // 2

        if list[mid] == value:
            return mid
        elif list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

index = int(binarySearch(list, value))

if index != -1:
    print(f"Value found at index: {index}")
else:
    print("Value not found")
