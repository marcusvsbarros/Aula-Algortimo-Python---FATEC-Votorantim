"""  EXERCÍCIO 5-2 - AULA 9

Faça um algoritmo que receba uma matriz 10x10
de elementos inteiros e localize a posição (linha
e coluna) do maior elemento da matriz"""

# Declaração
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input(f"Digite o elemento da matriz [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

maiorElemento = matriz[0][0]
linhaMaior = 0
colunaMaior = 0

for i in range(10):
    for j in range(10):
        if matriz[i][j] > maiorElemento:
            maiorElemento = matriz[i][j]
            linhaMaior = i
            colunaMaior = j

# Output
print(f"O maior elemento da matriz é: {maiorElemento}")
print(f"Sua posição (linha, coluna) é: ({linhaMaior + 1}, {colunaMaior + 1})")
