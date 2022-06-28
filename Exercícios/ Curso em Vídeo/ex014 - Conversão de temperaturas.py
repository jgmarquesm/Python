# -*- coding: UTF-8 -*-
def conversao_C_to_F(celsius):
    return (9/5)*celsius + 32


def conversao_F_to_C(fahrenheit):
    return (5/9)*(fahrenheit - 32)


print("Para converter de Celsius para Fahrenheit, digite C.\nPara converter de Fahrenheit para Celsius, digite F.")
case = input("Qual conversão deseja? ")
case = case.lower()
if case == "c":
    temp = float(input("Qual temperetura deseja converter? "))
    print(f"{temp}°C equivalem à {conversao_C_to_F(temp)}°F")
elif case == "f":
    temp = float(input("Qual temperetura deseja converter? "))
    print(f"{temp}°F equivalem à {conversao_F_to_C(temp)}°C")
