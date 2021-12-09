# Problem description:
# https://leetcode.com/problems/number-of-good-pairs/

def good_pairs(nums):
    occurances = {}
    result = 0
        
    for i in nums:
        if i not in occurances:
            occurances[i] = 1
        else:
            occurances[i] += 1
    for value in occurances.values():
        result += (value * (value - 1) // 2)
        
    return result

# Expected: 4
print(good_pairs([1, 2, 3, 1, 1, 3]))
