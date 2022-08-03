pares = lambda x: x % 2 == 0


def filtrarPares(lista):
    return [x for x in lista if pares(x)]


def fibonacci(n):
    i = 0
    fib = [1, 2]
    if n <= 0:
        return []
    elif n == 1:
        return fib[0]
    else:
        while i + 2 < n:
            fib_new = fib[i] + fib[i + 1]
            fib.append(fib_new)
            i += 1
        return fib  # [n - 1]


fibb = fibonacci(32)  # 32 encontrado por força bruta rsrs
soma = sum(filtrarPares(fibonacci(32)))
print(soma)
