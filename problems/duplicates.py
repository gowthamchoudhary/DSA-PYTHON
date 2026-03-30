#problem 3. Contains Duplicate
# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is
# distinct.

# Input: nums = [1,2,3,1]
# Output: true


nums = [1,2,3,5,1]
def duplicates(arr):
    nums_doop = set(arr)
    if len(arr)==len(nums_doop):
        return True
    else:
        return False
print(duplicates(nums))

