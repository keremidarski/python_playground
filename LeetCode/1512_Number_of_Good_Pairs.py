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