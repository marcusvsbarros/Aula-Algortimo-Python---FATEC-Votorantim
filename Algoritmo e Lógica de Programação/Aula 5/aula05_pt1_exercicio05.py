""" EXERCÍCIO 5-1 - AULA 5

(FORBELLONE; EBERSPÄCHER, 2000 - pág. 46)
Faça um algoritmo que leia o ano de nascimento de uma pessoa, calcule e mostre sua idade e, também, verifique e mostre se ela já tem 
idade para votar (16 anos ou mais) e para conseguir a Carteira de Habilitação (18 anos ou mais)
"""

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = 2023
idade = anoAtual - anoNascimento

print("Sua idade é: ", idade)

if idade >= 16:
    print("Você já tem idade para votar.")
else:
    print("Você ainda não tem idade para votar.")

if idade >= 18:
    print("Você já pode obter a Carteira de Habilitação.")
else:
    print("Você ainda não tem idade para obter a Carteira de Habilitação.")