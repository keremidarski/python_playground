# Problem description:
# https://leetcode.com/problems/single-number/

def single_number(nums):
    num_occurances = {}
    
    for num in nums:
        num_occurances[num] = num_occurances.get(num, 0) + 1
    
    for key, value in num_occurances.items():
        if value == 1:
            return key

# Expected: 1
print(single_number([2, 2, 1]))
# Expected: 4
print(single_number([4, 1, 2, 1, 2]))
# Expected: 2
print(single_number([2]))
