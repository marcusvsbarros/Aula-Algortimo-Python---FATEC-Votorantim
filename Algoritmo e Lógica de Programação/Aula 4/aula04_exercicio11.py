""" EXERCÍCIO 11 - AULA 4

Sabe-se que:
1 pé = 12 polegadas
1 jarda = 3 pés
1 milha = 1760 jardas
Faça um algoritmo que receba uma medida em pés, faça as conversões a seguir e mostre os resultados:
a) Polegadas
b) Jardas
c) milhas
"""

# Input
valoremPes = float(input("Digite um valor em Pés: "))

# a)
valorempolegadas = valoremPes * 12
print(f" O valor digitado em polegadas é {valorempolegadas}")

# b)
valoremJardas = valoremPes * 3
print(f" O valor digitado em jardas é {valoremJardas}")

# c)
valoremMilhas = valoremJardas * 1760
print(f" O valor digitado em milhas é {valoremMilhas}")


