# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C02-Linux-and-Python-Setup/05-C02P01

# chops the path into groups divided by ['/']
def get_groups(string): 
    result = []
    length = len(string)
    index = 0

    while index < length:
        next_index = index + 1
        char = string[index]
        temp_group = [char]
        
        if char == '/':
            result.append(temp_group)
            index = next_index
            continue

        while next_index < length and string[next_index] != '/':
            temp_group.append(string[next_index])
            next_index += 1

        result.append(temp_group)
        index = next_index
    
    return result


# removes unnecessary slashes
def reduce_slashes(groups): 
    result = []
    slash_count = 0

    for group in groups:

        if len(group) == 1 and group[0] == '/':
            if slash_count > 0:
                continue
            else:
                slash_count += 1
        else:
            slash_count = 0

        result.append(group)
        
    return result


def reduce_file_path(path):
    result = []
    groups = get_groups(path)
    trimmed_groups = reduce_slashes(groups)
    length = len(trimmed_groups)
    index = 0

    while index < length:
        group = trimmed_groups[index]

        if index + 2 < length:
            # skips the ['/'] and gets the next text group 
            next_group = trimmed_groups[index + 2]
            
            if next_group == ['.', '.']:
                # skips the next two text groups and the slashes
                index += 4
                continue 

        if group == ['.'] or group == ['.', '.']:
            index += 2
            continue

        index += 1
        result.append(''.join(group))

    final_result = ''.join(result)

    if len(final_result) > 1 and final_result[-1] == '/':
        return final_result[:-1]

    return final_result

# Expected: True
print(reduce_file_path("/") == "/")
print(reduce_file_path("/srv/../") == "/")
print(reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf")
print(reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf")
print(reduce_file_path("/srv/./././././") == "/srv")
print(reduce_file_path("/etc//wtf/") == "/etc/wtf")
print(reduce_file_path("/etc/../etc/../etc/../") == "/")
print(reduce_file_path("//////////////") == "/")
print(reduce_file_path("/../") == "/")
