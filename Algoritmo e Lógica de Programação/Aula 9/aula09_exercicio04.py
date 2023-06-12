"""  EXERCÍCIO 4 - AULA 9

Faça um algoritmo que leia 20 palavras de no
máximo 10 caracteres, e após a leitura, realize
um processo qualquer que inverta os
caracteres de cada uma das palavras.
"""


# Declaração
palavras = []


for i in range(20):
    palavra = input("Digite a palavra {}: ".format(i+1))
    palavras.append(palavra)

palavrasInvertidas = []
for palavra in palavras:
    palavraInvertida = palavra[::-1]
    palavrasInvertidas.append(palavraInvertida)

# Output
print("Palavras invertidas:")
for palavraInvertida in palavrasInvertidas:
    print(palavraInvertida)
