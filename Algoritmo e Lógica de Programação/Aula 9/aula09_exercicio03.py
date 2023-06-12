"""  EXERCÍCIO 3 - AULA 9

Faça algoritmo que carregue dois vetores de
dez elementos numéricos cada um e mostre
um vetor resultante na intercalação desses
dois vetores"""

# Declaração
vetor1 = []
vetor2 = []
vetorResultado = []

# Input - Vetor 1
for i in range(10):
    valor = int(input("Digite o valor do elemento do vetor1: "))
    vetor1.append(valor)

# Input - Vetor 2
for i in range(10):
    valor = int(input("Digite o valor do elemento do vetor2: "))
    vetor2.append(valor)

indice1 = 0
indice2 = 0
while indice1 < 10 and indice2 < 10:
    if vetor1[indice1] < vetor2[indice2]:
        vetorResultado.append(vetor1[indice1])
        indice1 += 1
    else:
        vetorResultado.append(vetor2[indice2])
        indice2 += 1


while indice1 < 10:
    vetorResultado.append(vetor1[indice1])
    indice1 += 1


while indice2 < 10:
    vetorResultado.append(vetor2[indice2])
    indice2 += 1

# Output
print("O vetor resultante da intercalação dos vetores é:", vetorResultado)
