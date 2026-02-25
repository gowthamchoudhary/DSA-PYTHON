# 4. Product of Array Except Self
# Given an integer array nums, return an array answer such that
# answer[i] is equal to the product of all the elements of nums
# except nums[I].

# The product of any prefix or suffix of nums is guaranteed to fit in a
# 32-bit integer.

# You must write an algorithm that runs in O(n) time and without
# using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
nums = [1,2,3,4]

def product_array(arr):
    product = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j :
                continue
            else:
                product[i]= product[i]*arr[j]
    return product
print(product_array(nums))
        