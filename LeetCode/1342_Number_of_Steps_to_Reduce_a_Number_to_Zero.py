# Problem description:
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

def number_of_steps(num):
    counter = 0
        
    while num > 0:
        if num % 2 == 0:
            num = num // 2
            counter += 1
        else:
            num -= 1
            counter += 1
            
    return counter

# Expected: 6
print(number_of_steps(14))
