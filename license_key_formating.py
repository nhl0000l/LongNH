s = str(input("Enter license key: "))
k = int(input("Enter key number: "))

def licenseKeyFormating(s, k):
    s = s.upper()
    key = [*s]
    key.reverse()
    licenseKey = ""

    arr = []

    for index in key:
        if index == "-":
            key.remove(index)

    count = 0
    for j in range(len(key)):
        arr.append(key[j])
        count += 1
        if count == k:
            arr.append("-")
            count = 0
    
    arr.reverse()

    if arr[0] == "-":
        arr.pop(0)

    for index in arr:
        licenseKey += index

    return licenseKey

print(licenseKeyFormating(s,k))
        
