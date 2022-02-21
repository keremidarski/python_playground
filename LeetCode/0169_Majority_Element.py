# Problem description:
# https://leetcode.com/problems/majority-element/

def majority_element(nums):
    count = {}
    result = 0
    max_count = 0

    for num in nums:
        count[num] = count.get(num, 0) + 1

        if count[num] > max_count:
            result = num

        max_count = max(count[num], max_count)

    return result
