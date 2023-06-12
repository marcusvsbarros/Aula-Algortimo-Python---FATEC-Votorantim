"""  EXERCÍCIO 2-2 - AULA 9

Faça um algoritmo que leia uma matriz 2x2,
calcule e mostre uma matriz resultante que
será a matriz digitada, multiplicada pelo
maior elemento da matriz"""

# Declaração
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)


maiorElemento = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > maiorElemento:
            maiorElemento = elemento


matrizResultante = []
for linha in matriz:
    linhaResultante = []
    for elemento in linha:
        elementoResultante = elemento * maiorElemento
        linhaResultante.append(elementoResultante)
    matrizResultante.append(linhaResultante)

# Output
print("Matriz digitada: ")
for linha in matriz:
    print(linha)

print("Matriz resultante: ")
for linha in matrizResultante:
    print(linha)
