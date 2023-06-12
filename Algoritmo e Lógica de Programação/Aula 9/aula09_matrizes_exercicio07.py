"""  EXERCÍCIO 7-2 - AULA 9

Crie um algoritmo que receba uma matriz 8x8
com números inteiros e mostre uma mensagem
dizendo se a matriz digitada é simétrica ou não.
Uma matriz só pode ser considerada simétrica
se A[i,j] = A[j,i]
"""

# Biblioteca
import numpy as np

# Declaração
matriz = np.zeros((8, 8), dtype=int)
for i in range(8):
    for j in range(8):
        matriz[i][j] = int(input(f"Digite o elemento da matriz [{i+1},{j+1}]: "))

simetrica = True
for i in range(8):
    for j in range(i+1, 8):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

# Output
if simetrica:
    print("A matriz digitada é simétrica.")
else:
    print("A matriz digitada não é simétrica.")
