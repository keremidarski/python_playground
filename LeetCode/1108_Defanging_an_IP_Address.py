# Problem description:
# https://leetcode.com/problems/defanging-an-ip-address/

def defang_ip_addr(address):
    result = []
        
    for char in address:
        if char == '.':
            result.append(f'[{char}]')
        else:
            result.append(char)
    return ''.join(result)

# Expected: '255[.]100[.]50[.]0'
print(defang_ip_addr('255.100.50.0'))
