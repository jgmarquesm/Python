# https://www.codewars.com/kata/599bb194b7a047b04d000077

def how_many_pizzas(n):
    pizzas = (pow(n, 2)//pow(8, 2))
    slices =  int(0.125*(pow(n, 2)%pow(8, 2))) # 0.125 = 8/64 = 1/8
    return f"pizzas: {pizzas}, slices: {slices}"
