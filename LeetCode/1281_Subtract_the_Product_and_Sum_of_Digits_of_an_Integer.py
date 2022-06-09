# Problem description:
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/ 


def subtract_product_and_sum(n):
    digits = []
    product = 0
    sum_of_d = 0
    counter = 0
    
    for num in str(n):
        digits.append(int(num))
        
    for digit in digits:
        if counter == 0:
            product += digit
            sum_of_d += digit
            counter += 1
        else:
            product = product * digit
            sum_of_d += digit
           
    return product - sum_of_d


# Expected: 15
print(subtract_product_and_sum(234))
