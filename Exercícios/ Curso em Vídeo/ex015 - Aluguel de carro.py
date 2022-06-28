# -*- coding: UTF-8 -*-
km = float(input("Quantos Kilometros rodou? "))
dias = int(input("Quantos dias ficou alugado? "))
valor_dia = 60
valor_km = 0.15

print(f"O total a ser pago é: R${valor_km * km + valor_dia * dias}")
