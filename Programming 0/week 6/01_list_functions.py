# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week6/1-List-Functions

def head(list):
    list_head = list[0]
    
    return list_head

def last(list):
    list_last = list[-1]
    
    return list_last

def tail(list):
    result = []

    for index in range(1, len(list)):
        item = list[index]
        result += [item]
        
    return result

def eq_lists(l1, l2):
    if len(l1) != len(l2):
        return False

    for index in range(0, len(l1)):
        if l1[index] != l2[index]:
            return False
        
    return True

def count_item(element, list):
    count = 0

    for ele in list:
        if ele == element:
            count += 1
            
    return count

def take(n, list):
    result = []

    for i in range(0, n):
        result.append(list[i])
        
    return result

def drop(n, list):
    result = []

    for i in range(n, len(list)):
        result.append(list[i])
        
    return result

def reverse(list):
    reversed = []
    for i in list:
        reversed.insert(0, i)
        
    return reversed
