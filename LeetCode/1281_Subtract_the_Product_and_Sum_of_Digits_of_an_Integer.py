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

print(subtract_product_and_sum(234))