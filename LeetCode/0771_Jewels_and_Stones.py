# Problem description:
# https://leetcode.com/problems/jewels-and-stones/


def jewels_in_stones(jewels, stones):
    counter = 0
    
    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                counter += 1
    
    return counter


# Expected: 3
print(jewels_in_stones('aA', 'aAAbbbb'))
# Expected: 0
print(jewels_in_stones('z', 'ZZ'))
