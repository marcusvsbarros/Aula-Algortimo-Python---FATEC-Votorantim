""" EXERCÍCIO 3 - AULA 8

Faça um algoritmo para ler nove caracteres numéricos em uma string. Mostre o conteúdo dessa string colando pontos e virgula, 
respectivamente nas posições inteiras e 
decimais. 
Exemplo: 
Digitado> 987654321
Mostrado> 9.876.543,21
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
