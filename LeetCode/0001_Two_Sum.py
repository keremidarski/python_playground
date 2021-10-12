def two_sum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i

print(two_sum([3,2,4], 6))
print(two_sum([3,2,4], 6) == [1, 2])