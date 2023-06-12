""" EXERCÍCIO 2-2 - AULA 5

Faça um programa que receba a idade de um nadador e mostre a sua categoria usando as regras a seguir:

Categoria       Idade
Infantil        5 a 7
Juvenil         8 a 10
Adolescente     11 a 15
Adulto          16 a 30
Sênior Acima de 30
"""

idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil")
elif idade >= 8 and idade <= 10:
    print("Categoria: Juvenil")
elif idade >= 11 and idade <= 15:
    print("Categoria: Adolescente")
elif idade >= 16 and idade <= 30:
    print("Categoria: Adulto")
else:
    print("Categoria: Sênior")
