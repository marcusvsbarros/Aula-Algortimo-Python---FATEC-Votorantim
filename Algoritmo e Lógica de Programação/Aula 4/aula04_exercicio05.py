""" EXERCÍCIO 5 - AULA 4

Faça um algoritmo que receba o salário de um funcionário, calcule e mostre o novo  salário, sabendo-se que este sofreu um  aumento de 25%.
"""

# Input
salario = float(input("Digite o valor do seu salário em R$: "))

# Cálculo reajuste
salarioNovo = salario * 1.25

# Output
print(f"Seu salário com reajuste de 25% foi para: R$ {salarioNovo:.2f}")
