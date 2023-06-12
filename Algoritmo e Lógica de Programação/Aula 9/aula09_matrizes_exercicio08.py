"""  EXERCÍCIO 8-2 - AULA 9

Faça um algoritmo que receba uma matriz de
5x5 com números reais. Ao final o algoritmo
deve calcular e mostrar a média dos elementos
que estão nas linhas pares da matriz"""

# Declaração
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        elemento = float(input(f"Digite o elemento da matriz [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

soma = 0
contador = 0
for i in range(0, 5, 2): 
    for j in range(5):
        soma += matriz[i][j]
        contador += 1

# Output
if contador > 0:
    media = soma / contador
    print(f"A média dos elementos das linhas pares da matriz é: {media:.2f}")
else:
    print("Não há linhas pares na matriz.")
