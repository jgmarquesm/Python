# https://www.codewars.com/kata/52549d3e19453df56f0000fe

def fib(n):
    i = 0
    fib = [0,1]
    while i + 2 < n:
        fib_new = fib[i] + fib[i+1]
        fib.append(fib_new)
        i += 1
    return (fib[n-1])
