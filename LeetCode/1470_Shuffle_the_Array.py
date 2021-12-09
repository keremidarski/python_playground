# Problem description:
# https://leetcode.com/problems/shuffle-the-array/

def shuffle_array(nums):
    result = []
    x_array = []
    y_array = []
        
    for i in range(nums):
        x_array.append(nums[i])
    for i in range(nums, nums * 2):
        y_array.append(nums[i])
    for i in range(nums):
        result.append(x_array[i])
        result.append(y_array[i])
        
    return result

# Expected: [2, 3, 5, 4, 1, 7]
print(shuffle_array([2, 5, 1, 3, 4, 7], 3))
