# Problem description:
# https://leetcode.com/problems/contains-duplicate/


def contains_duplicate(nums):
    occ = set()

    for num in nums:
        if num in occ:
            return True
        
        occ.add(num)

    return False


# Expected: True
print(contains_duplicate([1, 2, 3, 1]))
# Expected: False
print(contains_duplicate([1, 2, 3, 4]))
# Expected: True
print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
