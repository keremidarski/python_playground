def hourglass(n):
    if n % 2 != 0:
        start = 3
    else:
        start = 4
    for i in range(n, 0, -2):
        for j in range(0, (n - i) // 2):
            print('.', end = '')
        for k in range(n - i, n):
            print('*', end = '')
        for l in range(0, (n - i) // 2):
            print('.', end = '')
        print()
    for i in range(start, n + 2, 2):
        for j in range(0, (n - i) // 2):
            print('.', end = '')
        for k in range(n - i, n):
            print('*', end = '')
        for l in range(0, (n - i) // 2):
            print('.', end = '')
        print()

hourglass(7)