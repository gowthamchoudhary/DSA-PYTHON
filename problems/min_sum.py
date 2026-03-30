def minSum(arr, n):
    arr.sort()
    
    total = arr[0]
    
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1] + 1
        total += arr[i]
    
    return total
print(minSum([2 ,2, 3, 5, 6],5))