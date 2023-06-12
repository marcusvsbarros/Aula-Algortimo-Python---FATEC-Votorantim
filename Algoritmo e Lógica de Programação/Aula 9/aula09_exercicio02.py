"""  EXERCÍCIO 2 - AULA 9

Faça um algorimto que carregue um vetor de
10 elementos numéricos inteiros.
Após a finalização da entrada, o algoritmo
deve escrever o maior valor e sua posição.
"""

# Declaração
vetor = []

for i in range(10):
    valor = int(input("Digite o valor do elemento: "))
    vetor.append(valor)

maiorValor = vetor[0]
posicao = 0

for i in range(1, 10):
    if vetor[i] > maiorValor:
        maiorValor = vetor[i]
        posicao = i

# Output
print("O maior valor é:", maiorValor)
print("Sua posição no vetor é:", posicao)


