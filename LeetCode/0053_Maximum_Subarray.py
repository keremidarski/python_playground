# Problem description:
# https://leetcode.com/problems/maximum-subarray/


def max_sub_array(nums):
    max_sub = nums[0]
    curr_sum = 0

    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        
        curr_sum += n
        max_sub = max(max_sub, curr_sum)

    return max_sub


# Expected: 6
print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

