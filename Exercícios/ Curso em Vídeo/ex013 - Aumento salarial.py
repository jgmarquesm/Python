# -*- coding: UTF-8 -*-
salario_atual = float(input("Salário atual: "))
porcentagem_reajuste = float(input("Procentagem de reajuste: "))
novo_salario = salario_atual*(1+(porcentagem_reajuste/100))
print(f"O salário era R${salario_atual} e com reajuste de {porcentagem_reajuste}% ficou R${novo_salario}")
