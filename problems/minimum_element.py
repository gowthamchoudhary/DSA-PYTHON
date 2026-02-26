# 7. Find the Minimum in Rotated
# Sorted Array
# Given the sorted rotated array nums of unique elements, return
# the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
nums = [3,4,6,55,1,2]

def minimum_sorted(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
            
    return arr[low]
minimum_sorted(nums)
