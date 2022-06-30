# -*- coding: UTF-8 -*-
from math import sqrt


def hipotenusa(co, ca):
    return sqrt(co**2 + ca**2)


cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))

print(hipotenusa(cateto_oposto, cateto_adjacente))
