p = int(input('Enter p: '))
counter_p = 0

for i in range(1, p + 1):
    if p % i == 0:
        counter_p += 1

if counter_p != 2:
    print(f'{p} is not a prime.')
else:
    q = p + 2
    z = p - 2

    counter_q = 0
    counter_z = 0

    for i in range(1, q + 1):
        if q % i == 0:
            counter_q += 1
    
    for i in range(1, z + 1):
        if z % i == 0:
            counter_z += 1
    
    if counter_q == 2 or counter_z == 2:
        print(f'Twin primes with {p}:')
        if counter_z == 2:
            print(f'{z}, {p}')
        if counter_q == 2:
            print(f'{p}, {q}')
    else:
        print(f'{p} is prime but:')
        print(f'{z} is not')
        print(f'{q} is not')