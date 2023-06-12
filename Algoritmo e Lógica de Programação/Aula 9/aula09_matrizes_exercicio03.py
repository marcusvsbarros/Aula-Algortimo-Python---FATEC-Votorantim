"""  EXERCÍCIO 3-2 - AULA 9

Faça um algoritmo que leia os dados de uma
matriz de 4 linhas e 4 colunas, composta de
elementos reais, e calcule a soma dos
elementos da diagonal principal da matriz."""

# Declaração
matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)


somaDiagonal = 0
for i in range(4):
    somaDiagonal += matriz[i][i]

# Output
print(f"Soma dos elementos da diagonal principal: {somaDiagonal}")
