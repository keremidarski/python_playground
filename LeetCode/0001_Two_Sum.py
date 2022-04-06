# Problem description:
# https://leetcode.com/problems/two-sum/


def two_sum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

            
# Expected: [1, 2]
print(two_sum([3, 2, 4], 6))
