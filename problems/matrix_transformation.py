def transform_array(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    for i in range(n):
        arr[i].reverse()
    return arr
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(transform_array(arr))