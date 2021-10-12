def running_sum(nums):
    result = []
    current_sum = 0
    
    for num in nums:
        current_sum += num
        result.append(current_sum)         
        
    return result

# Expected: [1, 3, 6, 10]
print(running_sum([1, 2, 3, 4]))