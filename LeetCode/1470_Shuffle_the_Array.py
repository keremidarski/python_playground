# https://leetcode.com/problems/shuffle-the-array/

# Given the array nums consisting of 2n elements in the form [x1, x2, ..., xn, y1, y2, ..., yn].
# Return the array in the form [x1, y1, x2, y2, ..., xn, yn].

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
