# -*- coding: UTF-8 -*-
numero = int(input("Deseja a tabuada de que número? "))
limite = int(input("Deseja multiplicar até que número? "))
for i in range(1, limite+1):
    print(f"{numero} x {i} = {numero*i}")
