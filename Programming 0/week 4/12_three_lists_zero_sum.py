def three_lists_zero_sum(list_a, list_b, list_c):
    zero_sum = False
    
    for x in list_a:
        for y in list_b:
            for z in list_c:
                if x + y + z == 0:
                    zero_sum = True
                    print(x, y, z)
                    break

    return zero_sum

print(three_lists_zero_sum([1, 2, -10, 5, 0, 6], [10, -5, 2, 1], [0, -4, 10]))