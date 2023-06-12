""" EXERCÍCIO 4 - AULA 8

Elabore um algoritmo para determinar quantas vogais existem dentro de uma determinada frase (que deve ser recebida do usuário).
"""

# Input
numeros = input("Digite nove caracteres numéricos: ")

if len(numeros) != 9:
    print("A string deve conter exatamente nove caracteres.")
else:
    parteInteira = numeros[:6]
    parteDecimal = numeros[6:]
    novaString = parteInteira[:3] + '.' + parteInteira[3:] + ',' + parteDecimal

    print("Mostrado:", novaString)
