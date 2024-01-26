arr = input("Enter array: ")
list = list(map(int, arr.split(" ")))
value = int(input("Enter value: "))

def interpolationSearch(list, value):
    high = int(len(list) - 1)
    low = int(list[0])

    while(value >= list[low] and value <= list[high] and low <= high):
        probe = int(low + (high - low) * (value - list[low]) / (list[high] - list[low]))
        print(f"Probe = {probe}")

        if list[probe] == value:
            return probe
        elif list[probe] >= low:
            low = probe + 1
        else:
            high = probe - 1
    return -1

index = int(interpolationSearch(list, value))

if index != -1:
    print(f"Element found at index: {index}")
else:
    print(f"Element not found")