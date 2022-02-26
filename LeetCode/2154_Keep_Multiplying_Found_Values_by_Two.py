# Problem description:
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

def find_final_value(nums, original):
    while original in nums:
        original *= 2
    
    return original
