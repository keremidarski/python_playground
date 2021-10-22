# https://leetcode.com/problems/defanging-an-ip-address/

# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".

def defang_ip_addr(address):
    result = []
        
    for char in address:
        if char == '.':
            result.append(f'[{char}]')
        else:
            result.append(char)
    return ''.join(result)

# Expected: "255[.]100[.]50[.]0"
print(defang_ip_addr("255.100.50.0"))
