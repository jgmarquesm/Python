def nth_fib(n_in):
    n = int(n_in)
    i = 0
    fib = [0,1]
    while i + 2 < n:
        fib_new = fib[i] + fib[i+1]
        fib.append(fib_new)
        i += 1
    return (fib[n-1])