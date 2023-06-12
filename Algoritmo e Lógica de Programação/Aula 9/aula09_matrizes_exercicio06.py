"""  EXERCÍCIO 6-2 - AULA 9

Faça um algoritmo que leia uma matriz 10x20
com números inteiros e some cada uma das
linhas, armazenando o resultado das somas em
um vetor. A seguir, multiplique cada elemento
da matriz pela soma da linha e mostre a matriz
resultante.
"""

# Biblioteca
import numpy as np

# Declaração
matriz = np.zeros((10, 20), dtype=int)
for i in range(10):
    for j in range(20):
        matriz[i][j] = int(input(f"Digite o elemento da matriz [{i+1},{j+1}]: "))

# Declaração
somaLinhas = []
for i in range(10):
    soma = np.sum(matriz[i])
    somaLinhas.append(soma)

matrizResultante = np.zeros((10, 20), dtype=int)
for i in range(10):
    for j in range(20):
        matrizResultante[i][j] = matriz[i][j] * somaLinhas[i]

# Output
print("Matriz resultante:")
print(matrizResultante)
