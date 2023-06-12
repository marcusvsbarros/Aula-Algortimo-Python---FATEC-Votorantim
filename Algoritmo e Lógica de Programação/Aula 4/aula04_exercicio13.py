""" EXERCÍCIO 13 - AULA 4

Sabe-se que o quilowatt de energia custa um oitavo do salário mínimo. Faça um algoritmo que receba o valor do salário mínimo e a 
quantidade de quilowatts consumida por uma residência. Calcule e mostre:

a) O valor, em reais, de cada quilowatt
b) O valor, em reais, a ser pago por essa residência
c) O valor, em reais, a ser pago com desconto de 15%
"""

# Input
salarioMinimo = float(input("Digite o valor do salário mínimo: "))
consumoQuilowatt = float(input("Digite a quantidade de quilowatts consumidos: "))

# a) Calcular o valor de cada quilowatt em reais
valorQuilowatt = salarioMinimo / 8

# b) Calcular o valor a ser pago pela residência
total = valorQuilowatt * consumoQuilowatt

# c) Calcular o valor a ser pago com desconto de 15%
desconto = total * 0.15
valorFinal = total - desconto

# Output
print(f"O valor de cada quilowatt é R$ {valorQuilowatt:.2f}")
print(f"O valor a ser pago pela residência é R$ {total:.2f}")
print(f"O valor a ser pago com desconto de 15% é R$ {valorFinal:.2f}")
