def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter descending array: ").split()))
target = int(input("Enter target: "))

print("Index:", binarySearch(arr, target))