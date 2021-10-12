def defang_ip_addr(address):
    result = []
        
    for char in address:
        if char == '.':
            result.append(f'[{char}]')
        else:
            result.append(char)
    return ''.join(result)

print(defang_ip_addr("255.100.50.0"))