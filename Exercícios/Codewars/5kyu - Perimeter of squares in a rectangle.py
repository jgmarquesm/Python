# https://www.codewars.com/kata/559a28007caad2ac4e000083

def fibonacci(n):
    i = 0
    fib = [0,1]
    empty_list = []
    if n <= 0:
        return empty_list
    if n == 1:
        return [0]
    else:
        while i + 2 < n:
            fib_new = fib[i] + fib[i+1]
            fib.append(fib_new)
            i += 1
        return fib

def perimeter(n):
    fib_list = fibonacci(n+2)
    sum = 0
    for fib in fib_list:
        sum += fib
    perimeter = 4*sum
    return perimeter
