"""  EXERCÍCIO 2 - AULA 11

Faça um algorimto que carregue um dicionário de 10 elementos onde a chave é o sobrenome da pessoa e o valor a sua idade.
Após a finalização da entrada, o algoritmo deve escrever o sobrenome da pessoa com maior idade.
"""

# Declaração
dicionario = {}
for i in range(10):
    sobrenome = input("Digite o sobrenome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    dicionario[sobrenome] = idade

maiorIdade = max(dicionario.values())
sobrenomeMaior = [key for key, value in dicionario.items() if value == maiorIdade][0]

# Output
print("Sobrenome da pessoa com maior idade:", sobrenomeMaior)
