# Problem description:
# https://adventofcode.com/2015/day/4

import hashlib

def find_hash(prefix):
    n = 0

    while True:
        key = prefix + str(n)
        hash = hashlib.md5(f'{key}'.encode("utf-8")).hexdigest()

        if hash.startswith('00000'):
            return n

        n += 1

# Expected: 254575
print(find_hash('bgvyzdsv'))
