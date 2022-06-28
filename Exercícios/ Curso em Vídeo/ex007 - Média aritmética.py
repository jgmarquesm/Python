# -*- coding: UTF-8 -*-
n = int(input("Deseja fazer a média de quantos valores? "))
i = 0
valores = []
while i < n:
    valor = float(input(f"Valor {i+1}: "))
    valores.append(valor)
    i += 1
print(f"A média aritmética é: {sum(valores)/n}")