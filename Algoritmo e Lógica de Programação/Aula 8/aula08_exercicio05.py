""" EXERCÍCIO 5 - AULA 8

Faça um algoritmo para determinar quantas palavras existem em uma determinada frase 
Obs: tanto a palavra, quanto a frase, devem ser informadas pelo usuário.
"""

# Input
frase = input("Digite uma frase: ")

palavras = frase.split()
qtdePalavras = len(palavras)

#Output
print("Número de palavras na frase:", n=qtdePalavras)
