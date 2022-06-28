# -*- coding: UTF-8 -*-
largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
rendimento = 2 # 2m²/L

print(f"Para pintar toda a parede você precisa de {largura*altura/rendimento} L de tinta.")