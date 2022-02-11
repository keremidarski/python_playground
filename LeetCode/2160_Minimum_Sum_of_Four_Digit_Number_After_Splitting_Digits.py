def minimum_sum(num):
    nums = []

    for digit in (str(num)):
        nums.append(digit)

    nums.sort()

    new1 = f'{str(nums[0])}{str(nums[2])}'
    new2 = f'{str(nums[1])}{str(nums[3])}'

    return int(new1) + int(new2)
