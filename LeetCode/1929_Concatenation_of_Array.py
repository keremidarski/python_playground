# Problem description:
# https://leetcode.com/problems/concatenation-of-array/

def get_concatenation(nums):
    result = []
    counter = len(nums)
        
    for i in range(2):
        while counter > 0:
            for i in nums:
                result.append(i)               
                counter -= 1
        counter = len(nums)
    
    return result

# Expected: [1, 2, 1, 1, 2, 1]
print(get_concatenation([1, 2, 1]))
