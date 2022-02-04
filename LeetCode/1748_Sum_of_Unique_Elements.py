# Problem description:
# https://leetcode.com/problems/sum-of-unique-elements/

def sum_of_unique(nums):
    result = 0
    occurances = {}

    for num in nums:
        if num not in occurances:
            occurances[num] = 1
        else:
            occurances[num] += 1

    for key, value in occurances.items():
        if value == 1:
            result += key

    return result