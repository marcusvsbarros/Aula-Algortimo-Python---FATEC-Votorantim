"""  EXERCÍCIO 5 - AULA 9

Faça um Algoritmo que simule 6000 jogadas
de um dado de 6 faces. Para simular o
resultado utilize a função randint
Ao final, mostre a frequência de sorteio de
cada uma das faces"""

# Biblioteca
import random

frequencia = [0, 0, 0, 0, 0, 0]

for i in range(6000):
    resultado = random.randint(1, 6)
    frequencia[resultado-1] += 1

for i in range(6):
    print("Frequência de sorteio de cada face:")
    for face, valor in enumerate(frequencia):
        print("Face", face + 1, ":", valor)
