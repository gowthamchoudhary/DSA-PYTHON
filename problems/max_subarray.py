# 5. Maximum Subarray
# Given an integer array nums, find the subarray with the largest
# sum, and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum of 1.

nums = [1]
def max_sub(arr):

    max = arr[0]
    for i in range(len(arr)):
        max_1 = 0
        for j in range(i,len(arr)):
            max_1 +=arr[j]
            if max_1>max:
                max = max_1
    return max
            
            
print(max_sub(nums))

            

        