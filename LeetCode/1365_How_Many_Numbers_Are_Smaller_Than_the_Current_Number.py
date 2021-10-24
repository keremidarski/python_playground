# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

def smaller_numbers_than_current(nums):
    result = []
        
    for i in nums:
        counter = 0
        for j in nums:
            if j < i:
                counter += 1
        result.append(counter)
    return result

# Expected: [4, 0, 1, 1, 3]
print(smaller_numbers_than_current([8, 1, 2, 2, 3]))
