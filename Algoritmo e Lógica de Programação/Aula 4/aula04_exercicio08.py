""" EXERCÍCIO 8 - AULA 4

Faça um algoritmo que calcule e mostre a área de um triângulo. Sabe-se que Área = (base * altura)/2
"""

# Input
altura = float(input("Digite o valor de altura deste triângulo: "))
base = float(input("Digite o valor da base deste triângulo: "))

# Calculo
areaTriangulo = base * altura // 2

# Output
print("O resultado é: ", areaTriangulo)
