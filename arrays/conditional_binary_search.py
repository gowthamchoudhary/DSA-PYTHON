# set of the true or false values and should find from which date he  started felling better # the values are sorted in ascending order
def binary_search_conditional(arr):
    left = 0
    right = len(arr)-1
    while(left<right):
        mid = (left+right)//2
        if(arr[mid]=='True'):
            left = mid+1
        else:
            right = mid
            mid = left
    return mid
arr = ['True','True','True','True','False','False','False']
print(binary_search_conditional(arr)) 
