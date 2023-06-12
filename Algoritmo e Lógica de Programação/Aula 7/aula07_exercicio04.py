""" EXERCÍCIO 4 - AULA 7

Construa um algoritmo que calcule a média aritmética de um conjunto de números pares que forem fornecidos pelo usuário. O valor de 
finalização será a entrada do número 0. Observe que nada impede que o usuário forneça quantos números ímpares quiser, com a ressalva 
de que eles não poderão ser acumulados"""

numerosPares = []
numero = int(input("Digite um número par (ou 0 para encerrar): "))

while numero != 0:
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        print("Número ímpar fornecido. Apenas números pares são aceitos.")

    numero = int(input("Digite um número par (ou 0 para encerrar): "))

if len(numerosPares) > 0:
    media = sum(numerosPares) / len(numerosPares)
    print("A média dos números pares é:", media)
else:
    print("Nenhum número par foi fornecido.")
