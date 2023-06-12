""" EXERCÍCIO 4-1 - AULA 5

(FORBELLONE; EBERSPÄCHER, 2000 - pág. 46)
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as 
seguintes fórmulas:
- para homens: (72.7 * h) – 58;
- para mulheres: (62.1 * h) – 44.7.
"""

# Input
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino ou F para feminino): ")

if sexo == "M":
    pesoIdeal = (72.7 * altura) - 58;
    print("Seu peso ideal é", pesoIdeal, "quilogramas.")
elif sexo == "m":
    pesoIdeal = (72.7 * altura) - 58;
    print("Seu peso ideal é", pesoIdeal, "quilogramas.")
elif sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7;
    print("Seu peso ideal é", pesoIdeal, "quilogramas.")
elif sexo == "f":
    pesoIdeal = (62.1 * altura) - 44.7;
    print("Seu peso ideal é", pesoIdeal, "quilogramas.")
else:
    print("Sexo inválido.")
