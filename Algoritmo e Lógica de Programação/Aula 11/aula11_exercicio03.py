"""  EXERCÍCIO 3 - AULA 11

Faça algoritmo que carregue duas listas de dez elementos numéricos inteiros cada um. A partir dessas duas listas, 
crie um conjunto da união entre essas duas listas"""

# Declaração
lista1 = []
lista2 = []

print("Carregando a primeira lista:")
for i in range(10):
    elemento = int(input("Digite um elemento: "))
    lista1.append(elemento)

print("\nCarregando a segunda lista:")
for i in range(10):
    elemento = int(input("Digite um elemento: "))
    lista2.append(elemento)

conjunto = set(lista1).union(lista2)

# Output
print("\nConjunto da união:")
for elemento in conjunto:
    print(elemento)
