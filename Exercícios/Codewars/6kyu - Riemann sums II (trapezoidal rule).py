def riemann_trapezoidal(f, n, a, b):
    integral = 0
    dx = (b-a)/n
    x = []
    x0 = a
    while a < b:
        x.append(a)
        a += dx

    i = 1
    while i < n:
        integral += f(x[i])
        i += 1
    
    integral = round((integral + (f(b) + f(x0))/2)*dx, 2)
    
    return integral