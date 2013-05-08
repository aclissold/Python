print('First 5000 prime numbers:')
for n in range(2, 5000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, end=' ')
