"""  EXERCÍCIO 8 - AULA 9

Faça um algoritmo que lê 10 números inteiros e
os armazena em um vetor A.
Depois de armazenado, o algoritmo fará a
ordenação desses números (em ordem
crescente de valores) e os colocará no vetor B
Ao final o algoritmo deve mostrar os dois
vetores: A e B.
"""
# Declaração
vetorA = []

for i in range(10):
    numero = int(input("Digite o número {}: ".format(i + 1)))
    vetorA.append(numero)

vetorB = sorted(vetorA)

# Input
print("Vetor A: ", vetorA)
print("Vetor B: ", vetorB)
