# https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def running_sum(nums):
    result = []
    current_sum = 0
    
    for num in nums:
        current_sum += num
        result.append(current_sum)         
        
    return result

# Expected: [1, 3, 6, 10]
print(running_sum([1, 2, 3, 4]))
