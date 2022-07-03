# https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af

def fibonacci(n_in):
    n = int(n_in)
    i = 0
    fib = [0,1]
    while i + 2 <= n:
        fib_new = fib[i] + fib[i+1]
        fib.append(fib_new)
        i += 1
    fib_n = fib[n]
    return fib_n
