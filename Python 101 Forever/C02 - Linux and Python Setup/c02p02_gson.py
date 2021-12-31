# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C02-Linux-and-Python-Setup/12-C02P02

import sys
import json

def gson():
    file_name, key_path = sys.argv[1:3]

    with open(file_name, 'r') as the_file:
        contents = json.load(the_file)

    search_keys = []

    for token in key_path.split('.'):
        preprocessed = token.split('[')
        search_keys += [x.replace(']', '') for x in preprocessed]

    result = contents
    for key in search_keys:
        try:
            if key.isnumeric():
                result = result[int(key)]
            else:
                result = result.get(key)
        except (AttributeError, KeyError):
            print("Error: Property not found")
            sys.exit(1)

    return result

print(gson())
