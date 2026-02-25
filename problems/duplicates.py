#problem 3. Contains Duplicate
# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element is
# distinct.

# Input: nums = [1,2,3,1]
# Output: true


nums = [1,2,3,5,7]
def duplicates(arr):
    seen = []
    for i in arr:
        if not i in seen:
            seen.append(i)
        else:
            return False
    return True
print(duplicates(nums))

