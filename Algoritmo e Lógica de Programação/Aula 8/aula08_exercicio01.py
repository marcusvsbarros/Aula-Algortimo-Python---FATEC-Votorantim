""" EXERCÍCIO 1 - AULA 8

Elabore um algoritmo para ler/receber, separadamente, o primeiro nome, o nome do meio e o sobrenome de uma pessoa, e mostre o 
nome completo, correspondente"""

# input
primeiroNome = input("Digite o primeiro nome: ")
nomeMeio = input("Digite o nome do meio: ")
sobrenome = input("Digite o sobrenome: ")

nomeCompleto = primeiroNome + " " + nomeMeio + " " + sobrenome

# Output
print("Nome completo: " + nomeCompleto)
