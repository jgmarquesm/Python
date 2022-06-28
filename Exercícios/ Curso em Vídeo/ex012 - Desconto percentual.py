# -*- coding: UTF-8 -*-
valor_produto = float(input("Qual o valor do produto? "))
porcentagem_de_desconto = float(input("Qual a porcentagem de desconto? "))

print(f"O produto custa R${valor_produto}, com {porcentagem_de_desconto}% fica R${valor_produto*(1-(porcentagem_de_desconto/100))}.")