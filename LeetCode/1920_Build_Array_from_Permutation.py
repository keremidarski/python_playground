def build_array(nums):
    result = nums.copy()
        
    for i in range(len(nums)):
        result[i] = nums[nums[i]]
    return result

# Expected: [0, 1, 2, 4, 5, 3]
print(build_array([0, 2, 1, 5, 3, 4]))