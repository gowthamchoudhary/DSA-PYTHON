# 6. Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest
# product, and return the product.

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a
# subarray.
nums = [2,3,1,1]
def product_subarray(arr):
    max = arr[0]
    for i in range(len(arr)):
        max_1=arr[i]
        for j in range(i+1,len(arr)):
            max_1*=arr[j]
            if max_1>max:
                max = max_1
    return max
print(product_subarray(nums))
