# -*- coding: UTF-8 -*-
string = input("Digite algo: ")
print(f"{string} é um alfanumérico? {string.isalnum()}")
print(f"{string} pode ser convertido em um número? {string.isnumeric()}")
print(f"{string} está todo em minúsculo? {string.islower()}")
print(f"{string} está todo em maiúsculo? {string.isupper()}")
print(f"{string} é um espaço em branco? {string.isspace()}")
print(f"{string} está Capitalizado? {string.istitle()}")
