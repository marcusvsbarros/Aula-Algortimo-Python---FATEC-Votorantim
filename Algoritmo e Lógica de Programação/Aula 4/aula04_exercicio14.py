""" EXERCÍCIO 14 - AULA 4

Faça um algoritmo que receba uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos. 
Lembre-se de que:

Para quatro e meia deve-se digitar: 4,30
Os minutos vão de 0 a 60!"""

# Input
hora = float(input("Digite a hora no formato HH.MM: "))

horasInteiras = int(hora)
minutosDecimal = hora - horasInteiras

# Cálculo
horasemMinutos = horasInteiras * 60
totalMinutos = horasemMinutos + minutosDecimal * 100

#Output
print(f"A hora digitada em minutos é: {totalMinutos} minutos")
