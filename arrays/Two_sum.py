def Two_sum(arr,target,coord):
    for i in range(len(arr)):
        for j in range(len(arr)):
            cord = (i,j)
            if cord not in coord and arr[i]+arr[j] == target:                
                print(f"the indeces of the target sum :${(i,j)}")
                break


arr  = [1,2,3,5,6,89,8]
coord = set()
target = int(input("enter the target value to find the suitable sum :"))
Two_sum(arr,target,coord)
