"""  EXERCÍCIO 5 - AULA 12

Faça uma função que receba como parâmetro o raio de uma esfera, calcule e retorne o valor de seu volume.
Volume da Esfera : v = 4/3 * R"""

# Biblioteca
import math

# Declaração
def calcular_volume_esfera(raio):
    volume = (4/3) * math.pi * (raio ** 3)
    return volume


raio = float(input("Digite o raio da esfera: "))
volume = calcular_volume_esfera(raio)

# Output
print("O volume da esfera com raio", raio, "é:", volume)
