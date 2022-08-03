multiplosDe3ou5 = lambda n: sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)
soma = multiplosDe3ou5(1000)
print(soma)
