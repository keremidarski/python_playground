# Problem description:
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/

def find_final_value(nums, original):
    while original in nums:
        original *= 2
    
    return original


# Expected: 24
print(find_final_value([5,3,6,1,12], 3))
