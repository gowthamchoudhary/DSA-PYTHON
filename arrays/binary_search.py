# Binary search - Array
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return "Element found at index " + str(mid)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return "Element not found in array"


arr = [1,2,3,4,5,6,7,8,9,10]
target = 7
print(binary_search(arr, target))