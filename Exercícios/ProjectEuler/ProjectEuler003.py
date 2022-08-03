from math import sqrt as sq

def primeFactors(n):
    primeList = []
    while n % 2 == 0:
        primeList.append(2)
        n = n / 2
    for i in range(3, int(sq(n)) + 1, 2):
        while n % i == 0:
            primeList.append(i)
            n = n / i
    return primeList


x = 600851475143
print(primeFactors(x))