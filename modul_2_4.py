numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    a = (i)
    if a > 1:
        for j in range(2, (a // 2) + 1):
            if (a % j) == 0:
                not_primes.append(a)
                break
        else:
            primes.append(a)
print('Primes:', primes)
print('Not_primes:', not_primes)
