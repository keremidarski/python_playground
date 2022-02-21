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

# Expected: 3
print(majority_element([3, 2, 3]))
# Expected: 2
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
