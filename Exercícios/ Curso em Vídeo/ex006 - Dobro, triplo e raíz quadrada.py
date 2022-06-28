# -*- coding: UTF-8 -*-
print("Para saber o dobro do número, digite 2.")
print("Para saber o triplo do número, digite 3.")
print("Para saber a raíz quadrada do número, digite sqrt")

case = input("Caso escolhido: ")
if case.isnumeric():
    case = int(case)

numero = float(input("Digite seu número: "))

if case == 2:
    print(f"O dobro de {numero} é: {2*numero}")
if case == 3:
    print(f"O triplo de {numero} é: {3*numero}")
if case == "sqrt":
    print(f"A raíz quadrada de {numero} é: {numero**0.5}")
