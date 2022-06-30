# -*- coding: UTF-8 -*-
from math import sin, cos, tan, pi

tipo_angulo = input("Deseja usar radianos ou graus? ")
tipo_angulo = tipo_angulo.lower()

valor_angulo = float(input("Valor do ângulo: "))

radiano = ["r", "rad", "radiano", "radianos", "pi"]
graus = ["g", "graus", "º"]

if tipo_angulo in radiano:
    print(f"O sen({valor_angulo}*pi) = {sin(pi*valor_angulo)}")
    print(f"O cos({valor_angulo}*pi) = {cos(pi*valor_angulo)}")
    print(f"O tan({valor_angulo}*pi) = {tan(pi*valor_angulo)}")

elif tipo_angulo in graus:
    print(f"O sen({valor_angulo}º) = {sin(pi*valor_angulo/180)}")
    print(f"O cos({valor_angulo}º) = {cos(pi*valor_angulo/180)}")
    print(f"O tan({valor_angulo}º) = {tan(pi*valor_angulo/180)}")
