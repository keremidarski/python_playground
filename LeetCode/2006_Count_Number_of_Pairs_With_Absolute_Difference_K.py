# Problem description:
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

def count_k_difference(nums, k):
    result = 0

    for i in nums:
        for j in nums:
            if i - j == k:
                result += 1

    return result

print(count_k_difference([1, 2, 2, 1], 1))