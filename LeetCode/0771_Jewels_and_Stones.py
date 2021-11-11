# https://leetcode.com/problems/jewels-and-stones/

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

def jewels_in_stones(jewels, stones):
    counter = 0
    for stone in stones:
        for jewel in jewels:
            if stone == jewel:
                counter += 1
    
    return counter

# Expected: 3
print(jewels_in_stones('aA', 'aAAbbbb'))
