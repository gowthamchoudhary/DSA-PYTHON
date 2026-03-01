# 9. 3Sum
# Given an integer array nums, return all the triplets [nums[i],
# nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[O] + nums[1] + nums[2] = (-1) + 0 +1 = 0.
# nums[1]+ nums[2] + nums[4] = 0 +1 +(-1) = 0.
# nums[O] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].


def three_sum(arr):
    triplet = {
        "tri":[]
    }
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            for k in range(j,len(arr)):
                if i == j or j == k or k == i:
                    continue
                else:
                    if arr[i]+arr[j]+arr[k] == 0:
                        triplet["tri"].append([arr[i],arr[j],arr[k]]) 
    return triplet["tri"]

print(three_sum([-1,0,1,2,-1,-4]))                    


