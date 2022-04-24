# Problem description:
# https://leetcode.com/problems/count-items-matching-a-rule/

def count_matches(items, rule_key, rule_value):
    key = 0
    result = 0
        
    if rule_key == 'type':
        key = 0
    elif rule_key == 'color':
        key = 1
    elif rule_key == 'name':
        key = 2
            
    for item in items:
        if item[key] == rule_value:
            result += 1
            
    return result

# Expected: 1
print(count_matches([['phone', 'blue', 'pixel'], ['computer', 'silver', 'lenovo'], ['phone', 'gold', 'iphone']], 'color', 'silver'))
# Expected: 1
print(count_matches([['phone','blue','pixel'], ['computer','silver','phone'], ['phone','gold','iphone']], 'type', 'phone'))
