""" EXERCÍCIO 1 - AULA 7

Faça um algoritmo que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir.
E = (2 ** 1) + (2 ** 2) + (2 ** 3) + ... + (2 ** N)
"""

# Input
N = int(input("Digite um valor inteiro e positivo: "))

# Cálculo
E = 0
for i in range(1, N + 1):
    E += 2 ** i

# Output 
print("Esse valor 'E' será calculado da seguinte forma: E = 2^1 + 2^2 + 2^3 + ... + 2^N, onde N é o valor que você escolheu")
print("Então o valor de E é:", E)
