# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C02-Linux-and-Python-Setup/05-C02P01

def reduce_file_path(path):
    result = []

    for i in path.split('/'):
        if i == '' or i == '.':
            continue

        if i == '..':
            if len(result) > 0:
                result.pop()
                continue
            else:
                continue

        result.append(i)
        
    return '/' + '/'.join(result)

# Expected: True
print(reduce_file_path("/") == "/")
print(reduce_file_path("/srv/../") == "/")
print(reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf")
print(reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf")
print(reduce_file_path("/srv/./././././") == "/srv")
print(reduce_file_path("/etc//wtf/") == "/etc/wtf")
print(reduce_file_path("/etc/../etc/../etc/../") == "/")
print(reduce_file_path("//////////////") == "/")
print(reduce_file_path("/..//////.") == "/")
print(reduce_file_path('/home/.../'))
