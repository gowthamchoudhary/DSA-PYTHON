# problem:1. Two Sum
# Given an array of integer nums and an integer target, returnindices of the two numbers such that they add up to the target.
# You may assume that each input would have exactly one solution,and you may not use the same element twice.
# You can return the answer in any order.
# Input
# : nums = [2,7,11,15], target = 9
# Output
# : [0,1]
# Explanation
# : Because nums[0] + nums[1] == 9, we return [0, 1].


def two_sum(arr,target):
    output = {target:[]}
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                continue
            else:
                if arr[i]+arr[j] == target:
                    output[target].extend([i,j])
                    return output[target]

        
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))