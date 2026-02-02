arr = [4,1,5,3,2]
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print("Not sorted")
        break
    