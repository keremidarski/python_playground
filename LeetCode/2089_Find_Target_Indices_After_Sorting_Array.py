# Problem description:
# https://leetcode.com/problems/find-target-indices-after-sorting-array/

def find_target(nums, target):
    result = []
    
    for index, number in enumerate(sorted(nums)):
        if number == target:
            result.append(index)
        
    return result

print(find_target([1, 2, 5, 2, 3], 2))
