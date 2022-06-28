def left_riemann(f, n, a, b):
    left_sum = 0
    dx = (b-a)/n
    x = []
    while a <= b:
        x.append(a)
        a += dx

    i = 0
    while i < n:
        left_sum += f(x[i])*dx
        i += 1
    return left_sum