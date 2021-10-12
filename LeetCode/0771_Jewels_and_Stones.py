def jewels_in_stones(jewels, stones):
    counter = 0
    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                counter += 1
    return counter

print(jewels_in_stones("aA", "aAAbbbb"))