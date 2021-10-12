def sort_sentence(s):
    s_list = []
    temp_group = []
    result = []
    for i in s:
        if i != ' ':
            temp_group.append(i)
        else:
            s_list.append(temp_group)
            temp_group = []
            continue
        s_list.append(temp_group)
    
    for num in range(10):
        for i in range(len(s_list)):
            if str(num) in s_list[i]:
                s_list[i].pop(-1)
                result.append(''.join(s_list[i]))

    return ' '.join(result)

print(sort_sentence("Myself2 Me1 I4 and3"))