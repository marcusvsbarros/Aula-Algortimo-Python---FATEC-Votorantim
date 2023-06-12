""" EXERCÍCIO 7 - AULA 4

Faça um algoritmo que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total 
depois do rendimento.
"""

# Input
deposito = float(input("Digite o valor que deseja depositar em R$: "))
juros = float(input("Digite o valor percentual da taxa de juros: "))

# Calculo
jurosPercentual = deposito * juros // 100
rendimento = jurosPercentual
totalRendimentos = deposito + jurosPercentual

# Output
print(f"O valor do rendimento dos juros é de R$ {rendimento:.2f}")
print(f"O valor total do seu rendimento é de R$ {totalRendimentos:.2f}")