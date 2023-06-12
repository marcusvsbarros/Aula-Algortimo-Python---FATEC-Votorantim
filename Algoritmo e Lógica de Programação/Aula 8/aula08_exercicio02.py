""" EXERCÍCIO 2 - AULA 8

Faça um algoritmo que solicite uma data no formato de uma string – dd/mm/aaaa. Mostre essa data no formato AAAAMMDD
"""

# Input
data = input("Digite uma data (dd/mm/aaaa): ")


dia, mes, ano = data.split('/')
novaData = ano + mes + dia

#Output
print("Data no formato AAAAMMDD:", novaData)
