def contains_duplicate(nums):
    occ = set()

    for num in nums:
        if num in occ:
            return True
        
        occ.add(num)

    return False
