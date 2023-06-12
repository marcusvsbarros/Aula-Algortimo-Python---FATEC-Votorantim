"""  EXERCÍCIO 4-2 - AULA 9

Faça um algoritmo que leia os valores de uma
matriz 3x3 de elementos reais e crie a matriz
transposta da matriz fornecida.
Matriz transposta: Igual a simétrica. Em
matemática, é o resultado da troca de linhas por
colunas em uma determinada matriz.
A[i,j] = A[j,i"""

# Declaração
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        elemento = float(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

matrizTransposta = []
for i in range(3):
    linhaTransposta = []
    for j in range(3):
        linhaTransposta.append(matriz[j][i])
    matrizTransposta.append(linhaTransposta)

# Output
print("Matriz Transposta:")
for linha in matrizTransposta:
    print(linha)
