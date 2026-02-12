## time : O(n),Space:O(1)
A = [-4,3,1,0,2,5,10,8,12,9]
#Build Min Heap (heapify)
import heapq
heapq.heapify(A)


#Heap Push insert element
#time :O(log n)
heapq.heappush(A,4)
#heap pop 
#time O(Log n)
min = heapq.heappop(A)
#Heap Sort 
#Time :O(n log n)
#space:o(n)🤯
def heapSort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n
    for i in range(n):
        min = heapq.heappop(arr)
        new_list[i] = min
    return new_list
print(heapSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))
print(A)