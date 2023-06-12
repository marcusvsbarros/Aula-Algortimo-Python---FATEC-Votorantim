""" EXERCÍCIO 6 - AULA 4

Faça um algoritmo que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.
"""

# Input
salarioInicial = float(input("Digite o valor do seu salário em R$: "))
reajuste = float(input("Digite o valor do percentual do aumento de seu salário: "))

# Calculo
aumentoPercentual = reajuste / 100
aumento = salarioInicial * aumentoPercentual
salarioNovo = salarioInicial + aumento

# Output
print(f"O valor do aumento é de R$ {aumento:.2f}")
print(f"O valor atualizado do seu salário é de R$ {salarioNovo:.2f}")