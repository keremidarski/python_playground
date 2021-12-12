# Problem description:
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def final_value_after_operations(operations):
    result = 0
        
    for operation in operations:
        if '-' in operation:
            result += -1
        elif '+' in operation:
            result += 1
            
    return result

# Expected: 1
print(final_value_after_operations(["--X","X++","X++"]))
