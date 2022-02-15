# Problem description:
# https://leetcode.com/problems/single-number/

def single_number(nums):
    num_occurances = {}
    
    for num in nums:
        num_occurances[num] = num_occurances.get(num, 0) + 1
    
    for key, value in num_occurances.items():
        if value == 1:
            return key

