def restore_string(str, indices):
    result = indices.copy()
    str_list = list(str)
        
    for index, value in enumerate(indices):
        result[value] = str_list[index]
            
    return ''.join(result)

print(restore_string("aaiougrt", [4,0,2,6,7,3,1,5]))