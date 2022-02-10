# Problem description:
# https://leetcode.com/problems/self-dividing-numbers/

def is_self_dividing(left, right):
    result = []
    is_self_dividing = False
    
    for num in range(left, right + 1):
        for digit in str(num):
            if digit != '0' and num % int(digit) == 0:
                is_self_dividing = True
            else:
                is_self_dividing = False
                break
                
        if is_self_dividing:
            result.append(num)
            
    return result
