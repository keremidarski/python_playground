def smaller_numbers_than_current(nums):
    result = []
        
    for i in nums:
        counter = 0
        for j in nums:
            if j < i:
                counter += 1
        result.append(counter)
    return result

# Expected: [4, 0, 1, 1, 3]
print(smaller_numbers_than_current([8,1,2,2,3]))