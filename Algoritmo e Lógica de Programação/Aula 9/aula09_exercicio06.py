"""  EXERCÍCIO 6 - AULA 9

Faça um algoritmo que simule a jogada de dois
dados de 6 faces. O programa deve usar randint
para rolar o primeiro dado e deve usar randint
novamente para rolar o segundo dado. A soma
das duas faces deve ser calculada. Assim: a
soma variará de 2 a 12
O programa deve rolar 30.000 vezes e mostrar
a frequência com que a soma (de 2 a 12)
aparecem. Verifique se o valor 7 corresponde a
1/6 das jogadas!
"""
# Biblioteca
import random

frequencia = [0] * 11

for i in range(30000):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    frequencia[soma-2] += 1

print("Frequência das somas (de 2 a 12):")
for soma, valor in enumerate(frequencia, start=2):
    print("Soma", soma, ":", valor)

frequencia7 = frequencia[5]
percentual7 = (frequencia7 / 30000) * 100
print("Frequência do valor 7:", frequencia7)
print("Percentual do valor 7:", percentual7)

if abs(percentual7 - (1 / 6 * 100)) < 1:
    print("O valor 7 corresponde a aproximadamente 1/6 das jogadas.")
else:
    print("O valor 7 não corresponde a aproximadamente 1/6 das jogadas.")